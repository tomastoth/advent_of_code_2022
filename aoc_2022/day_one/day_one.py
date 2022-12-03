elf_weights = []
current_elf = 0

with open("./input.txt", "r") as input_file:
    for line in input_file:
        if line != "\n":
            line = line.replace("\n","")
            item_calories = int(line)
            current_elf += item_calories
        else:
            elf_weights.append(current_elf)
            current_elf = 0

top_elf = (max(elf_weights))

top_three_elves = sum(sorted(elf_weights, reverse=True)[:3])
print(top_three_elves)



