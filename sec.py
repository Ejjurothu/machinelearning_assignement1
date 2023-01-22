dog={}
dog["name"]="pandu"
dog["color"]="white"
dog["breed"]="lab"
dog["leg"]="7"
dog["age"]="5"
student={"fname":"divya","lname":"ejjurothu","gender":"female","age":"22","marital_status":"single","skills":["communication","python"],"country":"India","city":"vizianagaram","address":"india,moida"}
print("dog dictionary :",dog)
print("student dictionary:",student)
print("length of student dictionary :",len(student))
print("student skill :",student["skills"],"data type:",type(student["skills"]))
k=input("enter one extra skill")
student["skills"].append(k)
print("keys:",student.keys())
print("values",student.values())

