# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：unittestTest.py
@Author ：Yunmei Guan
@Date ：2023/5/13 18:18
"""


import unittest
import main
from unittest.mock import patch


class Testing(unittest.TestCase):
    """
    测试
    """

    def test_pipline(self):
        """一维"""
        self.assertEqual(main.pipline([-1, 2, 3, -4]),24)
        self.assertEqual(main.pipline([1, 2, 3, 4]),24)
        self.assertEqual(main.pipline([-1, 2, -5, 3, -4]),120)
        self.assertEqual(main.pipline([-1, 20, 0, 30, -4]),30)
        self.assertEqual(main.pipline([-2, -3, -5, -1, -9]),135)
        self.assertEqual(main.pipline([-2.0, -3.0, -5.0, -1.0, -9.0]),135.0)
        self.assertEqual(main.pipline([-2.0, -3.0, -5.0, -1, -9]),135.0)
        """二维"""
        self.assertEqual(main.pipline([[1,2,3],[0,1,2]]),6)
        self.assertEqual(main.pipline([[1, 2, 3,4], [0, 1, 2,4]]), 24)
        self.assertEqual(main.pipline([[-1.0,-2.0,7],[1,2,0]]),14.0)


    @patch('builtins.input')
    def test_in(self, mock_input):
        mock_input.return_value = '1'
        self.assertEqual(main.get_in(), [1])

        mock_input.return_value = '[1, 2]'
        self.assertEqual(main.get_in(), [1, 2])

        mock_input.return_value = '[1, 2, 0]'
        self.assertEqual(main.get_in(), [1, 2, 0])

        mock_input.return_value = '[[1, 2,-3],[0,1,2]]'
        self.assertEqual(main.get_in(), [[1, 2,-3],[0,1,2]])

        mock_input.return_value = '(1, 2)'
        self.assertEqual(main.get_in(), [1, 2])

    @patch('builtins.input')
    def test_error(self, mock_input):

        mock_input.return_value = '[1, 2 ,'
        self.assertRaises(BaseException, main.get_in(), TypeError)

        mock_input.return_value = '[[-50.0, 3.0, 34.0], ' \
                                  '[-3.0, 25.0, -25.0, 50.0, -34.0], [-8.0, 9.0, 7.0, -31.0, -2.0]])'
        self.assertRaises(BaseException, main.get_in(), TypeError)

        mock_input.return_value = "['a', 'b', 'c']"
        self.assertRaises(BaseException, main.get_in(), AssertionError)

        mock_input.return_value = "[['a'], ['b']]"
        self.assertRaises(BaseException, main.get_in(), AssertionError)

        mock_input.return_value = '[[1], [2], [3]]'
        self.assertRaises(BaseException, main.get_in(), TypeError)


if __name__ == "__main__":
    suite = unittest.TestSuite()

    tests = [Testing("test_pipline"), Testing("test_in"),Testing("test_error")]
    suite.addTests(tests)

    with open('./TestResult.txt','w') as file:
        runner = unittest.TextTestRunner(stream=file, verbosity=2)
        runner.run(suite)