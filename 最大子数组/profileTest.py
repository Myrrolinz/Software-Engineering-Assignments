# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：profileTest.py
@Author ：Yunmei Guan
@Date ：2023/5/13 16:24
"""

import yappi
import numpy as np
import main


yappi.clear_stats()
test1 = [np.random.randint(1, 1000) for i in range(100000)]
test2 = [np.random.rand() for i in range(100000)]

yappi.start()
main.get_list(test1)
yappi.stop()
stats = yappi.convert2pstats(yappi.get_func_stats())
stats.sort_stats("cumulative")
stats.print_stats()

yappi.start()
main.get_list(test2)
yappi.stop()
stats = yappi.convert2pstats(yappi.get_func_stats())
stats.sort_stats("cumulative")
stats.print_stats()


