
import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = () => {
        axios.post('http://localhost:5000/chat', { message })
            .then(res => {
                setResponse(res.data);
            })
            .catch(error => {
                console.error('There was an error sending the message!', error);
            });
    };

    return (
        <div>
            <h1>Chat with GPT</h1>
            <textarea value={message} onChange={e => setMessage(e.target.value)}></textarea>
            <button onClick={sendMessage}>Send</button>
            <div>{response}</div>
        </div>
    );
};

export default Chat;
                