import React, { useEffect } from 'react';

export default function Toast({ message, onClose }) {
  
  return (
    <div className="toast">
      <div dangerouslySetInnerHTML={{ __html: message }} />
      <span className="cross" onClick={onClose}>
        <i className="fa-solid fa-xmark"></i>
      </span>
    </div>
  );
}
