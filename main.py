import numpy as np
import pandas as pd
import timeit, gc
import matplotlib.pyplot as plt


class RealTime():

    

    def animatePlot(self):
        print('ehys')
    

    def realTimeComplex(self,stmt='pass', globals=globals(), value=40):
         
        
        result = timeit.repeat(stmt=stmt, globals=globals,repeat=value)
        
        x = np.arange(1,value+1)
        y = np.asarray(result) * 1000
        mean = np.mean(y)
        bottom90 = np.percentile(y,90)
        top10 = np.percentile(y,10)
        #write outputs to files eventually
        print(
            f"""
Mean is {round(mean,3)} ms
Bottom 90 is {round(bottom90,3)} ms
top 10 is {round(top10,3)} ms
            """ 
              )

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



    
    def complexGuess(self,looper,n,v):
        gc.disable()
        arr = np.array([])
        for x in range(n,n+v,10):
            start = timeit.default_timer()
            
            looper(x)
            end = timeit.default_timer()
            print(start)
            print(end)
            arr = np.append(arr,[end-start])


        x = np.arange(1,21)
        y = arr
        plt.scatter(x,y)
        plt.show()


        gc.enable()
        

        



def looper(n):
    for x in range(n):
        for y in range(n):
            print(x*y)

x = RealTime()

#x.realTimeComplex(stmt="looper(10)",value=10)

x.complexGuess(looper,10,200)