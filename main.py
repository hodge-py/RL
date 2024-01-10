import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class RealTime():
    
    def animatePlot(self, x, y,time=.1,plotter='scatter'):
        xplace = np.array([])
        yplace = np.array([])

        for z in range(len(x)):
            xplace = np.append(xplace,x[z])
            yplace = np.append(yplace,y[z])
            if plotter == 'scatter':
                plt.scatter(xplace, yplace)
            else:
                plt.plot(xplace, yplace)
            plt.draw()
            plt.pause(time)
            
        plt.show()


x = np.arange(0, 10, 0.1)
y = np.sin(x)


time = RealTime()

time.animatePlot(x,y,plotter='plot')