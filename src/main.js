import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery";
import "popper.js";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

//* Runs Python File in environment shell
// var myPythonScriptPath = 'src/data/database.py';
// Use python shell

// const path = require('path')
// const {spawn} = require('child_process')

// function runScript(){
//   return spawn('python', [
//     "-u",
//     path.join(__dirname, 'myscript.py'),
//    "--foo", "some value for foo",
//   ]);
// }

// const subprocess = runScript();

// subprocess.stdout.on('data', (data) => {
//   console.log(`data:${data}`);
// });
// subprocess.stderr.on('data', (data) => {
//   console.log(`error:${data}`);
// });
// subprocess.stderr.on('close', () => {
//   console.log("Closed");
// });

// Py
let {PythonShell} = require('python-shell')
var options = {
  mode: 'text',
  pythonPath: '/usr/local/bin/python3',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
}

PythonShell.run('src/data/database.py', options, function (err, results) {
  if  (err)  throw err;
 console.log('test.py finished.');
 console.log('results', results);
});

//     python.stdout.on('data',function(data){
//         console.log("data: ",data.toString('utf8'));
//     });

// let {PythonShell} = require('python-shell')
// var spawn = require('child_process').spawn

// PythonShell.run('./src/data/database.py', null, function (err) {
//   if (err) throw err;
//   console.log('finished');
//   console.log(child)
// });

// PythonShell.runString('x=1;print(x)', null, function (err, results) {
//   console.log('hello.py finished.');
//   console.log('results', results);
//   // script finished
//   });
// PythonShell.run('database.py',  function  (err, results)  {
//  if  (err)  throw err;
//  console.log('hello.py finished.');
//  console.log('results', results);
// });
