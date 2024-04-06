import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Main signal
    fc = 60
    fs = fc
    # time
    Ts = int(1/fs)
    N = 100
    t = np.linspace(0, 2*np.pi, N) 
    
    y = 5 * np.sin(2 * np.pi * fc * t)
    
    plt.plot(t, y, label='Original signal', color='black')
    plt.show()