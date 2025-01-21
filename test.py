import pandas as pd


data = [
    
    {'Name': 'sunny', 'Age': 23, 'City': 'Bangalore'},
    {'Name': 'derick', 'Age': 25, 'City': 'Mumbai'},
    {'Name': 'priyanka', 'Age': 30, 'City': 'Delhi'},
    {'Name': 'Ayiri', 'Age': 27, 'City': 'Chennai'},
    {'Name': 'Micheal', 'Age': 35, 'City': 'Kolkata'}
    
]
    

data = pd.DataFrame(data)

data.to_csv('data/data.csv', index=False)