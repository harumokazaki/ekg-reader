from scipy.signal import find_peaks
import wfdb
import matplotlib.pyplot as plt
import numpy as np
record = wfdb.rdrecord('100', pn_dir='mitdb', sampto=3600) # Import's the recording from MIT Database
lead_names = record.sig_name
signal = record.p_signal[:, :] #Takes both leads (Electrodes)
fs = record.fs #360 Samples Per Second
t = np.arange(len(signal)) / fs #Turns what would be samples into seconds for easier intepretation in the data
plt.plot(t, signal[:, 0], label=record.sig_name[0]) #Takes the signal name from the DB to avoid hardcoding
plt.plot(t, signal[:, 1], label=record.sig_name[1])
plt.legend() #Since I have two signals I need this function to separate between the two
plt.xlabel('Seconds'); plt.ylabel('mV')
preferred_leads = ['MLII', 'II', 'V5', 'V4', 'V1'] #Ranks the strongest Lead for accurate reading of the heartbeat
for lead in preferred_leads: #Uses the lead variable as a container while searching through the names
    if lead in lead_names: 
        index = lead_names.index(lead) #If found, looks at what lead is and looks into lead_names to find the exact array number
        break
peaks, rpeak = find_peaks(signal[:, index], height=0.1) #Detects every single peak above the 0.1mV threshold
plt.plot(t[peaks], signal[peaks, index],'xr') #Takes the X value from Peaks, and finds what array is stored in Index for the mV (Y value)
#t[peaks] Looks at what peaks were found from find_peaks the 't' returns the time(seconds). At which the peak happened (X value)
plt.show()