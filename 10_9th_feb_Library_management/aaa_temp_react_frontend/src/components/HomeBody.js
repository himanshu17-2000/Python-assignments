import React from "react";
import BookBorrow from "./BookBorrow";
import BookReturn from "./BookReturn";
import FetchBooks from "./FetchBooks";
import FetchTransactions from "./FetchTransactions";
const HomeBody = () => {
  return (
    <div className="container-fluid">
      <div className="row">
        <div className="main-div1 col-6 ">
          <div
            className="sub-div2-borrow"
            style={{
              height: 500,
              marginBottom: 5,
              borderTop: "2px solid black",
              borderRight: "2px solid black",
            }}
          >
            <h1 style={{ textAlign: "center", width: "100%" }}>Borrow Book</h1>
            <BookBorrow />
          </div>
          <div
            className="sub-div2-return"
            style={{
              height: 500,

              marginBottom: 5,
              borderTop: "2px solid black",
              borderRight: "2px solid black",
            }}
          >
            <h1 style={{ textAlign: "center", width: "100%" }}>Return Book</h1>
            <BookReturn />
          </div>
        </div>
        <div className="main-div2 col-6">
          <div
            className="sub-div2-books"
            style={{
              height: 500,
              overflowY: "scroll",
              marginBottom: 5,
              borderTop: "2px solid black",
              borderLeft: "2px solid black",
            }}
          >
            <h1 style={{ textAlign: "center", width: "100%" }}>Books</h1>
            <FetchBooks />
          </div>
          <div
            className="sub-div2-transactions"
            style={{
              height: 500,
              overflowY: "scroll",
              marginBottom: 5,
              borderTop: "2px solid black",
              borderLeft: "2px solid black",
             
            }}
          >
            <h1 style={{ textAlign: "center", width: "100%" }}>Transactions</h1>
            <FetchTransactions />
          </div>
        </div>
        <div
          className="col-12"
          style={{
            width: "100%",
            textAlign: "center",
            borderTop: "2px solid black",
          }}
        >
          <h1 style={{ width: "100%", textAlign: "center" }}>
            Report interface
          </h1>
        </div>
      </div>
    </div>
  );
};

export default HomeBody;
