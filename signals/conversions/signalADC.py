import numpy as  np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    
    # Main signal
    fc = 1
    fs = 140
    
    # Sampling time
    Ts = 1/fs
   
    '''
    The number of samples is defined by the variable N, N depends on how many bits
    you have. The more bits you have, the more samples you will have. N = 2^b, where
    b is the number of bits. 
    '''   
    b = 3 # 10 bits
    N_1 = pow(2,b) # number of samples = 1024
    N_2  = pow(2,b-1) # number of samples = 256 
    
    N = 1000
    t = np.linspace(0, 1, N)
    np.pi
    t_1 = np.linspace(0, 1, N_1)
    t_2 = np.linspace(0, 1, N_2)
    
    y = 5 * np.sin(2 * np.pi * fc * t)
    y_1 = 5 * np.sin(2 * np.pi * fc * t_1)
    y_2 = 5 * np.sin(2 * np.pi * fc * t_2)

    
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(t, y, label='Original Signal')
    plt.legend()
    plt.subplot(3,1,2)
    plt.stem(t_1, y_1, label='Digital Signal for 3 bits')
    plt.legend()
    plt.subplot(3,1,3)
    plt.stem(t_2, y_2, label='Digital Signal for 2 bits')
    plt.legend()
    plt.show()