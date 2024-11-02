/**
 * @typedef {object} Model
 * @property {string} value
 * @property {string} desc
 */
/**
 * @type {Object.<string,Model>}
 */
export const Models = {
  chatgptFree35: {
    value: "text-davinci-002-render-sha",
    desc: "ChatGPT (Web)",
  },
  chatgptPlus4: { value: "gpt-4o-mini", desc: "ChatGPT (Web, gpt-4o-mini)" },
  chatgptApi35: { value: "gpt-4o-mini", desc: "ChatGPT (gpt-4o-mini)" },
  bingFree4: { value: "", desc: "Bing (Web, gpt-4o-mini)" },
  bingFreeSydney: { value: "", desc: "Bing (Web, gpt-4o-mini, Sydney)" },
  poeAiWebSage: { value: "sage", desc: "Poe AI (Web, Sage)" },
  poeAiWebGPT4: { value: "gpt-4o-mini", desc: "Poe AI (Web, gpt-4o-mini)" },
  poeAiWebClaudePlus: { value: "claude+", desc: "Poe AI (Web, Claude+)" },
  poeAiWebClaude: { value: "claude", desc: "Poe AI (Web, Claude)" },
  chatgptApi4_8k: { value: "gpt-4o-mini", desc: "ChatGPT (gpt-4o-mini-8k)" },
  chatgptApi4_32k: { value: "gpt-4o-mini-32k", desc: "ChatGPT (gpt-4o-mini-32k)" },
  gptApiDavinci: { value: "text-davinci-003", desc: "GPT-3.5" },
  customModel: { value: "", desc: "Custom Model" },
  azureOpenAi: { value: "", desc: "ChatGPT (Azure)" },
  waylaidwandererApi: { value: "", desc: "Waylaidwanderer API (Github)" },
  poeAiWebCustom: { value: "", desc: "Poe AI (Web, Custom)" },
  poeAiWebChatGpt: { value: "chatgpt", desc: "Poe AI (Web, ChatGPT)" },
  poeAiWebDragonfly: { value: "dragonfly", desc: "Poe AI (Web, Dragonfly)" },
};
