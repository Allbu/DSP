import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
        
        # Main signal
        fc = 60
        fs = 1000
        # Sampling time
        Ts = 1/fs
        N = 100
        t = np.linspace(0, 100, N)*Ts 
        
        y = 5 * np.sin(2 * np.pi * fc * t)
        
        '''
        The signal flip in the x-axis is used to invert the signal in the x-axis.
        It is a simple operation that can be done by multiplying the time vector by -1.
        e.g: t = np.linspace(0, 100, N)*Ts * -1
        '''
        
        t_1 = -1*t # signal flip in the x-axis
        
        plt.figure()
        plt.subplot(2,1,1)
        plt.plot(t, y, label='Original Signal')
        plt.legend()
        plt.subplot(2,1,2)
        plt.plot(t_1, y, label='Flipped Signal')
        plt.legend()
        plt.show()