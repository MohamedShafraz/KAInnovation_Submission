import React from 'react'
import { Button, Panel, Input, Title, Avatar, Select } from '@/components'
import { useGlobal } from './context'
import { themeOptions, languageOptions, sendCommandOptions, modelOptions, sizeOptions,dbOptions } from './utils'
import { Tooltip } from '../components'
import styles from './style/config.module'
import { classnames } from '../components/utils'
import { useOptions } from './hooks'

export function ConfigHeader() {
  const { setIs, is } = useGlobal()
  return (
    <div className={classnames(styles.header, 'flex-c-sb')}>
      <Title type="h5">Setting</ Title>
      <div className="flex-c">
        <Button type="icon" onClick={() => setIs({ config: !is.config })} icon="refresh" />
        <Button type="icon" onClick={() => setIs({ config: !is.config })} icon="close" />
      </div>
    </div >
  )
}

export function ChatOpitons() {
  const { options } = useGlobal()
  const { account, openai, general } = options
  const { setAccount, setGeneral, setModel } = useOptions()
  return (
    <div className={classnames(styles.config, 'flex-c-sb flex-column')}>
      <ConfigHeader />
      <div className={classnames(styles.inner, 'flex-1')}>
        
        <Panel className={styles.panel} title="General">
          <Panel.Item icon="light" title="Theme Style" desc="Select interface style">
            <Select value={general.theme} onChange={(val) => setGeneral({ theme: val })} options={themeOptions} placeholder="Select interface style" />
          </Panel.Item>
          <Panel.Item icon="files" title="Send messages" desc="Want to make this keyboard shortcut a global one?">
            <Select value={general.command} onChange={(val) => setGeneral({ sendCommand: val })} options={sendCommandOptions} placeholder="Select interface style" />
          </Panel.Item>
          <Panel.Item icon="lang" title="Language" desc="Select interface language">
            <Select value={general.language} onChange={val => setGeneral({ language: val })} options={languageOptions} placeholder="language" />
          </Panel.Item>
        </Panel>
        
      </div>
    </div>
  )
}
