import React from "react"; 

import { apiTweetCreate } from "./lookup";

export function TweetCreate(props) {
    console.log(props);
    // const {username} = props
    // createRef will allow to get value of textarea
    const textAreaRef = React.createRef();
    const {didTweet} = props
    // const [newTweets, setNewTweets] = useState([]);
    
    // const canTweet = props.canTweet === 'false' ? false : true
    const handleBackendUpdate = (response, status) => {
        // backend api response handler
        // let tempNewTweets = [...newTweets];
        if (status === 201) {
            // push sends to end of array, unshift to top of array
            // tempNewTweets.unshift(response);
            didTweet(response);
        } else {
            console.log(response);
            alert("An error occurred please try again.");
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(event);
        const newVal = textAreaRef.current.value;
        // backend api request
        apiTweetCreate(newVal, handleBackendUpdate);
        textAreaRef.current.value = "";
    };

    return (
        <div className={props.className}>
            <form onSubmit={handleSubmit}>
                <textarea
                    ref={textAreaRef}
                    required={true}
                    className="form-control"
                    name="tweet"
                ></textarea>
                <button type="submit" className="btn btn-primary my-3">
                    Tweet
                </button>
            </form>
        </div>
    );
}

