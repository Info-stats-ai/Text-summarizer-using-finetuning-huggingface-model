# 📝 Text Summarization Project

A comprehensive **Machine Learning Pipeline** for text summarization using **Hugging Face Transformers** and **FastAPI**. This project demonstrates end-to-end ML engineering practices including data processing, model training, evaluation, and deployment.

## 🎯 Project Overview

This project implements an **automated text summarization system** that can take long text inputs and generate concise, meaningful summaries. Built using state-of-the-art NLP models and following ML engineering best practices.

### Key Features
- **End-to-end ML Pipeline**: From raw data to deployed model
- **Hugging Face Integration**: Uses Pegasus model for summarization
- **RESTful API**: FastAPI-based web service
- **Clean Architecture**: Modular, maintainable code structure
- **Production Ready**: Comprehensive logging, error handling, and monitoring

## 🏗️ Project Architecture

```
Text-Summary/
├── src/textsummarization/          # Main source code
│   ├── components/                 # ML components
│   │   ├── data_ingestion.py      # Data downloading & extraction
│   │   ├── data_transformation.py # Data preprocessing
│   │   ├── model_trainer.py       # Model training logic
│   │   └── model_evaluation.py    # Model evaluation
│   ├── pipeline/                   # Pipeline orchestration
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_transformation.py
│   │   └── stage_04_model_evaluation.py
│   ├── config/                     # Configuration management
│   ├── entity/                     # Data classes
│   ├── utils/                      # Utility functions
│   └── logging/                    # Logging configuration
├── config/                         # Configuration files
│   ├── config.yaml                # Main configuration
│   └── params.yaml                # Model hyperparameters
├── research/                       # Jupyter notebooks for experimentation
├── artifacts/                      # Generated outputs (models, data)
├── logs/                          # Application logs
├── templates/                     # HTML templates
├── app.py                         # FastAPI application
├── main.py                        # Pipeline orchestration
└── requirements.txt               # Dependencies
```

## 🚀 What This Project Achieves

### 1. **Complete ML Pipeline**
- **Data Ingestion**: Automated downloading and extraction of datasets
- **Data Transformation**: Text preprocessing and tokenization
- **Model Training**: Fine-tuning of Pegasus model on custom dataset
- **Model Evaluation**: Comprehensive evaluation using ROUGE metrics
- **Model Deployment**: Production-ready API service

### 2. **Production-Grade Code**
- **Modular Design**: Clean separation of concerns
- **Configuration Management**: YAML-based configuration system
- **Error Handling**: Comprehensive exception handling
- **Logging**: Detailed logging for monitoring and debugging
- **Type Safety**: Type hints and validation throughout

### 3. **User-Friendly Interface**
- **REST API**: Simple HTTP endpoints for text summarization
- **Web Interface**: Clean HTML frontend for easy interaction
- **API Documentation**: Auto-generated Swagger UI documentation

## 🛠️ Technical Stack

### Core Technologies
- **Python 3.10**: Main programming language
- **Hugging Face Transformers**: Pre-trained models and tokenizers
- **PyTorch**: Deep learning framework
- **FastAPI**: Modern web framework for APIs
- **Uvicorn**: ASGI server for FastAPI

### Key Libraries
- `transformers`: State-of-the-art NLP models
- `torch`: Deep learning computations
- `datasets`: Dataset loading and processing
- `evaluate`: Model evaluation metrics
- `pandas`: Data manipulation
- `pyyaml`: Configuration file parsing
- `python-box`: Enhanced dictionary access

## 📊 Dataset & Model

### Dataset
- **SamSum Dataset**: Conversation summarization dataset
- **Format**: Dialogue → Summary pairs
- **Size**: ~16,000 training examples
- **Source**: Hugging Face Datasets

### Model
- **Base Model**: `google/pegasus-cnn_dailymail`
- **Architecture**: Transformer-based encoder-decoder
- **Fine-tuning**: Custom training on SamSum dataset
- **Output**: Concise summaries of input text

## 🎯 Key Challenges Overcome

### 1. **Environment & Dependencies**
- **Challenge**: Python version compatibility issues (3.13 vs 3.10)
- **Solution**: Created isolated virtual environment with Python 3.10
- **Learning**: Always test library compatibility before starting projects

