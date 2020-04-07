from datetime import datetime

class GlobalCovidConstants:
    covid_daily_link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv"
    csv_start_date = datetime(2020, 1, 22, 0, 0)
    date_format = "%m-%d-%Y"
    time_series_confirmed_link = "https://raw.githubusercontent.com/winniezepooh/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
    time_series_death_link = "https://raw.githubusercontent.com/winniezepooh/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
    time_series_recovered_link = "https://raw.githubusercontent.com/winniezepooh/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"

class CanadaCovidConstants:
    source_link = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
    date_format = "%d-%m-%Y"
    provinces = ['Ontario', 'British Columbia', 'Quebec', 'Alberta', 'Saskatchewan', 'Manitoba',
       'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia',
       'Prince Edward Island', 'Yukon', 'Northwest Territories']