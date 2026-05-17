import dashscope
import os

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

def generate_report(question, analysis):
    prompt = f"""
Question: {question}

Analysis:
{analysis}

Generate a clear report.
"""

    return dashscope.Generation.call(
        model="qwen-turbo",
        prompt=prompt
    ).output.text