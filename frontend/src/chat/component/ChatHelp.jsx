import React from 'react'
import styles from './style.module'
import EmptyImg from './EmptyImg'
import './ChatHelp.css';
import action from '../context/action';
import { Button } from 'react-bootstrap';
import { ChatMessage,MessageBar } from '../ChatMessage';

export function ChatHelp() {
  const handleButtonClick = () => {
    // Call the triggerSendButtonClick function from the ChatHelp component
    
  };
  
  return (
    <div className={styles.help}>
      <h1 className='name'>GPT-Chat</h1>
          </div>
  )
}
