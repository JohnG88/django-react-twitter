import logo from "./logo.svg";
import "./App.css";

import { TweetsComponent } from "./tweets";

// useEffect will help into looking http requests from backend
// useState

function App() {
    // function loadTweets is from index.html

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <div>
                    <TweetsComponent/>
                </div>
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
