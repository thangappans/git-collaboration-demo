import unittest
from pathlib import Path

class TestApplication(unittest.TestCase):

    def test_html_file_exists(self):
        self.assertTrue(Path("index.html").exists())

    def test_application_content(self):
        content = Path("index.html").read_text()
        self.assertIn("Welcome to CI/CD Pipeline", content)

if __name__ == "__main__":
    unittest.main()
