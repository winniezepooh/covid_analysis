from datetime import datetime


class GlobalCovidConstants:
    covid_daily_link = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{date}.csv"
    csv_start_date = datetime(2020, 1, 22, 0, 0)
    data_change_date = datetime(2020, 3, 22, 0, 0)
    date_format = "%m-%d-%Y"

    source_links = {
        "confirmed_cases": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
        "deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
        "recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv",
    }


class CanadaCovidConstants:
    source_link = "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
    date_format = "%d-%m-%Y"
    provinces = [
        "Ontario",
        "British Columbia",
        "Quebec",
        "Alberta",
        "Saskatchewan",
        "Manitoba",
        "New Brunswick",
        "Newfoundland and Labrador",
        "Nova Scotia",
        "Prince Edward Island",
        "Yukon",
        "Northwest Territories",
        #"Canada"
    ]
