"""
三层LangChain工作流演示程序
第一层：需求分析
第二层：架构设计  
第三层：代码实现
"""

import sys
import os
import datetime
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from chains.workflow_chain import ThreeLayerWorkflowChain
import json

def save_results_to_files(results, base_filename="workflow_result"):
    """保存结果到三个不同的文件（Markdown格式）"""
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 保存第一层 - 需求分析
    if "requirement_analysis" in results:
        filepath1 = os.path.join(output_dir, f"{base_filename}_1_需求分析.md")
        with open(filepath1, 'w', encoding='utf-8') as f:
            f.write("# 🔍 第一层 - 需求分析结果\n\n")
            f.write(f"生成时间: {timestamp}\n\n")
            f.write("---\n\n")
            f.write(results["requirement_analysis"])
            f.write("\n")
        print(f"📁 需求分析结果已保存到 {filepath1}")
    
    # 保存第二层 - 架构设计
    if "architecture_design" in results:
        filepath2 = os.path.join(output_dir, f"{base_filename}_2_架构设计.md")
        with open(filepath2, 'w', encoding='utf-8') as f:
            f.write("# 🏗️ 第二层 - 架构设计结果\n\n")
            f.write(f"生成时间: {timestamp}\n\n")
            f.write("---\n\n")
            f.write(results["architecture_design"])
            f.write("\n")
        print(f"📁 架构设计结果已保存到 {filepath2}")
    
    # 保存第三层 - 代码实现
    if "code_implementation" in results:
        filepath3 = os.path.join(output_dir, f"{base_filename}_3_代码实现.md")
        with open(filepath3, 'w', encoding='utf-8') as f:
            f.write("# 💻 第三层 - 代码实现结果\n\n")
            f.write(f"生成时间: {timestamp}\n\n")
            f.write("---\n\n")
            f.write(results["code_implementation"])
            f.write("\n")
        print(f"📁 代码实现结果已保存到 {filepath3}")
    
    # 生成汇总文件
    summary_filepath = os.path.join(output_dir, f"{base_filename}_汇总.md")
    with open(summary_filepath, 'w', encoding='utf-8') as f:
        f.write("# 🚀 三层LangChain工作流汇总\n\n")
        f.write(f"生成时间: {timestamp}\n\n")
        f.write("## 📋 生成文件列表\n\n")
        if "requirement_analysis" in results:
            f.write(f"- � [需求分析结果]({base_filename}_1_需求分析.md)\n")
        if "architecture_design" in results:
            f.write(f"- 🏗️ [架构设计结果]({base_filename}_2_架构设计.md)\n")
        if "code_implementation" in results:
            f.write(f"- 💻 [代码实现结果]({base_filename}_3_代码实现.md)\n")
        f.write("\n## ✅ 工作流执行状态\n\n")
        f.write("- 第一层需求分析: ✅ 完成\n")
        f.write("- 第二层架构设计: ✅ 完成\n")
        f.write("- 第三层代码实现: ✅ 完成\n")
    
    print(f"� 工作流汇总已保存到 {summary_filepath}")

def print_layer_result(layer_name, result, max_length=500):
    """格式化打印层级结果（不显示具体内容）"""
    print(f"✅ {layer_name} - 已完成并保存到文件")

def demo_workflow():
    """演示完整的三层工作流"""
    # 你的硅基流动API密钥
    API_KEY = "sk-qdsixyljzeyoessydhkwnjqnijnrylztfhccdnyoweqshyku"
    
    # 初始化三层工作流
    workflow = ThreeLayerWorkflowChain(api_key=API_KEY)
    
    # 示例需求
    user_requirements = [
        "我想要一个简单的待办事项管理器，可以添加、删除、标记完成任务",
        "创建一个计算器程序，支持基本的四则运算",
        "开发一个简单的文件整理工具，可以按照文件类型自动分类文件"
    ]
    
    print("🚀 三层LangChain工作流演示")
    print("="*60)
    
    for i, requirement in enumerate(user_requirements, 1):
        print(f"\n🔥 示例 {i}: {requirement}")
        print("🎬 开始执行三层工作流...")
        
        try:
            # 执行完整工作流
            results = workflow.execute_full_workflow(requirement, verbose=True)
            
            # 简化显示各层结果状态
            if "requirement_analysis" in results:
                print_layer_result("第一层 - 需求分析", results["requirement_analysis"])
            
            if "architecture_design" in results:
                print_layer_result("第二层 - 架构设计", results["architecture_design"])
            
            if "code_implementation" in results:
                print_layer_result("第三层 - 代码实现", results["code_implementation"])
            
            # 保存结果到文件
            save_results_to_files(results, f"example_{i}")
            
            # 询问是否继续下一个例子
            if i < len(user_requirements):
                continue_choice = input(f"\n✨ 是否继续执行下一个例子？(y/n): ").lower().strip()
                if continue_choice != 'y':
                    break
                    
        except Exception as e:
            print(f"❌ 执行第{i}个例子时出错: {str(e)}")
            continue
    
    print("\n🎉 演示完成！")

def interactive_mode():
    """交互式模式"""
    print("🤖 欢迎使用三层LangChain工作流交互模式！")
    print("💡 请输入你的需求，我将通过三层模型为你生成完整的代码解决方案")
    print("📝 输入 'quit' 退出程序")
    
    # 你的硅基流动API密钥
    API_KEY = "sk-qdsixyljzeyoessydhkwnjqnijnrylztfhccdnyoweqshyku"
    
    try:
        workflow = ThreeLayerWorkflowChain(api_key=API_KEY)
        
        while True:
            print("\n" + "="*60)
            user_input = input("🎯 请输入你的需求: ").strip()
            
            if user_input.lower() == 'quit':
                print("👋 再见！")
                break
            
            if not user_input:
                print("⚠️ 请输入有效的需求")
                continue
            
            print(f"\n🚀 开始处理需求: {user_input}")
            
            try:
                results = workflow.execute_full_workflow(user_input, verbose=True)
                
                # 保存结果
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                save_results_to_files(results, f"interactive_{timestamp}")
                
                print(f"\n🎉 需求处理完成！结果已保存到文件。")
                
            except Exception as e:
                print(f"❌ 处理需求时出错: {str(e)}")
                
    except Exception as e:
        print(f"❌ 初始化工作流时出错: {str(e)}")

def main():
    """主函数"""
    print("🌟 三层LangChain工作流系统")
    print("="*60)
    print("选择运行模式:")
    print("1. 演示模式 - 运行预设的几个例子")
    print("2. 交互模式 - 输入自定义需求")
    print("3. 退出")
    
    while True:
        choice = input("\n请选择 (1/2/3): ").strip()
        
        if choice == '1':
            demo_workflow()
            break
        elif choice == '2':
            interactive_mode()
            break
        elif choice == '3':
            print("👋 再见！")
            break
        else:
            print("⚠️ 请输入有效的选择 (1/2/3)")

if __name__ == "__main__":
    main()