import React from "react";

export const MessageBorrow = (props) => {
  return (
    <div style={{ background: "#089616", color: "white", padding: 5 }}>
      <h6>TransactionID : {props.msg.tra_id}</h6>
      <p>{props.msg.message}</p>
    </div>
  );
};

export const MessageReturn = (props) => {
  return (
    <div>
      <div style={{ background: "#2b04b8", color: "white", padding: 5 }}>
        <h6>Your Total rent : {props.msg.rent}/- Rs</h6>
        <p>{props.msg.message}</p>
      </div>
    </div>
  );
};
