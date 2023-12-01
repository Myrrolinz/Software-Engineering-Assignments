# -*- coding: UTF-8 -*-
"""
@Project ：作业二
@File ：main.py
@Author ：Yunmei Guan
@Date ：2023/5/13 16:06
"""
from ast import literal_eval
import numpy as np

class MaxProduct:
    """
    乘积最大子数组
    """
    def __init__(self):
        """初始化"""
        self.num=[]
        self.nums=[]
        self.max_dp=0
        self.min_dp=0
        self.ans_dp=0
        self.shape=0

    def set(self,in_num):
        """赋值输入数组"""
        self.nums=in_num
        self.shape=np.array(self.nums).ndim

    def calculate_list(self):
        """计算乘积最大子数组的值"""
        if len(self.num) <= 1:
            self.ans_dp=self.num[0]
        self.max_dp,self.min_dp,self.ans_dp = self.num[0],self.num[0],self.num[0]
        for i in range(1, len(self.num)):
            self.max_dp,self.min_dp= max(self.max_dp * self.num[i], self.num[i], self.min_dp * self.num[i]),\
                                     min(self.max_dp * self.num[i], self.num[i],self.min_dp * self.num[i])
            self.ans_dp = max(self.ans_dp, self.max_dp)
        return self.ans_dp

    def calculate(self):
        """对输入数列处理后计算MP"""
        if self.shape==1:
            self.num=self.nums
            print(self.num)
            return self.calculate_list()
        if self.shape==2:
            ans_list=[]
            for i in range(self.shape):
                self.num=self.nums[i]
                ans_list.append(self.calculate_list())
            return max(ans_list)
        print("Program error!")
        return TypeError


    def get_ans(self):
        """返回计算结果"""
        return self.ans_dp

def pipline(input_nums):
    """计算流水线"""
    my_mp=MaxProduct()
    my_mp.set(input_nums)
    return my_mp.calculate()

def get_list(the_set):
    """
    :param the_set: 要处理的集合
    :return:最大的数
    """
    return pipline(the_set)

def get_in():
    """获取输入数组
       包括错误处理
    """
    inlist=[]
    try:
        inlist=literal_eval(input("please input a One-dim Or Two-dim array："))
    except (SyntaxError, ValueError):
        print("error input！")
    except TypeError:
        print("Format error!")
    if isinstance(inlist,tuple):
        inlist=list(inlist)
    elif isinstance(inlist,int):
        inlist=[inlist]
    elif isinstance(inlist, list):
        temp=np.array(inlist)
        if len(temp.shape) == 1:
            for index in inlist:
                try:
                    assert isinstance(index, (int, float))
                except AssertionError:
                    print("error input!")
        elif len(temp.shape)==2:
            for index_1 in inlist:
                for index_2 in index_1:
                    try:
                        assert isinstance(index_2,(int,float))
                    except AssertionError:
                        print("error input!")
        else:
            print("本程序仅支持一维数组和二维数组")
            return TypeError
    else:
        print("error input！")
        return TypeError
    return inlist


if __name__=='__main__':
    #获取一组数，用list存储
    nums=get_in()
    """执行计算"""
    print(pipline(nums))
