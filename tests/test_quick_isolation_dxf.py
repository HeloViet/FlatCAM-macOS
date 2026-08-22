import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
APP_SOURCE = (ROOT / "appMain.py").read_text()
ISOLATION_SOURCE = (ROOT / "appPlugins" / "ToolIsolation.py").read_text()


class QuickIsolationDxfTests(unittest.TestCase):
    def test_project_toolbar_has_quick_isolation_dxf_button(self):
        self.assertIn("Quick Isolation DXF", APP_SOURCE)
        self.assertIn("quick_isolation_dxf", APP_SOURCE)

    def test_quick_workflow_requires_selected_gerber_and_uses_point_zero_one_tool(self):
        self.assertIn("def quick_isolation_dxf", ISOLATION_SOURCE)
        self.assertIn("No Gerber object is selected", ISOLATION_SOURCE)
        self.assertIn("getattr(selected_obj, 'kind', None)", ISOLATION_SOURCE)
        self.assertIn("0.01", ISOLATION_SOURCE)
        self.assertIn("on_iso_button_click", ISOLATION_SOURCE)

    def test_quick_workflow_exports_created_geometry_with_macos_save_dialog(self):
        self.assertIn("FCFileSaveDialog.get_saved_filename", ISOLATION_SOURCE)
        self.assertIn("export_dxf", ISOLATION_SOURCE)
        self.assertIn("geometry_ready", ISOLATION_SOURCE)


if __name__ == "__main__":
    unittest.main()
