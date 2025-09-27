from src.models.llm_config import LLMConfig
import unittest

class TestLLMConfig(unittest.TestCase):

    def setUp(self):
        self.config = LLMConfig(api_key="test_api_key", model_name="test_model")

    def test_api_key(self):
        self.assertEqual(self.config.api_key, "test_api_key")

    def test_model_name(self):
        self.assertEqual(self.config.model_name, "test_model")

if __name__ == '__main__':
    unittest.main()