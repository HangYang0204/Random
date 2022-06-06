import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import random


def get_random():
    '''
        function returns a random number of type float between 0 and 1
    '''
    return random.uniform(0,1)
    

def random_walkers(nWalker, nSteps, isPlotSave=False):
    ''' 
        M = number of walkers
        N = number of steps taken
        IsPlotSave : when ture the file will be saved in workspace as jpeg
    '''
    M = nWalker
    N = nSteps
    aix = [ 0*i for i in range(M)]
    for i in range(M):
        x = 0
        x2ave = [ 0*i for i in range(N)]
        #i-th walker
        for j in range(N):
            if(get_random() < 0.5):
                x += 1
            else:
                x-= 1
            x2ave[j] += x
        #plot i-th walker 
        x = np.array([i for i in range(N)])
        y = np.array(x2ave)
        # this will plot 2 seperate scatter lines on same canvas 
        # aix[i] = plt.subplot(2, 1, i + 1)
        # if(i == 0):
        #     aix[i].plot(x, y, 'o', color='blue') 
        # else:
        #     aix[i].plot(x, y, 'o', color='red') 
        if(i == 0):
            fig, aix[i] = plt.subplots()
            aix[i].plot(x, y, 'o', color='red')#primary one
        else:
            aix[i] = aix[i - 1].twinx()
            aix[i].plot(x, y, 'o', color='blue')
    
    plt.show()       
    # save the plot as a file
    if(isPlotSave):
        fig.savefig('Random_walker_demo.jpg',
                    format='jpeg',
                    dpi=100,
                    bbox_inches='tight')

#run the main method
random_walkers(2, 100, False)