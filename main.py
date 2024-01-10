import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class RealTime():
    
    def animatePlot(self, x, y,time=.1,plotter='scatter',color='black'):
        xplace = np.array([])
        yplace = np.array([])

        for z in range(len(x)):
            xplace = np.append(xplace,x[z])
            yplace = np.append(yplace,y[z])
            if plotter == 'scatter':
                plt.scatter(xplace, yplace, c=color)
            else:
                plt.plot(xplace, yplace, c=color)
            plt.draw()
            plt.pause(time)
            
        plt.show()

    def animateHist(self, x, time=.1,color='black'):
        xplace = np.array([])

        for z in range(len(x)):
            xplace = np.append(xplace,x[z])
            plt.hist(xplace, color=color)
            plt.draw()
            plt.pause(time)
            
        plt.show()

    
    def animateRealTime():
        pass



x = np.arange(0, 10, 0.1)
y = np.sin(x)


time = RealTime()

#time.animatePlot(x,y)


x = np.random.normal(100, 20, 250)

time.animateHist(x)