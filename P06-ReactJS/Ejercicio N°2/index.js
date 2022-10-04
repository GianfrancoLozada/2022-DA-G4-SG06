import React,{ useState } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

//Componentes y props
function Header(){
   return (<header><h1>Integrantes</h1></header>,
   <ul>
    <li>Rodrigo</li>
    <li>Nicole</li>
    <li>Maria Fernanda</li>
    <li>Gianfranco</li>
   </ul>
   );
  } 
function Main(){ return (<main><h2>Primera Pagina en React</h2></main>);} 

//iteradores
function Red(props){
  return <li> Nuestras plataformas favoritas son {props.socia}</li>
}
function Media(){
  const redes = ['Spotify', 'YouTUbe', 'Netflix', 'Disney +', 'Deezer' ];
  return (
    <ul>
      {redes.map((argCar) => <Red socia = {argCar}/>)}
    </ul>
  );
}

//CON USESTATE Y CON CLASES Y EVENTOS
function Banderar() {
  const [color, setColor] = useState({
    nombre: "Jose",
    nacionalidad1: "peruano",
    nacionalidad2: "cataris",
    color: "rojo"
  });

  const nuevoCOlor = () => {
    setColor(antes => {
      return { ...antes, color: "morado" }
    });
  }

  return (
    <>
    
      <p>
        Nosotros somos {color.nacionalidad1} o  {color.nacionalidad2}. NUestra bandera es de color {color.color} y blanco. Si presionas el boton veras el nuevo color de la
        </p>
        <p>
          Presiona el siguiente boton para ver el cambio
        </p>
      <button
        type="button"
        onClick={nuevoCOlor}
      >Otro Color</button>
    </>
  )
}
 //Estados con clase
 
 class SegundoConEstado extends React.Component{
  constructor(props){
    super(props);
    //Aquí se puede inicializar cualquier valor
    this.state ={
      contador:0,
      mensaje:""
    }
  };

  miSuma = () =>{
    
    if(this.state.contador % 2 == 0){
      console.log(this.state.contador);
      
      this.setState({
        contador : this.state.contador + 1,
        mensaje : "Falso"        
      });
    }
    else
      this.setState({
        contador : this.state.contador + 1,
        mensaje : "Verdad"        
      });
    
  }


  render(){
    return (
      <div>
        <h3 onClick={this.miSuma}>Click para saber si es Verdadero o Falso</h3>
        <h3>{this.state.contador}</h3>
        <h3>{this.state.mensaje}</h3>
      </div>
    );
  }
  
}

 

function Agrupador(props){ 
  console.log(props); 
return (<div>{props} 
<Header/> 
<Main/> 
<Media/>
<Banderar/>
<br></br>
<SegundoConEstado/>
</div>); 
} 

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(Agrupador('Grupo 03 '));
//root.render(<Media/>);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();