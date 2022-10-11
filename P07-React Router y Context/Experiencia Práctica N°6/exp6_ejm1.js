//import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import React, {useState, useEffect} from 'react';

const [intervalo, setInterval] = useState(0);
useEffect(()=>{
const [usuario, setUsuario] = useState(0);
useEffect(() => {
  console.log(' La cuenta del usuario es { usuario } ');
  document.title = 'La cuenta es { usuario}';
 });
 return (
 <div>
  <h1> La cuenta del usuario es : {usuario} </h1>
  <button onClick={() => setUsuario(usuario + 1)} > Aumentar </button>
 </div>
 );
})