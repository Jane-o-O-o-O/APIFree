from langchain_openai import OpenAI
import os

class ThreeLayerLLMConfig:
    """三层模型配置类"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.siliconflow.cn/v1"):
        self.api_key = api_key
        self.base_url = base_url
        os.environ["OPENAI_API_KEY"] = api_key
        
        # 第一层：需求分析模型 - 添加防重复参数
        self.requirement_analyzer = OpenAI(
            temperature=0.05,  # 极低温度减少随机性
            base_url=base_url,
            model="Qwen/Qwen2.5-7B-Instruct",
            max_tokens=999999,    # 减少token数量
            frequency_penalty=0.8,  # 高频率惩罚防止重复
            presence_penalty=0.5,   # 存在惩罚
            stop=["\n\n", "重复", "再次", "以上", "总结"]  # 停止词
        )
        
        # 第二层：架构设计模型 - 专注于设计代码架构
        self.architecture_designer = OpenAI(
            temperature=0.1,  # 低温度确保结构化输出
            base_url=base_url,
            model="Qwen/Qwen2.5-7B-Instruct",
            max_tokens=999999,
            frequency_penalty=0.6,
            presence_penalty=0.4,
            stop=["\n\n\n", "重复", "再次"]
        )
        
        # 第三层：代码实现模型 - 专注于代码生成
        self.code_implementer = OpenAI(
            temperature=0.1,  # 低温度确保代码准确性
            base_url=base_url,
            model="Qwen/Qwen2.5-7B-Instruct",
            max_tokens=999999,
            frequency_penalty=0.4,
            presence_penalty=0.3,
            stop=["重复", "再次"]
        )
    
    def get_analyzer(self):
        """获取需求分析模型"""
        return self.requirement_analyzer
    
    def get_designer(self):
        """获取架构设计模型"""
        return self.architecture_designer
    
    def get_implementer(self):
        """获取代码实现模型"""
        return self.code_implementer

# 单例模式，确保全局使用同一配置
_llm_config = None

def get_llm_config(api_key: str = None, base_url: str = "https://api.siliconflow.cn/v1"):
    """获取LLM配置实例"""
    global _llm_config
    if _llm_config is None:
        if api_key is None:
            raise ValueError("API key is required for first initialization")
        _llm_config = ThreeLayerLLMConfig(api_key, base_url)
    return _llm_config