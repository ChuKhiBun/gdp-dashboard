import seaborn as sns
mpg_df = sns.load_dataset("mpg")
ax = sns.scatterplot(x="weight", y="mpg", data=mpg_df)
