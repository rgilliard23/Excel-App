import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery'
import 'popper.js'

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");


//* Runs Python File in environment shell

var pyshell =  require('python-shell');

pyshell.run('database.py',  function  (err, results)  {
 if  (err)  throw err;
 console.log('hello.py finished.');
 console.log('results', results);
});
