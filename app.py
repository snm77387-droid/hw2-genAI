import os
import warnings
from google import genai  # 2026年标准导入方式

# 1. 忽略警告，让输出更清爽
warnings.filterwarnings("ignore")

# 2. 初始化 Client (你在美国，确保 Key 没有前后空格)
# 提示：上传 GitHub 前请记得删掉这里的 Key 字符串
API_KEY = os.getenv("GEMINI_API_KEY") or ""
client = genai.Client(api_key=API_KEY.strip())

def run_genai_workflow(customer_review, system_instruction):
    """
    执行 AI 工作流
    """
    # 使用你之前列表里确认可用的 2.5 版本
    model_id = "gemini-2.5-flash" 
    
    # 新版 SDK 调用语法
    response = client.models.generate_content(
        model=model_id,
        config={
            "system_instruction": system_instruction,
            "temperature": 0.7,
        },
        contents=customer_review
    )
    return response.text

def main():
    print("--- 🚀 E-commerce Review Assistant (2026 Edition) ---")
    
    # 定义提示词版本 (Step 5 迭代时在这里改)
    # V1: 初始版本
    system_prompt_v1 = """
    You are a professional customer service representative for an e-commerce company.
    Respond to the following customer review in a polite and helpful manner.
    """
    
    eval_set = [
        "I've been waiting for my package for over two weeks! The tracking hasn't updated in 5 days. This is ridiculous, I needed this for a birthday gift tomorrow.",
        "The blender arrived today but the glass jar is cracked. I was really looking forward to using it. How can you send out damaged goods?",
        "1 star. Never again.",
        "I used your new face cream and my skin broke out in a red itchy rash immediately. It's burning! I'm going to sue your company for selling toxic products!",
        "If you don't give me a full refund AND a $50 gift card right now, I will post this story on TikTok and Twitter to make sure everyone knows how terrible you are."
    ]
    
    # 初始化输出文件
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("=== BATCH EVALUATION RESULTS (V1) ===\n\n")

    # 循环跑所有案例
    for i, test_input in enumerate(eval_set):
        print(f"[Case {i+1}/5] Processing...")
        
        try:
            # 调用工作流
            output = run_genai_workflow(test_input, system_prompt_v1)
            
            # 保存结果到文件
            with open("output.txt", "a", encoding="utf-8") as f:
                f.write(f"--- CASE {i+1} ---\n")
                f.write(f"INPUT: {test_input}\n")
                f.write(f"OUTPUT:\n{output}\n")
                f.write("-" * 30 + "\n\n")
            
            print(f"   ✅ Done.")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")

    print("\n--- All finished! Results saved to output.txt ---")

if __name__ == "__main__":
    main()