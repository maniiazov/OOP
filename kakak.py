data = [1, 2, 3, 2, 4, 1, 5, 3]
unique_data = []

for item in data:
    if item not in unique_data:
        unique_data.append(item)

print("Список без повторений:", unique_data)