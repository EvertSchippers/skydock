
def get_tag(text: str, tag_name: str, index: int = 0) -> tuple[int, int, str] | None:

    tag_start = f"<{tag_name}>"
    tag_end = f"</{tag_name}>"

    start_index = text.find(tag_start, index)
    if start_index == -1:
        return None
    end_index = text.find(tag_end, start_index)
    if end_index == -1:
        return None

    content_start = start_index + len(tag_start)
    content_length = end_index - content_start

    total_length = len(tag_start) + content_length + len(tag_end)

    content = text[content_start:end_index].strip()
    return start_index, total_length, content


def get_tags(text: str, tag_name: str) -> list[tuple[int, int, str]]:
    tags = []
    index = 0

    while index < len(text):
        result = get_tag(text, tag_name, index)
        if result is None:
            break
        start_index, total_length, content = result
        tags.append((start_index, total_length, content))
        index = start_index + total_length
    return tags
