#!/usr/bin/env python3
"""Run the three specified checks for the programming-tutor example."""
import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'examples' / 'parse_integers.py'
spec = importlib.util.spec_from_file_location('parse_integers_example', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
assert module.parse_integers('1, 2,-3') == [1, 2, -3]
assert module.parse_integers('   ') == []
try:
    module.parse_integers('1,,2')
except ValueError:
    pass
else:
    raise AssertionError('An empty comma-separated item must raise ValueError')
print('PASS: all three specified parser checks')
