#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# 
# 生成GIF
# 
# author Cheetah
# version: v 0.1.0
# date 2020-06-18 21:26
#
import re
import os
import imageio


def try_int(s):  # 将元素中的数字转换为int后再排序
    try:
        return int(s)
    except ValueError:
        return s


def str2int(v_str):  # 将元素中的字符串和数字分割开
    return [try_int(sub_str) for sub_str in re.split('([0-9]+)', v_str)]


def sort_humanly(v_list):  # 以分割后的list为单位进行排序
    return sorted(v_list, key=str2int)


if __name__ == '__main__':

    dir_location = 'frames/'
    filenames = os.listdir(dir_location)
    path_files = []
    for filename in filenames:
        filename = filename.split('.')
        if filename[-1] == 'png':
            filename = str.join('.', filename)
            path_files.append(dir_location + filename)
    path_files = sort_humanly(path_files)

    gif_images = []
    for path in path_files:
        gif_images.append(imageio.imread(path))
    imageio.mimsave("test.gif", gif_images, fps=20)  # fps 50, is 20ms gap.
