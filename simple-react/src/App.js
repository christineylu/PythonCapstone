import React, { useState } from 'react';
import useInterval from './useInterval';
import react_logo from './react-logo.svg';
import flask_logo from './flask-logo.svg';
import './App.css';

function getRandomColor() {
  let colorValues = ["red", "blue", "green"];
  return colorValues[Math.floor(Math.random() * colorValues.length)];
}

function App() {
  const [currentTime, setCurrentTime] = useState('01/01/1970, 00:00:00');
  const delay = 1000;

  useInterval(() => {
    fetch('/api/time')
      .then(response => response.json())
      .then(data => {
        setCurrentTime(data.datetime);
        //console.log(currentTime);
      });
  }, delay);

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
        <p>The current time is</p>
        <div style={{background: `${getRandomColor()}`}}>
          {currentTime}
        </div>
      </header>
    </div>
  );
}

export default App;
