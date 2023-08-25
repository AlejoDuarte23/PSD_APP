<template>
  <div class="app-container">

      <!-- Top Bar -->
      <div class="top-bar">
          <!-- Placeholder for app name or logo -->
      </div>

      <!-- File Input Bar -->
      <div class="input-bar">
          <input v-model="file_location" placeholder="File Location" class="file-input"/>
          <button @click="sendData" class="send-btn">Send Data</button>
      </div>

      <!-- Modal for extra inputs -->
      <transition name="fade">
          <div v-if="showModal" class="modal-overlay">
              <div class="modal">
                  <h2>Settings</h2>
                  <div class="settings-container">
                      <div class="modal-section">
                          <h3>PSD Settings</h3>
                          <input v-model="Fs" placeholder="Fs"/>
                          <input v-model="NFFT" placeholder="NFFT"/>
                      </div>
                      <div class="modal-section">
                          <h3>File Settings</h3>
                          <input v-model="ncol" placeholder="ncol"/>
                          <input v-model="skr" placeholder="rows to skip"/>
                          <input v-model="deli" placeholder="delimeter"/>
                      </div>
                  </div>
                  <button @click="toggleModal" class="close-btn">Close</button>
              </div>
          </div>
      </transition>

      <!-- Trigger modal button -->
      <button @click="toggleModal" class="modal-trigger">Settings</button>

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
      deli: '',
      showModal: false  // To control the modal visibility
    };
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
    async sendData() {
      try {
        const dataToSend = {
          file_location: this.file_location,
          Fs: this.Fs,
          NFFT: this.NFFT,
          ncol: this.ncol,
          deli: this.deli,
          skr: this.skr
        };

        const response = await axios.post('http://localhost:5000/calculate_psd', dataToSend);

        const freq = response.data.freq;
        const Pxx = response.data.Pxx;

        const traces = Pxx[0].map((_, index) => ({
          x: freq,
          y: Pxx.map(column => column[index]),
          type: 'scatter',
          mode: 'lines'
        }));

        const layout = {
          title: {
            text: 'Power Spectral Density',
            font: {
              family: 'Arial, sans-serif',
              size: 18,
              color: 'black'
            }
          },
          xaxis: {
            title: {
              text: 'Frequency (Hz)',
              font: {
                color: 'black'
              },
            },
            gridcolor: '#888',
            tickfont: {
              color: 'black',
            },
            autorange: true
          },
          yaxis: {
            title: 'Power/Frequency (dB/Hz)',
            gridcolor: '#888'
          },
          paper_bgcolor: 'rgba(0,0,0,0)',
          plot_bgcolor: 'rgba(0,0,0,0)',
        };

        Plotly.newPlot('plotly_div', traces, layout);

        // Close the modal after sending data
        this.showModal = false;

      } catch (error) {
        console.error("There was an error sending the data:", error);
      }
    }
  }
}
</script>
<style scoped>
.app-container {
  font-family: 'Arial', sans-serif;
  background: linear-gradient(135deg, #ffffff 0%, #ffffff 100%);
  color: #f1f1f1;
  height: 100vh;
  padding: 20px;
}

.top-bar {
  height: 60px;
  background-color: transparent;
  padding: 10px;
  margin-bottom: 20px;
}

.input-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.file-input, .send-btn, .modal-trigger, .close-btn, .modal input {
  transition: all 0.3s ease-in-out;
  padding: 10px;
  border: 1px solid #444;
  background-color: transparent;
  color: #000000;
  border-radius: 5px;
}

.file-input {
  flex: 1;
  margin-right: 10px;
}

.send-btn, .close-btn, .modal-trigger {
  cursor: pointer;
}

.send-btn:hover, .close-btn:hover, .modal-trigger:hover {
  background-color: #e8e8e8;  /* Lighter gray for hover effect */
}

/* Overlay to blur the background and center the modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.9); /* Semi-transparent white to slightly blur the background */
  backdrop-filter: blur(5px); /* Blur effect */
  z-index: 10; /* Ensure the overlay is below the modal */

}

/* Modal styling */
.modal {
  width: 60%;
  background-color: #fafafa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  flex-direction: column; /* Column direction to stack elements vertically */
  align-items: center;    /* Center align for the close button */
}

.modal h2 {
  text-align: center;
  width: 100%;
  margin-bottom: 20px;
  color: black;  /* Set title font color to black */
  z-index: 11; /* Ensure the modal is above the overlay */

}

.settings-container {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-bottom: 20px;
  align-items: flex-start; 
}

.modal-section {
  flex: 1;
  height: 200px;  /* Set a fixed height for both sections */
  padding: 15px;  
  border: 2px solid #aaa;
  margin: 0 10px;
  display: flex; 
  flex-direction: column; 
  align-items: center; 
  justify-content: center;
}

.modal-section h3 {
  margin-bottom: 10px;  /* Space between the title and inputs */
  color: black;  /* Set font color to black for section titles */
  margin-top: 0;  /* Remove top margin to align titles at the same level */
}


.modal-section input {
  width: 80%;  /* Reduce input width for better centering */
  margin-bottom: 10px;  /* Space between inputs */
}

.close-btn {
  margin-top: 20px;  /* Margin above the close button */
}

#plotly_div {
    max-width: 1080px;  /* Adjust this to your desired width */
    margin: 0 auto;
}

</style>