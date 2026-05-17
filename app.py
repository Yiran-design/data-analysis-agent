from dotenv import load_dotenv
load_dotenv()

from agent.multi_agent import run_agent
from agent.reporter import generate_report
from tools.data_loader import load_data


def main():
    file_path = "data/sample.csv"
    question = input("Enter your question: ")

    df = load_data(file_path)

    agent_output = run_agent(df, question)

    report = generate_report(question, agent_output)
    print("
[FINAL REPORT]
", report)


if __name__ == "__main__":
    main()
