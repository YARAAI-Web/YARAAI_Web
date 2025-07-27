import ast
import pathlib
import argparse
import pytest

# Load the _schedule_beta function from the source without importing heavy deps
src = pathlib.Path('src/cli/explainer_train.py').read_text()
module = ast.parse(src)
for node in module.body:
    if isinstance(node, ast.FunctionDef) and node.name == '_schedule_beta':
        code = ast.get_source_segment(src, node)
        break
else:
    raise AssertionError('_schedule_beta not found')
namespace = {'argparse': argparse}
exec(code, namespace)
_schedule_beta = namespace['_schedule_beta']

def test_schedule_beta_reaches_target():
    args = argparse.Namespace(
        beta=0.1,
        beta_schedule=True,
        beta_schedule_factor=10.0,
        beta_schedule_epochs=1,
    )
    cap = args.beta
    beta = 1e-4
    for _ in range(3):
        beta = _schedule_beta(beta, args, cap)
    assert beta == pytest.approx(args.beta)

