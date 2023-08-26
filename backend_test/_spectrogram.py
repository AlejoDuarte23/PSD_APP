import numpy as np
from scipy.signal import spectrogram
import plotly.graph_objects as go

def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    return np.array([float(x.strip()) for x in data])

def calculate_spectrogram(signal, fs):
    f, t, Sxx = spectrogram(signal, fs)
    return f, t, Sxx

def plot_3d_spectrogram(f, t, Sxx):
    fig = go.Figure(data=[go.Surface(z=Sxx, x=t, y=f)])
    fig.update_layout(
        title='3D Spectrogram',
        scene=dict(
            xaxis_title='Time [s]',
            yaxis_title='Frequency [Hz]',
            zaxis_title='Power'
        )
    )
    fig.show()

if __name__ == '__main__':
    file_path = "C:\\Users\\aleja\\Downloads\\Ansys digiduce\\MODL4\\Centrifuge MOD 4 G.txt"
    signal = read_data(file_path)
    fs = 1000  # Sampling frequency, you'll need to set this according to your own data
    
    f, t, Sxx = calculate_spectrogram(signal, fs)
    plot_3d_spectrogram(f, t, Sxx)
