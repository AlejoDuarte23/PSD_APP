<!-- src/App.vue -->

<template>
  <div id="app">
    <MyComponent />
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
</style>
