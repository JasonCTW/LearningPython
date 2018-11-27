"""
Author ：SunJie
在3里面，我写了一个testcase，但是我可能会有一堆testcase一起跑
所以，我这边用testsutie（testcase容器），然后直接跑这个testsuite
"""

import unittest
from python_learn.python_learn_3 import Mytest
from python_learn.python_learn_3_copy import Mytest as Mytest_copy


def suite():
    test_suite = unittest.TestSuite()  # 申明一个testsuite
    test_suite.addTest(Mytest('test_a_one'))  # 把第一个测试case添加进testsuite
    test_suite.addTest(Mytest_copy('test_a_one_copy'))  # 把第二个测试case添加进testsuite
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())  # 运行suite
