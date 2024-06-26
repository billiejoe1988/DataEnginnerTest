import pandas as pd

df=pd.read_csv('train.csv')

print(df)
print('-------------------------------------------------------------')
print(df.columns)
print('-------------------------------------------------------------')
print(df.dtypes)
print('-------------------------------------------------------------')
print(df["Age"])
print('-------------------------------------------------------------')
print(df[["Name","Age", 'Sex','Survived']])
print('-------------------------------------------------------------')
df2 = df[["Name", "Age"]]
print(df2)
print('-------------------------------------------------------------')
print(df2.shape)
print('-------------------------------------------------------------')
print(df[df["Age"] > 30])
print('-------------------------------------------------------------')
print(df[df["Sex"] == "male"])
print('-------------------------------------------------------------')
print(df[df["Pclass"].isin([2,3])])
print('-------------------------------------------------------------')
print(df.loc[:, ["Age", "Sex"]])
print('---------------------TRANSFORM-------------------------------')
df["Nuevacolumna"] = 1
print(df.columns)
print('-------------------------------------------------------------')
df["Fare"] *20
print('-------------------------------------------------------------')
def pay_if_rich(x):
    if x["Pclass"] == 1:
        return x["Fare"] * 1.2
    else :
        return x["Fare"]
df["Fare_with_rich_tax"] = df.apply(pay_if_rich, axis=1)
#df df["Fare_with_rich_tax"] = df.apply(lamba x: x["Fare"] * 1.20 if x["Pclass"] == 1 else x["Fare"] , axis=1)
print(df)
print('-------------------------------------------------------------')
df_aux = pd.DataFrame({"Pclass": [1,2,3], "Pclass_Description": ["Upper class", "Mid class", "Low class"]})
print(df_aux)
print('-------------------------------------------------------------')
df_merge = pd.merge(df, df_aux, how="left", on="Pclass")
print(df_merge)
print('-------------------------------------------------------------')
print(df.groupby('Sex')['PassengerId'].count())
print('-------------------------------------------------------------')
print(df.groupby('Pclass').Fare.mean())
print('-------------------------------------------------------------')
print(df["Age"].mean())
print('-------------------------------------------------------------')
print(df["Age"].max())
print('-------------------------------------------------------------')
print(df["Age"].min())
print('-------------------------------------------------------------')
print(df.groupby(['Pclass'])[['Fare', 'Age']].mean())
print('-------------------------------------------------------------')
print('-------------------------------------------------------------')
