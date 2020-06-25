import React, { useState, useEffect } from 'react';
import react_logo from './react-logo.svg';
import flask_logo from './flask-logo.svg';
import './App.css';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.datetime);
      console.log(currentTime);
    });
  }, [currentTime]);

  return (
    <div className="App">
      <header className="App-header">
        <img src={react_logo} className="App-logo" alt="react-logo" />
        <img src={flask_logo} className="App-logo" alt="flask-logo" />
        <a
          className="App-link"
          href="https://github.com/robmarano/aws_elastic_beanstalk_flask"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn how to spin React with Python Flask
        </a>
        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default App;
