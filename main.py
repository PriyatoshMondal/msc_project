import json as js
from utilityFun import inputTaker, checkDataAndReturn

dictInput = inputTaker()
file = open('./1kf1_metbp_01.json')
fileData = js.load(file)
res = checkDataAndReturn(dictInput, fileData)
print(res)