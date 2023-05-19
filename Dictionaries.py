student_attendance = {"Hamza": 22, "Ekrem": 42, "Mansur": 63}
for student in student_attendance :
  print(f"{student}: {student_attendance[student]}")
  
  
##################################
for student,attendance in student_attendance.items() :
  print(f"{student}: {attendance}")
  
###################################

if "Mahmut" in student_attendance:
  print(f"Mahmut: {student_attendance['Mahmut']}")
else:
  print("Not in this class")
  
####################################

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))

  
