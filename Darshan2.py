import os
from flask import Flask, request, jsonify
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo,
)
from pymongo import MongoClient

# Set up MongoDB Atlas connection
# Replace 'YOUR_CONNECTION_STRING' with your actual MongoDB Atlas connection string
mongo_client = MongoClient('mongodb+srv://priyanshurouth:Paromita@model.chpqwbx.mongodb.net/?retryWrites=true&w=majority')
db = mongo_client['mydb']  # Replace 'mydb' with your database name

# Check if MongoDB is connected
try:
    mongo_client.server_info()  # This will raise an exception if MongoDB is not connected
    print("Connected to MongoDB Atlas")
except Exception as e:
    print(f"Failed to connect to MongoDB Atlas: {str(e)}")

# Import OpenAI API key
os.environ['OPENAI_API_KEY'] = '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'

# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()

# Create and load PDF Loader
loader = PyPDFLoader('Divorce.pdf')
pages = loader.load_and_split()

# Create and load documents into MongoDB-based vector database
store = MongoDBAtlasVectorSearch(
    collection=db['mydb'],  # Specify your desired collection
    embedding=OpenAIEmbeddings(),   # Specify your embedding model
    text_key='text_field_name',     # Specify the text field name
    embedding_key='embedding_field_name',  # Specify the embedding field name
    index_name='my_search_index'    # Specify your custom search index name
)
store.insert_documents(pages, embeddings)

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
    name="Divorce.pdf",
    description="A Divorce petition filed by husband",
    vectorstore=store
)

# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

# Create a Flask application instance
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_response():
    # Get the prompt from the request
    prompt = request.json['prompt']

    # Check if the prompt is provided
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Generate a response using the LLM
    response = agent_executor.run(prompt)

    # Find document similarity
    search = store.similarity_search_with_score(prompt)
    top_similar_page = search[0][0].page_content

    return jsonify({'response': response, 'top_similar_page': top_similar_page})

if __name__ == '__main__':
    app.run(debug=True)
