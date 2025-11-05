"""
Azure AI Search Index Deployment Script

This script deploys a multimodal RAG-enhanced index to Azure AI Search.
It supports creating, updating, and managing search indexes with vector search capabilities.
"""

import json
import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex
from typing import Optional


def load_index_schema(schema_path: str = "corrected_index_schema.json") -> dict:
    """
    Load the index schema from a JSON file.
    
    Args:
        schema_path: Path to the schema JSON file
        
    Returns:
        Dictionary containing the index schema
    """
    with open(schema_path, 'r') as f:
        return json.load(f)


def create_search_index(
    service_endpoint: str,
    api_key: str,
    index_name: Optional[str] = None,
    schema_path: str = "corrected_index_schema.json"
) -> SearchIndex:
    """
    Create or update an Azure AI Search index.
    
    Args:
        service_endpoint: Azure AI Search service endpoint URL
        api_key: Azure AI Search admin API key
        index_name: Name for the index (overrides schema name if provided)
        schema_path: Path to the index schema JSON file
        
    Returns:
        The created or updated SearchIndex object
    """
    # Create the search index client
    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
    
    # Load the schema
    schema = load_index_schema(schema_path)
    
    # Override index name if provided
    if index_name:
        schema['name'] = index_name
    
    # Create the index from the schema
    index = SearchIndex.deserialize(schema)
    
    # Create or update the index
    result = index_client.create_or_update_index(index)
    print(f"Index '{result.name}' created/updated successfully!")
    
    return result


def delete_search_index(service_endpoint: str, api_key: str, index_name: str) -> None:
    """
    Delete an Azure AI Search index.
    
    Args:
        service_endpoint: Azure AI Search service endpoint URL
        api_key: Azure AI Search admin API key
        index_name: Name of the index to delete
    """
    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
    
    index_client.delete_index(index_name)
    print(f"Index '{index_name}' deleted successfully!")


def list_indexes(service_endpoint: str, api_key: str) -> list:
    """
    List all indexes in the Azure AI Search service.
    
    Args:
        service_endpoint: Azure AI Search service endpoint URL
        api_key: Azure AI Search admin API key
        
    Returns:
        List of index names
    """
    credential = AzureKeyCredential(api_key)
    index_client = SearchIndexClient(endpoint=service_endpoint, credential=credential)
    
    indexes = index_client.list_indexes()
    index_names = [index.name for index in indexes]
    
    print(f"Found {len(index_names)} indexes:")
    for name in index_names:
        print(f"  - {name}")
    
    return index_names


def main():
    """
    Main function to demonstrate index deployment.
    """
    # Load configuration from environment variables
    service_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    
    if not service_endpoint or not api_key:
        print("Error: Please set AZURE_SEARCH_ENDPOINT and AZURE_SEARCH_API_KEY environment variables")
        return
    
    # Create the index
    try:
        create_search_index(
            service_endpoint=service_endpoint,
            api_key=api_key,
            schema_path="corrected_index_schema.json"
        )
    except Exception as e:
        print(f"Error creating index: {e}")


if __name__ == "__main__":
    main()
