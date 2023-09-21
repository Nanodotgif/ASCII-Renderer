# Create visuals to use with the ASCII Renderer.
output = []
name = input("Name your renderable(python variable format): ")
print("Create your visual from top to bottom. For transparency, use '`', otherwise use ' '.")
user_input = ""
i = 0
while user_input != "done":
    user_input = input(f"({i}): ")
    if user_input == "undo":
        i -= 1
        continue
    if i < len(output):
        output[i] = user_input
    else:
        output.append(user_input)
    i+=1
print(f"{'_'.join(name.lower().split(' '))} = asciirenderer.create_renderable((0,0), {output[:-1]})")