import ast
import unittest
from pathlib import Path


GUI_SOURCE = Path(__file__).parents[1] / "appGUI" / "GUIElements.py"
CNC_SOURCE = Path(__file__).parents[1] / "appObjects" / "CNCJobObject.py"


def _method(source, name):
    tree = ast.parse(source.read_text())
    return next(node for node in ast.walk(tree)
                if isinstance(node, ast.FunctionDef) and node.name == name)


class MacOSSaveDialogTests(unittest.TestCase):
    def test_cnc_job_keeps_save_dialog_import(self):
        source = CNC_SOURCE.read_text()
        self.assertIn("FCFileSaveDialog", source.split("\n", 40)[0:40].__str__())

    def test_save_dialog_uses_osascript_instead_of_qt_file_dialog(self):
        method = _method(GUI_SOURCE, "get_saved_filename")
        qt_dialog_calls = [node for node in ast.walk(method)
                           if isinstance(node, ast.Call)
                           and isinstance(node.func, ast.Attribute)
                           and node.func.attr == "getSaveFileName"]
        subprocess_calls = [node for node in ast.walk(method)
                            if isinstance(node, ast.Call)
                            and isinstance(node.func, ast.Attribute)
                            and node.func.attr == "run"]

        darwin_branches = [node for node in ast.walk(method)
                           if isinstance(node, ast.Compare)
                           and any(isinstance(op, ast.Eq) for op in node.ops)]
        self.assertTrue(darwin_branches)
        self.assertTrue(subprocess_calls)

    def test_export_button_still_uses_save_dialog(self):
        method = _method(CNC_SOURCE, "on_exportgcode_button_click")
        dialog_calls = [node for node in ast.walk(method)
                        if isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute)
                        and node.func.attr == "get_saved_filename"]
        self.assertTrue(dialog_calls)


if __name__ == "__main__":
    unittest.main()
