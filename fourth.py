it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
n=len(age)
print("length of it_companies",len(it_companies))
it_companies.add("Twitter")
it_companies.update(["tcs","infosys"])
print(it_companies)
it_companies.remove("tcs")

print("Join A and B",A|B)
print("intersection of A and B :",A&B)
print("Is A subset of B",A.issubset(B))
print("A and B are disjoint Sets?", A.isdisjoint(B))

print("What is the symmetric difference between A and B",A-B)
del A
del B
age=set(age)
print("compare the length of the list and the set ","list len :",n,"set len :",len(age))





#• Join A with B and B with A
#• What is the symmetric difference between A and B
#• Delete the sets completely
#• Convert the ages to a set and compare the length of the list and the set