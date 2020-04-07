import pandas as pd
from datetime import datetime, timedelta 

import pkgutil
search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)

import covid_constants


class CovidDataClass:
    covid_daily_link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv"
    csv_start_date = '01-22-2020'
    

    def ingest_daily_data():
        daily_cases_df = pd.DataFrame()
        today = datetime.now()
        today = today.strftime("%m-%d-%Y")
        day = datetime(2020, 1, 22, 0, 0)

        while day.strftime("%m-%d-%Y") != today:
            date_data_df = pd.read_csv(covid_daily_link.format(date = day.strftime("%m-%d-%Y")))
            #adding date of the recording
            date_data_df["date"] = datetime.now().strftime("%d-%m-%Y")
            print(date_data_df)
            daily_cases_df = daily_cases_df.append(date_data_df)

            day = day + timedelta(days=1)

        return daily_cases_df    

