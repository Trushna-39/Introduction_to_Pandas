# Trushnaben Bharatkumar Patel - C0886910

import pandas

df = pandas.read_csv('F:\PycharmProjects\Session3\COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv')

# Using df.head()
print("Display dataframe head:")
print(df.head())

# Access particular column data
print("Display the column 'critical_staffing_shortage_today_no': ")
print(df['critical_staffing_shortage_today_no'])

# Access all columns from the dataset
print("List of columns present in the dataset:")
print(df.columns)

# Find the maximum value from the selected column
print("The maximum value for the 'column critical_staffing_shortage_today_no' is: ", df['critical_staffing_shortage_today_no'].max())
print("The minimum value for the 'column critical_staffing_shortage_today_no' is: ", df['critical_staffing_shortage_today_no'].min())
print("The mode value for the 'column critical_staffing_shortage_today_no' is: ", df['critical_staffing_shortage_today_no'].mode())

