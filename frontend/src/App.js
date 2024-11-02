import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Tab, Tabs } from "react-bootstrap";
//import ChatWithPDFs from "./ChatWithPdf";
import RAGApplication from "./RAGApplication";

function App() {
  return (
    <div>
      <h1>MULTIMODAL LLM APPLICATION</h1>
      <Tabs defaultActiveKey="chat">
        <Tab eventKey="rag" title="RAG Application">
          <RAGApplication />
        </Tab>
      </Tabs>
    </div>
  );
}

export default App;
