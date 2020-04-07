import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from covid_analysis.data_etl.covid_constants import CanadaCovidConstants as constants

data = pd.read_csv(constants.source_link)

data["date"] = pd.to_datetime(data['date'], format=constants.date_format)


fig, a = plt.subplots(4,3)
i = 0
for y in range(0,4):
    for x in range(0,3):
    
        province = constants.provinces[i]
        print(province)
        df = data[data['prname']==province]
        df = df.sort_values('date')  
        df['numconf_change'] = df.numconf.diff()
        a[y][x].plot(df['date'], df['numconf_change'])
        a[y][x].set_title(province)
        i = i + 1
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.show()