# 🤖 LLM-based Multi-step Data Analysis Agent

A lightweight **Agentic AI system** that automates data analysis workflows using multi-step reasoning, tool execution, and iterative decision-making.

---

## ✨ Highlights

- ✅ Built a **multi-step agent with reasoning loop (Thought → Action → Observation)**
- ✅ Implemented **dynamic task execution** instead of one-shot LLM responses  
- ✅ Designed an **end-to-end pipeline** from raw CSV input to structured report  
- ✅ Integrated **LLM + data processing (Pandas) + Streamlit UI**  
- ✅ Supports **domestic LLM (Qwen / DashScope)** for stable execution without VPN  
- ✅ Automatically generates **data analysis reports from raw data in seconds**

---

## 🚀 Overview

This project demonstrates the transition from:

> **LLM as a responder → AI as a task executor (Agent)**

Instead of generating a single response, the system is able to:

- Understand user queries  
- Plan analysis steps dynamically  
- Select actions  
- Execute data analysis tools  
- Iterate based on intermediate results  
- Produce structured insights  

---

## 🧠 Agent Architecture

The system follows a **multi-step reasoning loop**:

```
Thought → Action → Observation → Thought → ...
```

Pipeline:

```
User Input (CSV + question)
        ↓
LLM Planner (reasoning)
        ↓
Multi-step Agent Loop
        ↓
Tool Execution (Pandas)
        ↓
Context Update
        ↓
Final Report Generation
```

---

## 🖼️ Demo

👉 assets/demo.pdf

The demo shows:
- Uploading dataset  
- Agent reasoning process  
- Final generated report  

---

## 🔧 Tech Stack

- Python  
- DashScope (Qwen LLM)  
- Pandas  
- Streamlit  

---

## 🧪 Example

**Input**

```
Which products generate the highest revenue?
```

**Process**

- Identify relevant columns  
- Perform aggregation  
- Rank results  
- Generate insights  

---

## ▶️ How to Run

### 1. Clone repo
```bash
git clone https://github.com/your-username/data-analysis-agent.git
cd data-analysis-agent
```

---

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 3. Set API key

Create `.env` file:

```
DASHSCOPE_API_KEY=your_api_key_here
```

---

### 4. Run UI
```bash
streamlit run streamlit_app.py
```

Open:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
agent/
    multi_agent.py   # reasoning loop
    reporter.py      # report generation

tools/
    data_loader.py   # load data
    analysis.py      # data processing

app.py               # CLI version
streamlit_app.py     # UI version
```

---

## 🎯 Key Idea

> AI should not only generate answers, but **execute tasks**

This project focuses on designing **agent systems that complete workflows**.

---

## 📌 Future Work

- Function calling / tool abstraction  
- Data visualization integration  
- Memory for multi-step workflows  
- Deployment as API service  

---

## 👤 Author

Yiran Zhang  
MSc Industrial Data Analytics  
Interested in AI / Agentic Systems / Applied AI  

---

## 💬 One-line Summary

> Built a multi-step LLM agent that converts raw data and user queries into automated, actionable insights.
