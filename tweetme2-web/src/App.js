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
        // console.log(response, status)
        if (status === 200) {
          setTweets(response)
        } else {
          alert('There was an error!')
        }
      }
      loadTweets(myCallback)
    }, [])

    function ActionBtn(props) {
      const className = props.className ? props.className : "btn btn-primary btn-sm"
      const {tweet, action} = props;
      return (
          action.type === 'like' ? <button className={className}> {tweet.likes} Like</button> : null
      )
  }

    function Tweet(props) {
      const {tweet} = props
      const className = props.className ? props.className : "col-10 mx-auto col-md-6"
      return (
        <>
            <div className={className}>
                <p>{tweet.id} - {tweet.content}</p>
                <div className="btn btn-group">
                    <ActionBtn tweet={tweet} action={{type: 'like'}}/>
                    <ActionBtn tweet={tweet} action={{type: 'unlike'}}/>
                </div>
            </div>
        </>
      )
    }

    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <div>
                    {tweets.map((item, index) =>{
                        return <Tweet tweet={item} key={`${index}-{item.id}`} className="col-12 col-md-10 mx-auto mb-4 tweet border rounded py-3" />
                    })}
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
