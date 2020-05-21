import numpy as np


def getCDF(data):
    for key,value in data.items():
        value = np.sort(value)
        y = np.arange(1,len(value) +1)/len(value)

    return [value.tolist(),y.tolist()]

def byPairsCDF(data):

    rdt = [[[[],[]],[[],[]]],[[[],[]],[[],[]]],[[[],[]],[[],[]]],[[[],[]],[[],[]]]]

    sc = {'method1':0,'method2':1,'method3':2,'method4':3}


    for key,value in data.items():


        for j in range(0,2):
            x = np.sort(value[j])
            y = np.arange(1,len(value[j]) +1)/len(value[j])
            i = sc[key]

            rdt[i][j][0] = x.tolist()
            rdt[i][j][1] = y.tolist()

    return rdt
