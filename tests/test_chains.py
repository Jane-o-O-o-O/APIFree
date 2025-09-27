import unittest
from src.chains.chat_chain import ChatChain
from src.chains.workflow_chain import WorkflowChain

class TestChatChain(unittest.TestCase):
    def setUp(self):
        self.chat_chain = ChatChain()

    def test_run(self):
        response = self.chat_chain.run("Hello, how are you?")
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

class TestWorkflowChain(unittest.TestCase):
    def setUp(self):
        self.workflow_chain = WorkflowChain()

    def test_execute(self):
        result = self.workflow_chain.execute("Sample input for workflow")
        self.assertIsInstance(result, dict)
        self.assertIn("output", result)

if __name__ == "__main__":
    unittest.main()