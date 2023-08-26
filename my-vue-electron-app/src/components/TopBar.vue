<template>
    <div class="tab-container">
      <button @click="addTab" class="add-tab-button">+</button>
      <div v-for="tab in tabs" :key="tab.id" class="tab" @click="setActiveTab(tab.id)">
        <span class="tab-name">{{ tab.name }}</span>
        <span class="close-tab" @click.stop="removeTab(tab.id)">x</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tabs: [
          { id: 1, name: "Tab 1" }
        ]
      };
    },
    methods: {
      addTab() {
        const newId = this.tabs.length + 1;
        this.tabs.push({ id: newId, name: `Tab ${newId}` });
        this.$emit("add-tab", newId);
      },
      setActiveTab(id) {
        this.$emit("set-active-tab", id);
      },
      removeTab(id) {
        const index = this.tabs.findIndex(tab => tab.id === id);
        if (index > -1) {
          this.tabs.splice(index, 1);
        }
        this.$emit("remove-tab", id);
      }
    }
  };
  </script>
  
  <style scoped>
  .tab-container {
    display: flex;
    font-family: 'Arial', sans-serif;
    background-color: transparent;
    border-bottom: 1px solid #444;
    padding: 10px;
    margin-bottom: 10px;  /* Reduced spacing */
  }
  
  .tab {
    padding: 10px;
    border: 1px solid #444;
    background-color: transparent;
    color: #000000;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
    transition: all 0.3s ease-in-out;
  }
  
  .tab:hover {
    background-color: #e8e8e8;
  }
  
  .add-tab-button {
    background-color: transparent;
    border: 1px solid #444;
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
    color: #000000;
    border-radius: 5px;
    transition: all 0.3s ease-in-out;
  }
  
  .add-tab-button:hover {
    background-color: #e8e8e8;
  }
  </style>
  