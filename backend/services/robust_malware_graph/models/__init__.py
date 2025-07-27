import importlib, sys

gnn = importlib.import_module('src.models.gnn')
sys.modules[__name__ + '.gnn'] = gnn
__all__ = ['gnn']
