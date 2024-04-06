import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fc = 60
    fs = 6000
    # Sampling time
    Ts = 1/fs
    N = 100
    t = np.linspace(0, 100, N)*Ts
    y = 5 * np.sin(2 * np.pi * fc * t)
    
    '''
    The signal contraction happens when the argument of the signal is multiplied by a 
    constante value > 1.
    '''
    
    y_1 = 5*np.sin(2*np.pi*fc*t * 10) # signal contraction by 2
    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t, y, label='Original Signal')
    plt.legend()
    plt.subplot(3,1,2)
    plt.plot(t, y_1, label='Contracted Signal')
    plt.legend()
    plt.subplot(3,1,3)
    plt.plot(t, y, label='Original signal')
    plt.legend()
    plt.plot(t, y_1, label='Contracted Signal')
    plt.legend()
    plt.show()