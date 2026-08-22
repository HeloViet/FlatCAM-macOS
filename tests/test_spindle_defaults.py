import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class SpindleDefaultTests(unittest.TestCase):
    def test_global_milling_and_drilling_defaults_are_500(self):
        source = (ROOT / "defaults.py").read_text()
        self.assertIn('"tools_drill_spindlespeed": 500', source)
        self.assertIn('"tools_mill_spindlespeed": 500', source)

    def test_geometry_objects_default_to_500(self):
        source = (ROOT / "appObjects" / "GeometryObject.py").read_text()
        self.assertIn('"tools_mill_spindlespeed": 500', source)

    def test_tool_plugins_normalize_existing_zero_values(self):
        milling = (ROOT / "appPlugins" / "ToolMilling.py").read_text()
        drilling = (ROOT / "appPlugins" / "ToolDrilling.py").read_text()
        self.assertGreaterEqual(milling.count("tools_mill_spindlespeed"), 3)
        self.assertGreaterEqual(drilling.count("tools_drill_spindlespeed"), 3)
        self.assertIn("= 500", milling)
        self.assertIn("= 500", drilling)


if __name__ == "__main__":
    unittest.main()
