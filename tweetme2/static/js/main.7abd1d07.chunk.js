(this["webpackJsonptweetme2-web"]=this["webpackJsonptweetme2-web"]||[]).push([[0],{14:function(e,t,n){},16:function(e,t,n){"use strict";n.r(t);var c=n(1),a=n.n(c),s=n(6),r=n.n(s);n(14);function o(e,t,n,c){var a;c&&(a=JSON.stringify(c));var s=new XMLHttpRequest,r="http://localhost:8000/api".concat(t);s.responseType="json",s.open(e,r);var o=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),c=0;c<n.length;c++){var a=n[c].trim();if(a.substring(0,e.length+1)===e+"="){t=decodeURIComponent(a.substring(e.length+1));break}}return t}("csrftoken");s.setRequestHeader("Content-Type","application/json"),o&&(s.setRequestHeader("X-Requested-With","XMLHttpRequest"),s.setRequestHeader("X-CSRFToken",o)),s.onload=function(){403===s.status&&("Authentication credentials were not provided."===s.response.detail&&-1===window.location.href.indexOf("login")&&(window.location.href="/login?showLoginRequired=true"));n(s.response,s.status)},s.onerror=function(e){console.log("error",e),n({message:"The request was an error."},400)},s.send(a)}function i(e,t,n){var c="/tweets/";e&&(c="/tweets/?username=".concat(e)),null!==n&&void 0!==n&&(c=n.replace("http://localhost:8000/api","")),o("GET",c,t)}function l(e,t){var n="/tweets/feed/";null!==t&&void 0!==t&&(n=t.replace("http://localhost:8000/api","")),o("GET",n,e)}var u=n(0);function d(e){var t=e.tweet,n=e.action,c=e.didPerformAction,a=t.likes?t.likes:0,s=e.className?e.className:"btn btn-primary btn-sm",r=n.display?n.display:"Action",i="like"===n.type?"".concat(a," ").concat(r):r,l=function(e,t){console.log(e,t),200!==t&&201!==t||!c||c(e,t)};return Object(u.jsx)("button",{className:s,onClick:function(e){e.preventDefault(),function(e,t,n){o("POST","/tweets/action/",n,{id:e,action:t})}(t.id,n.type,l)},children:i})}var j=n(9),b=n(2);function m(e){var t=e.username;return Object(u.jsx)("span",{className:"pointer",onClick:function(e){window.location.href="/profile/".concat(t)},children:e.children})}function f(e){var t=e.user,n=!0===e.includeFullName?"".concat(t.first_name," ").concat(t.last_name," "):null;return Object(u.jsxs)(a.a.Fragment,{children:[n,Object(u.jsxs)(m,{username:t.username,children:["@",t.username]})]})}function O(e){var t=e.user;return Object(u.jsx)(m,{username:t.username,children:Object(u.jsx)("span",{className:"mx-1 px-3 py-2 rounded-circle bg-dark text-white",children:t.username[0]})})}function w(e){var t=e.tweet;return Object(u.jsx)(u.Fragment,{children:t.parent?Object(u.jsx)(h,{isRetweet:!0,retweeter:e.retweeter,hideActions:!0,className:" ",tweet:t.parent}):null})}function h(e){var t=e.tweet,n=e.didRetweet,s=e.hideActions,r=e.isRetweet,o=e.retweeter,i=Object(c.useState)(e.tweet?e.tweet:null),l=Object(b.a)(i,2),m=l[0],h=l[1],p=e.className?e.className:"col-10 mx-auto col-md-6";p=!0===r?"".concat(p," p-2 border rounded"):p;var x=window.location.pathname.match(Object(j.a)(/([0-9]+)/,{tweetid:1})),v=x?x.groups.tweetid:-1,g="".concat(t.id)==="".concat(v),N=function(e,t){200===t?h(e):201===t&&n&&n(e)};return Object(u.jsx)(u.Fragment,{children:Object(u.jsxs)("div",{className:p,children:[!0===r&&Object(u.jsx)("div",{className:"mb-2",children:Object(u.jsxs)("span",{className:"small text-muted",children:["Retweet via ",Object(u.jsx)(f,{user:o})]})}),Object(u.jsxs)("div",{className:"d-flex",children:[Object(u.jsx)("div",{className:"col-1",children:Object(u.jsx)(O,{user:t.user})}),Object(u.jsxs)("div",{className:"col-11",children:[Object(u.jsxs)("div",{children:[Object(u.jsx)("p",{children:Object(u.jsx)(f,{includeFullName:!0,user:t.user})}),Object(u.jsx)("p",{children:t.content}),Object(u.jsx)(w,{tweet:t,retweeter:t.user})]}),Object(u.jsxs)("div",{className:"btn btn-group px-0",children:[m&&!0!==s&&Object(u.jsxs)(a.a.Fragment,{children:[Object(u.jsx)(d,{tweet:m,didPerformAction:N,action:{type:"like",display:"Likes"}}),Object(u.jsx)(d,{tweet:m,didPerformAction:N,action:{type:"unlike",display:"Unlike"}}),Object(u.jsx)(d,{tweet:m,didPerformAction:N,action:{type:"retweet",display:"Retweet"}})]}),!0===g?null:Object(u.jsx)("button",{className:"btn btn-outline-primary btn-sm",onClick:function(e){e.preventDefault(),window.location.href="/".concat(t.id)},children:"View"})]})]})]})]})})}var p=n(3);function x(e){var t=Object(c.useState)([]),n=Object(b.a)(t,2),s=n[0],r=n[1],o=Object(c.useState)([]),l=Object(b.a)(o,2),d=l[0],j=l[1],m=Object(c.useState)(null),f=Object(b.a)(m,2),O=f[0],w=f[1],x=Object(c.useState)(!1),v=Object(b.a)(x,2),g=v[0],N=v[1];Object(c.useEffect)((function(){var t=Object(p.a)(e.newTweets).concat(s);t.length!==d.length&&j(t)}),[e.newTweets,d,s]),Object(c.useEffect)((function(){if(!1===g){i(e.username,(function(e,t){200===t?(w(e.next),r(e.results),N(!0)):alert("There was an error!")}))}}),[s,g,N,e.username]);var y=function(e){var t=Object(p.a)(s);t.unshift(e),r(t);var n=Object(p.a)(d);n.unshift(d),j(n)};return Object(u.jsxs)(a.a.Fragment,{children:[d.map((function(e,t){return Object(u.jsx)(h,{tweet:e,didRetweet:y,className:"col-12 col-md-10 mx-auto mb-4 tweet border rounded py-3"},"".concat(t,"-{item.id}"))})),null!==O&&Object(u.jsx)("button",{onClick:function(t){if(t.preventDefault(),null!==O){i(e.username,(function(e,t){if(200===t){w(e.next);var n=Object(p.a)(d).concat(e.results);r(n),j(n)}else alert("There was an error!")}),O),console.log("nextUrl",O),console.log("next response")}},className:"btn btn-outline-primary",children:"Load next"})]})}var v=n(8);function g(e){var t=Object(c.useState)([]),n=Object(b.a)(t,2),s=n[0],r=n[1],o=Object(c.useState)([]),i=Object(b.a)(o,2),d=i[0],j=i[1],m=Object(c.useState)(null),f=Object(b.a)(m,2),O=f[0],w=f[1],x=Object(c.useState)(!1),v=Object(b.a)(x,2),g=v[0],N=v[1];Object(c.useEffect)((function(){var t=Object(p.a)(e.newTweets).concat(s);t.length!==d.length&&j(t)}),[e.newTweets,d,s]),Object(c.useEffect)((function(){if(!1===g){l((function(e,t){200===t?(w(e.next),r(e.results),N(!0)):alert("There was an error!")}))}}),[s,g,N,e.username]);var y=function(e){var t=Object(p.a)(s);t.unshift(e),r(t);var n=Object(p.a)(d);n.unshift(d),j(n)};return Object(u.jsxs)(a.a.Fragment,{children:[d.map((function(e,t){return Object(u.jsx)(h,{tweet:e,didRetweet:y,className:"col-12 col-md-10 mx-auto mb-4 tweet border rounded py-3"},"".concat(t,"-{item.id}"))})),null!==O&&Object(u.jsx)("button",{onClick:function(e){if(e.preventDefault(),null!==O){l((function(e,t){if(200===t){w(e.next);var n=Object(p.a)(d).concat(e.results);r(n),j(n)}else alert("There was an error!")}),O),console.log("nextUrl",O),console.log("next response")}},className:"btn btn-outline-primary",children:"Load next"})]})}function N(e){console.log(e);var t=a.a.createRef(),n=e.didTweet,c=function(e,t){201===t?n(e):(console.log(e),alert("An error occurred please try again."))};return Object(u.jsx)("div",{className:e.className,children:Object(u.jsxs)("form",{onSubmit:function(e){e.preventDefault(),console.log(e);var n=t.current.value;o("POST","/tweets/create/",c,{content:n}),t.current.value=""},children:[Object(u.jsx)("textarea",{ref:t,required:!0,className:"form-control",name:"tweet"}),Object(u.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:"Tweet"})]})})}function y(e){var t=e.tweetId,n=Object(c.useState)(!1),a=Object(b.a)(n,2),s=a[0],r=a[1],i=Object(c.useState)(null),l=Object(b.a)(i,2),d=l[0],j=l[1],m=function(e,t){200===t?j(e):alert("There was an error finding your tweet.")};return Object(c.useEffect)((function(){!1===s&&(!function(e,t){o("GET","/tweets/".concat(e),t)}(t,m),r(!0))}),[s,r]),null===d?null:Object(u.jsx)(h,{tweet:d,className:e.className})}var T=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,17)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,s=t.getLCP,r=t.getTTFB;n(e),c(e),a(e),s(e),r(e)}))},k=a.a.createElement,S=document.getElementById("tweetme-2");S&&(console.log(S.dataset),r.a.render(k((function(e){var t=Object(c.useState)([]),n=Object(b.a)(t,2),a=n[0],s=n[1],r="false"!==e.canTweet;return Object(u.jsxs)("div",{className:e.className,children:[!0===r&&Object(u.jsx)(N,{didTweet:function(e){var t=Object(p.a)(a);t.unshift(e),s(t)},className:"col-12 mb-3"}),Object(u.jsx)(x,Object(v.a)({newTweets:a},e))]})}),S.dataset),S));var R=document.getElementById("tweetme-2-feed");R&&r.a.render(k((function(e){var t=Object(c.useState)([]),n=Object(b.a)(t,2),a=n[0],s=n[1],r="false"!==e.canTweet;return Object(u.jsxs)("div",{className:e.className,children:[!0===r&&Object(u.jsx)(N,{didTweet:function(e){var t=Object(p.a)(a);t.unshift(e),s(t)},className:"col-12 mb-3"}),Object(u.jsx)(g,Object(v.a)({newTweets:a},e))]})}),R.dataset),R),document.querySelectorAll(".tweetme-2-detail").forEach((function(e){r.a.render(k(y,e.dataset),e)})),T()}},[[16,1,2]]]);
//# sourceMappingURL=main.7abd1d07.chunk.js.map