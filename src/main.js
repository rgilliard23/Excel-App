import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");


//* Runs Python File in environment shell
var pyshell =  require('python-shell');
pyshell.run('database.py',  function  (err, results)  {
 if(err){
   console.log(err);
   return;
  }  
  console.log(results)

}); 
