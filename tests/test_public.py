"""Public tests for Lab 01. Hidden tests are harder!"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
import lab01 as lab  # noqa: E402

def test_bfs_simple():
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert lab.bfs(g, "A", "D") == ["A", "B", "D"]

def test_dfs_simple():
    g = {"A": ["B"], "B": ["C"], "C": []}
    assert lab.dfs(g, "A", "C") == ["A", "B", "C"]
