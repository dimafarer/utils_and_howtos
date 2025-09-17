from strands import Agent
from strands.models import BedrockModel
from strands_tools import shell

"""
using a tool that comes as part of the Strands API.
"""
# Create a Bedrock model instance
bedrock_model = BedrockModel(
    model_id="us.amazon.nova-premier-v1:0",
    temperature=0.3,
    top_p=0.8,
)

agent = Agent(
    system_prompt="You are a helpfull agent.",
    model=bedrock_model,
    tools=[shell],
)
response = agent("What operating system am I using?")
# print(response)



# Documentation: https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/community-tools-package/

# GitHub Source: https://github.com/strands-agents/tools

# ### Available Tools by Category:

# RAG & Memory:
# • retrieve, memory, agent_core_memory, mem0_memory

# File Operations:
# • editor, file_read, file_write

# Shell & System:
# • environment, shell, cron, use_computer

# Code Interpretation:
# • python_repl, code_interpreter

# Web & Network:
# • http_request, slack, browser, rss

# Multi-modal:
# • generate_image_stability, image_reader, generate_image, nova_reels, speak, diagram

# AWS Services:
# • use_aws

# Utilities:
# • calculator, current_time, load_tool, sleep

# Agents & Workflows:
# • graph, agent_graph, journal, swarm, stop, handoff_to_user, use_agent, think, use_llm, workflow, batch, a2a_client

# Each tool links to its source code on GitHub for detailed implementation and usage examples.