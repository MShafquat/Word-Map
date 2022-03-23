import pandas as pd

country_df = pd.read_csv('../data/country.csv')
language_df = pd.read_csv('../data/country_list.csv', encoding='ISO-8859-1')

merged_df = pd.merge(country_df, language_df, how='inner', left_on='name', right_on='country_name')
merged_df = merged_df.reset_index(drop=True).drop(['ID', 'name', 'country'], axis=1)
merged_df.index += 1
merged_df.to_csv('./data/country_with_language.csv', index_label='id')
merged_df.to_json('./data/country_with_language.json', orient='records', indent=2)
