"""
TestReadme tests the examples of the README: every python block runs,
statement by statement, and where an expression's comment states its
result, as a value ('minecraft:wool:6', [...], 1697) or an error
('NotInVersion: ...'), the result is what the comment says. A comment of
words alone ('# the same: ...') states no result and is not checked.

The examples run in a process of their own, as a user runs them: a test
that subclasses a catalogue changes how its members print for the rest
of its process ('<CatalogueMetaNum>.DIAMOND'), worktoy naming a member
several enumerations hold by the root of their family.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import ast
import contextlib
import io
import json
import os
import re
import subprocess
import sys

from worktoy.work_test import BaseTest

README = os.path.join(os.path.dirname(os.path.dirname(
  os.path.abspath(__file__))), 'README.md')
#  A comment states a result when it begins as a value or an error does.
_STATES = re.compile(r"""^(['"\[({<\d-]|True\b|False\b|None\b|[A-Z]\w*[(:])""")


def _claims() -> list:
  """
  Each expression of the README's python blocks with the comment on its
  line, or on the comment lines right after it, in the order they run, as
  (block number, source, claim, code).
  """
  with open(README, encoding='utf-8') as file:
    text = file.read()
  out = []
  blocks = re.findall(r'```python\n(.*?)```', text, re.S)
  for number, block in enumerate(blocks, 1):
    lines = block.split('\n')
    for node in ast.parse(block).body:
      endLine = lines[node.end_lineno - 1]
      source = ast.get_source_segment(block, node)
      claim = ''
      if '#' in endLine[len(source.split('\n')[-1]):]:
        claim = endLine.split('#', 1)[1].strip()
      follow = []
      for later in lines[node.end_lineno:]:
        if not later.strip().startswith('#'):
          break
        follow.append(later.strip()[1:].strip())
      if not claim and follow:
        claim = str.join(' ', follow)
      out.append((number, source, claim, node))
  return out


def mismatches() -> tuple:
  """
  How many examples state their result, and each whose result is not
  what it states, the examples' own printing held back.
  """
  namespace: dict = {}
  checked, out = 0, []
  with contextlib.redirect_stdout(io.StringIO()):
    for number, source, claim, node in _claims():
      isExpression = isinstance(node, ast.Expr)
      if isExpression:
        code = compile(ast.Expression(node.value), '<README>', 'eval')
      else:
        code = compile(ast.Module([node], []), '<README>', 'exec')
      try:
        result = eval(code, namespace)
        shown = repr(result) if isExpression else ''
      except Exception as exception:
        shown = '%s: %s' % (type(exception).__name__, exception)
      if not (isExpression and _STATES.match(claim)):
        continue
      checked += 1
      said = re.sub(r'\s+', '', claim)
      got = re.sub(r'\s+', '', shown)
      if not (said.startswith(got) or got.startswith(said)):
        infoSpec = 'block %d: %s\n  gives %s\n  says  %s'
        out.append(infoSpec % (number, source, shown, claim))
  return checked, out


class TestReadme(BaseTest):
  """
  TestReadme runs the README's examples against their comments.
  """

  def test_examples(self) -> None:
    env = dict(os.environ, PYTHONPATH=str.join(os.pathsep, sys.path))
    code = ('import json, test_readme; '
            'print(json.dumps(test_readme.mismatches()))')
    result = subprocess.run(
        [sys.executable, '-c', code], capture_output=True, text=True,
        env=env, cwd=os.path.dirname(os.path.abspath(__file__)), )
    self.assertEqual(result.returncode, 0, result.stderr)
    checked, found = json.loads(result.stdout.strip().split('\n')[-1])
    self.assertEqual(found, [], str.join('\n', found))
    self.assertGreater(checked, 200)
