import numpy as np
import pandas as pd
import timeit
import matplotlib.pyplot as plt


class RealTime():

    

    def animatePlot(self):
        print('ehys')
    

    def realTimeComplex(self,stmt='pass', globals=globals(), value=40,number=1):
         
        
        result = timeit.repeat(stmt=stmt, globals=globals,repeat=value, number=number)

        
        
        x = np.arange(1,value+1)
        y = np.asarray(result)
        mean = np.mean(y)
        print(mean)
        bottom90 = np.percentile(y,90)
        top10 = np.percentile(y,10)


        m, b = np.polyfit(x, y, 1)
        plt.scatter(x,y,zorder=0)
        plt.plot(x,m*x+b,zorder=3,c='green')
        plt.grid(zorder=-1.0)
        plt.axhline(y=mean, zorder=4)
        plt.axhline(y=bottom90,c='red')
        plt.axhline(y=top10,c='purple')
        plt.xlabel("Runs")
        plt.ylabel("Time (ms)")
        plt.show()


    
    def animateRealTime():
        pass




def looper():
    for x in range(100):
        print(x*x)


x = RealTime()

x.realTimeComplex(stmt='looper()',value=500)