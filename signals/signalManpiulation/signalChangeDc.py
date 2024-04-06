import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    
    fc = 400 # Hz
    fs = 8000 # Hz
    Ts = 1/fs # sampling period
    N = 128 # number of samples
    
    a = 6 # V
    t = np.linspace(0, 100, N)*Ts
    y = a*np.cos(2*np.pi*fc*t)
    
    #plt.subplot(2,1,1)
    plt.plot(t, y, label='Original signal', color='black')
    
    
    # Manipulation: Add a DC component to the signal
    '''
        THe dc component of the signal is the average value of the signal.
        If i wnat to add a DC component to the signal, i will add a constant value to the signal.
        e.g: y = y + 5
    '''
    #plt.subplot(2,1,2)
    y_1 = y + 2
    
    
    plt.plot(t, y_1 , label='Extra DC signal', color='blue')
    plt.show()
    
    y_mean = np.mean(y)
    y_1_mean = np.mean(y_1)
    
    print('Mean of y: ', math.floor(y_mean))
    print('Mean of y_1: ',  math.floor(y_1_mean))