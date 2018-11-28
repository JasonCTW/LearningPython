'''
Author ：SunJie
'''

from python_learn.tools import HTMLTestRunner
import time
import os
import unittest


case_path = os.path.join(os.getcwd())
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 2、html报告文件路径
report_path = os.path.join(os.getcwd(), 'report')
report_abspath = os.path.join(report_path, "result_"+now+".html")
# 3、打开一个文件，将result写入此file中
fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试', description=u'测试')
runner.run(discover)
fp.close()

