import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
// import App from "./App";
import { FeedComponent, TweetsComponent, TweetDetailComponent } from "./tweets";
import reportWebVitals from "./reportWebVitals";

// ReactDOM.render(
//     <React.StrictMode>
//         <App />
//     </React.StrictMode>,
//     document.getElementById("root")
// );
// lines below help to be able to use attributes from index.html div
const e = React.createElement
const tweetsEl = document.getElementById("tweetme-2");
if (tweetsEl) {
    console.log(tweetsEl.dataset)
    ReactDOM.render(e(TweetsComponent, tweetsEl.dataset),
        tweetsEl
    );
}

const tweetFeedEl = document.getElementById("tweetme-2-feed");
if (tweetFeedEl) {
    ReactDOM.render(e(FeedComponent, tweetFeedEl.dataset),
        tweetFeedEl
    );
}

const tweetDetailElements = document.querySelectorAll('.tweetme-2-detail')

tweetDetailElements.forEach(container => {
    ReactDOM.render(e(TweetDetailComponent, container.dataset),
        container
    );
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
