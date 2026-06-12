with open("Input/Letters/starting_letter.txt", "r") as letter_base:
    content = letter_base.readlines()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

content_copy = content
new_data = []
for name in names:
    new_name = name.strip("\n")
    new_content = content_copy[0].replace("[name]", new_name)
    new_data = []
    for i in range(0, len(content)):
        if i == 0:
            new_data.append(f"{new_content}")
        else:
            new_data.append(content[i])

    with open(f"Output/ReadyToSend/letter_for_{new_name}.docx", "w") as file:
        for line in new_data:
            file.write(str(line))
