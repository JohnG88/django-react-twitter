import React, { useEffect, useState } from "react";

import {loadTweets} from '../lookup'

export function TweetsList(props) {
    const [tweets, setTweets] = useState([{ content: 123 }]);
    useEffect(() => {
        const myCallback = (response, status) => {
            // console.log(response, status)
            if (status === 200) {
                setTweets(response);
            } else {
                alert("There was an error!");
            }
        };
        loadTweets(myCallback);
    }, []);
    return tweets.map((item, index) => {
        return (
            <Tweet
                tweet={item}
                key={`${index}-{item.id}`}
                className="col-12 col-md-10 mx-auto mb-4 tweet border rounded py-3"
            />
        );
    });
}

export function ActionBtn(props) {
    const className = props.className
        ? props.className
        : "btn btn-primary btn-sm";
    const { tweet, action } = props;
    return action.type === "like" ? (
        <button className={className}> {tweet.likes} Like</button>
    ) : null;
}

export function Tweet(props) {
    const { tweet } = props;
    const className = props.className
        ? props.className
        : "col-10 mx-auto col-md-6";
    return (
        <>
            <div className={className}>
                <p>
                    {tweet.id} - {tweet.content}
                </p>
                <div className="btn btn-group">
                    <ActionBtn tweet={tweet} action={{ type: "like" }} />
                    <ActionBtn tweet={tweet} action={{ type: "unlike" }} />
                </div>
            </div>
        </>
    );
}
