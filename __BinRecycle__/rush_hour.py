# import pandas as pd
import pandas as pd

# load CSV file

rush_hour_data = pd.read_csv("gameboards/Rushhour6x6_1.csv")

# extract the field names 

rush_hour_data.columns 

# extract the rows

# data can be accessed using the field names

# rush_hour_data.orientation



# steps to write to a CSV using pandas

# create a pandas dataframe using pd.DataFrame

# header = ['Car', 'Orientation', 'Col', 'Row', 'lenght']

# data = [['A', ]]

# data = pd.DataFrame(data, columns=header)

# write to a CSV file using to_csv()

# Index=False to remove the index numbers

# syntax: data.to_csv("rush_hour_data", index=False)



