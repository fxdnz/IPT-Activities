import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/v1/posts/").then((response) => {
      setPosts(response.data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Posts from Django</h1>
        <div style={{ display: "flex" }}>
          {posts.map((obj, index) => (
            <div
              style={{
                border: "1px solid white",
                paddingLeft: "60px",
                paddingRight: "60px",
                paddingBottom: "20px",
                paddingTop: "20px",
                margin: "20px",
              }}
              key={index}
            >
              <h4>Title: {obj.title} </h4>
              <p>
                {obj.content}
                <br />
                Author: {obj.author}
              </p>
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;
