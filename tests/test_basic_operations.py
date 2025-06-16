import unittest
import sys
import os

# 添加项目根目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from operations.basic_operations import (
    AddOperation,
    SubtractOperation,
    MultiplyOperation,
    DivideOperation,
    PowerOperation
)

class TestBasicOperations(unittest.TestCase):
    def setUp(self):
        self.add = AddOperation()
        self.subtract = SubtractOperation()
        self.multiply = MultiplyOperation()
        self.divide = DivideOperation()

    def test_add_operation(self):
        # 测试正数加法
        self.assertEqual(self.add.calculate(1, 2), 3)
        # 测试负数加法
        self.assertEqual(self.add.calculate(-1, -2), -3)
        # 测试小数加法
        self.assertAlmostEqual(self.add.calculate(1.1, 2.2), 3.3)
        # 测试零的加法
        self.assertEqual(self.add.calculate(0, 5), 5)

    def test_subtract_operation(self):
        # 测试正数减法
        self.assertEqual(self.subtract.calculate(5, 3), 2)
        # 测试负数减法
        self.assertEqual(self.subtract.calculate(-5, -3), -2)
        # 测试小数减法
        self.assertAlmostEqual(self.subtract.calculate(5.5, 2.2), 3.3)
        # 测试零的减法
        self.assertEqual(self.subtract.calculate(5, 0), 5)

    def test_multiply_operation(self):
        # 测试正数乘法
        self.assertEqual(self.multiply.calculate(2, 3), 6)
        # 测试负数乘法
        self.assertEqual(self.multiply.calculate(-2, 3), -6)
        # 测试小数乘法
        self.assertAlmostEqual(self.multiply.calculate(2.5, 2), 5)
        # 测试零的乘法
        self.assertEqual(self.multiply.calculate(5, 0), 0)

    def test_divide_operation(self):
        # 测试正数除法
        self.assertEqual(self.divide.calculate(6, 2), 3)
        # 测试负数除法
        self.assertEqual(self.divide.calculate(-6, 2), -3)
        # 测试小数除法
        self.assertAlmostEqual(self.divide.calculate(5.5, 2), 2.75)
        # 测试除以1
        self.assertEqual(self.divide.calculate(5, 1), 5)
        
        # 测试除零异常
        with self.assertRaises(ZeroDivisionError):
            self.divide.calculate(5, 0)

class TestPowerOperation(unittest.TestCase):
    def setUp(self):
        self.power = PowerOperation()

    def test_positive_integer_powers(self):
        self.assertEqual(self.power.calculate(2, 3), 8)
        self.assertEqual(self.power.calculate(5, 2), 25)
        self.assertEqual(self.power.calculate(1, 100), 1)

    def test_base_zero(self):
        self.assertEqual(self.power.calculate(0, 5), 0)
        self.assertEqual(self.power.calculate(0, 1), 0)
        # 0 to a negative power is DivisionByZero
        with self.assertRaises(ZeroDivisionError): # 0^-2 is 1/0^2
            self.power.calculate(0,-2)


    def test_exponent_zero(self):
        self.assertEqual(self.power.calculate(5, 0), 1)
        self.assertEqual(self.power.calculate(-2, 0), 1)
        self.assertEqual(self.power.calculate(0.5, 0), 1)

    def test_zero_power_zero(self):
        # 0^0 is conventionally 1 in many contexts
        self.assertEqual(self.power.calculate(0, 0), 1)

    def test_negative_base_even_exponent(self):
        self.assertEqual(self.power.calculate(-2, 2), 4)
        self.assertEqual(self.power.calculate(-3, 4), 81)
        self.assertAlmostEqual(self.power.calculate(-2.5, 2), 6.25)

    def test_negative_base_odd_exponent(self):
        self.assertEqual(self.power.calculate(-2, 3), -8)
        self.assertEqual(self.power.calculate(-3, 1), -3)
        self.assertAlmostEqual(self.power.calculate(-2.5, 3), -15.625)

    def test_negative_exponent(self):
        self.assertAlmostEqual(self.power.calculate(2, -1), 0.5)
        self.assertAlmostEqual(self.power.calculate(4, -2), 0.0625)
        self.assertAlmostEqual(self.power.calculate(5, -3), 0.008) # 1/125

    def test_fractional_exponent(self):
        self.assertAlmostEqual(self.power.calculate(4, 0.5), 2)
        self.assertAlmostEqual(self.power.calculate(8, 1/3), 2)
        self.assertAlmostEqual(self.power.calculate(9, 1.5), 27) # 9 * 3

    def test_float_base_and_exponent(self):
        self.assertAlmostEqual(self.power.calculate(2.5, 1.5), 2.5 * (2.5**0.5)) # approx 3.9528
        # Example: 2.5 ^ 1.5 = 2.5 * sqrt(2.5) approx 2.5 * 1.58113883 = 3.952847075
        self.assertAlmostEqual(self.power.calculate(2.5, 1.5), 3.952847075110012)


if __name__ == '__main__':
    unittest.main()
