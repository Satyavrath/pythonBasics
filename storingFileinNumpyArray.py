import numpy as np

salary = np.genfromtxt('SalaryGender.csv',delimiter=',')
numpyArray1 = []
numpyArray2 = []
numpyArray3 = []
numpyArray4 = []


# using list comprehension
numpyArray1 = [salary[row][0] for row in range(1,len(salary))]
numpyArray2 = [salary[row][1] for row in range(1,len(salary))]
numpyArray3 = [salary[row][2] for row in range(1,len(salary))]
numpyArray4 = [salary[row][3] for row in range(1,len(salary))]

# for i in range(1,len(salary)):
#     for j in range(4):
#         if j == 0:
#             numpyArray1.append(salary[i][j])
#         if j ==1:
#             numpyArray2.append(salary[i][j])
#         if j == 2:
#             numpyArray3.append(salary[i][j])
#         if j == 3:
#             numpyArray4.append(salary[i][j])
# print(numpyArray1)
# print(numpyArray2)
# print(numpyArray3)
# print(numpyArray4)

