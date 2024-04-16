import pandas as pd
import pyplot 

players = pd.read_csv("players-data.csv",sep=",")
collages =pd.read_csv("players-collage.csv",sep=",")
salary=pd.read_csv("players-salary.csv",sep=",")
temp = pd.read_csv("temperature.csv",sep=",")

print(temp.to_string)
print(f"ilosc rekordow wynosi : { players.count()}")


print(players.head(3))
print(players.tail(3))

merged_inner = pd.merge(left=players,right=collages,how="left")
merged_left = pd.merge(salary,how="left")

print(temp["City"]["Country"])




def lb2kg(w:float):
    return float(w*0.045359237)

def imp2metric(w:str):
    d = w.split("-")
    return float(d[0]*30.48 + float(d[1]))*2.54

merged_left["Weight"] = merged_left["Weight"].map(lb2kg)
merged_left["Height"] = merged_left["Height"].map(imp2metric)

print(merged_left)

gr1= merged_left.groupby("Team").agg(srednie=('Salary','mean'))

gr1['srednie'] = gr['srednie'].map('{:.f}'.format)








