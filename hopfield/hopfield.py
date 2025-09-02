import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
from pathlib import Path
import random
N = 2 ###最终状态组数
Length = 6
Width = 6
M = Length * Width ###图像维数
b = np.zeros((M,M)) ###阈值函数

def sigma(x):
    if x >= 0:
        return 1
    else:
        return -1

def creat_pictures(flattened_data , num):
    picture_path = "pictures/"
    picture = [[flattened_data[Width * i + j] for j in range(0,Width)] for i in range(0,Length)]
    plt.imshow(picture , cmap = "gray_r")
    plt.savefig(picture_path + f"{num}.jpg")
###创建单个图像

def if_change(a , b):
    for i in range(0,len(a)):
        if a[i] != b[i]:
            return True
    return False

def patt_from_strings(rows):
    arr = []
    for r in rows:###😡
        arr.append([1 if c == "#" else -1 for c in r])
    return np.array(arr, dtype=int)
###根据存储的图像得到一个36维的向量,返回一个numpy向量
###😡这鸟地方返回的不是一个36维向量，是一个6*6矩阵，草
###可恶的AI😡😡😡害我找半天,早知道手搓了。

digit_patterns = {
    0: patt_from_strings([
        "######",
        "#....#",
        "#....#",
        "#....#",
        "#....#",
        "######",
    ]),
    1: patt_from_strings([
        "..#...",
        ".##...",
        "..#...",
        "..#...",
        "..#...",
        ".###..",
    ]),
    2: patt_from_strings([
        "####.#",
        "....#.",
        "...#..",
        "..#...",
        ".#....",
        "#####.",
    ]),
    3: patt_from_strings([
        "####..",
        "....#.",
        "..###.",
        "....#.",
        "....#.",
        "####..",
    ]),
    4: patt_from_strings([
        "#...#.",
        "#...#.",
        "#####.",
        "....#.",
        "....#.",
        "....#.",
    ]),
    5: patt_from_strings([
        "#####.",
        "#.....",
        "####..",
        "....#.",
        "....#.",
        "####..",
    ]),
    6: patt_from_strings([
        ".####.",
        "#.....",
        "####..",
        "#...#.",
        "#...#.",
        ".###..",
    ]),
    7: patt_from_strings([
        "#####.",
        "....#.",
        "...#..",
        "..#...",
        ".#....",
        ".#....",
    ]),
    8: patt_from_strings([
        ".###..",
        "#...#.",
        ".###..",
        "#...#.",
        "#...#.",
        ".###..",
    ]),
    9: patt_from_strings([
        ".###..",
        "#...#.",
        "#...#.",
        ".####.",
        "....#.",
        ".###..",
    ]),
}
###这里是0-9的36维向量
###😡6*6矩阵

unknown_num = patt_from_strings([
        "####..",
        "....#.",
        "..###.",
        "....#.",
        "....#.",
        "####..",
    ])
###这里是我们随便定义的一个数字图像

def input():
    print("hello")
###还没开始做的输入函数（主要得找训练集）

def training(datas):
    w = np.zeros((M,M))
    for i in range(0,M):
        for j in range(0,M):
            for mu in range(0,N):
                w[i][j] = datas[mu][i] * datas[mu][j] + w[i][j]
    w = w / N
    for i in range(0,M):
        w[i][i] = 0
    return w
###训练，返回权值函数
###datas为结果构成的数组

def computing(data , w , time = 0 ):
    ###算了，不写随机了，感觉好麻烦
    new_data = data.copy()
    creat_pictures(data , time)
    for i in range(0,M):
        for j in range(0,M):
            ans = w[i][j]*data[j] + w[i][j] + b[i][j] 
        new_data[i] = sigma(ans)
        time = time + 1
        creat_pictures(new_data , time)
    if if_change(new_data , data): 
        computing(new_data , w , time + 1)

###打印结果
if __name__ == "__main__":
    digits = [digit_patterns[i].flatten() for i in range(0,N)]
    w = training(digits)
    computing(unknown_num.flatten() , w)

    ###print(w)
###🤔这玩意应该还算好拓展吧🤔



