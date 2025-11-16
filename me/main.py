
from pathlib import Path
from anthropic import Anthropic
from me.prompts.read import read_prompt
import os


def wake_up():

    # My system prompt:
    system_prompt = read_prompt("system")

    client = Anthropic()

    print(system_prompt)

    # message = client.messages.create(
        
    #     system=system_prompt,
    #     max_tokens=1024,
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Hello, Claude",
    #         }
    #     ],
    #     model="claude-sonnet-4-5-20250929",
    # )

    # print("Claude's response:")
    # print(message.content)
