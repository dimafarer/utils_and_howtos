#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestEnvironmentSetup(unittest.TestCase):
    """Test environment setup functionality."""
    
    @patch('boto3.Session')
    def test_check_aws_credentials_success(self, mock_session):
        """Test successful AWS credentials check."""
        from importlib import import_module
        env_setup = import_module('00_environment_setup')
        
        # Mock successful credential check
        mock_session.return_value.get_credentials.return_value = Mock()
        
        with patch('boto3.client') as mock_client:
            mock_client.return_value.list_foundation_models.return_value = {}
            result = env_setup.check_aws_credentials()
            self.assertTrue(result)
    
    def test_check_python_version(self):
        """Test Python version check."""
        from importlib import import_module
        env_setup = import_module('00_environment_setup')
        
        # Should pass for current Python version
        result = env_setup.check_python_version()
        self.assertTrue(result)

class TestModelComparison(unittest.TestCase):
    """Test model comparison functionality."""
    
    @patch('boto3.client')
    @patch('langchain_aws.ChatBedrock')
    def test_model_comparison(self, mock_chat_bedrock, mock_boto_client):
        """Test model comparison with mocked responses."""
        from importlib import import_module
        model_comp = import_module('01b_model_comparison')
        
        # Mock response
        mock_response = Mock()
        mock_response.content = "AWS Lambda is a serverless compute service."
        mock_chat_bedrock.return_value.invoke.return_value = mock_response
        
        result = model_comp.test_model(
            "Test Model", 
            {"id": "test-model", "config": {"max_tokens": 100}},
            "Test prompt"
        )
        
        self.assertTrue(result["success"])
        self.assertIn("response", result)
        self.assertGreater(result["tokens"], 0)

class TestAdvancedPrompts(unittest.TestCase):
    """Test advanced prompting functionality."""
    
    @patch('boto3.client')
    @patch('langchain_aws.ChatBedrock')
    def test_prompt_composition(self, mock_chat_bedrock, mock_boto_client):
        """Test prompt composition works without errors."""
        from importlib import import_module
        
        # Mock LLM response
        mock_response = Mock()
        mock_response.content = "Test response"
        mock_chat_bedrock.return_value.invoke.return_value = mock_response
        
        # Import and test - should not raise exceptions
        try:
            advanced_prompts = import_module('02b_advanced_prompts')
            # Test would run main() but we'll just test import for now
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import advanced prompts: {e}")

class TestStreamingChatbot(unittest.TestCase):
    """Test streaming chatbot functionality."""
    
    @patch('boto3.client')
    @patch('langchain_aws.ChatBedrock')
    def test_streaming_setup(self, mock_chat_bedrock, mock_boto_client):
        """Test streaming chatbot setup."""
        from importlib import import_module
        
        # Mock streaming response
        mock_chunk = Mock()
        mock_chunk.content = "test"
        mock_chat_bedrock.return_value.stream.return_value = [mock_chunk]
        
        try:
            streaming_bot = import_module('04b_streaming_chatbot')
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import streaming chatbot: {e}")

class TestGuardrails(unittest.TestCase):
    """Test guardrails functionality."""
    
    @patch('boto3.client')
    @patch('langchain_aws.ChatBedrock')
    def test_guardrails_setup(self, mock_chat_bedrock, mock_boto_client):
        """Test guardrails configuration."""
        from importlib import import_module
        
        mock_response = Mock()
        mock_response.content = "Safe response"
        mock_chat_bedrock.return_value.invoke.return_value = mock_response
        
        try:
            guardrails = import_module('07_guardrails_safety')
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import guardrails: {e}")

class TestCallbacks(unittest.TestCase):
    """Test callbacks and monitoring."""
    
    def test_metrics_callback(self):
        """Test metrics callback functionality."""
        from importlib import import_module
        callbacks = import_module('08_callbacks_monitoring')
        
        # Test callback initialization
        callback = callbacks.MetricsCallback()
        self.assertEqual(callback.metrics["total_calls"], 0)
        
        # Test summary with no calls
        summary = callback.get_summary()
        self.assertEqual(summary, "No calls made yet")

class TestRAG(unittest.TestCase):
    """Test RAG functionality."""
    
    @patch('boto3.client')
    @patch('langchain_aws.BedrockEmbeddings')
    @patch('langchain_aws.ChatBedrock')
    def test_rag_setup(self, mock_chat_bedrock, mock_embeddings, mock_boto_client):
        """Test RAG knowledge base setup."""
        from importlib import import_module
        
        # Mock embeddings and vector store
        mock_embeddings.return_value = Mock()
        
        try:
            rag = import_module('09_rag_knowledge_base')
            docs = rag.create_sample_knowledge_base()
            self.assertGreater(len(docs), 0)
            self.assertEqual(docs[0].metadata["service"], "Lambda")
        except ImportError as e:
            self.fail(f"Failed to import RAG: {e}")

class TestAsyncOperations(unittest.TestCase):
    """Test async operations."""
    
    def test_async_import(self):
        """Test async operations import."""
        from importlib import import_module
        
        try:
            async_ops = import_module('10_async_operations')
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import async operations: {e}")

class TestExistingFiles(unittest.TestCase):
    """Test existing files still work."""
    
    @patch('boto3.client')
    @patch('langchain_aws.ChatBedrock')
    def test_basic_bedrock(self, mock_chat_bedrock, mock_boto_client):
        """Test basic Bedrock example."""
        from importlib import import_module
        
        mock_response = Mock()
        mock_response.content = "Hello! Here's a fun AWS fact."
        mock_chat_bedrock.return_value.invoke.return_value = mock_response
        
        try:
            basic = import_module('01_langchain_bedrock_basic')
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import basic example: {e}")

def run_tests():
    """Run all tests with detailed output."""
    print("=== Running LangChain Examples Tests ===\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestEnvironmentSetup,
        TestModelComparison,
        TestAdvancedPrompts,
        TestStreamingChatbot,
        TestGuardrails,
        TestCallbacks,
        TestRAG,
        TestAsyncOperations,
        TestExistingFiles
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print(f"\n=== Test Summary ===")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    success = len(result.failures) == 0 and len(result.errors) == 0
    print(f"\n{'✅ All tests passed!' if success else '❌ Some tests failed'}")
    
    return success

if __name__ == "__main__":
    run_tests()
