# solved pine cone issue

import os
import uuid
import base64
from IPython import display
from unstructured.partition.pdf import partition_pdf
from langchain_openai import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings as fe
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain.schema.document import Document
from langchain.vectorstores import FAISS
from langchain.retrievers.multi_vector import MultiVectorRetriever
from pinecone import Pinecone
from langchain.vectorstores import Pinecone as pine
import numpy as np
from langchain_community.chat_models import ChatAnthropic
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings as pe
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_community.llms import Together
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from dotenv import load_dotenv
load_dotenv() 
openai_api_key = os.getenv("open_ai_key")

prompt_template = """
You are financial analyst tasking with providing investment advice.
Answer the question based only on the following context, which can include text, images and tables:
{context}
Question: {question}
Just return the helpful answer in as much as detailed possible.
Answer:
"""

# loading faiss db
embeddings = fe(openai_api_key=Openai_api_key)
# db = FAISS.load_local("faiss_index", embeddings)
db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)




# initialize the model
def initialize_model(model_name):
    if model_name == "gpt-4o-mini":
        prompt = PromptTemplate(
    input_variables=["context", "question"], 
    template=prompt_template
)
        llm = LLMChain(llm=ChatOpenAI(model="gpt-4o-mini", openai_api_key=Openai_api_key), prompt=prompt)
        # return LLMChain(
        #     llm=ChatOpenAI(
        #         model="gpt-4o-mini", openai_api_key=openai_api_key, max_tokens=1024
        #     ),
        #     prompt=PromptTemplate.from_template(prompt_template),
        # )
        return llm
    elif model_name == "gpt-3.5-turbo":
        return llm(
            llm=ChatOpenAI(
                model="gpt-3.5-turbo", openai_api_key=Openai_api_key, max_tokens=1024
            ),
            prompt=PromptTemplate.from_template(prompt_template),
        )
    # elif model_name == "claude-2":
    #     return llm(
    #         llm=ChatAnthropic(
    #             temperature=0, anthropic_api_key=claude_api_key, model_name="claude-2"
    #         ),
    #         prompt=PromptTemplate.from_template(prompt_template),
    #     )
    # elif model_name == "mistral":
    #     return llm(
    #         llm=Together(
    #             model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    #             temperature=0,
    #             max_tokens=500,
    #             top_k=3,
    #             together_api_key=together_api_key,
    #         ),
    #         prompt=PromptTemplate.from_template(prompt_template),
    #     )
    # elif model_name == "llama2-7b":
    #     return llm(
    #         llm=Together(
    #             model="meta-llama/Llama-2-7b-chat-hf",
    #             temperature=0,
    #             max_tokens=500,
    #             top_k=3,
    #             together_api_key=together_api_key,
    #         ),
    #         prompt=PromptTemplate.from_template(prompt_template),
    #     )
    # elif model_name == "gemma-7b":
    #     return llm(
    #         llm=Together(
    #             model="google/gemma-7b-it",
    #             temperature=0,
    #             max_tokens=500,
    #             top_k=3,
    #             together_api_key=together_api_key,
    #         ),
    #         prompt=PromptTemplate.from_template(prompt_template),
    #     )

    else:
        raise ValueError(f"Unsupported model name: {model_name}")


def answer_question(question, model, database_name):
    # Default assignment to prevent UnboundLocalError
    vector_db = None

    if database_name == "faiss":
        vector_db = (
            db  # Ensure 'db' is defined earlier in your code or passed as an argument
        )
    
    # Handle case where vector_db is not assigned
    if vector_db is None:
        raise ValueError(f"Unsupported database_name: {database_name}")

    qa_chain = initialize_model(
        model
    )  # Ensure this function is defined and works as expected
    relevant_docs = vector_db.similarity_search(question)
    context = ""
    relevant_images = []

    for d in relevant_docs:
        if database_name == "faiss":
            if d.metadata["type"] == "text":
                context += "[text]" + d.metadata["original_content"]
            elif d.metadata["type"] == "table":
                context += "[table]" + d.metadata["original_content"]
            elif d.metadata["type"] == "image":
                context += "[image]" + d.page_content
                relevant_images.append(d.metadata["original_content"])


    result = qa_chain.run({"context": context, "question": question})
    return result, relevant_images

