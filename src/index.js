import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import loader from "@monaco-editor/loader";
import code from './code/python/python.js'
import {isMobile} from 'react-device-detect';


loader.init().then(monaco => {
  const wrapper = document.getElementById("root");
  wrapper.style.height = "100vh";
  wrapper.style.width = "100%";
  let properties = {
    value: code,
    language:  "python",
    theme: 'vs-dark',
    fontSize: "20%",
    readOnly: true
  }
  if (isMobile) {
    properties = {
      value: code,
      language:  "python",
      theme: 'vs-dark',
      fontSize: "10%",
      readOnly: true
    }
  }
  
  monaco.editor.create(wrapper,  properties);
});
console.log("Welcome to my website");

ReactDOM.render(
  <React.StrictMode>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
