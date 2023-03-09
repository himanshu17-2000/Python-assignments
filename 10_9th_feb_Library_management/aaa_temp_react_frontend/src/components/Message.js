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
        <h6>Your Total rent : {props.msg.rent ? props.msg.rent : 0 }/- Rs</h6>
        <p>{props.msg.message}</p>
      </div>
    </div>
  );
};

export const MessageFine= (props) => {
  return (
    <div>
      <div style={{ background: "#slateblue", color: "white", padding: 5 }}>
        <h6>Amount paid :- {props.msg.amount ? props.msg.amount : 0 }/- Rs</h6>
        <p>{props.msg.message}</p>
        <p> Remaining Amount :- {props.msg.remaining}</p>
      </div>
    </div>
  );
};
