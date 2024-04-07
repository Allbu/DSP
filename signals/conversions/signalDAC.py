import numpy as np
import matplotlib.pyplot as plt
import math

def rect(t, Ts, shift_value):
    return np.where(np.abs(t-shift_value) <= 0.5*Ts, 1, 0)

if __name__ == '__main__':
    
  
    # Original signal with fundamental frequency fc = 10 Hz
    fc = 10
    t = np.linspace(-1, 1, 10_000)
    y = np.sin(2*np.pi*fc*t)
    
    # Sampling time Fs > 2*fc ''''Aliasing = Fs <= 2*fc'''
    Fs = 5 * fc
    Ts = 1/Fs
    
    # Calculate the number of samples to skip for each sample in the sampled signal
    skip = int(np.round(Ts / (t[1] - t[0])))

    y_sampled = np.zeros(len(t)) # Initialize it

    # Iterate over the indices of the t array
    for i in range(0, len(t), skip):
        y_sampled[i] = y[i]
    
    # Number of samples 2^Nº_bits
    n_bits = 10
    N = pow(2,n_bits)
    y_digital = np.zeros(len(t))
    
    skip = int(np.round(len(y_sampled)/N))
    for i in range(0, len(t), skip):
        y_digital[i] = y_sampled[i]
    
    '''
    Reconstruct with ZOH and SINC
    
    U(t) = Π((t - 0.5Ts)/Ts) -- ZOH ====> A*rect((t - 0.5*Ts)/Ts)
    S(T) = h(t) = sinc(t/Ts) -- SINC
    '''
    
    # Return to sampled signal. Because we are treating it as it doesn't have errors
    # in reconstruction the digital signal is the same one of the sampled signal
    y_digital_sampled = y_digital
    
    # Get the time where the sample is not zero
    non_zero_indices = []
    for i in range(0, len(t)):
        if(y_digital_sampled[i] != 0):
            non_zero_indices.append(t[i])

    '''
    Define the reconstructed signal by using ZOH: 
    Multiply each impulse of the sampled signal 
    by a rect function centered at the time
    
    The impulse will increase or decrease the amplitude of the signal
    and if it has a phase/delay, it will shift the signal in time/frequency 
    '''
    y_rect = np.zeros(len(t))
    iterator = 0
    
    # Multiply each impulse by a rect function and sum them getting the reconstructed signal
    for individual_sample in y_digital_sampled[y_digital_sampled != 0]:
        y_rect += individual_sample * rect(t, Ts, non_zero_indices[iterator])
        iterator += 1
    
    '''
    Define the reconstructed signal by using SINC: 
    Multiply each impulse of the sampled signal 
    by a sinc function centered at the time
    
    The impulse will increase or decrease the amplitude of the signal
    and if it has a phase/delay, it will shift the signal in time/frequency 
    '''
    
    y_sinc = np.zeros(len(t))
    iterator = 0
    
    # Multiply each impulse by a rect function and sum them getting the reconstructed signal
    for individual_sample in y_digital_sampled[y_digital_sampled != 0]:
        y_sinc += individual_sample * np.sinc((t - non_zero_indices[iterator])/Ts)
        iterator += 1
    
    # Plot the signals
    plt.figure(figsize=(100,100))
    plt.subplot(3,2,1)
    plt.plot(t, y, label='Original Signal')
    plt.legend()
    plt.subplot(3,2,3)
    plt.stem(t, y_sampled, label='Sampled Signal', markerfmt='^')
    plt.legend()
    plt.subplot(3,2,5)
    plt.stem(t, y_digital, label='Digital Signal')
    plt.legend()
    plt.subplot(3,2,2)
    plt.stem(t, y_digital_sampled, label='Resampled Signal', markerfmt='^')
    plt.legend()
    plt.subplot(3,2,4)
    plt.plot(t, y_rect, label='Reconstructed Signal (ZOH)')
    plt.legend()
    plt.subplot(3,2,6)
    plt.plot(t, y_sinc, label='Reconstructed Signal (SINC)')
    plt.legend()
    plt.show()