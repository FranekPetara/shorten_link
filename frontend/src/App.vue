<template>
  <ShortenLink/>
</template>

<script>
import ShortenLink from './components/ShortenLink.vue'

export default {
  name: 'App',
  components: {
    ShortenLink
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
