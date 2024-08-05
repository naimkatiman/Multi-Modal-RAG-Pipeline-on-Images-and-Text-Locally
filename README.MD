# Multi-Modal RAG Pipeline on Images and Text Locally

![RAG Pipeline Banner](D:\Anaconda\Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally\RAG.jpg)

This repository contains a Multi-Modal Retrieval-Augmented Generation (RAG) Pipeline that processes both images and text locally. It leverages advanced NLP and computer vision techniques to create a powerful information retrieval and generation system.

## 🌟 Features

- Local processing of images and text
- Integration with Qdrant vector store
- CLIP image embedding for efficient image retrieval
- Multi-modal index creation using LlamaIndex
- Interactive query system with both text and image results

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/naimkatiman/Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally.git
   cd Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare your data:
   - Place your image files (.jpg or .png) in the `data` directory
   - Ensure corresponding text files (.txt) with the same name exist for each image

4. Run the pipeline:
   ```python
   python main.py
   ```

## 📚 How It Works

1. **Data Preparation**: The system scans the specified directory for image-text pairs.

2. **Index Creation**: A multi-modal index is created using LlamaIndex, storing both text and image embeddings.

3. **Query Processing**: Users can input queries, and the system retrieves relevant text and images.

4. **Visualization**: Retrieved images are displayed using matplotlib.

Here's a simple visualization of the pipeline:

```mermaid
graph TD
    A[Data Preparation] --> B[Index Creation]
    B --> C[Query Processing]
    C --> D[Result Visualization]
    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style B fill:#eeac99,stroke:#333,stroke-width:2px
    style C fill:#e06377,stroke:#333,stroke-width:2px
    style D fill:#c83349,stroke:#333,stroke-width:2px
```

## 🖼️ Example Queries

Here are some example queries and their results:

1. "Who is Naim?"
   ![Naim Query Result](D:\Anaconda\Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally\Naim.png)

2. "What is space?"
   ![Space Query Result](D:\Anaconda\Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally\space.png)

3. "Where is AI?"
   ![AI Query Result](D:\Anaconda\Multi-Modal-RAG-Pipeline-on-Images-and-Text-Locally\ai.png)

## 🛠️ Configuration

You can customize the pipeline by modifying the following parameters in `config.py`:

- `DATA_PATH`: Path to your image and text data
- `QDRANT_PATH`: Path for local Qdrant storage
- `TOP_K`: Number of results to retrieve for each query

## 📊 Performance

The Multi-Modal RAG Pipeline offers:

- Fast retrieval times (typically <100ms)
- High accuracy in matching relevant images and text
- Scalability to handle large datasets

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [LlamaIndex](https://github.com/jerryjliu/llama_index) for the indexing framework
- [Qdrant](https://github.com/qdrant/qdrant) for the vector database
- [CLIP](https://github.com/openai/CLIP) for image embeddings

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/naimkatiman">Naim Katiman</a>
</div>