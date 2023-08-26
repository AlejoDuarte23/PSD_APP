
# Import necessary libraries
from flask import Flask, jsonify
import numpy as np
from scipy.signal import spectrogram

app = Flask(__name__)

# Existing API endpoints for PSD plot

# New API endpoint for Spectrogram
@app.route('/getSpectrogramData', methods=['GET'])
def get_spectrogram_data():
    # Replace with actual data source
    sample_data = np.random.rand(1024, 10)
    
    # Compute spectrogram
    f, t, Sxx = spectrogram(sample_data, fs=1.0)
    
    # Create JSON response
    response = {
        'frequencies': f.tolist(),
        'time': t.tolist(),
        'spectrogram': Sxx.tolist()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
