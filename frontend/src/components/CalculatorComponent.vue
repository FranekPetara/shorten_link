<template>
  <div class="container">
    <div class="box">
      <img src="@/assets/logo.png" alt="Logo" class="logo">
      <h2 class="title">Shortlink</h2>
      <p class="subtitle">Link to shortcut</p>
      <div class="input-wrapper">
        <input v-model="url" type="text" placeholder="Enter URL..." class="url-input">
      </div>
      <button @click="shortenLink" class="button">Shorten it</button>
        <div class="response" v-if="shortenedLink">
          <div class="response-content">
            <a :href="url" target="_blank">{{ shortenedLink }}</a>
            <button @click="copyToClipboard(shortenedLink)" class="copy-button">
              <i class="fas fa-copy"></i> 
            </button>
          </div>
        </div>
    </div>
    <div>
      <div v-if="listLastLinks.length > 0">
      <h2 class="subtitle" style="margin-left : 20px;" >Last Links</h2>
      <div class="box" style="border: 1px solid gray; background-color: transparent; ">

          
              <div v-for="(link, index) in listLastLinks" :key="index" class="inner-box">
                <div class="link-container">
                <h class="subtitle" >{{ link.original_url }}</h>
                <a style='font-size: 10px;' :href="link.original_url">{{ link.short_url }}</a>
                </div>
                <div >
                <button @click="copyToClipboard(link.short_url)" class="copy-button">
                <i class="fas fa-copy"></i> 
                </button>
                </div>
              </div>

      </div>
      </div>
    </div>  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      url: '',
      shortenedLink: '',
      listLastLinks: [] 
    };
  },
  methods: {
    shortenLink() {
      axios.post('http://localhost:8000/api/shorten/', { original_url: this.url })
        .then(response => {
          this.shortenedLink = response.data.short_url;
          this.listLastLinks = response.data.last_three_links; 
        })
      .catch(error => {
      if (error.response) {
        let errorMessage = '';
        for (const errorKey in error.response.data) {
          if (Array.isArray(error.response.data[errorKey])) {
            errorMessage += error.response.data[errorKey][0] + '\n';
          } else {
            errorMessage += error.response.data[errorKey] + '\n';
          }
        }
        alert(errorMessage.trim()); 
        console.error('Server Error:', error.response.data); 
      } else {
  
        alert(error.message); 
        console.error('Error:', error.message); 
      }
    });
    },
    copyToClipboard(text) {
      const el = document.createElement('textarea');
      el.value = text;
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
      alert('Link copied to clipboard!');
    }
  }
}
</script>

<style scoped lang="scss">
.link-container {
  display: flex;
  flex-direction: column; 
  justify-content: flex-start; 
  align-items: flex-start; 
}


.inner-box {
  background-color: white;
  border-radius: 20px;
  padding: 10px;
  margin-bottom: 10px;
  display: flex;  
  justify-content: space-between; 
  align-items: center; 
}

.response {
  background-color: #f0f0f0;
  border-radius: 20px;
  padding: 10px;
}

.response-content {
  display: flex;
  justify-content: space-between; 
  align-items: center; 
  width: 100%;

}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column; 
  align-items: center; 
  height: 100vh;
  text-align: left;
  background-color: #f0f0f0;
}

.box {
  background-color: white;
  border-radius: 20px;
  padding: 20px;
  width: 300px;
  text-align: center;
  margin-bottom: 20px; 
}

.logo {
  margin-bottom: 10px;
}

.title {
  color: #4a24ac; 
  margin-bottom: 20px;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
}

.subtitle {
  color: #4a24ac; 
  margin-bottom: 5px;
  font-size: 10px; 
  text-align: left; 
}

.input-wrapper {
  position: relative;
  margin-bottom: 15px;
}

.url-input {
  padding: 0px; 
  border: none;
  outline: none;
  border-bottom: 2px solid #4a24ac; 
}

input {
  width: 100%;
  border: none;
  outline: none;
  padding: 10px;
  border-bottom: 2px solid #4a24ac; 
}

.line {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.button {
  background-color: #4a24ac; 
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  margin-bottom: 15px;
}

.response {
  background-color: #f0f0f0;
  border-radius: 20px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.copy-button {
  background-color: transparent; 
  color: grey;
  padding: 5px 10px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-left: 10px;
}
</style>
