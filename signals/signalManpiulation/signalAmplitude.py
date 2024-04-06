import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    # Main signal
    fc = 60
    fs = 120
    # Sampling time
    Ts = 1/fs
    N = 100
    t = np.linspace(0, 100, N)*Ts 
    
    y = 5 * np.sin(2 * np.pi * fc * t)
    
    '''
    The signal amplification is used to increase the amplitude of the signal.
    It is a simple operation that can be done by multiplying the signal by a constant.
    e.g: y = 5 * np.sin(2 * np.pi * fc * t) * (constant = 4) 
    
    NOTE: It does NOT modify the avareage of the signal.
    '''
    
    y_1 = 4*y # signal amplification by 4
    
    
    
    
    
    