//import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import React, {useState, useEffect} from 'react';

const [intervalo, setInterval] = useState(0);
useEffect(()=>{
  //Contador
  const intervalo = setInterval(() => {
    console.log("Intervalo...")
    setContador(contador + 1);
  }, 1000);

  return ()=>{
    console.log("Intervalo");
    clearInterval(intervalo);
  }
})
 

ReactDOM.render(
  <useEffect />,
  document.getElementById('root')
)
