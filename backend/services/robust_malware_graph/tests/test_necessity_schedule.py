import ast
import pathlib
import argparse
import pytest

src = pathlib.Path('src/cli/explainer_train.py').read_text()
module = ast.parse(src)
for node in module.body:
    if isinstance(node, ast.FunctionDef) and node.name == '_schedule_necessity_weight':
        code = ast.get_source_segment(src, node)
        break
else:
    raise AssertionError('_schedule_necessity_weight not found')
namespace = {'argparse': argparse}
exec(code, namespace)
_schedule_necessity_weight = namespace['_schedule_necessity_weight']

def test_schedule_necessity_reaches_target():
    args = argparse.Namespace(
        necessity_weight=0.05,
        necessity_schedule=True,
        necessity_schedule_factor=10.0,
        necessity_schedule_epochs=1,
    )
    cap = args.necessity_weight
    weight = 1e-4
    for _ in range(3):
        weight = _schedule_necessity_weight(weight, args, cap)
    assert weight == pytest.approx(args.necessity_weight)
