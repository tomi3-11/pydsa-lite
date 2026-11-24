from pydsa_lite.structures import Stack
history=Stack[str]()
for action in ["open file","edit file","save file"]:history.push(action)
while not history.is_empty():print("Undo:",history.pop())
