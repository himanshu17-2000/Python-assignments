import React, { useState, useRef } from "react";
import { URL } from "./constant";
import axios from "axios";
import { MessageFine, MessageReturn } from "./Message";
function BookReturn() {
  const [traId, settraId] = useState("");
  const [message, setmessage] = useState({});
  const [isVisible1, setVisible1] = useState(false);
  const [isVisible2, setVisible2] = useState(false);
  const [fine, setFine] = useState();
  const [member , setMember] = useState() ; 
  const timeoutId = useRef(null);
  const submitHandler = async (e) => {
    e.preventDefault();
    const data = {
      tra_id: parseInt(traId),
    };
    var res = await axios.post(`${URL}/return`, data);
    console.log(res.data);
    setmessage(res.data);
    setVisible1(true);
    if (timeoutId.current) {
      clearTimeout(timeoutId.current);
    }
    setVisible1(true);
    timeoutId.current = setTimeout(() => {
      setVisible1(false);
    }, 5000);
  };
  const submitHandlerFine = async (e) => {
    e.preventDefault();
    const data = {
      member_id:parseInt(member),
      amount :parseInt(fine),
    };
    var res = await axios.post(`${URL}/debt`, data);
    console.log(res.data);
    setmessage(res.data);
    setVisible2(true);
    if (timeoutId.current) {
      clearTimeout(timeoutId.current);
    }
    setVisible2(true);
    timeoutId.current = setTimeout(() => {
      setVisible2(false);
    }, 5000);
  };
  return (
    <div className="container-fluid">
      <form>
        <div className="form-group">
          <label htmlFor="Transaction">Transaction ID</label>
          <input
            onChange={(e) => {
              settraId(e.target.value);
            }}
            type="text"
            className="form-control"
            id="Transaction"
            placeholder="Enter Transaction ID"
            value={traId}
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
        <div className="payment"></div>
        <br />
      </form>

      <form>
        <div className="form-group">
          <label htmlFor="Fine">Fine</label>
          <input
            onChange={(e) => {
              setFine(e.target.value);
            }}
            type="text"
            className="form-control"
            id="Fine"
            placeholder="Enter fine "
            value={fine}
          />
        </div>
        <div className="form-group">
          <label htmlFor="member">Member-ID</label>
          <input
            onChange={(e) => {
              setMember(e.target.value);
            }}
            type="text"
            className="form-control"
            id="member"
            placeholder="Enter member-id "
            value={member}
          />
        </div>
            <br/>
        <button
          type="button"
          onClick={submitHandlerFine}
          className="btn btn-primary"
        >
          Submit
        </button>
      </form>
      {isVisible1 === true ? (
        <div>
          <MessageReturn msg={message} />
        </div>
      ) : (
        <div></div>
      )}
      {isVisible2 === true ? (
        <div>
          <MessageFine msg={message} />
        </div>
      ) : (
        <div></div>
      )}
    </div>
  );
}

export default BookReturn;
