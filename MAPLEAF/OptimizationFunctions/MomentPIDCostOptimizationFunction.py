import pandas as pd
import numpy as np
import sys
import os

from MAPLEAF.IO import Plotting

def OptimizationFunction(logFilesList):

    #print(logFilesList)
    #print("HEEEEEYYYYYY!!!!!!", file=sys.__stdout__)
    #print(logFilesList, file=sys.__stdout__)

    filePath = logFilesList[2]
    columnSpecs = ["Time","Error"]

    columns, columnNames = Plotting.getLoggedColumns(filePath, columnSpecs, enableCache=False)

    pitchErrorIntegral = 0
    yawErrorIntegral = 0
    rollErrorIntegral = 0

    for i in range(len(columns[0])):

        if i == 0:
            pass
        
        else:
            deltaT = columns[0][i] - columns[0][i-1]
            pitchErrorIntegral += ((columns[1][i])**2)*deltaT
            yawErrorIntegral += ((columns[2][i])**2)*deltaT
            rollErrorIntegral += ((columns[3][i])**2)*deltaT
    
    #print(deltaT, file=sys.__stdout__)
    #print(pitchErrorIntegral, file=sys.__stdout__)
    #print(yawErrorIntegral, file=sys.__stdout__)
    #print(rollErrorIntegral, file=sys.__stdout__)

    cost = 100*(0.5*pitchErrorIntegral + 0.5*yawErrorIntegral + rollErrorIntegral)

    print(cost, file=sys.__stdout__)

    for logFileName in logFilesList:
        os.remove(logFileName)


    return cost