### 2. **Import & Module Structure**
- **Challenge**: Complex import errors due to package naming conventions
- **Solution**: Standardized package structure with proper `__init__.py` files
- **Learning**: Python package naming conventions (no hyphens, use underscores)

### 3. **Configuration Management**
- **Challenge**: Managing complex configuration across multiple components
- **Solution**: Centralized YAML configuration with type-safe data classes
- **Learning**: Configuration as code principles

### 4. **Model Training & Evaluation**
- **Challenge**: Long training times and resource management
- **Solution**: Implemented evaluation pipeline for pre-trained models
- **Learning**: Balance between training time and model performance

### 5. **API Development**
- **Challenge**: Creating user-friendly API responses
- **Solution**: Clean JSON responses with proper error handling
- **Learning**: API design principles for end users

### 6. **Data Pipeline Orchestration**
- **Challenge**: Managing data dependencies and pipeline stages
- **Solution**: Implemented stage-based pipeline with proper error handling
- **Learning**: ML pipeline orchestration best practices

## 🏆 Achievements

### Technical Achievements
✅ **Complete ML Pipeline**: End-to-end implementation from data to deployment  
✅ **Production-Ready Code**: Clean, maintainable, and well-documented codebase  
✅ **API Service**: Functional REST API with web interface  
✅ **Model Evaluation**: Comprehensive evaluation using industry-standard metrics  
✅ **Error Handling**: Robust error handling and logging throughout  
✅ **Configuration Management**: Flexible, maintainable configuration system  

### Learning Achievements
✅ **ML Engineering**: Understanding of production ML system design  
✅ **API Development**: FastAPI and RESTful service development  
✅ **Pipeline Orchestration**: Managing complex ML workflows  
✅ **Debugging Skills**: Systematic problem-solving and error resolution  
✅ **Best Practices**: Code organization, logging, and documentation  

## 🚀 Getting Started

### Prerequisites
- Python 3.10
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Text-Summary
   ```

2. **Create virtual environment**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the pipeline**
   ```bash
   python main.py
   ```

5. **Start the API server**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Web Interface: `http://localhost:8080`
   - API Documentation: `http://localhost:8080/docs`

## 📖 Usage Examples

### API Usage
```bash
# Summarize text via API
curl -X POST "http://localhost:8080/predict?text=Your long text here"
```

### Python Usage
```python
from src.textsummarization.pipeline.prediction_pipeline import PredictionPipeline

# Initialize pipeline
pipeline = PredictionPipeline()

# Generate summary
summary = pipeline.predict("Your long text here")
print(summary)
```

## 📈 Performance Metrics

The model is evaluated using **ROUGE metrics**:
- **ROUGE-1**: Unigram overlap
- **ROUGE-2**: Bigram overlap  
- **ROUGE-L**: Longest common subsequence
- **ROUGE-Lsum**: Summary-level LCS

## 🔧 Configuration

### Main Configuration (`config/config.yaml`)
- Data paths and URLs
- Model checkpoints
- Output directories
- Evaluation settings

### Hyperparameters (`params.yaml`)
- Training arguments
- Model parameters
- Evaluation settings

## 📝 Logging

Comprehensive logging system:
- **File Logging**: All logs saved to `logs/running_logs.log`
- **Console Logging**: Real-time output to terminal
- **Structured Logging**: Consistent format across all components

## 🧪 Research & Experimentation

The `research/` directory contains Jupyter notebooks for:
- Data exploration and analysis
- Model experimentation
- Pipeline testing
- Performance evaluation

## 🚀 Deployment

### Local Deployment
```bash
python app.py
```

### Production Considerations
- Environment variables for configuration
- Docker containerization
- Load balancing for high traffic
- Monitoring and alerting
- Model versioning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Hugging Face**: For providing excellent NLP models and tools
- **SamSum Dataset**: For the conversation summarization dataset
- **FastAPI**: For the modern web framework
- **Open Source Community**: For the amazing tools and libraries

## 📞 Support

For questions or issues:
1. Check the logs in `logs/running_logs.log`
2. Review the API documentation at `/docs`
3. Open an issue in the repository

---

**Built with ❤️ using Python, Hugging Face, and FastAPI**