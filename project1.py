import csv
import re # for regex

print()

xytech_directories = list()
# Read from the Xytech work order:
with open('Xytech.txt') as xytech:
    for _ in range(2): # skip first two lines
        next(xytech)
    producer = xytech.readline()
    operator = xytech.readline()
    job = xytech.readline()
    for line in xytech: # get directories
        if(re.search("/hpsans", line)):
            xytech_directories.append(line.rstrip()) # rstrip() removes newline char from the end
    notes = line # last line has notes 

# Sanitize input:
producer = producer.split(': ')[1]
operator = operator.split(': ')[1]
job = job.split(': ')[1]

frame_dictionary = dict() # key: subdirectory, value(s): frame(s)
# Read from the baselight file:
with open('Baselight_export.txt') as baselight:

    # For each line, find the corresponding hpsans directory in the Xytech work order (use regex)
    line_list = baselight.readlines() # store each line in a list

    for line in line_list:
        if line != "\n":
            line = line.rstrip().split("/images1/")[1].split(" ") # line is a list containing the subdirectory followed by a bunch of frames
            subdirectory = line[0] # everything from line[1] onward is a list of frames
            frames = line[1:len(line)]
            if not bool(frame_dictionary.get(subdirectory)): # if key doesn't exist yet, create a new list...
                frame_dictionary[subdirectory] = list()
            for frame in frames: # ...then append each frame one by one
                if frame != '<err>' and frame != '<null>':
                    frame_dictionary[subdirectory].append(int(frame))

xytech.close()
baselight.close()

# Sort frames:
for subdir in frame_dictionary:
    frame_dictionary[subdir].sort()

# if subdirectory in readline then print that readline directory
# print(frame_dictionary)

# If a Xytech directory contains a Baselight subdirectory, replace with Xytech directory in frame_dictionary:
final_dict = dict()
for baselight_dir in frame_dictionary:
    for xytech_dir in xytech_directories:
        if(re.search(baselight_dir, xytech_dir)):
            final_dict[xytech_dir] = frame_dictionary[baselight_dir]
            # basically, make a copy frame_dictionary, but use the Xytech directories instead of the Baselight ones

print(final_dict)

# Write results to csv file:
with open('frame_fixes.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(["Producer", "Operator", "Job", "Notes"])
     writer.writerow([producer, operator, job, notes])
     writer.writerow(["Location", "Frame(s)"])

print()