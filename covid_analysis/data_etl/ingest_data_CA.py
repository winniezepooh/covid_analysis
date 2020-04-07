import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from covid_analysis.data_etl.covid_constants import CanadaCovidConstants as constants


class CovidCaDataClass:

    data_df = pd.read_csv(constants.source_link)
    data_df["date"] = pd.to_datetime(data_df['date'], format=constants.date_format)

    def plot_total_cases(self):
        fig, a = plt.subplots(4,3)
        i = 0
        for y in range(0,4):
            for x in range(0,3):
            
                province = constants.provinces[i]
                print(province)
                df = self.data_df[self.data_df['prname']==province]
                df = df.sort_values('date')  
                df['numconf_diff'] = df.numconf.diff()
                a[y][x].plot(df['date'], df['numconf_diff'])
                a[y][x].set_title(province)
                i = i + 1
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
        plt.show()