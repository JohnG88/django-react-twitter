import React, { useEffect, useState } from "react";

import { loadTweets } from "../lookup";

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
    const { tweet, action } = props;
    // remember likes is variable and setLikes is to update variable
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0);
    const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false);
    const className = props.className
        ? props.className
        : "btn btn-primary btn-sm";
    // if action.display then show action.display else show 'Action'
    const actionDisplay = action.display ? action.display : "Action";
    // if action type = 'like' show tweet likes actionDisplay, else show actionDisplay
    const display =
        action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
    const handleClick = (event) => {
        event.preventDefault();
        if (action.type === "like") {
            if (userLike === true) {
                // perhaps unlike it?
                setLikes(likes - 1);
                setUserLike(false);
            } else {
                setLikes(likes + 1);
                setUserLike(true);
            }
        }
    };
    return (
        <button className={className} onClick={handleClick}>
            {display}
        </button>
    );
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
                    <ActionBtn
                        tweet={tweet}
                        action={{ type: "like", display: "Likes" }}
                    />
                    <ActionBtn
                        tweet={tweet}
                        action={{ type: "unlike", display: "Unlike" }}
                    />
                    <ActionBtn
                        tweet={tweet}
                        action={{ type: "retweet", display: "Retweet" }}
                    />
                </div>
            </div>
        </>
    );
}
