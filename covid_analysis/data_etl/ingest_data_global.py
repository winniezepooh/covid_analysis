from datetime import datetime, timedelta

import pandas as pd

from covid_analysis.data_etl.covid_constants import GlobalCovidConstants as constants


class CovidGlobalDataClass:
    # def __init__(self):
    #    self.daily_data = self.ingest_daily_data()

    def ingest_daily_data(self):
        daily_cases_df = pd.DataFrame()
        today = datetime.now()
        today = today.strftime(constants.date_format)
        day = constants.csv_start_date

        while day.strftime(constants.date_format) != today:
            date_data_df = pd.read_csv(
                constants.covid_daily_link.format(
                    date=day.strftime(constants.date_format)
                )
            )
            # adding date of the recording
            date_data_df["date"] = datetime.now().strftime(constants.date_format)
            daily_cases_df = daily_cases_df.append(date_data_df)

            day = day + timedelta(days=1)

        return daily_cases_df

    def ingest_time_series_data(self, data_set):
        """
        data_set can either be "deaths", "recovered", or "confirmed_cases"
        """
        if data_set == "deaths":
            source_link = constants.source_links["deaths"]
        elif data_set == "recovered":
            source_link = constants.source_links["recovered"]
        else:
            source_link = constants.source_links["confirmed_cases"]

        data_df = pd.read_csv(source_link)
        df_null_prov = data_df[data_df["Province/State"].isnull()]
        df_null_prov["location"] = df_null_prov["Country/Region"]
        df_with_prov = data_df[data_df["Province/State"].notnull()]
        df_with_prov["location"] = (
            df_with_prov["Province/State"] + ", " + df_with_prov["Country/Region"]
        )
        df_with_location = df_null_prov.append(df_with_prov)
        col_list = ["location"] + list(data_df.columns[4:])
        final_df = df_with_location[col_list]
        final_df = final_df.T
        # transpose made the country names part of the rows
        # need to take the country names and make it column names
        col_list = list(final_df.iloc[0])
        final_df.columns = final_df.iloc[0]
        final_df = final_df.iloc[1:]
        final_df.index.name = "date"
        return final_df
