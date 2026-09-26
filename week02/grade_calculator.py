totalscore = 0
studentcount = 0
while True:
  name = input("enter student name (or q to quit): ")
  if name == "q" or name == "Q":
    break
  score = float(input("enter score: "))
  if score < 0 or score > 100:
    print("invalid score. Plesase enter a number between 0 and 100 ")
    continue
  if score >= 90:
    grade = "A"
  elif score >= 80:
    grade = "B"
  elif score >= 70:
    grade = "C"
  elif score >= 60:
    grade = "D"
  else:
    grade = "F"
  if score == int(score):
    displayscore = int(score)
  else:
    displayscore = score
  print(f"{name}: {displayscore} -> {grade} ")
  totalscore = totalscore + score
  studentcount = studentcount + 1 
if studentcount > 0:
  average = totalscore / studentcount
  print(f"total student: {studentcount}")
  print(f"average score: {average:.2f}")
else:
  print("no students entered.")
  
     
