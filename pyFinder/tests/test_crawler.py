import unittest
from pyfinder import Crawler

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler()
        self.n = 10

    def test_build_test(self):
        images = self.crawler.build_test(num_images_test=self.n)
        self.assertEqual(len(images), self.n)

    def test_load_test(self):
        load = self.crawler.load_test_images()
        self.assertEqual(self.n, len(load))


if __name__ == '__main__':
    unittest.main()
