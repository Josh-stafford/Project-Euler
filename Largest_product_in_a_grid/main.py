import grid_data
import evaluate

temp = grid_data.nums.replace('\n', ' ')
grid = temp.split(' ')

highest_val = 0

for i in range(len(grid)):
    current = evaluate.evaluate(grid, i)
    if current > highest_val:
        highest_val = current

print(highest_val)





