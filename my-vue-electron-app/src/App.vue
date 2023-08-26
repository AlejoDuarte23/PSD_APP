<template>
  <div id="app">
    <div class="header">
       <h1 class="title">Modal&Co</h1>
      <p class="subtitle">Breaking the Boundaries of Structural Health And Monitoring Through Aggressive Innovations</p>
      <TopBar @add-tab="addTab" @set-active-tab="setActiveTab" />
    </div>
    <div>
      <MyComponent 
        v-for="tab in tabs" 
        :key="tab.id" 
        :tab-id="tab.id" 
        v-show="tab.id === activeTab" />
    </div>
  </div>
</template>

<script>
import MyComponent from './components/MyComponent.vue'
import TopBar from './components/TopBar.vue'

export default {
  name: 'App',
  components: {
    MyComponent,
    TopBar
  },
  data() {
    return {
      tabs: [
        { id: 1 }
      ],
      activeTab: 1
    };
  },
  methods: {
    addTab(newId) {
      this.tabs.push({ id: newId });
      this.activeTab = newId;
    },
    setActiveTab(id) {
      this.activeTab = id;
    }
  }
}
</script>

<style>
/* Your existing App.vue styles */
.header {
  text-align: center;
  margin-bottom: 20px;
}

.title {
  font-family: 'Playfair Display', serif;
  font-size: 2.5em;
  color: black;
}

.subtitle {
  font-family: 'Arial', sans-serif;
  font-size: 1em;
  color: black;
  max-width: 600px;
  margin: 10px auto;
  line-height: 1.5;
}
</style>
