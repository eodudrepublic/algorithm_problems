# 2023-12-24
import sys

while True:
    try:
        ins = input()

        lower_count = 0
        upper_count = 0
        num_count = 0
        space_count = 0
        for char in ins :
            if char.islower() : lower_count += 1
            elif char.isupper() : upper_count += 1
            elif char.isdigit() : num_count += 1
            else : space_count += 1
        sys.stdout.write(' '.join([str(lower_count), str(upper_count), str(num_count), str(space_count), '\n']))
        
    except EOFError:
        break