# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
  
total_height = 0
for i in student_heights:
  total_height += i

print("Total height = ",total_height)

number = len(student_heights)

print("number of students =",number)

print("average height = ", total_height//number)