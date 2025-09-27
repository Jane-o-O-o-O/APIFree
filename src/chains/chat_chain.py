class ChatChain:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def run(self, user_input):
        prompt = self.prompt_template.format(user_input=user_input)
        response = self.llm.generate(prompt)
        return response