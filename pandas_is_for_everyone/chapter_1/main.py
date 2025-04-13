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

#