import numpy as np
salary = np.genfromtxt("SalaryGender.csv",delimiter = ",")

for i in range(1,len(salary)):
    dictmen = {'men': 0, 'women': 0}
    for i in range(1, len(salary)):
        if salary[i][1] == 1.0 and salary[i][3] == 1.0:
            dictmen['men'] += 1
        if salary[i][1] == 0 and salary[i][3] == 1.0:
            dictmen['women'] += 1

print("{} is the count of men with PhD \n{} is the count of women with PhD".format(dictmen['men'], dictmen['women']))