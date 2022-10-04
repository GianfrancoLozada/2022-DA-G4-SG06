import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user1 = {
  firstName: 'Franck',
  lastName: 'Lozada'
};

const user2 = {
  firstName: 'Rodrigo',
  lastName: 'Delgadillo'
};

const user3 = {
  firstName: 'Maria',
  lastName: 'Valverde'
};
const user4 = {
    firstName: 'Nicole',
    lastName: 'Pinto'
  };
  
const element = (
  <h1>
    Buenos dias, {formatName(user1)}!<br></br>
    Buenos tardes, {formatName(user2)}!<br></br>
    Buenos tardes, {formatName(user3)}!<br></br>
    Buenos noches, {formatName(user4)}!<br></br>
  </h1>
);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  element
);