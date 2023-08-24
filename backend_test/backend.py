from flask import Flask, request, jsonify
from flask_cors import CORS  
from scipy.signal import welch 
import numpy as np 
app = Flask(__name__)
CORS(app)  

@app.route('/calculate_psd', methods=['POST'])
def calculate_psd():
    data = request.json
    print("Received data:", data)
    
    # Load the acceleration data
    _dir = data['file_location']
    sk_row = data.get('skr', 0)  # Provide a default value in case 'skr' is not provided
    deli = data['deli']
    with open(_dir, 'r') as fd:
        acceleration_data = np.loadtxt(fd, skiprows=int(sk_row))

    # Get the fs and NFFT
    fs = float(data['Fs'])
    NFFT = int(data['NFFT'])
    
    psd_results = np.zeros((NFFT//2+1, acceleration_data.shape[1]))
    for i in range(acceleration_data.shape[1]):
        _freq, _psd = welch(acceleration_data[:, i], fs, nperseg=NFFT)
        psd_results[:, i] = np.log(_psd)
    
    # Convert the data to lists to send as JSON
    return jsonify({"freq": _freq.tolist(), "Pxx": psd_results.tolist()})

if __name__ == "__main__":
    app.run(debug=True)