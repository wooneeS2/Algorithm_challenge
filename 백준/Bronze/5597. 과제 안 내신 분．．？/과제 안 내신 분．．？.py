import sys

attendance_number = []
for i in range(28):
    attendance_number.append(int(sys.stdin.readline()))  
students = list(range(1,31))
attendance_number.sort()

absent_number = list(set(students).difference(attendance_number))
print(min(absent_number))
print(max(absent_number))