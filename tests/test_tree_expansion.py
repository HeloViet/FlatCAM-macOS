import ast
import unittest
from pathlib import Path


SOURCE = Path(__file__).parents[1] / "appObjects" / "ObjectCollection.py"


def _object_collection_class():
    tree = ast.parse(SOURCE.read_text())
    return next(node for node in tree.body if isinstance(node, ast.ClassDef)
                and node.name == "ObjectCollection")


class TreeExpansionTests(unittest.TestCase):
    def test_object_collection_schedules_tree_expansion_after_insertion(self):
        class_node = _object_collection_class()
        methods = {node.name: node for node in class_node.body
                   if isinstance(node, ast.FunctionDef)}

        self.assertIn("schedule_expand_all_groups", methods)

        append_object = methods["append"]
        scheduled_calls = [node for node in ast.walk(append_object)
                           if isinstance(node, ast.Call)
                           and isinstance(node.func, ast.Attribute)
                           and node.func.attr == "schedule_expand_all_groups"]
        self.assertFalse(scheduled_calls)

    def test_initial_tree_expansion_is_deferred(self):
        class_node = _object_collection_class()
        methods = {node.name: node for node in class_node.body
                   if isinstance(node, ast.FunctionDef)}

        schedule_method = methods["schedule_expand_all_groups"]
        single_shot_calls = [node for node in ast.walk(schedule_method)
                             if isinstance(node, ast.Call)
                             and isinstance(node.func, ast.Attribute)
                             and node.func.attr == "singleShot"]
        self.assertEqual(len(single_shot_calls), 1)
        self.assertGreater(single_shot_calls[0].args[0].value, 0)


if __name__ == "__main__":
    unittest.main()
