from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from routers.ask import VECTOR_DIR


VECTOR_DIR="backend/vectorstore"

def build_rag_chain(): #构建 RAG 检索 + 生成链
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 4})
    
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

    prompt_template = """
    You are a helpful assistant that answers questions **only** using the provided context.
    Be concise, factual, and avoid speculation.
    If the context does not contain the answer, reply:
    "I don't have relevant information from the uploaded documents."


    Context:
    {context}

    Question:
    {question}
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain


def query_rag(question: str):
    chain = build_rag_chain() # 执行一次 RAG 检索问答
    result = chain.run(question)
    return result
