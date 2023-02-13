import React, { useEffect, useState } from "react";
import axios from "axios";
import { URL } from "./constant";
function FetchTransactions() {
  const [transactions, settransactions] = useState([]);
  const [traID, settraID] = useState("");
  const [memberID, setmemberID] = useState("");

  const fetchbook = async () => {
    const res = await axios.get(`${URL}/transactions`);

    settransactions(res.data);
    console.log(res.data);
  };

  return (
    <div>
      <br />
      <div className="form-group">
        <label htmlFor="traid">Transaction ID</label>
        <input
          className="form-control"
          id="traid"
          type={"number"}
          placeholder="filter by trasaction id "
          value={traID}
          onChange={(e) => {
            settraID(e.target.value);
          }}
        />
      </div>

      <div className="form-group">
        <label htmlFor="member">Member ID</label>
        <input
          className="form-control"
          id="member"
          type={"number"}
          placeholder="filter by member id "
          value={memberID}
          onChange={(e) => {
            setmemberID(e.target.value);
          }}
        />
      </div>
      
      <button style={{marginTop:"3px"}}  className="btn btn-primary" onClick={fetchbook}>Fetch Transactions</button>
      <div>
        {transactions
          .filter((item) => {
            if (traID === "" && memberID === "" ) return item;
            else if (
              item.tra_id
                .toString()
                .toLowerCase()
                .includes(traID.toString().toLowerCase()) &&
              item.member_id
                .toString()
                .toLowerCase()
                .includes(memberID.toString().toLowerCase())
            ) {
              return item;
            }
          })
          .map((item) => {
            const col = item.borrowed == true ? "red" : "green";
            const message = item.borrowed == true ? "Rented" : "Returned";
            return (
              <div
                key={item.tra_id}
                style={{ background: "#bdbdbd", padding: "5px", margin: "5px" }}
              >
                <h3>Member_id:{item.member_id}</h3>
                <span>name : {item.book_name} , </span>
                <span>From : {item.from_date} , </span>
                <span>fine : {item.fine}/- Rs ,</span>
                <p>
                  <span>Borrowed :</span>
                  <span style={{ color: `${col}` }}>
                    <strong>{message}</strong>
                  </span>
                </p>
              </div>
            );
          })}
      </div>
    </div>
  );
}
// "book_id": 1,
//         "book_name": "From Blood and Ash",
//         "borrowed": false,
//         "fine": 0,
//         "from_date": "2023-02-10",
//         "member_id": 1,
//         "tra_id": 1

export default FetchTransactions;
