import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from covid_analysis.data_etl.covid_constants import \
    CanadaCovidConstants as constants


class CovidCaDataClass:
    def __init__(self):
        self.data_df = self.ingest_data()

    def ingest_data(self):
        data_df = pd.read_csv(constants.source_link)
        data_df["date"] = pd.to_datetime(data_df["date"], format=constants.date_format)
        #adding log for confirmed cases
        data_df["numconf_log"] = np.log(data_df["numconf"])
        return data_df

    def plot_cases_per_province(self, column):
        fig, a = plt.subplots(4, 3)
        i = 0
        for y in range(0, 4):
            for x in range(0, 3):

                province = constants.provinces[i]
                print(province)
                df = self.data_df[self.data_df["prname"] == province]
                df = df.sort_values("date")
                df["numconf_diff"] = df.numconf.diff()
                a[y][x].plot(df["date"], df[column])
                a[y][x].set_title(province)

                i = i + 1
        fig.autofmt_xdate()
        plt.subplots_adjust(
            left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5
        )
        plt.show()
