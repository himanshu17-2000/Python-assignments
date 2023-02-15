import React, { useEffect, useState , useRef } from "react";
import { URL } from "./constant";
import axios from "axios";
import { MessageBorrow } from "./Message";

function BookBorrow() {
  const [memberId, setmemberId] = useState("");
  const [bookId, setbookId] = useState("");
  const [message, setmessage] = useState({});
  const [isVisible, setVisible] = useState(false);
  const timeoutId = useRef(null);
  const submitHandler = async (e) => {
    e.preventDefault();
    const data = {
      book_id: parseInt(bookId),
      member_id: parseInt(bookId),
    };
    var res = await axios.post(`${URL}/borrow`, data);
    console.log(res.data)
    setmessage(res.data);
    
    setVisible(true);
    if (timeoutId.current) {
      clearTimeout(timeoutId.current);
    }
    setVisible(true);
    timeoutId.current = setTimeout(() => {
      setVisible(false);
    }, 5000);

  };
  return (
    <div className="container-fluid">
      <form>
        <div className="form-group">
          <label htmlFor="member">Member ID</label>
          <input
            onChange={(e) => {
              setmemberId(e.target.value);
            }}
            type="text"
            className="form-control"
            id="member"
            placeholder="Enter Member ID"
            value={memberId}
          />
        </div>
        <div className="form-group">
          <label htmlFor="book">Book ID</label>
          <input
            onChange={(e) => {
              setbookId(e.target.value);
            }}
            value={bookId}
            type="text"
            className="form-control"
            id="book"
            placeholder="Enter Book ID"
          />
        </div>
        <br />
        <button
          type="button"
          onClick={submitHandler}
          className="btn btn-primary"
        >
          Submit
        </button>
        <br />
        <br />
        {isVisible === true ? (
          <div>
            <MessageBorrow msg={message} />
          </div>
        ) : (
          <div></div>
        )}
      </form>
    </div>
  );
}

export default BookBorrow;
