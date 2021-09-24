import React, { useEffect, useState } from "react";

import logo from "./logo.svg";
import "./App.css";

// useEffect will help into looking http requests from backend
// useState

function App() {
    const [tweets, setTweets] = useState([{content: 123}]);

    // function loadTweets is from index.html
    function loadTweets(callback) {
      // New instance of class
      const xhr = new XMLHttpRequest(); // like python, xhr = new SomeClass()
      const method = "GET";
      const url = "http://127.0.0.1:8000/api/tweets/";
      const responseType = "json";

      xhr.responseType = responseType;
      xhr.open(method, url);
      xhr.onload = function () {
        callback(xhr.response, xhr.status)
      };
      xhr.onerror = function(e) {
        console.log(e)
        callback({'message': 'The request was an error.'}, 400)
      }
      xhr.send();
  }

    useEffect(() => {
      const myCallback = (response, status) => {
        console.log(response, status)
        if (status === 200) {
          setTweets(response)
        } else {
          alert('There was an error!')
        }
      }
      loadTweets(myCallback)
    }, [])

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <p>
                    {tweets.map((tweet, index) =>{
                        return <li key={index}>{tweet.content}</li>
                    })}
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
