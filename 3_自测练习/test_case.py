#!/usr/bin/env python3

from my_solution import NBClassify

# 测试用例
def test_solution():
    # 数据集(featureDict, tag)
    trainSet = [
        ({"身高": "高","体重": "重","鞋码": "大"}, "男"),
        ({"身高": "高","体重": "重","鞋码": "大"}, "男"),
        ({"身高": "中","体重": "中","鞋码": "大"}, "男"),
        ({"身高": "中","体重": "中","鞋码": "中"}, "男"),
        ({"身高": "矮","体重": "轻","鞋码": "小"}, "女"),
        ({"身高": "矮","体重": "轻","鞋码": "小"}, "女"),
        ({"身高": "矮","体重": "中","鞋码": "中"}, "女"),
        ({"身高": "中","体重": "中","鞋码": "中"}, "女"),
    ]

    baiveBayes = NBClassify()
    baiveBayes.train(trainSet)
    # 正确答案
    correct_solution = "男"
    # 程序求解结果
    result=baiveBayes.classify(
        {"身高": "高",
         "体重": "中",
         "鞋码": "中"})
    assert correct_solution == result