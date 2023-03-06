import csv
import re # for regex

print()

# Read from the Xytech work order:
with open('Xytech.txt') as xytech:
    for _ in range(2): # skip first two lines
        next(xytech)
    producer = xytech.readline()
    operator = xytech.readline()
    job = xytech.readline()
    for line in xytech: # last line has notes
        pass
    notes = line

# Sanitize input:
producer = producer.split(': ')[1]
operator = operator.split(': ')[1]
job = job.split(': ')[1]


''' 
Get the problem frames from the baselight export, and spit out a list 
of directories from the work order followed by the problem frames.

Shopping List

- Producer : Line 2
- Operator : Line 3
- Job : Line 4
- Notes : Last line
- Location
- Frames
'''

frame_dictionary = dict() # key: subdirectory, value(s): frame(s)
# Read from the baselight file:
with open('Baselight_export.txt') as baselight:

    # For each line, find the corresponding hpsans directory in the Xytech work order (use regex)
    line_list = baselight.readlines() # store each line in a list

    '''
    looks like dis
    ['/images1/starwars/reel1/partA/1920x1080 32 33 34 67 68 69 122 123 155 1023 1111 1112 1160 1201 1202 1203 1204 1205 1211 1212 1213 1214\n', 
    '/images1/starwars/reel1/VFX/Hydraulx 1251 1252 1253 1260 <err> 1270 1271 1272 \n', 
    '/images1/starwars/reel1/partA/1920x1080 1302 1303 1310 1500 5000 5001 5002\n', 
    '/images1/starwars/pickups/shot_1ab/1920x1080 5010 5011 5012 5013 5014\n', 
    '/images1/starwars/reel1/partA/1920x1080 5111 5122 5133 5144 5155 5166\n', 
    '/images1/starwars/reel1/VFX/Framestore 6188 6189 6190 6191\n', 
    '/images1/starwars/reel1/partA/1920x1080 6200 6201 6209 6212 6219 6233 6234 6267 6269 6271 6278 6282 6288 6289 6290 6292 6293 6294\n', 
    '/images1/starwars/reel1/partB/1920x1080 6409 6410 6411 6413 6450 6666 6667 6668 6670 6671 6680 6681 6682 6683 6684\n', 
    '/images1/starwars/reel1/VFX/AnimalLogic 6832 6833 6834 6911 6912 6913 6914\n', '/images1/starwars/reel1/partB/1920x1080 8845\n', 
    '/images1/starwars/pickups/shot_1ab/1920x1080 10001 10002 10008 11113 \n', 
    '/images1/starwars/reel1/partB/1920x1080 12011 12021 12031 12041 12051 12111 12121 12131 12141 <null>\n', 
    '\n']
    '''

    for line in line_list:
        if line != "\n":
            line = line.rstrip().split("/images1/")[1].split(" ") # line is a list containing the subdirectory followed by a bunch of frames
            subdirectory = line[0] # everything from line[1] onward is a list of frames
            frames = line[1:len(line)]
            # if bool(frame_dictionary.get(subdirectory)):
            #     for frame in frames:
            #         frame_dictionary[subdirectory].append(frame)
            # else:
            #     frame_dictionary[subdirectory] = line[1:len(line)]
            if not bool(frame_dictionary.get(subdirectory)): # if key doesn't exist yet, create a new list...
                frame_dictionary[subdirectory] = list()
            for frame in frames: # ...then append each frame one by one
                if frame != '<err>' and frame != '<null>':
                    frame_dictionary[subdirectory].append(int(frame))
            # print(f"subdirectory: {subdirectory}")
            # for i in range(1,len(line)):
            #     print(line[i])

# Sort frames:
for subdir in frame_dictionary:
    frame_dictionary[subdir].sort()

# if subdirectory in readline then print that readline directory
print(frame_dictionary)



# Write results to csv file:
with open('frame_fixes.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Producer", "Operator", "Job", "Notes"])
     writer.writerow([producer, operator, job, notes])
     writer.writerow(["Location", "Frame(s)"])

# baselight.close()
xytech.close()

'''
 import csv
 i = 0
 with open('frame_fixes.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     
     writer.writerow(["Producer", "Operator", "Job", "Notes"])
     writer.writerow([producer_name, operator_name, job_type, job_notes])
     writer.writerow(["Location", "Frame(s)"])
     
     loop:
        writer.writerow([i, directory, frames])

'''

print()