import logo from './logo.svg';
import './App.css';
import { useEffect } from 'react';

const valid_keys = ["w", "a", "s", "d"];

async function getInfo(key) {
  const res = await fetch('http://localhost:8000/' + key, {
    method: 'GET'
  })
  console.log(res)
  // const data = await res.json()
}

function App() {
  // https://github.com/facebook/react/issues/15815#issuecomment-498693570
  useEffect(() => {
    const keyPressHandler = (e) => {
      if (valid_keys.includes(e.key)) { getInfo(e.key) }
    };

    document.addEventListener('keydown', keyPressHandler);
    return () => {
      document.removeEventListener('keydown', keyPressHandler);
    };
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
