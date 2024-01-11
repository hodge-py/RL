import numpy as np
import pandas as pd
import time as newTime



class RealTime():
    
    def animatePlot(self, x, y,time=.1,plotter='scatter',color='black'):
        #xplace = np.array([])
        #yplace = np.array([])


        for z in range(len(x)):
            newTime.sleep(1)
            x = np.arange(0, 10, 0.1)
            y = np.sin(x)
            
    

    def animateHist(self, x, time=.1,color='black'):
        xplace = np.array([])
        
        
        for z in range(len(x)):
            pass


    
    def animateRealTime():
        pass


   

x = np.arange(0, 10, 0.1)
y = np.sin(x)


time = RealTime()

time.animatePlot(x,y)


#x = np.random.normal(100, 20, 250)

#time.animateHist(x)