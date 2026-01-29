import numpy as np

def fft_power(signal):
    spectrum = np.fft.rfft(signal)
    power = np.abs(spectrum)**2
    freqs = np.fft.rfftfreq(len(signal))
    return freqs, power

def dominant_frequency(signal):
    freqs, power = fft_power(signal)
    idx = power.argmax()
    return freqs[idx], power[idx]