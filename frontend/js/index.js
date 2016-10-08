import '../css/main.styl'
import Application from 'App';
import React from 'react';
import ReactDOM from 'react-dom';

window.putInto = function(token) {
	localStorage.setItem('token', token);
}

document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelectorAll('.js-xr-container')[0];
    if (! container) {
        alert('Could not find root element: app is useless');
    }
    ReactDOM.render(<Application />, container);
});
