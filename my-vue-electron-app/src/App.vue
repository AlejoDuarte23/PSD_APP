<template>
  <div id="app">
    <div class="header">
      <h1 class="title">Modal&Co</h1>
      <p class="subtitle">Breaking the Boundaries of Structural Health And Monitoring Through Aggressive Innovations</p>
      <MyComponent />
    </div>
    <!-- The rest of your App.vue template -->
  </div>
</template>

<script>
// Import the MyComponent
import MyComponent from './components/MyComponent.vue'

export default {
  name: 'App',
  components: {
    MyComponent  // Register the MyComponent
  }
}
</script>

<style>
/* Your App.vue styles */
.header {
  text-align: center;
  margin-bottom: 20px;
}

.title {
  font-family: 'Playfair Display', serif;  /* This is just an example, you'd need to include the font in your project */
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
