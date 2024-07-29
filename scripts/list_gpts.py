import os
import re


def get_sorted_first_lines():
    current_dir = os.getcwd()
    file_data = []

    for filename in os.listdir(current_dir):
        match = re.match(r"Day-(\d+).*\.md", filename)
        if match:
            day_number = int(match.group(1))
            with open(filename, "r", encoding="utf-8") as file:
                first_line = file.readline().strip()[2:]
            file_data.append((day_number, first_line))

    # Sort the data based on the day number
    file_data.sort(key=lambda x: x[0], reverse=True)

    # Return only the sorted first lines
    return [line for _, line in file_data]


result = "\n".join(get_sorted_first_lines())
print(result)
