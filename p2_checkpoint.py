def calcu_ave(score1, score2, score3):
  average = (score1 + score2 + score3) / 3
  return average
students = int(input("how many students?: "))
for i in range(students):
  print("Student", i + 1)
  name = input("enter name: ")

  score1 = float(input("activity 1: "))
  score2 = float(input("activity 2: "))
  score3 = float(input("activity 3: "))

  average = calcu_ave(score1, score2, score3)
  if average >= 90:
   Status = "Excellent"
  elif average >= 80:
   Status = "Very good"
  elif average >= 75:
   Status = "Passed"
  else:
   Status = "Failed"

  print("Name:", name)
  print("Activity 1:", score1)
  print("Activity 2:", score2)
  print("Activity 3:", score3)
  print("Average:", round(average, 2))
  print("Status:", Status)
