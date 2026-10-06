import unittest
from pathlib import Path


APP_SOURCE = (Path(__file__).parents[1] / "appMain.py").read_text()
MAIN_GUI_SOURCE = (Path(__file__).parents[1] / "appGUI" / "MainGUI.py").read_text()


class PlotToggleSafetyTests(unittest.TestCase):
    def test_app_has_safe_plot_ui_recovery(self):
        self.assertIn("def _ensure_object_plot_ui", APP_SOURCE)
        self.assertIn("obj.set_ui(obj.ui_type(app=self))", APP_SOURCE)
        self.assertIn("except (AttributeError, RuntimeError)", APP_SOURCE)

    def test_enable_plots_uses_safe_plot_ui_recovery(self):
        method = APP_SOURCE.split("    def enable_plots", 1)[1].split("    def disable_plots", 1)[0]
        self.assertIn("_ensure_object_plot_ui", method)

    def test_space_toggle_uses_safe_app_helper(self):
        space_block = MAIN_GUI_SOURCE.split("# Space = Toggle Active/Inactive", 1)[1].split(
            "# Select the object in the Tree above the current one", 1)[0]
        self.assertIn("toggle_object_plot", space_block)


if __name__ == "__main__":
    unittest.main()
