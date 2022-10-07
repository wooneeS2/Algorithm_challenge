import sys

num = int(sys.stdin.readline())
employee = {}
employee_in_office = []
for _ in range(num):
    name,isEnter = map(str,sys.stdin.readline().split())
    employee[name]=isEnter 

for key,value in employee.items():
        if value == 'enter':
                employee_in_office.append(key);


employee_in_office.sort(reverse=True)
for employee in employee_in_office:
        print(employee)
                
