import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://www.lookintobitcoin.com/django_plotly_dash/app/rhodl_ratio/_dash-layout"
x = requests.get(url).json()

#{"props": {"children": [{"props": {"id": "rhodl_ratio", "figure": {"data": [1

with open('netData.json', 'w') as outfile:
    json.dump(x, outfile)

f = open('netData.json')
data = json.load(f)
rholdData = data['props']['children'][0]['props']['figure']['data'][1]

with open('rholdRatio.json', 'w') as outfile:
    json.dump(rholdData, outfile)

#gather the x values - dates
rholdX = rholdData['x']
numDates = len(rholdX)
firstDateI = 0
lastDateI = numDates - 1

#gather the y values - ratio data
rholdY = rholdData['y']
numVals = len(rholdY)
firstValI = 0
lastValI = numVals - 1

if numDates < numVals:
    lastValI = lastDateI
else:
    lastDateI = lastValI

j = 0
rholdXRevised = []
for i in range(firstDateI, lastDateI + 1):
    rholdXRevised.append(rholdX[i])
    # check that the numbers are aligned
    # if rholdXRevised[i] == "2017-12-13":
    #     j = i
    #     print(j)

rholdYRevised = []
for i in range(firstValI, lastValI + 1):
    rholdYRevised.append(rholdY[i])
    # if i == j:
    #     print(rholdYRevised[i])

# print('num vals: ', len(rholdYRevised))
# print('num dates: ', len(rholdXRevised))
# print('last val I: ', lastValI)
# print('last date I: ', lastDateI)

print('most recent RHODLR:', rholdYRevised[lastValI])
temp = rholdYRevised[lastValI]
# variables["rholdValue"] = temp


# xpoints = np.array(rholdXRevised)
# ypoints = np.array(rholdYRevised)

# plt.plot(xpoints, ypoints)
# plt.show()v