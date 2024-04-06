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
    The signal flip in the y-axis is used to invert the signal in the y-axis.
    It is a simple operation that can be done by multiplying the signal by -1.
    e.g: y = 5 * np.sin(2 * np.pi * fc * t) * -1
    
    NOTE: It does NOT modify the avareage of the signal.
    '''
    
    y_1 = -1*y # signal flip in the y-axis
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t, y, label='Original Signal')
    plt.legend()
    plt.subplot(2,1,2)
    plt.plot(t, y_1, label='Flipped Signal')
    plt.legend()
    plt.show()