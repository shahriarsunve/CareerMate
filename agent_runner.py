from langchain.agents import initialize_agent, AgentType
from langchain_ollama import OllamaLLM
from tools import get_missing_skills, find_jobs, recommend_courses

tools = [get_missing_skills, find_jobs, recommend_courses]

llm = OllamaLLM(model="llama3", system_prompt=(
    "You are a helpful AI agent. "
    "You MUST respond in exactly one of the following formats and NOTHING ELSE:\n"
    "If you need to use a tool:\n"
    "Thought: <your reasoning>\n"
    "Action: {\"action\": \"<tool_name>\", \"action_input\": \"<input>\"}\n"
    "If you are done:\n"
    "Thought: <your reasoning>\n"
    "Final Answer: <your answer>\n"
    "Do NOT include greetings, explanations, lists, or any other text. "
    "If you do not follow this format, your response will be rejected."
))

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)
