import React, { useState ,useRef } from "react";
import { URL } from "./constant";
import axios from "axios";
import {MessageReturn} from "./Message";
function BookReturn() {
  const [traId, settraId] = useState("");
  const [message, setmessage] = useState({});
  const [isVisible, setVisible] = useState(false);
  const timeoutId = useRef(null);
  const submitHandler = async (e) => {
    e.preventDefault();
    const data = {
      tra_id: parseInt(traId),
    };
    var res = await axios.post(`${URL}/return`, data);
    console.log(res.data);
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
        <br/>
        <button
          type="button"
          onClick={submitHandler}
          className="btn btn-primary"
        >
          Submit
        </button>
        <br/>
        <br/>
        {isVisible === true ? (
          <div>
            <MessageReturn msg={message} />
          </div>
        ) : (
          <div></div>
        )}
      </form>
    </div>
  );
}

export default BookReturn;
