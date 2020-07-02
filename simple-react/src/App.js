import React, { useState } from 'react';
import useInterval from './useInterval';
import react_logo from './react-logo.svg';
import flask_logo from './flask-logo.svg';
import './App.css';

function getRandomColor() {
  let colorValues = ["red", "blue", "green"];
  return colorValues[Math.floor(Math.random() * colorValues.length)];
}

function buttonClicked() {
  console.log('Button was clicked!')
  fetch('/random/quote')
    .then(response => response.json())
    .then(data => {
      console.log(data);
    });
}

function App() {
  const [currentTime, setCurrentTime] = useState('01/01/1970, 00:00:00');
  const [currentRandomNumber, setCurrentRandomNumber] = useState('-1');
  const [currentRandomString, setCurrentRandomString] = useState('<null>');
  const [quoteText, setQuoteText] = useState('To be or not to be.');
  const [quoteAuthor, setQuoteAuthor] = useState('William Shakespeare');

  const delay = 15000; // in milliseconds
  const quoteDelay = 15000; // in milliseconds

  useInterval(() => {
    fetch('/api/time')
      .then(response => response.json())
      .then(data => {
        setCurrentTime(data.datetime);
        // console.log(currentTime);
      });
  }, delay);

  useInterval(() => {
    fetch('/random/number')
      .then(response => response.json())
      .then(data => {
        setCurrentRandomNumber(data.random_number);
        // console.log(currentRandomNumber);
      });
  }, delay);

  useInterval(() => {
    fetch('/random/string')
      .then(response => response.json())
      .then(data => {
        setCurrentRandomString(data.random_string);
        // console.log(currentRandomString);
      });
  }, delay);

    useInterval(() => {
    fetch('/random/quote')
      .then(response => response.json())
      .then(data => {
        setQuoteText(data.random_quote);
        setQuoteAuthor(data.quote_author)
        // console.log(quoteText);
        // console.log(quoteAuthor)
      });
  }, quoteDelay);

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
        <p>The current random number is</p>
        <div style={{background: `${getRandomColor()}`}}>
          {currentRandomNumber}
        </div>
        <p>The current random string is</p>
        <div style={{background: `${getRandomColor()}`}}>
          {currentRandomString}
        </div>
        <p>The current quote is</p>
        <button className="button" onClick={buttonClicked}>Click to Refresh</button>
        <div>
          <blockquote>
          <p>{quoteText}</p>
          <footer>— <cite>{quoteAuthor}</cite>
          </footer>
          </blockquote>
        </div>
        <p></p>
        <p></p>
        <p></p>
      </header>
    </div>
  );
}

export default App;
