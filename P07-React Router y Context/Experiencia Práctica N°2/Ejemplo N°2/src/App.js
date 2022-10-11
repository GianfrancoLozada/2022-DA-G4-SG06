import React from 'react';
import ThemeContext from './ThemeContext';

const App = () => (
  <div>
    <Primeralinea> Hola a todos </Primeralinea>

    <Segundalinea>
      La Formula 1 es el mejor deporte que existe.
    </Segundalinea>

    <Terceralinea>
      Adios a todos
    </Terceralinea>
  </div>
);

const Primeralinea = ({ children }) => (
  <ThemeContext.Consumer>
    {value => <h1 style={{ color: value }}>{children}</h1>}
  </ThemeContext.Consumer>
);

const Segundalinea = ({ children }) => (
  <ThemeContext.Consumer>
    {color => <p style={{ color: color }}>{children}</p>}
  </ThemeContext.Consumer>
);

const Terceralinea = ({ children }) => {
  const color = React.useContext(ThemeContext);

  return <h2 style={{ color }}>{children}</h2>;
};

export default App;
