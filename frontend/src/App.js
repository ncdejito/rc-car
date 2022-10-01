import logo from './logo.svg';
import './App.css';
import { useEffect } from 'react';
import { fromEvent, map, filter, distinctUntilChanged } from 'rxjs';

const valid_keys = ["w", "a", "s", "d"];

async function getInfo(key) {
  const res = await fetch('http://localhost:8000/' + key, {
    method: 'GET'
  })
  console.log(res)
  // const data = await res.json()
}

function App() {
  // https://dev.to/rxjs/fetching-data-in-react-with-rxjs-and-lt-gt-fragment-54h7
  useEffect(() => {

    const subscription = fromEvent(document, 'keydown')
      .pipe(map(event => event.key))
      .pipe(filter(key => valid_keys.includes(key)))
      .pipe(distinctUntilChanged())
      .subscribe(getInfo);

    return () => subscription.unsubscribe();
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
