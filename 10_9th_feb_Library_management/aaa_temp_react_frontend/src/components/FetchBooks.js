import React, { useEffect, useState } from "react";
import axios from "axios";
import { URL } from "./constant";

function FetchBooks() {
  const [books, setbooks] = useState([]);
  const [bookName, setbookName] = useState("");

  const fetchbook = async () => {
    const res = await axios.get(`${URL}/books`);
    setbooks(res.data);
  };
  return (
    <div>
      <div className="form-group">
        <label htmlFor="Bookname">Bookname</label>
        <input
          className="form-control"
          id="Bookname"
          placeholder="filter by name"
          value={bookName}
          onChange={(e) => {
            setbookName(e.target.value);
          }}
        />
      </div>

      <button  style={{marginTop:"3px"}}  className="btn btn-primary" onClick={fetchbook}>
        Fetch books
      </button>
      <div>
        {books
          .filter((item) => {
            if (bookName === " ") {
              return item;
            } else if (
              item.book_name.toLowerCase().includes(bookName.toLowerCase())
            ) {
              return item;
            }
          })
          .map((item) => {
            return (
              <div
                key={item.book_id}
                style={{ background: "#bdbdbd", padding: "5px", margin: "5px" }}
              >
                <h3> {item.book_name}</h3>
                <h6> book id: {item.book_id}</h6>
                <span>Author : {item.book_author} , </span>
                <span>Stock : {item.book_stock} , </span>
                <span>Votes : {item.votes} </span>
              </div>
            );
          })}
      </div>
    </div>
  );
}

export default FetchBooks;
