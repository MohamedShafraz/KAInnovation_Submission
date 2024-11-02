import React from 'react'
import { Form, FormControl, Button, Image } from "react-bootstrap";
import { Tab, Tabs } from 'react-bootstrap';
import { ChatMessage } from './ChatMessage'
import { ChatSideBar } from './ChatSideBar'
import { ChatOpitons } from './ChatOpitons'
import { Apps } from './apps/index'
import { ChatList } from './ChatList'
import { classnames } from '../components/utils'
import { useGlobal } from './context'
import { Search } from '@/components'
import styles from './style/chat.module.less'
import { ScrollView } from './component'
import { useOptions } from './hooks';
import { options } from 'less';
import { Icon } from '../components';
import { FileUploader } from './fileupload';

export default function Chats() {
  const { is } = useGlobal()
  const chatStyle = is.fullScreen ? styles.full : styles.normal
  // console.log(is);
  const { setGeneral } = useOptions()
  
  // setGeneral({ theme: options.general.theme === 'light' ? 'dark' : 'light' });
  // options.general.theme = 'dark';
  
  // console.log(options.general);
  const onSearch = (e) => {
    console.log(e)
  }
  return (
    <div id="x">
    
      
    <div className={classnames(styles.chat, chatStyle)}>

      <div className={styles.chat_inner}>
      
        <ChatSideBar />
        {
          is.config ?
            <ChatOpitons /> :
            <React.Fragment>
              {
                is.sidebar && <div className={styles.sider}>
                  <div className={styles.search}>
                    <Search onSearch={onSearch} />
                  </div>
                  <ScrollView>
                    {is.apps ? <Apps /> : <ChatList />}
                  </ScrollView>
                </div>
              }
              <ChatMessage />
            </React.Fragment>
        }
      </div>
    </div>
   
    </div>
  )
}
