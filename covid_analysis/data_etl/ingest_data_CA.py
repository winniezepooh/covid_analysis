import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

source_link = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
data = pd.read_csv(source_link)

data["date"] = pd.to_datetime(data['date'], format='%d-%m-%Y')

provinces = data['prname'].unique()  
provinces = ['Ontario', 'British Columbia', 'Quebec', 'Alberta', 'Saskatchewan', 'Manitoba',
       'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia',
       'Prince Edward Island', 'Yukon', 'Northwest Territories']
fig, a = plt.subplots(4,3)
i = 0
for y in range(0,4):
    for x in range(0,3):
    
        province = provinces[i]
        print(province)
        df = data[data['prname']==province]
        df = df.sort_values('date')  
        df['numconf_change'] = df.numconf.diff()
        a[y][x].plot(df['date'], df['numconf_change'])
        a[y][x].set_title(province)
        i = i + 1
    
plt.show()