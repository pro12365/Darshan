# Naydarshan AI Legal Document Assistant

Naydarshan AI Legal Document Assistant is a prototype application designed to assist users in drafting legal documents. This application leverages the power of GPT-3, a state-of-the-art language model developed by OpenAI, to provide intelligent responses to legal queries and generate legal document content.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

Naydarshan AI is a legal document assistant that simplifies the process of drafting legal documents. It is built using Python and various libraries and services, including Streamlit for the user interface and OpenAI's GPT-3 for natural language processing. The application allows users to input legal queries, and it generates responses and document content based on those queries. Additionally, it provides a document similarity search feature to find relevant documents.

## Features

- **User-Friendly Interface**: Naydarshan AI offers an intuitive web interface powered by Streamlit, making it easy for users to interact with the application.

- **Legal Document Assistance**: Users can input legal queries, and the application uses GPT-3 to provide intelligent and context-aware responses, assisting in legal document drafting.

- **Document Similarity Search**: The application performs document similarity searches to find relevant documents based on the user's query.

- **History Tracking**: The application keeps track of query history, allowing users to view and revisit previous queries.

## Getting Started

To get started with Naydarshan AI Legal Document Assistant, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/pro12365/Darshan.git
   ```

2. Install the required dependencies. You can use `pip` to install them:

   ```shell
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   
   - OpenAI's GPT-3 service is used in this application. You'll need to obtain an API key from OpenAI and set it as an environment variable. Replace `'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'` with your API key in the code:

     ```python
     os.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'
     ```

4. Run the application:

   ```shell
   streamlit run app.py
   ```

5. Access the Naydarshan AI Legal Document Assistant in your web browser at the provided URL (usually `http://localhost:8501`).

## Usage

Once you have the application running, you can use it as follows:

1. Enter your legal query in the text box provided on the main interface.

2. Click the "Search" button to submit your query.

3. The application will generate a response based on your query using GPT-3 and display it on the screen.

4. You can also expand the "Document Similarity Search" section to find relevant documents related to your query.

5. The sidebar displays your query history, allowing you to revisit previous queries.

## Dependencies

Naydarshan AI Legal Document Assistant relies on several Python libraries and services, including:

- [Streamlit](https://streamlit.io/): For creating the user interface.
- [OpenAI GPT-3](https://beta.openai.com/): For natural language processing.
- [PyPDF2](https://pythonhosted.org/PyPDF2/): For handling PDF document loading.
- [langchain](https://github.com/langchain/langchain): For vectorization and similarity search.
- [streamlit-scrollable-textbox](https://github.com/andfanilo/streamlit-scrollable-textbox): For scrollable text box functionality.

You can find a full list of dependencies in the `requirements.txt` file.

## Contributing

Contributions to Naydarshan AI Legal Document Assistant are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository to your own GitHub account.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your fork.

5. Create a pull request to the main repository's `master` branch.

Please make sure to follow the code of conduct and guidelines provided in the repository.
