from strands import Agent
"""
using the strands default. This is using my default credentials; which are saved in this environment
and that gives me accss to  claude sonnet in bedrock in us-west-2 in my account which is strand's 
current default
"""

agent = Agent()
response = agent("What is the capital of France?")

print('end of file')
# print(response)