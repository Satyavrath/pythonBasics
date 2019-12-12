inputFIle = open('bank-data.csv','r')
set = set()
individulAge = []
for line in inputFIle:
    Age,JobDescription,MaritalStatus,Y  = line.strip().split(",")
    # print(JobDescription)
    set.add(JobDescription)
    individulAge.append(Age)


userInput = input("Please enter the profession")

if userInput in set:
    print("Profession is eligible")
else:
    print("Please enter different profession")
inputFIle.close()

