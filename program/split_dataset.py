import pandas as pd
import numpy as np

df = pd.read_csv("penguins.csv")


df_split = np.array_split(df, 10)
print(len(df_split))


for i in range(10):
    df_split[i].to_csv(f"temp/penguins{i}.csv", index=False)


