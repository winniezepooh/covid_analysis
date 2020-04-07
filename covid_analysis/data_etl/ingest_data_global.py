import pandas as pd
from datetime import datetime, timedelta 

from covid_analysis.data_etl.covid_constants import GlobalCovidConstants as constants


class CovidGlobalDataClass:

    def ingest_daily_data(self):
        daily_cases_df = pd.DataFrame()
        today = datetime.now()
        today = today.strftime(constants.date_format)
        day = constants.csv_start_date

        while day.strftime(constants.date_format) != today:
            date_data_df = pd.read_csv(constants.covid_daily_link.format(date = day.strftime(constants.date_format)))
            #adding date of the recording
            date_data_df["date"] = datetime.now().strftime(constants.date_format)
            #print(date_data_df)
            daily_cases_df = daily_cases_df.append(date_data_df)

            day = day + timedelta(days=1)

        return daily_cases_df  

    def ingest_time_series_confirmed(self):
        data_df = pd.read_csv(constants.time_series_confirmed_link)
        return data_df  

    def ingest_time_series_deaths(self):
        data_df = pd.read_csv(constants.time_series_deaths_link)
        return data_df  

    def ingest_time_series_recovered(self):
        data_df = pd.read_csv(constants.time_series_recovered_link)
        return data_df      
  

