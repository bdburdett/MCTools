import pandas as pd
 
#-----------------------------------------------------------------------------#
#   1. Reads the current CSV file and makes data frame ("data") variable      #
#   2. Sets the data type in entire csv to string object with dtype           #
#   3. To adjust for another client, export their courses list and insert the #
#      extract name to the csv parameter in line 9.                           #
#-----------------------------------------------------------------------------#
data = pd.read_csv('import_southside.csv', dtype=str)

# sorting by header
data.sort_values('Course OID', inplace=True)

# print the amount of courses before removing duplicate rows
print(data.shape[0])

# dropping ALL duplicate values based on course OID, keeping the first instance of the value
print (data[data.duplicated(subset=['Course OID'])])
data.drop_duplicates(subset=['Course OID'], keep='first', inplace=True)

# print the amount of courses after removing duplicate rows
print(data.shape[0])

# displaying data
print(data)

# columns to keep in new output file
keep_cols = [
             'Course OID', 
             'Subject', 
             'Name',
             'Code',
             'Short Title'
            ]
data = data[keep_cols]

# create a new CSV file to import into Acalog with the updated columns you want
data.to_csv('output.csv', index=False)


#-----------------Additional Data Analysis Print Statements--------------------#

# show the column header data type 
# print(data.info())

# head shows first 5 courses, tails shows last 5 courses
# print(data.head(5))
# print(data.tail(5))

#-----------------------------------------------------------------------------#
