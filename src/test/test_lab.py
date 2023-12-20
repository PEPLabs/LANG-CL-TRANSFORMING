import unittest
from src.main.lab import get_html_headers, get_md_headers, transform_txt

class TestTransform(unittest.TestCase):

    def test_html_headers(self):
        headers = get_html_headers()
        L = []
        for header in headers:
            self.assertIsInstance(header, tuple)
            L.append(header[0])
        self.assertIn("h1", L)
        self.assertIn("h2", L)
    
    def test_md_headers(self):
        headers = get_md_headers()
        L = []
        for header in headers:
            self.assertIsInstance(header, tuple)
            L.append(header[0])
        self.assertIn("##", L)
        self.assertIn("###", L)
        self.assertIn("####", L)
        self.assertIn("#####", L)
    
    def test_text_splitter(self):
        split_text = transform_txt("src/resources/sample.txt")
        self.assertIsInstance(split_text, list)
        self.assertGreater(len(split_text), 1)
        self.assertLess(len(split_text), 10)

if __name__ == '__main__':
    unittest.main()