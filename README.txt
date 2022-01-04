README

Ethan Miller
011075077

Module 7:

Please run Anaconda powershell prompt and pip install heartpy
Begin by running the module7.py program file.



#1 - FFT/IFFT Audio Signal Processing

All plots are found under the 'plots' tab of Spyder. Primary plots are found in the program folder. Code was leveraged from the lecture.

For this task, we wrote a python program to generate 3 tones in 1 signal. First, we wrote code to generate 3 separate signals and plotted each. The first tone was 440Hz, the second was 880Hz, and the third was 1000Hz. We then simply added the separate signals together to acquire a combined 3-tone signal. This can be found in the program file as 'Combined_Signal.png'. The signal was converted to a CSV file found in the program file as 'Original_Signal.csv', and was also converted into a WAV file as 'Original_Sound.wav'. Next, FFT was applied to the signal thus showing the signals in the frequency domain. This can be found in the program file as 'FFT_Unfiltered.png'. We then used the method of filtering out high frequencies discussed in lecture to acquire a filtered Time domain, and filtered frequency domain plot. These can be found in the program folder as 'Original_and_Filtered_Time_Domain.png', and 'FFT_Filtered.png'. The filtered Signal was finally converted to WAV, found in the program folder as 'Filtered_Sound.wav'.


Note: we conclude that this task was a success as we started with a signal of 3 tones: 440 Hz, 880 Hz, and 1000 Hz. The 'Original_Sound.wav' file noticeably has 3 tones playing at once. The filtered signal only contains the lowest frequency: 440 Hz. This is also apparent when we listen to 'Filtered_Sound.wav', and only hear the single lowest tone.



#2 - Heart Rate Analysis – Time Domain Measurements

Wav file acquired from: https://soundbible.com/1001-Heartbeat.html. 
Original wav file can be found in program folder as 'Heartbeat-SoundBible.com-1259675634.wav'
WAV to CSV was converted using: https://github.com/Lukious/wav-to-csv , which was provided in lecture.


For this task, we were asked to convert a WAV file of a heartbeat to CVS, plot the heart rate signal, and acquire time-domain measurements. First we acquired a .wav file of a hearbeat, which was then converted to csv using the above mentioned code, found in the program folder as 'Heartbeat_Output_stereo_R.csv'. With this data, we plotted the original heart rate signal, found in the program folder as 'Original_Heart_Rate_Signal.png'. The csv data was then processed using the heartpy module, and measurements were placed in the console. A saved image of the measurements is found in the program folder as 'Measurements.png'. Another heart rate signal plot was made which included peak detection found as 'Heart_Rate_Signal_Peak_Detection.png'. 


Note: We conclude that this task was a success because we successfully utilized csv info converted from a wav file to acquire reasonable measurements as designated by the rubric. It is important to note that we used a high sample rate to acquire accurate measurements, primarily noted by the measured BPM being 85, which is within the resting heart rate for humans.

