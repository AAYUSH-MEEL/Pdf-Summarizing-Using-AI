# PDF Summarizing Tool

This project is a PDF summarization web application built using Streamlit and Langchain. It allows users to upload PDF files and generates concise summaries of their content using OpenAI's GPT models.

## Features

- Upload PDF files through a simple web interface.
- Extract text from PDF pages.
- Split text into manageable chunks for processing.
- Generate semantic embeddings for text chunks.
- Perform similarity search to find relevant content.
- Use OpenAI GPT-3.5-turbo-16k model to generate a summary of the PDF content.
- Display the summary on the web app.

## Technologies Used

- Python
- Streamlit
- Langchain
- OpenAI API
- FAISS (Facebook AI Similarity Search)
- pypdf

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AAYUSH-MEEL/Pdf-Summarizing-Using-AI.git
   cd Pdf-Summarizing-Using-AI
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY="your_openai_api_key"
   ```

## Usage

Run the Streamlit app:
```
streamlit run test.py
```

Open the URL provided by Streamlit in your browser. Upload a PDF file and click "Generate Summary" to get a concise summary of the document.

## Notes

- Make sure you have a valid OpenAI API key.
- The summarization quality depends on the input PDF and the OpenAI model used.
- The app currently uses the GPT-3.5-turbo-16k model.

## License

This project is licensed under the MIT License.

## Author

Developed by Aayush Meel
