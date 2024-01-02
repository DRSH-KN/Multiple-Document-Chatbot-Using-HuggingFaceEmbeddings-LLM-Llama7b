The "Document Search & Chat" application represents an innovative solution designed to facilitate seamless interaction and information retrieval from a vast array of documents.
Leveraging cutting-edge technologies like Streamlit, PyPDF2, Hugging Face embeddings, and Llama7b, this application offers users the ability to not only search through a multitude 
of uploaded PDF files but also engage in conversational interactions based on the content within these documents.

Methodology: 
1. Application Flow Overview
   
User Interaction: Users upload PDF documents through the Streamlit interface.

Text Extraction: PyPDF2 extracts text content from the uploaded PDF files.

Text Chunking: The extracted text is divided into manageable chunks for further processing.

Embedding Generation: Hugging Face embeddings transform text chunks into vector representations.

Conversational Chain: Llama7b facilitates context-driven conversations based on the document content.
