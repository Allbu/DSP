import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    fc = 400 # Hz
    fs = 8000 # Hz
    Ts = 1/fs # sampling period
    N = 128 # number of samples
    
    a = 6 # V
    t = np.linspace(0, 100, N)*Ts
    y = a*np.cos(2*np.pi*fc*t)
    
    
    ## Plot
    
    plt.plot(t, y, label='Original signal', color='black')
    plt.show()