import ast
import unittest
from pathlib import Path


SOURCE = Path(__file__).parents[1] / "appPlugins" / "ToolMilling.py"


def _method(name):
    tree = ast.parse(SOURCE.read_text())
    return next(node for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef) and node.name == name)


class ToolMillingTests(unittest.TestCase):
    def test_apply_all_validates_tool_uid_cell_before_reading_text(self):
        method = _method("on_apply_param_to_all_clicked")
        source = ast.unparse(method)
        self.assertIn("row_count = table.rowCount() - 2", source)
        self.assertIn("is None", source)


if __name__ == "__main__":
    unittest.main()
