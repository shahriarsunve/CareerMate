import re

from agent_runner import agent, llm

questions = [
    "I want to become a data scientist. My skills are Excel, Python.",
    "Find me jobs. My skills are SQL, Excel. Location: Remote.",
    "How do I learn SQL and Pandas?"
]

#This block is for the full response. 

# def extract_agent_format(text):
#     text = re.sub(r"```", "", text)
#     matches = re.findall(
#         r"(Thought:.*?)(Action: ?\{.*?\}|Final Answer:.*)", text, re.DOTALL
#     )
#     if matches:
#         return "".join(matches[-1]).strip()
#     return text.strip()

# for q in questions:
#     strict_q = (
#         "Remember: Only respond in the specified format. "
#         "Do not answer unless you use the format.\n"
#         + q
#     )
#     cleaned_output = extract_agent_format(llm.invoke(strict_q))
#     response = agent.invoke(cleaned_output)
#     print(f"\n👤 User: {q}")
#     print("Agent answer:\n", response['output'])


#This block is for the final response only 

def extract_final_answer(text):
    # Remove code block markers
    text = re.sub(r"```", "", text)
    # Find the last Final Answer block
    matches = re.findall(r"Final Answer: ?(.*)", text)
    if matches:
        return matches[-1].strip()
    return text.strip()



for q in questions:
    strict_q = (
        "Remember: Only respond in the specified format. "
        "Do not answer unless you use the format.\n"
        + q
    )
    raw_output = llm.invoke(strict_q)
    final_answer = extract_final_answer(raw_output)
    print(f"\n => User: {q}")
    print("Agent answer:\n", final_answer)