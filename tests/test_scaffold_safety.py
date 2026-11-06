"""Regression tests for non-destructive LeetCode scaffolding."""
import os
import tempfile
import unittest

from utils import LeetCodeDirectoryManager


class ScaffoldSafetyTests(unittest.TestCase):
    def test_existing_cpp_is_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            path = os.path.join(root, "answer.cpp")
            with open(path, "w", encoding="utf-8") as output:
                output.write("int main() { return 42; }")
            LeetCodeDirectoryManager.create_file(path)
            with open(path, encoding="utf-8") as source:
                self.assertEqual(source.read(), "int main() { return 42; }")

    def test_existing_markdown_is_preserved(self):
        with tempfile.TemporaryDirectory() as root:
            path = os.path.join(root, "answer.md")
            with open(path, "w", encoding="utf-8") as output:
                output.write("My notes")
            LeetCodeDirectoryManager.create_file(path, "question", "https://example.com")
            with open(path, encoding="utf-8") as source:
                self.assertEqual(source.read(), "My notes")

    def test_new_markdown_contains_question_link(self):
        with tempfile.TemporaryDirectory() as root:
            path = os.path.join(root, "answer.md")
            LeetCodeDirectoryManager.create_file(path, "Question", "https://example.com")
            with open(path, encoding="utf-8") as source:
                self.assertIn("[Question](https://example.com)", source.read())

    def test_new_cpp_is_empty(self):
        with tempfile.TemporaryDirectory() as root:
            path = os.path.join(root, "answer.cpp")
            LeetCodeDirectoryManager.create_file(path)
            with open(path, encoding="utf-8") as source:
                self.assertEqual(source.read(), "")


if __name__ == "__main__":
    unittest.main()
