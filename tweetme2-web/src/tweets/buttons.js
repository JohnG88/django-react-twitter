import React from "react";

import { apiTweetAction } from "./lookup";

export function ActionBtn(props) {
    const { tweet, action, didPerformAction } = props;
    const likes = tweet.likes ? tweet.likes : 0
    // remember likes is variable and setLikes is to update variable
    // const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0);
    // const [userLike, setUserLike] = useState(tweet.userLike === true ? true : false);
    const className = props.className
        ? props.className
        : "btn btn-primary btn-sm";
    // if action.display then show action.display else show 'Action'
    const actionDisplay = action.display ? action.display : "Action";
    // if action type = 'like' show tweet likes actionDisplay, else show actionDisplay
    const display =
        action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
    const handleActionBackendEvent = (response, status) => {
        console.log(response, status);
        if ((status === 200 || status === 201) && didPerformAction) {
            // setLikes(response.likes);
            didPerformAction(response, status)
            // setUserLike(true)
        }
    };
    const handleClick = (event) => {
        event.preventDefault();
        apiTweetAction(tweet.id, action.type, handleActionBackendEvent);
    };
    return (
        <button className={className} onClick={handleClick}>
            {display}
        </button>
    );
}