import unittest
from pathlib import Path


DEFAULTS_SOURCE = Path(__file__).parents[1] / "defaults.py"


class AppDefaultTests(unittest.TestCase):
    def test_default_app_level_is_advanced(self):
        source = DEFAULTS_SOURCE.read_text()
        self.assertIn('"global_app_level": \'a\'', source)


if __name__ == "__main__":
    unittest.main()
