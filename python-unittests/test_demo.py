import unittest
import demo
class TestDemo(unittest.TestCase):

    def test_add(self):
        result =demo.add(2,3)
        self.assertEqual(result,5)
        self.assertEqual(demo.add(10,4),14)
        self.assertEqual(demo.add(23,7),30)

    def test_sub(self):
        self.assertEqual(demo.sub(10,4),6)
        self.assertEqual(demo.sub(5,4),1)
        self.assertEqual(demo.sub(15,3),12)

    def test_mul(self):
        self.assertEqual(demo.mul(10,4),40)
        self.assertEqual(demo.mul(5,4),20)
        self.assertEqual(demo.mul(15,3),45)

    def test_div(self):
        self.assertEqual(demo.div(10,4),2.5)
        self.assertEqual(demo.div(5,5),1)
        self.assertEqual(demo.div(15,3),5)


if __name__ == '__main__':
    unittest.main()
