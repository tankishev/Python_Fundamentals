# Create a program that manages the state of the treasure chest along the way. 
# On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:

# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
# o	If an item is already contained, don't insert it.

# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest. 
# o	If the index is invalid, skip the command.

# •	"Steal {count}":
# o	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are. 
# o	Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"

# In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."
# Input
# •	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
# •	On the following lines, until "Yohoho!", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The loot items will be strings containing any ASCII code.
# •	The indexes will be integers in the range [-200…200]
# •	The count will be an integer in the range [1….100]

loot = input().split("|")
while True:
    input_line = input()
    if input_line == 'Yohoho!':
        break

    tokens = input_line.split(' ')
    command = tokens[0]

    if command == 'Loot':
        items = [x for i, x in enumerate(tokens) if i != 0 and x not in loot]
        items.reverse()
        loot = items + loot
        
    elif command == 'Drop':
        i = int(tokens[1])
        if 0 <= i < len(loot):
            loot.append(loot.pop(i))
        
    elif command == 'Steal':
        i = int(tokens[1])
        if i > len(loot):
            print(*loot, sep=', ')
            loot.clear()
        else:
            print(*loot[-i:], sep=', ')
            loot = loot[:-i]

if loot:
    gain = sum([len(x) for x in loot]) / len(loot)
    print(f"Average treasure gain: {gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")