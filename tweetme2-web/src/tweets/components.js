import React, { useEffect, useState } from "react";

import { loadTweets } from "../lookup";

export function TweetsComponent(props) {
    // createRef will allow to get value of textarea
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(event);
        const newVal = textAreaRef.current.value;
        let tempNewTweets = [...newTweets]
        // push sends to end of array, unshift to top of array
        tempNewTweets.unshift({
            content: newVal,
            likes: 0,
            id: 12313
        })
        setNewTweets(tempNewTweets)
        console.log(newVal);
        textAreaRef.current.value = ''
    }

    return (
        <div className={props.className}>
            <div className="col-12 mb-3 ">
                <form onSubmit={handleSubmit}>
                    <textarea ref={textAreaRef} required={true} className="form-control" name="tweet">
                        
                    </textarea>
                    <button type="submit"className="btn btn-primary my-3">Tweet</button>
                </form>
            </div>
            <TweetsList newTweets={newTweets}/>
        </div>
    )
}

export function TweetsList(props) {
    const [tweetsInit, setTweetsInit] = useState([]);
    const [tweets, setTweets] = useState([])

    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if (final.length !== tweets.length) {
            setTweets(final)
        }
        
    },[props.newTweets, tweets, tweetsInit])

    useEffect(() => {
        const myCallback = (response, status) => {
            // console.log(response, status)
            if (status === 200) {
                setTweetsInit(response);
            } else {
                alert("There was an error!");
            }
        };
        loadTweets(myCallback);
    }, [tweetsInit]);
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
