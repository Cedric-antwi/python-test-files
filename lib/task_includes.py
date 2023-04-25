def task_includes(text):
    task = text.split(" ")
    for char in task:
        if char == "#TODO":
            return True
        else:
            return False
