import csv

# csv.writer

# baselight = open("Baselight_export.txt", "r")
# xytech = open("Xytech.txt", "r")

with open('Xytech.txt') as xytech:
    for _ in range(2):
        next(xytech)
    producer = xytech.readline()
    operator = xytech.readline()
    job = xytech.readline()
    for line in xytech:
        pass
    notes = line

print(f"{producer}\n{operator}\n{job}\n{notes}")



# string_baselight = baselight.read()
# string_xytech = xytech.read()

# print("---------- BASELIGHT REPORT ----------")
# print(string_baselight)
# print("---------- XYTECH REPORT ----------")
# print(string_xytech)

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
     #writer.writerow([producer_name, operator_name, job_type, job_notes])
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