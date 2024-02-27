<template>
  <CalculatorComponent/>
</template>

<script>
import CalculatorComponent from './components/CalculatorComponent.vue'

export default {
  name: 'App',
  components: {
    CalculatorComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
