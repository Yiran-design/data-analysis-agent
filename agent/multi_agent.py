import dashscope
import os

dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

def call_llm(prompt):
    response = dashscope.Generation.call(
        model="qwen-turbo",
        prompt=prompt
    )
    return response.output.text

def run_agent(df, question, max_steps=3):
    context = ""

    for step in range(max_steps):
        prompt = f"""
You are a data analysis agent.

Question: {question}

Context: {context}

Decide next action:
- describe_data
- summarize
- find_top_products

Respond with:
Thought: ...
Action: ...
"""

        output = call_llm(prompt)
        print(f"\n[STEP {step+1}]\n{output}")

        if "describe_data" in output:
            obs = str(df.head())
        elif "summarize" in output:
            obs = str(df.describe())
        elif "find_top_products" in output:
            if "product" in df.columns and "revenue" in df.columns:
                obs = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head().to_string()
            else:
                obs = "Missing columns"
        else:
            obs = "No valid action"

        context += f"\nObservation: {obs}"

    return context
