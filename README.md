# Azure AI Search - Multimodal RAG Enhanced Index

[![Azure AI Search](https://img.shields.io/badge/Azure-AI%20Search-0078D4?style=flat&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/en-us/products/ai-services/ai-search)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Microsoft](https://img.shields.io/badge/Microsoft-Azure-0078D4?style=flat&logo=microsoft&logoColor=white)](https://azure.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 🚀 **Production-ready search index schema** for multimodal content with advanced RAG capabilities, vector search, and semantic ranking

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Schema Overview](#-schema-overview)
- [Quick Start](#-quick-start)
- [Use Cases](#-use-cases)
- [Architecture](#-architecture)
- [Scoring Profiles](#-scoring-profiles)
- [Configuration Details](#-configuration-details)
- [Example Usage](#-example-usage)
- [Best Practices](#-best-practices)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The **Azure AI Search Multimodal RAG Enhanced Index** is a comprehensive, enterprise-grade search index schema designed for modern Retrieval-Augmented Generation (RAG) applications. This project provides a battle-tested foundation for building intelligent search solutions that combine traditional full-text search with cutting-edge vector search and semantic ranking capabilities.

### 🌟 Key Highlights

- **🎨 Multimodal Support**: Index and search across text, images, and structured data seamlessly
- **🔍 Hybrid Search**: Combine keyword search, vector similarity, and semantic ranking for superior results
- **🧠 AI-Powered Enrichment**: Built-in support for entity extraction, key phrase identification, and sentiment analysis
- **⚡ High Performance**: Optimized with HNSW algorithm for fast approximate nearest neighbor search
- **📊 Flexible Metadata**: Comprehensive document metadata tracking for advanced filtering and faceting
- **🎯 Semantic Understanding**: Leverage Azure's semantic ranking for context-aware search results

### 💡 What Makes This Special

This isn't just another search schema—it's a production-ready template that incorporates best practices from real-world enterprise deployments. Whether you're building a document intelligence system, enterprise knowledge base, or media asset management platform, this schema provides the foundation you need with:

- Pre-configured scoring profiles for freshness and relevance boosting
- Support for parent-child document relationships via `parent_id`
- Deduplication support through `chunk_hash`
- Multi-language support with configurable analyzers
- Vector embeddings for both text and image content

---

## ✨ Features

### Core Capabilities

| Feature | Description | Benefits |
|---------|-------------|----------|
| **Vector Search** | HNSW and exhaustive KNN algorithms | Fast, accurate similarity search at scale |
| **Semantic Ranking** | Azure Cognitive Search semantic capabilities | Context-aware results with better relevance |
| **Multimodal Indexing** | Text and image vector embeddings | Unified search across content types |
| **AI Enrichment** | Entities, key phrases, sentiment, language detection | Enhanced discoverability and insights |
| **Scoring Profiles** | Freshness and relevance boosting | Customizable ranking for business needs |
| **Suggesters** | Auto-complete and search suggestions | Improved user search experience |

### 🎨 Multimodal Content Support

```
┌─────────────────────────────────────────────────────────┐
│                  Multimodal Index                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  📄 Text Content     🖼️ Images        📊 Metadata      │
│  ├─ Full-text        ├─ Image vectors  ├─ Categories   │
│  ├─ Summaries        └─ Visual search  ├─ Tags         │
│  └─ Content vectors                     └─ Timestamps   │
│                                                         │
│  🔍 Search Modes:                                       │
│  • Keyword Search (BM25)                                │
│  • Vector Similarity (Cosine/Euclidean)                 │
│  • Semantic Ranking (AI-powered)                        │
│  • Hybrid (Combined scores)                             │
└─────────────────────────────────────────────────────────┘
```

### 🎯 Advanced Features

- **Chunk-level Indexing**: Support for document chunking with parent-child relationships
- **Deduplication**: Content hash tracking to prevent duplicate indexing
- **Multi-vector Search**: Separate embeddings for text and image content
- **Rich Filtering**: Filter by date ranges, categories, file types, authors, and more
- **Faceted Navigation**: Enable drill-down search experiences with facets
- **Custom Analyzers**: Language-specific text analysis for global applications

---

## 🗂️ Schema Overview

The index schema is organized into logical field categories for clarity and maintainability.

<details>
<summary><b>🔑 Identity & Relationships</b></summary>

```json
{
  "id": "Unique document identifier (key field)",
  "parent_id": "Reference to parent document for chunk hierarchies",
  "chunk_hash": "Content hash for deduplication"
}
```

**Purpose**: Manage document identity, parent-child relationships, and prevent duplicates.

</details>

<details>
<summary><b>📝 Content Fields</b></summary>

```json
{
  "content": "Main searchable content (full-text indexed)",
  "title": "Document title (boosted in search)",
  "summary": "Document summary or excerpt"
}
```

**Purpose**: Store the primary textual content with appropriate search configurations.

</details>

<details>
<summary><b>🧬 Vector Embeddings</b></summary>

```json
{
  "content_vector": "1536-dimensional embedding of text content",
  "image_vector": "1536-dimensional embedding of image content"
}
```

**Purpose**: Enable semantic and similarity-based search using vector representations.

**Configuration**:
- Dimensions: 1536 (compatible with OpenAI embeddings)
- Algorithm: HNSW for efficient approximate search
- Metric: Cosine similarity

</details>

<details>
<summary><b>🎯 Enrichment & Classification</b></summary>

```json
{
  "entities": "Named entities extracted from content",
  "key_phrases": "Important phrases identified by AI",
  "tags": "User-defined or auto-generated tags",
  "category": "Document category/classification",
  "sentiment": "Sentiment analysis result (positive/negative/neutral)",
  "language": "Detected or specified language code"
}
```

**Purpose**: AI-powered metadata for enhanced discoverability and analytics.

</details>

<details>
<summary><b>📄 Document Metadata</b></summary>

```json
{
  "file_path": "Original file location",
  "file_type": "File extension or MIME type",
  "file_size": "File size in bytes",
  "created_date": "Document creation timestamp",
  "modified_date": "Last modification timestamp",
  "indexed_date": "Indexing timestamp",
  "author": "Document author",
  "source": "Content source system",
  "url": "Original document URL"
}
```

**Purpose**: Track document provenance, enable time-based filtering, and support governance requirements.

</details>

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- ✅ Azure subscription with Azure AI Search service provisioned
- ✅ Python 3.8 or higher installed
- ✅ Azure AI Search admin API key
- ✅ (Optional) OpenAI API key for generating embeddings

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MosheHM/azure-ai-search-schema-index-example.git
   cd azure-ai-search-schema-index-example
   ```

2. **Install dependencies**
   ```bash
   pip install azure-search-documents azure-core
   ```

3. **Configure environment variables**
   ```bash
   export AZURE_SEARCH_ENDPOINT="https://your-service.search.windows.net"
   export AZURE_SEARCH_API_KEY="your-admin-api-key"
   ```

### Deployment Options

#### Option 1: Using Python Script

```python
from deploy_index import create_search_index

# Deploy the index
create_search_index(
    service_endpoint="https://your-service.search.windows.net",
    api_key="your-admin-api-key",
    schema_path="corrected_index_schema.json"
)
```

#### Option 2: Using Azure CLI

```bash
az search index create \
    --service-name your-service-name \
    --name multimodal-rag-index \
    --schema @corrected_index_schema.json
```

#### Option 3: Using Azure Portal

1. Navigate to your Azure AI Search service
2. Select "Indexes" from the left menu
3. Click "Add Index"
4. Import the JSON schema from `corrected_index_schema.json`

---

## 💼 Use Cases

### 🔬 Document Intelligence RAG

Build intelligent document Q&A systems that understand context across multiple documents.

**Example**: Legal contract analysis, technical documentation search, research paper discovery

**Key Features Used**:
- Semantic search for contextual understanding
- Parent-child relationships for document sections
- Entity extraction for key information retrieval

### 🏢 Enterprise Knowledge Base

Create a unified search experience across all company documentation and assets.

**Example**: Employee handbook, policy documents, training materials, project documentation

**Key Features Used**:
- Multi-language support
- Category and tag-based organization
- Author and date filtering
- Freshness boosting for recent content

### 📚 Research & Academic

Index and search academic papers, articles, and research materials with citation tracking.

**Example**: University library systems, research databases, literature review tools

**Key Features Used**:
- Vector search for finding similar papers
- Entity extraction for authors and topics
- Key phrase identification for indexing
- Citation and source tracking

### 🎬 Media Asset Management

Organize and search multimedia content including images, videos, and documents.

**Example**: Digital asset libraries, marketing content repositories, media archives

**Key Features Used**:
- Image vector search
- Multi-format support (file_type faceting)
- Tag-based organization
- File metadata tracking

---

## 🏗️ Architecture

### Deployment Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     Content Ingestion                           │
└────────────┬────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  📄 Document Processing                                         │
│  ├─ Text Extraction                                             │
│  ├─ Image Analysis                                              │
│  ├─ Metadata Extraction                                         │
│  └─ Chunking (if needed)                                        │
└────────────┬────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  🧠 AI Enrichment                                               │
│  ├─ Generate embeddings (OpenAI/Azure OpenAI)                   │
│  ├─ Extract entities (Azure AI)                                 │
│  ├─ Identify key phrases                                        │
│  ├─ Detect sentiment                                            │
│  └─ Classify language                                           │
└────────────┬────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  🔍 Azure AI Search Index                                       │
│  ├─ Store in multimodal-rag-index                               │
│  ├─ Build HNSW vector index                                     │
│  ├─ Create inverted text index                                  │
│  └─ Enable semantic ranking                                     │
└────────────┬────────────────────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────────┐
│  🎯 Search & Retrieval                                          │
│  ├─ Hybrid search (text + vector)                               │
│  ├─ Semantic ranking                                            │
│  ├─ Filtering & faceting                                        │
│  └─ Scoring profiles                                            │
└─────────────────────────────────────────────────────────────────┘
```

### Vector Search Configuration

The index uses two vector search algorithms optimized for different scenarios:

**HNSW (Hierarchical Navigable Small World)**
- **Use Case**: Production workloads requiring fast queries
- **Parameters**:
  - `m`: 4 (bi-directional links per element)
  - `efConstruction`: 400 (construction-time accuracy)
  - `efSearch`: 500 (query-time accuracy)
- **Trade-off**: ~95% accuracy with 10x faster queries

**Exhaustive KNN**
- **Use Case**: Scenarios requiring 100% accuracy
- **Parameters**: Cosine similarity metric
- **Trade-off**: Slower but guarantees finding the most similar vectors

---

## 📊 Scoring Profiles

Scoring profiles customize document ranking to match your business requirements.

### 🕐 Freshness Boost Profile

Prioritizes recently modified content while maintaining relevance.

**Configuration**:
```json
{
  "name": "freshness-boost",
  "text": {
    "weights": {
      "title": 3.0,
      "content": 2.0,
      "summary": 1.5
    }
  },
  "functions": [
    {
      "type": "freshness",
      "fieldName": "modified_date",
      "boost": 2.0,
      "interpolation": "linear",
      "freshness": {
        "boostingDuration": "P30D"
      }
    }
  ]
}
```

**Use Cases**:
- News and blog search
- Company announcements
- Policy and compliance documents
- Any content where recency matters

**Behavior**: Documents modified within the last 30 days receive up to 2x score boost, linearly decreasing over time.

### 🎯 Relevance Boost Profile

Emphasizes content quality and comprehensiveness.

**Configuration**:
```json
{
  "name": "relevance-boost",
  "text": {
    "weights": {
      "title": 5.0,
      "content": 3.0,
      "summary": 2.0,
      "key_phrases": 1.5,
      "tags": 1.5
    }
  },
  "functions": [
    {
      "type": "magnitude",
      "fieldName": "file_size",
      "boost": 0.5,
      "interpolation": "logarithmic",
      "magnitude": {
        "boostingRangeStart": 1000,
        "boostingRangeEnd": 10000000
      }
    }
  ]
}
```

**Use Cases**:
- Knowledge base articles
- Technical documentation
- Research papers
- Comprehensive guides

**Behavior**: Longer, more comprehensive documents (1KB-10MB) receive up to 1.5x boost with logarithmic scaling.

---

## ⚙️ Configuration Details

### Vector Search Algorithms Comparison

| Algorithm | Speed | Accuracy | Memory | Best For |
|-----------|-------|----------|--------|----------|
| **HNSW** | ⚡⚡⚡ Fast | ~95% | Medium | Production queries |
| **Exhaustive KNN** | 🐌 Slow | 100% | Low | Quality validation |

### Semantic Configuration

The semantic configuration prioritizes fields for AI-powered ranking:

```json
{
  "name": "semantic-config",
  "prioritizedFields": {
    "titleField": {
      "fieldName": "title"
    },
    "prioritizedContentFields": [
      { "fieldName": "content" },
      { "fieldName": "summary" }
    ],
    "prioritizedKeywordsFields": [
      { "fieldName": "key_phrases" },
      { "fieldName": "tags" },
      { "fieldName": "entities" }
    ]
  }
}
```

**How It Works**:
1. **Title Field**: Highest priority for semantic understanding
2. **Content Fields**: Body text analyzed for context and meaning
3. **Keywords Fields**: Terms used to refine semantic matches

---

## 💻 Example Usage

### Indexing Documents

```python
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import openai

# Initialize clients
search_client = SearchClient(
    endpoint="https://your-service.search.windows.net",
    index_name="multimodal-rag-index",
    credential=AzureKeyCredential("your-api-key")
)

# Generate embeddings (using OpenAI)
def get_embedding(text: str) -> list:
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

# Prepare document
document = {
    "id": "doc-001",
    "title": "Introduction to Azure AI Search",
    "content": "Azure AI Search is a cloud search service...",
    "summary": "Learn about Azure AI Search capabilities",
    "content_vector": get_embedding("Azure AI Search is a cloud search service..."),
    "tags": ["azure", "search", "ai"],
    "category": "Tutorial",
    "created_date": "2024-01-15T10:00:00Z",
    "modified_date": "2024-01-15T10:00:00Z",
    "indexed_date": "2024-01-15T10:30:00Z",
    "author": "Tech Writer",
    "source": "Documentation",
    "language": "en"
}

# Upload document
result = search_client.upload_documents(documents=[document])
print(f"Document indexed: {result[0].succeeded}")
```

### Hybrid Search Query

```python
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential

# Initialize search client
search_client = SearchClient(
    endpoint="https://your-service.search.windows.net",
    index_name="multimodal-rag-index",
    credential=AzureKeyCredential("your-api-key")
)

# User query
query_text = "How to implement vector search?"
query_vector = get_embedding(query_text)  # Generate embedding for query

# Create vectorized query
vector_query = VectorizedQuery(
    vector=query_vector,
    k_nearest_neighbors=5,
    fields="content_vector"
)

# Execute hybrid search
results = search_client.search(
    search_text=query_text,
    vector_queries=[vector_query],
    select=["id", "title", "content", "summary"],
    query_type="semantic",
    semantic_configuration_name="semantic-config",
    top=10
)

# Process results
for result in results:
    print(f"Title: {result['title']}")
    print(f"Score: {result['@search.score']}")
    print(f"Summary: {result['summary']}")
    print("---")
```

### Advanced Filtering

```python
# Search with filters
results = search_client.search(
    search_text="machine learning",
    filter="category eq 'Tutorial' and language eq 'en'",
    order_by=["modified_date desc"],
    facets=["category", "tags", "author"],
    scoring_profile="freshness-boost",
    top=20
)

for result in results:
    print(f"{result['title']} - {result['category']}")
```

---

## 🎓 Best Practices

### 📚 Chunking Strategy

**Optimal Chunk Size**: 500-1000 tokens per chunk
- Maintains semantic coherence
- Balances retrieval precision and context
- Prevents embedding quality degradation

**Implementation Tips**:
```python
def chunk_document(text: str, chunk_size: int = 800, overlap: int = 100):
    """
    Split document into overlapping chunks.
    
    Args:
        text: Document text
        chunk_size: Target tokens per chunk
        overlap: Overlap tokens between chunks
    """
    # Use parent_id to link chunks to source document
    # Use chunk_hash to prevent duplicate chunks
    pass
```

### 🧬 Vector Embeddings

**Recommended Models**:
- **Text**: `text-embedding-ada-002` (1536 dimensions)
- **Images**: `CLIP` or Azure Computer Vision (1536 dimensions)

**Best Practices**:
1. ✅ **Normalize embeddings** before indexing
2. ✅ **Batch embedding generation** for efficiency (up to 2048 texts)
3. ✅ **Cache embeddings** to avoid regeneration
4. ✅ **Use same model** for indexing and querying
5. ❌ **Don't mix** different embedding models in same field

### ⚡ Performance Optimization

**Indexing Performance**:
- Use batch operations (up to 1000 documents per batch)
- Enable parallel uploads with async clients
- Set appropriate `efConstruction` for index build time

**Query Performance**:
- Adjust `efSearch` based on accuracy requirements
- Use field selection to minimize payload size
- Implement caching for frequent queries
- Consider replica scaling for read-heavy workloads

### 💰 Cost Optimization

**Storage Costs**:
- Store only necessary vector dimensions
- Use appropriate field types (avoid Collection when single value suffices)
- Implement data lifecycle policies

**Compute Costs**:
- Right-size your search service tier
- Use standard tier for development/testing
- Scale replicas during peak hours only
- Optimize semantic ranking usage (metered per query)

**Embedding Costs**:
- Batch embedding generation
- Cache frequently used embeddings
- Consider local embedding models for high-volume scenarios

---

## 🔧 Troubleshooting

<details>
<summary><b>❌ Error: "Index creation failed - Invalid vector dimensions"</b></summary>

**Problem**: Vector field dimensions don't match embedding model output.

**Solution**:
```json
// Ensure dimensions match your embedding model
{
  "name": "content_vector",
  "dimensions": 1536  // Must match OpenAI ada-002
}
```

Check your embedding model's output dimensions and update the schema accordingly.

</details>

<details>
<summary><b>❌ Error: "Query timeout on vector search"</b></summary>

**Problem**: Vector search taking too long, possibly using exhaustive KNN.

**Solution**:
- Switch to HNSW algorithm for faster queries
- Increase `efSearch` value if accuracy is insufficient
- Consider scaling up your search service tier
- Reduce `k_nearest_neighbors` in queries

</details>

<details>
<summary><b>❌ Error: "Semantic ranking not available"</b></summary>

**Problem**: Semantic ranking requires specific service tiers.

**Solution**:
- Semantic ranking is available on Basic tier and above
- Verify your search service tier in Azure Portal
- Check semantic configuration is properly defined in index schema

</details>

<details>
<summary><b>⚠️ Warning: Poor search relevance</b></summary>

**Problem**: Search results not matching user expectations.

**Diagnosis Steps**:
1. Check if semantic ranking is enabled
2. Verify scoring profile configuration
3. Test with different query types (simple, full, semantic)
4. Analyze search scores to identify ranking issues

**Solutions**:
- Adjust field weights in scoring profiles
- Enable semantic ranking for better contextual understanding
- Fine-tune vector search k parameter
- Consider hybrid search combining text and vector queries

</details>

<details>
<summary><b>⚠️ Warning: High indexing latency</b></summary>

**Problem**: Documents taking too long to index.

**Solutions**:
- Reduce batch size if hitting service limits
- Disable semantic configuration during bulk indexing
- Use asynchronous client for parallel uploads
- Consider temporary scale-up during bulk operations

</details>

---

## 🤝 Contributing

We welcome contributions to improve this schema and documentation! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-improvement`)
3. **Make your changes**
4. **Test thoroughly** with real data
5. **Commit your changes** (`git commit -m 'Add amazing improvement'`)
6. **Push to the branch** (`git push origin feature/amazing-improvement`)
7. **Open a Pull Request**

### Contribution Guidelines

- ✅ Follow existing schema structure and naming conventions
- ✅ Add comments explaining complex configurations
- ✅ Update documentation for any schema changes
- ✅ Test changes with sample data
- ✅ Include examples for new features

### Areas for Contribution

- 🔧 Additional scoring profile examples
- 📚 More use case documentation
- 🐛 Bug fixes and optimizations
- 🌍 Multi-language analyzer configurations
- 💡 Feature suggestions and enhancements

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Azure AI Search Schema Index Example

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

This project builds upon excellent technologies and services:

- **[Microsoft Azure](https://azure.microsoft.com/)** - Cloud infrastructure and AI services
- **[Azure Cognitive Services](https://azure.microsoft.com/en-us/products/cognitive-services/)** - AI enrichment capabilities
- **[OpenAI](https://openai.com/)** - Embedding models and language understanding

### Support & Resources

- 📖 [Azure AI Search Documentation](https://learn.microsoft.com/en-us/azure/search/)
- 💬 [Azure AI Search Community](https://techcommunity.microsoft.com/t5/azure-ai-search/bd-p/AzureAISearch)
- 🎓 [Vector Search Tutorials](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)
- 🔧 [Python SDK Documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/search-documents-readme)

### Questions or Issues?

- 🐛 **Found a bug?** [Open an issue](https://github.com/MosheHM/azure-ai-search-schema-index-example/issues)
- 💡 **Have a suggestion?** [Start a discussion](https://github.com/MosheHM/azure-ai-search-schema-index-example/discussions)
- 📧 **Need help?** Check the [troubleshooting section](#-troubleshooting)

---

<div align="center">

**Built with ❤️ for the Azure AI Search community**

[![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![Microsoft](https://img.shields.io/badge/Microsoft-666666?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.microsoft.com/)

⭐ **Star this repo** if you find it helpful!

</div>
