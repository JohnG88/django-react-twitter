export function loadTweets(callback) {
    // New instance of class
    const xhr = new XMLHttpRequest(); // like python, xhr = new SomeClass()
    const method = "GET";
    const url = "http://127.0.0.1:8000/api/tweets/";
    const responseType = "json";

    xhr.responseType = responseType;
    xhr.open(method, url);
    xhr.onload = function () {
        callback(xhr.response, xhr.status);
    };
    xhr.onerror = function (e) {
        console.log(e);
        callback({ message: "The request was an error." }, 400);
    };
    xhr.send();
}