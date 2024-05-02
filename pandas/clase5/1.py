import pandas as pd

df = pd.DataFrame({"Nombre": ["Juan", "Pedro", "Marcos"], "Edad":[13,15,33], "Sexo": ["M", "M", "M"] })

print(df)
print ("----------------------------- columna edad-----------------------------")
print(df["Edad"])
print ("---------------------------- Data type ( son series) ------------------")
print(type(df["Edad"]))
print ("---------------------------- edad maxima ------------------------------")
print(df["Edad"].max())