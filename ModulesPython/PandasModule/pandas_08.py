import pandas as pd

df = pd.read_csv("D:\DataScienceWithRahul\Operations_data\sample2.csv")

# print(df.head())

# grooup_branch = df.groupby(by='Branch')
# # print(grooup_branch)
# print(grooup_branch.groups)

group_sec_branch = df.groupby(by=['Section','Branch'])

# print(group_sec_branch.groups)
# for group, data_frame in group_sec_branch:
#     print(group)
#     print(data_frame)
#     print()

# for group, data_frame in group_sec_branch:
    # print(group)
    # print(data_frame)
    # print() mean of all the columns


