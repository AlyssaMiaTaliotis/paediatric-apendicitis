import pandas as pd

# App data
df = pd.read_excel("app_data.xlsx", sheet_name="All cases")
df.to_csv("data/app_data.csv", index=False)


