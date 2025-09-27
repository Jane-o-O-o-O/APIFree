from langchain.chains import LLMChain
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.llm_config import get_llm_config
from prompts.templates import ThreeLayerPromptTemplates

class RequirementAnalysisChain:
    """需求分析链 - 第一层"""
    
    def __init__(self, llm_config):
        self.llm = llm_config.get_analyzer()
        self.prompt = ThreeLayerPromptTemplates.get_requirement_analysis_prompt()
        self.chain = self.prompt | self.llm
    
    def analyze(self, user_requirement: str):
        """分析用户需求"""
        result = self.chain.invoke({"user_requirement": user_requirement})
        return result

class ArchitectureDesignChain:
    """架构设计链 - 第二层"""
    
    def __init__(self, llm_config):
        self.llm = llm_config.get_designer()
        self.prompt = ThreeLayerPromptTemplates.get_architecture_design_prompt()
        self.chain = self.prompt | self.llm
    
    def design(self, requirement_analysis: str):
        """基于需求分析设计架构"""
        result = self.chain.invoke({"requirement_analysis": requirement_analysis})
        return result

class CodeImplementationChain:
    """代码实现链 - 第三层"""
    
    def __init__(self, llm_config):
        self.llm = llm_config.get_implementer()
        self.prompt = ThreeLayerPromptTemplates.get_code_implementation_prompt()
        self.chain = self.prompt | self.llm
    
    def implement(self, architecture_design: str):
        """基于架构设计实现代码"""
        result = self.chain.invoke({"architecture_design": architecture_design})
        return result

class ThreeLayerWorkflowChain:
    """三层工作流主链"""
    
    def __init__(self, api_key: str, base_url: str = "https://api.siliconflow.cn/v1"):
        # 初始化LLM配置
        self.llm_config = get_llm_config(api_key, base_url)
        
        # 初始化三层链
        self.requirement_chain = RequirementAnalysisChain(self.llm_config)
        self.architecture_chain = ArchitectureDesignChain(self.llm_config)
        self.implementation_chain = CodeImplementationChain(self.llm_config)
    
    def execute_full_workflow(self, user_requirement: str, verbose: bool = True):
        """执行完整的三层工作流"""
        results = {}
        
        try:
            # 第一层：需求分析
            if verbose:
                print("🔍 第一层：正在分析用户需求...")
            requirement_analysis = self.requirement_chain.analyze(user_requirement)
            results["requirement_analysis"] = requirement_analysis
            if verbose:
                print("✅ 需求分析完成")
                print("-" * 50)
            
            # 第二层：架构设计
            if verbose:
                print("🏗️ 第二层：正在设计代码架构...")
            architecture_design = self.architecture_chain.design(requirement_analysis)
            results["architecture_design"] = architecture_design
            if verbose:
                print("✅ 架构设计完成")
                print("-" * 50)
            
            # 第三层：代码实现
            if verbose:
                print("💻 第三层：正在实现完整代码...")
            code_implementation = self.implementation_chain.implement(architecture_design)
            results["code_implementation"] = code_implementation
            if verbose:
                print("✅ 代码实现完成")
                print("-" * 50)
            
            return results
            
        except Exception as e:
            print(f"❌ 工作流执行出错: {str(e)}")
            return results
    
    def execute_single_layer(self, layer: str, input_data: str):
        """执行单一层级（用于调试）"""
        if layer == "requirement":
            return self.requirement_chain.analyze(input_data)
        elif layer == "architecture":
            return self.architecture_chain.design(input_data)
        elif layer == "implementation":
            return self.implementation_chain.implement(input_data)
        else:
            raise ValueError("layer must be one of: 'requirement', 'architecture', 'implementation'")

# 保持向后兼容的旧版本WorkflowChain
class WorkflowChain:
    """旧版本工作流链（保持向后兼容）"""
    def __init__(self, chains):
        self.chains = chains

    def execute(self, input_data):
        results = {}
        for chain in self.chains:
            result = chain.run(input_data)
            results[chain.__class__.__name__] = result
            input_data = result  # Pass the result to the next chain
        return results