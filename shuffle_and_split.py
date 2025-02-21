import random

# Set the file names and split ratios
input_filename = "observations.txt"
train_filename = "train.txt"
val_filename = "val.txt"
test_filename = "test.txt"

# Define split ratios (they should sum to 1.0)
train_ratio = 0.70
val_ratio = 0.15
test_ratio = 0.15

# Read the rows from the input file
with open(input_filename, "r") as infile:
    lines = infile.readlines()

# Shuffle the list of rows to randomize the order
random.shuffle(lines)

# Determine split indices
total_lines = len(lines)
train_end = int(total_lines * train_ratio)
val_end = train_end + int(total_lines * val_ratio)

# Split the data
train_lines = lines[:train_end]
val_lines = lines[train_end:val_end]
test_lines = lines[val_end:]

# Write the splits into separate files
with open(train_filename, "w") as train_file:
    train_file.writelines(train_lines)

with open(val_filename, "w") as val_file:
    val_file.writelines(val_lines)

with open(test_filename, "w") as test_file:
    test_file.writelines(test_lines)

print(f"Data has been split into {train_filename} ({len(train_lines)} lines), "
      f"{val_filename} ({len(val_lines)} lines), and {test_filename} ({len(test_lines)} lines).")