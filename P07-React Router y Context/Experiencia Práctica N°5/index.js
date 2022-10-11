import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

//Componente funcional
/*const Componente = (props)=>{
          //Declaración de punto 
          const state = React.useState();
          //useState regresa un array
          const _state = state[0]; //valor del state
          const setState = state[1]; //función

         return(
              <p>{_state }</p>
         )
}/*/

//import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import React, {useState} from 'react';

//Componentes funcionales
const Componente = (props)=>{
         //Declarar un Hook por cada variable de estado que necesitemos
         const [booleanos, setBooleanos] = useState();
        
         return(
              <p>{booleanos ? "True":"False"}</p>
         )
}


ReactDOM.render(
  <useState />,
  document.getElementById('root')
)