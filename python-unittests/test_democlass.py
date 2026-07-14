import unittest
import democlass
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = democlass.Calculate()

    def tearDown(self):
        return super().tearDown()
    
    def test_add(self):
        self.assertEqual(self.calculate.add(4,5),9)

    def test_sub(self):
        self.assertEqual(self.calculate.sub(14,5),9)
    
    def test_mul(self):
        self.assertEqual(self.calculate.mul(4,5),20)

    def test_div(self):
        self.assertEqual(self.calculate.div(15,5),3)
        with self.assertRaises(ValueError):
            self.calculate.div(10,0)


if __name__=='__main__':
    unittest.main()