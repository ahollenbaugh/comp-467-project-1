import csv
import re # for regex

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