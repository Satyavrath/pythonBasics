import pandas,numpy as np
# store input file in multi-dimensional format
salaryData = np.genfromtxt('SalaryGender.csv',delimiter=',')
# stores column data from multi-dimensional array of people with phD
npToSeriesphD = pandas.Series([salaryData[phd][3] for phd in range(1,len(salaryData))])
# stores column data from multi-dimensional array of people with Age
npToSeriesAge = pandas.Series([salaryData[age][2] for age in range(1,len(salaryData))])
# Assigns column names to each series input
ageSeries = {"Age": npToSeriesAge,"Phd": npToSeriesphD }
# prints data in 2-dimensional using dataframe function
data = pandas.DataFrame(ageSeries)
# phDdata = data.drop(val)
for i in range(len(data)):
    if data.loc[i]["Phd"] == 0:
        data = data.drop(i)
print(data)
# Question 4:

print(" Total number of people with PhD Degree" ,data.count().get("Phd"))

# reads input data in 2-dimensional format using pandas

# salaryData = pandas.read_csv("SalaryGender.csv")

# # Assigns column names to each series input and allocate data to each column based on row location and column name
# ageSeries1 = {"Age": pandas.Series([salaryData.iloc[age]["Age"] for age in range(len(salaryData))]),
# "Phd": pandas.Series([salaryData.iloc[phd]["PhD"]for phd in range(len(salaryData))]]) }
# print(pandas.DataFrame(ageSeries1))