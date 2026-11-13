"""
TestWorkflows tests the shell scripts of the GitHub workflows: no
'${{ ... }}' expression is pasted into a 'run:' script.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re

from . import ReleaseToolingTest

#  The repository root, three folders above this file's folder.
_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
WORKFLOWS = os.path.join(ROOT, '.github', 'workflows')
#  A 'run:' key, alone or as the first key of a step, and what follows it.
_RUN = re.compile(r'^(\s*)(?:- )?run:\s*(.*)$')


def runScripts(text: str) -> list:
  """
  The lines of every 'run:' script of a workflow, as (line number, line)
  pairs: the one line of a script on the key's line, or each line of a
  '|' or '>' block, up to the next line indented no deeper than the key.
  """
  lines = str.split(text, '\n')
  out = []
  index = 0
  while index < len(lines):
    match = _RUN.match(lines[index])
    index += 1
    if not match:
      continue
    indent, rest = len(match.group(1)), str.strip(match.group(2))
    if rest[:1] not in ('|', '>'):
      out.append((index, rest))
      continue
    while index < len(lines):
      line = lines[index]
      if str.strip(line) and len(line) - len(str.lstrip(line)) <= indent:
        break
      index += 1
      out.append((index, line))
  return out


def workflowPaths() -> list:
  """The workflow files of the repository, by name."""
  names = sorted(os.listdir(WORKFLOWS))
  return [os.path.join(WORKFLOWS, n) for n in names if n.endswith('.yml')]


class TestWorkflows(ReleaseToolingTest):
  """
  GitHub expands a '${{ ... }}' expression into the text of a 'run:'
  script before the shell reads it, so a value holding shell syntax
  would run as code. A script reads what it needs from the environment
  instead, quoted: GitHub's own variables, as '$GITHUB_REF', or one an
  earlier step exported, as '$VERSION_INFO'. An expression stays fine
  where no shell reads it: in 'with:', 'env:' and 'if:'.
  """

  def test_finds_expressions(self) -> None:
    """The guard itself, on a workflow of the test's own."""
    text = str.join('\n', [
      'jobs:',
      '  publish:',
      '    if: ${{ github.ref }}',
      '    steps:',
      '      - run: echo ${{ github.ref }}',
      '      - name: Block',
      '        env:',
      '          REF: ${{ github.ref }}',
      '        run: |',
      '          echo "$REF"',
      '          git push origin HEAD:${{ github.ref }}',
      '      - uses: some/action@v1',
      '        with:',
      '          tag: ${{ env.VERSION_INFO }}',
      '',
    ])
    pasted = [line for _, line in runScripts(text) if '${{' in line]
    self.assertEqual(pasted, [
      'echo ${{ github.ref }}',
      '          git push origin HEAD:${{ github.ref }}',
    ])

  def test_every_workflow_has_scripts(self) -> None:
    paths = workflowPaths()
    self.assertTrue(paths, 'no workflows in %s' % WORKFLOWS)
    for path in paths:
      with self.subTest(workflow=os.path.basename(path)):
        self.assertTrue(runScripts(self.readText(path)))

  def test_no_expression_in_a_script(self) -> None:
    pasted = []
    for path in workflowPaths():
      for number, line in runScripts(self.readText(path)):
        if '${{' in line:
          name = os.path.basename(path)
          pasted.append('%s:%d: %s' % (name, number, str.strip(line)))
    self.assertEqual(pasted, [], str.join('\n', pasted))
