
from pathlib import Path
from me.helpers import get_tag
from me.prompts.read import read_prompt


def new():

    system_prompt = read_prompt("system")

    while True:
        index, length, content = get_tag(system_prompt, "file_content") or (None, None, None)

        if index is None:
            break

        file = Path(content)

        if file.exists():
            file_content = file.read_text(encoding="utf-8")
        else:
            file_content = f"<Tried to insert file '{content}' but it does not exist.>"
        
        system_prompt = (
            system_prompt[0:index] +
            f"\n{file_content}\n" +
            system_prompt[index+length:]
        )

    return system_prompt