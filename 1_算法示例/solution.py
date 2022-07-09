class NBClassify(object):
    def train(self, trainSet):
        # 计算每种类别的概率
        # 存放每种类别的数量
        dictTag = {}
        for subTuple in trainSet:
            dictTag[str(
                subTuple[1])] = 1 if str(subTuple[1]) \
                    not in dictTag.keys() \
                        else dictTag[str(subTuple[1])] + 1
        # 存放每种类别的概率
        tagProbablity = {}
        totalFreq = sum([value for value in dictTag.values()])
        for key, value in dictTag.items():
            tagProbablity[key] = value / totalFreq
        self.tagProbablity = tagProbablity

        # 计算特征的条件概率
        # 存放每种特征的不同值的频率
        dictFeaturesBase = {}
        for subTuple in trainSet:
            for key, value in subTuple[0].items():
                if key not in dictFeaturesBase.keys():
                    dictFeaturesBase[key] = {value: 1}
                else:
                    if value not in dictFeaturesBase[key].keys():
                        dictFeaturesBase[key][value] = 1
                    else:
                        dictFeaturesBase[key][value] += 1
        # 存放每种类别的每种特征的不同值的频率
        dictFeatures = {}.fromkeys([key for key in dictTag])
        for key in dictFeatures.keys():
            dictFeatures[key] = {}.fromkeys([key for key \
                in dictFeaturesBase])
        for key, value in dictFeatures.items():
            for subkey in value.keys():
                value[subkey] = {}.fromkeys(
                    [x for x in dictFeaturesBase[subkey].keys()])
        for subTuple in trainSet:
            for key, value in subTuple[0].items():
                dictFeatures[subTuple[1]][key][value] = 1 if \
                    dictFeatures[subTuple[1]][key][value] \
                        == None else \
                            dictFeatures[subTuple[1]][key][value] + 1
        # 由特征频率计算特征的条件概率
        for _, featuresDict in dictFeatures.items():
            for featureName, fetureValueDict in featuresDict.items():
                totalCount = sum(
                    [x for x in fetureValueDict.values() if x != None])
                for featureKey, featureValues in \
                    fetureValueDict.items():
                    fetureValueDict[featureKey] = \
                        featureValues / totalCount \
                            if featureValues != None else None
        self.featuresProbablity = dictFeatures

    def classify(self, featureDict):
        # 存放每个类的条件概率
        resultDict = {}
        # 计算每个类的条件概率
        for key, value in self.tagProbablity.items():
            iNumList = []
            for f, v in featureDict.items():
                if self.featuresProbablity[key][f][v] == None:
                    iNumList.append(0)
                else:
                    iNumList.append(self.featuresProbablity[key][f][v])
            conditionPr = 1
            for iNum in iNumList:
                conditionPr *= iNum
            resultDict[key] = value * conditionPr
        # 对比每个类的条件概率值，取最大者
        resultList = sorted(resultDict.items(),
                            key=lambda x: x[1],
                            reverse=True)
        return resultList[0][0]


if __name__ == '__main__':
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
    result = baiveBayes.classify(
        {"身高": "高", "体重": "中", "鞋码": "中"})
    print("此人性别为:", result)
