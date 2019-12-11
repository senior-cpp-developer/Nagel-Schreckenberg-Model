from scipy import stats
import numpy as np

def calculateAvg(results):
    speed50 = []
    speed80 = []
    speed100 = []
    speed130 = []

    for timeSamp in results:
        speedCounter = 0
        for item in timeSamp:
            if speedCounter == 0:
                speed50.append(item)
            elif speedCounter == 1:
                speed80.append(item)
            elif speedCounter == 2:
                speed100.append(item)
            elif speedCounter == 3:
                speed130.append(item)
            speedCounter += 1
    print(np.mean(speed50))
    print(np.mean(speed80))
    print(np.mean(speed100))
    print(np.mean(speed130))

    print(stats.mode(speed50))
    print(stats.mode(speed80))
    print(stats.mode(speed100))
    print(stats.mode(speed130))

    print('SD')
    print(np.sqrt((np.mean(abs(speed50 - np.mean(speed50) ** 2)))/len(speed50)))
    print(np.sqrt((np.mean(abs(speed80 - np.mean(speed80) ** 2)))/len(speed80)))
    print(np.sqrt((np.mean(abs(speed100 - np.mean(speed100) ** 2)))/len(speed100)))
    print(np.sqrt((np.mean(abs(speed130 - np.mean(speed130) ** 2)))/len(speed130)))



