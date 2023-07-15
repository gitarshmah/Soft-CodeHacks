import pandas as pd
import pickle

df = pd.read_csv('Processed Data/save.csv')

list_of_states = list(df.State_Name.unique())

with open('model/tmodel', 'rb') as f:
    model=pickle.load(f)

def find_crop(a, b, c, d):
    x = model.predict([[a, b, c, d]])
    return x


x = find_crop(20.130175,81.604873, 7.628473, 262.717340)

print("Predicted crop: ", str(x[0]))




def find_secity(a, b):
    y = len(df[(df.Crop==a)&(df.State_Name==b)])
    if y==0:
        return f"The weather of the predicted {a} is not possible in the state {b}"

    y = list(df[(df.Crop==a)&(df.State_Name==b)].District_Name)
    str1 = ", "
    secities=str1.join(y)
    return f"You Should grow {a} in the districts of {secities} in the state of {b}"

print(find_secity('rice', 'Madhya Pradesh'))




