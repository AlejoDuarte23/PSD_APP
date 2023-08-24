

<template>
  <div>
    <input v-model="file_location" placeholder="File Location"/>
    <input v-model="Fs" placeholder="Fs"/>
    <input v-model="NFFT" placeholder="NFFT"/>
    <input v-model="ncol" placeholder="ncol"/>
    <input v-model="skr" placeholder="rows to skip"/>
    <input v-model="deli" placeholder="delimeter"/>


    <!-- Add more inputs for a, b, channels, Nd, etc. -->
    <div>
      <button @click="sendData">Send Data</button>
    </div>
    <!-- Div for Plotly plot -->
    <div id="plotly_div"></div>
  </div>
</template>

<script>
import axios from 'axios';
import Plotly from 'plotly.js-dist';
export default {
  data() {
    return {
      file_location: '',
      Fs: '',
      NFFT: '',
      ncol: '',
      skr: '',
      deli: '',      // Add more data bindings for a, b, channels, Nd, etc.
    };
  },
  methods: {
    async sendData() {
      try {
        const dataToSend = {
          file_location: this.file_location,
          Fs: this.Fs,
          NFFT: this.NFFT,
          ncol: this.ncol,
          deli: this.deli,
          skr: this.skr
          // Add more data fields for a, b, channels, Nd, etc.
        };
        
        const response = await axios.post('http://localhost:5000/calculate_psd', dataToSend);
        
        // Extract data from the response
        const freq = response.data.freq;
        const Pxx = response.data.Pxx;
        
        // Create traces for each column of data
        const traces = Pxx[0].map((_, index) => ({
            x: freq,
            y: Pxx.map(column => column[index]),
            type: 'scatter',
            mode: 'lines'
        }));
        
        const layout = {
            title: 'Power Spectral Density',
            xaxis: { title: 'Frequency (Hz)' },
            yaxis: { title: 'Power/Frequency (dB/Hz)' }
        };

        Plotly.newPlot('plotly_div', traces, layout);

      } catch (error) {
        console.error("There was an error sending the data:", error);
      }
    }
  }

}
</script>
