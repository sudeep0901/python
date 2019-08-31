import numpy as np
import pandas as pd

jobData = pd.read_csv("jobData.csv")
print(jobData['JobName'])
jobData.index = jobData['JobName']
threshold = 20

jobMatrix = np.zeros(shape=(len(jobData),len(jobData)))


def processNode(idx, inputFrame ):
    # print(idx)
    # print(len(inputFrame))
    localIndex = idx + 1
    tempsum = inputFrame[idx + 1]
    for index in range(maxElem - idx) :
        # print(index, item)
        if (tempsum <= threshold):
            jobMatrix[idx][localIndex] = 1
            if localIndex < (maxElem):
                tempsum = inputFrame[localIndex] + inputFrame[localIndex + 1]
        else:
            break

        localIndex += 1

# indx = 0

maxElem = len(jobData) - 1
for indx in range(maxElem):
    tempFrame = jobData['Duration']
    processNode(indx,tempFrame)
    # indx += 1


# print(jobMatrix)

columns = jobData['JobName']
# print(jobData.index)
# print(columns[0:])
jobMatrixDf  = pd.DataFrame(jobMatrix, columns=columns, index=jobData.index )
print(jobMatrixDf.columns)
