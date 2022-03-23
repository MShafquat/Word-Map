# Word Map
A world map of how people of different regions say a word.

## Data
[country.csv](./data/country.csv) contains countries and their latitude and longitude, the file is collected from: [https://developers.google.com/public-data/docs/canonical/countries_csv](https://developers.google.com/public-data/docs/canonical/countries_csv)

[country_list.csv](./data/country_list.csv) contains major language of each country with language code. The file is collected from: [http://www.fullstacks.io/2016/07/countries-and-their-spoken-languages.html](http://www.fullstacks.io/2016/07/countries-and-their-spoken-languages.html)

[join-country-and-language-data.py](./utils/join-country-and-language-data.py) is used to merge these two files and create a [csv](./data/country_with_language.csv) and a [json](./data/country_with_language.json) file that contains country code, country name, latitude, longitude information along with major language of the country.

## Running the app

The app uses streamlit, all the required packages can be installed using `pip install -r requirements.txt`.
To run the app, run `streamlit run src/app.py`. Please note that, the number of translated text may be less than the `Number of countries to show` specified in the slider because the dataset used has missing entries for some countries.

## TODO

1. Dataset for the languages of the countries collected from [http://www.fullstacks.io/2016/07/countries-and-their-spoken-languages.html](http://www.fullstacks.io/2016/07/countries-and-their-spoken-languages.html) has some misinformation and missing entries, need to use or create a correct one.
