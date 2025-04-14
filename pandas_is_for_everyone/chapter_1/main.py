import pandas as pd

# 1.2 Loading Your First Data Set

df = pd.read_csv('../data/gapminder.tsv', sep='\t')

# Displays the first 5 rows in the dataframe
df.head()

# Every Datafram object has a shape attribute to tell you its rows and columns
df.shape # (1704, 6) => (rows, columns)

# To see what columns are defined in df

df.columns

# Each column (Series) has the same type, where as each row has many different types

df.dtypes # Tells you what each column, types are

df.info() # More info for each column

"""
Pandas Type     Python Type     Description

object          string          most common type
int64           int             Whole numbers
float64         float           Numbers with decimals
datetime64      datetime        datetime is found in the Python standard library (i.e. is not loaded
                                by default and needs to be imported)
"""

# 1.3 Looking at Columns, Rows and Cells

# Subsetting columns by name
country_df = df['country']
country_df.shape
country_df.head()
country_df.tail()

# Multiple columns
subset = df[['country', 'continent', 'year']]
subset.shape
subset.head()
subset.tail()

# 1.3.2 Subsetting Rows - Intro to loc and iloc
df.loc[0] # Prints out the first row ( As a series )
df.loc[df.shape[0] -1] # Prints out the last element ( As a series )
df.tail(1) # Also prints out the last element ( As a dataframe )
df.loc[[0,99,999]] # Prints out the first, 100th and 1000th row as a df
# iloc and loc are the same except when loc is used as time series or other labels thats not index.
# iloc forces use of index location
df.iloc[0] # Prints out the first row ( As a series )
df.iloc[df.shape[0] -1] # Prints out the last element ( As a series )
df.tail(1) # Also prints out the last element ( As a dataframe )
df.iloc[[0,99,999]] # Prints out the first, 100th and 1000th row as a df
df.iloc[-1] # This works in index loc unlike loc where it tries to match the item in the column of index
# If indexing, user iloc if matching use loc etc

# 1.3.3 Using the second argument in iloc df[[row],[columns]]

df.loc[:, ['year', 'pop']] # Gets every row with year and pop columns
df.iloc[:, [2, 4, -1]] # iloc allow allows us to use integers, -1 from python slicing will allow us to get the last value
df.iloc[:, :3] # every row for first 3 columns
df.iloc[:, 3:6] # every row column 3,4,5
df.iloc[:, 0:6:2] # every row for 0,2,4

# 1.3.3.4 Subsetting rows as well as columns

df.loc[42, 'country'] # row index 42 with column 'country'
type(df.loc[42, 'country']) # Returns the actual value in this case str
df.iloc[42, 0] # row index 42 with column 'index 0' returns stringA
series = df.iloc[42, :3] # Returns a series, which is equilvalent to a sub row
type(series)
d = series.to_dict() # Converting a series to dict

# 1.3.3.5 Subsetting multiple rows and cols
df.iloc[[0,99,999], [0,3,5]]
df.loc[[0,99,999], ['country', 'lifeExp', 'gdpPercap']]
df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']]


# 1.4 Grouped and Aggregated Calculations

df.head(10)
# For each year in our data, what was the average life expectancy?
df.groupby('year')['lifeExp'].mean()

# Break down:
# Returns the memory location of th eobject 'DataFrameGroupBy' in this case the years with all our data
groupBy = df.groupby('year')

# Returns a series as we asked for one column
groupByLifeExp = groupBy['lifeExp'] 

# as column lifeExp is a float64 can do some maths operation
mean_life_exp_per_year = groupByLifeExp.mean()
mean_life_exp_per_year

# Do this calculation on multiple columns:
a = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
flat_example = a.reset_index()

# 1.4.2 Group Frequency count example



