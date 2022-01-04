# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 18:13:36 2021

@author: Ethan Miller
011075077
"""

import numpy as np
from scipy import fftpack, signal
from matplotlib import pyplot as plt
import heartpy as hp
import pandas as pd
from scipy.io import wavfile



# 1 - FFT/IFFT Audio Signal Processing

#Primarily leveraged from lecture notes provided in class

print('\n 1 - FFT/IFFT Audio Signal Processing\n')
#creating parameters for 440Hz signal
freq1 = 440 # 440Hz
time_step=1/44100
period1 = 1/freq1
time_vec = np.arange(0, 20, time_step)

#creating 440Hz signal
sig1 = 3000*(np.sin(2 * np.pi / period1 * time_vec))

#plotting 440Hz signal
plt.figure(figsize=(20,10))
plt.title('440Hz Signal', fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, sig1)


#creating parameters for 880Hz signal
freq2 = 880 # 880Hz
period2 = 1/freq2
noise_amplitude1 = 0.75

#creating 880Hz signal
sig2 = noise_amplitude1*3000*(np.sin(2 * np.pi / period2 * time_vec))

#plotting 880Hz signal
plt.figure(figsize=(20,10))
plt.title('880Hz Signal', fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, sig2)


#creating parameters for 1000Hz signal
freq3 = 1000 # 1000Hz
period3 = 1/freq3
noise_amplitude2 = 0.50

#creating 1000Hz signal
sig3 = noise_amplitude2*3000*(np.sin(2 * np.pi / period3 * time_vec))

#plotting 1000Hz signal
plt.figure(figsize=(20,10))
plt.title("1000Hz Signal", fontsize=35)
plt.ylabel('Amplitude', fontsize=25)
plt.xlabel('Time (s)', fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(0,.01)
plt.plot(time_vec, sig3)

#combining and plotting the three signals into 1 signal
sig = sig1 + sig2 + sig3
plt.figure(figsize=(60,30))
plt.title('Combined Signals (440Hz, 8800Hz, 1000Hz)', fontsize=80)
plt.ylabel('Amplitude', fontsize=60)
plt.xlabel('Time (s)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(0,.01)
plt.plot(time_vec, sig)
plt.savefig('Combined_Signal')

#Writing the Original signal to a .wav file, found in program folder as 'Original_Sound.wav'
wavfile.write('Original_Sound.wav', 44100, sig.astype(np.int16))

#FFT of signal
sig_fft = fftpack.fft(sig)

#power
power = np.abs(sig_fft)**2

#Sample Frequency
sample_freq = fftpack.fftfreq(sig.size, d=time_step)

#plotting FFT
plt.figure(figsize=(60, 30))
plt.title('Signal in Frequency Domain', fontsize=80)
plt.ylabel('Power', fontsize=60)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(-1500,1500)
plt.plot(sample_freq, power)
plt.savefig('FFT_Unfiltered')

#finding peak frequency
pos_mask = np.where(sample_freq > 0)
freqs = sample_freq[pos_mask]
peak_freq = freqs[power[pos_mask].argmax()]

#Filtering out high frequencies
high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
filtered_sig = fftpack.ifft(high_freq_fft)

#Writing the filtered signal to a .wav file, found in program folder as 'Filtered_Sound.wav'
wavfile.write('Filtered_Sound.wav', 44100, filtered_sig.astype(np.int16))

#plotting original and filtered time domain signal
plt.figure(figsize=(60,30))
plt.title('Original and Filtered Time Domain Signals', fontsize=80)
plt.plot(time_vec, sig, label='Original signal')
plt.plot(time_vec, filtered_sig, linewidth=5, label='Filtered signal')
plt.xlabel('Time (s)', fontsize=60)
plt.ylabel('Amplitude', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(0,.01)
plt.legend(loc='best')
plt.savefig('Original_and_Filtered_Time_Domain')

#confirming filtered signal in frequency domain
sig_fft1 = fftpack.fft(filtered_sig)
power = np.abs(sig_fft1)**2
sample_freq = fftpack.fftfreq(filtered_sig.size, d=time_step)

#plotting new filtered signal in frequency domain
plt.figure(figsize=(60, 30))
plt.title('Filtered Signal in Frequency Domain', fontsize=80)
plt.ylabel('Power', fontsize=60)
plt.xlabel('Frequency (Hz)', fontsize=60)
plt.xticks(fontsize=55)
plt.yticks(fontsize=55)
plt.xlim(-1500,1500)
plt.plot(sample_freq, power)
plt.savefig('FFT_Filtered')


# 2 - Heart Rate Analysis - Time Domain Measurements

# Heartbeat .wav file acquired from: https://soundbible.com/1001-Heartbeat.html
# Converted .wav to .csv using:https://github.com/Lukious/wav-to-csv , which was provided in lecture
# Original .wav file as well as converted .csv files all found in project folder

print('\n#2 - Heart Rate Analysis - Time Domain measurements:\n')

#data converted from .wav to then read as .csv
data2 = hp.get_data('Heartbeat_Output_stereo_R.csv')

#a large sample rate is used to acquire reasonable measurements,
#i.e. a heart rate close to the average human resting heart rate
sample_rate2 = 45000

#plotting our original signal
plt.figure(figsize=(18,13))
plt.plot(data2)
plt.title('Heart Rate Signal', fontsize=60)
plt.xlabel("Time", fontsize=40)
plt.ylabel("Amplitude", fontsize=40)
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
plt.savefig('Original_Heart_Rate_Signal')
plt.show()


#processing data at given sample rate
wd, m = hp.process(data2, sample_rate2)

#plotting processed data
plt.figure(figsize=(20,11))
hp.plotter(wd, m)
plt.savefig('Heart_Rate_Signal_Peak_Detection')

print('\n Data: \n')

#acquiring measurement array and presenting it in console
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))
        
print('\n\n')