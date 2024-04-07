import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    '''
    Sometimes, the trade off of Analogic to digital conversion is the number of bits
    that will be used versus the sample frequency (Fs). When higher the number of bits
    less the sample frequency you may need to get the signal.
    '''
    
    # Original signal with fundamental frequency fc = 10 Hz
    fc = 10
    t = np.linspace(-1, 1, 10_000)
    y = np.sin(2*np.pi*fc*t)
    
    # Sampling time with Fs = 100*fc 
    Fs = 10000 * fc
    Ts_1 = 1/Fs
    
    # Calculate the number of samples to skip for each sample in the sampled signal
    skip = int(np.round(Ts_1 / (t[1] - t[0])))
    
    y_sampled = np.zeros(len(t)) # Initialize it
    
    # Iterate over the indices of the t array
    for i in range(0, len(t)):
        y_sampled[i] = y[i]
    
    # Number of samples 2^Nº_bits
    n_bits = 7
    N = pow(2,n_bits)
    
    y_digital = np.zeros(len(t))
    
    skip = int(np.round(len(y_sampled)/N))
    
    for i in range(0, len(t), skip):
        y_digital[i] = y_sampled[i]
    
    '''
    Here, we use different sample frequencies and number of bits 
    to get the signal.
    '''
    
    # Sampling time with Fs = 10*fc
    Fs = 10 * fc
    Ts_2 = 1/Fs
    
    # Calculate the number of samples to skip for each sample in the sampled signal
    skip = int(np.round(Ts_2 / (t[1] - t[0])))
    
    y_less_sampled = np.zeros(len(t)) # Initialize it
    
    for i in range(0, len(t), skip):
        y_less_sampled[i] = y[i]
    
    # Number of samples 2^Nº_bits
    n_bits = 10
    N = pow(2,n_bits)
    
    y_digital_high = np.zeros(len(t))
    
    skip = int(np.round(len(y_less_sampled)/N))
    
    for i in range(0, len(t), skip):
        y_digital_high[i] = y_less_sampled[i]
    
    y_high_reconstructed_signal = y_digital_high[y_digital_high != 0]
    y_reconstructed_signal = y_digital[y_digital != 0]
    
    plt.figure(figsize=(10,5))
    plt.subplot(4,1,1)
    plt.plot(t, y, label='Original signal')
    plt.legend()
    plt.subplot(4,2,3)
    plt.plot(t, y_sampled, label='Sampled signal for Fs = 10000*fc')
    plt.legend()
    plt.subplot(4,2,5)
    plt.stem(t, y_digital, label='Digital signal for N = 2^7 bits')
    plt.legend()
    plt.subplot(4,2,4)
    plt.plot(t, y_less_sampled, label='Sampled signal for Fs = 10*fc')
    plt.legend()
    plt.subplot(4,2,6)
    plt.stem(t, y_digital_high, label='Digital signal for N = 2^10 bits. Ignore the x-dimensional axis')
    plt.legend()
    plt.subplot(4,2,7)
    plt.plot(y_reconstructed_signal, label='Digital signal simple reconstruction. Ignore the x-dimensional axis')
    plt.legend()
    plt.subplot(4,2,8)
    plt.plot(y_high_reconstructed_signal, label='Digital signal high reconstruction')
    plt.legend()
    plt.show()
    