import React from 'react';
import ReactDOM from 'react-dom';
import registro from './registro';

import App from './App';
import ThemeContext from './ThemeContext';

ReactDOM.render(
  <ThemeContext.Provider value="green">
    <App />
  </ThemeContext.Provider>,
  document.getElementById('root')
);

registro();
