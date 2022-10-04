import logo from './logo.svg';
import './App.css';
import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render() {
      return <h2>Probando</h2>;
  }
};
    const constante = <h3>Elementos</h3>
      class Lista extends React.Component {
        render() {
                return <ul>
                    <li>1</li>
                    <li>2</li>
                    <li>3</li>
                    <li>4</li>
                    <li>5</li>
                </ul>;
            }
        }
        
        ReactDOM.render(<App />, document.getElementById('root'));
        ReactDOM.render(constante, document.getElementById('root2'));
        ReactDOM.render(<Lista />, document.getElementById('lista'));



export default App;
