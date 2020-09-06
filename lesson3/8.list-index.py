companies = ['Google', 'Facebook', 'Yahoo', 'Microsoft', 'AirBnb']

index_of_google_in_the_list = companies.index('Google')

print(index_of_google_in_the_list)
print(companies[index_of_google_in_the_list] == 'Google')

where_is_yahoo = companies.index('Yahoo', 0, len(companies))

print('Yahoo is on index {}'.format(where_is_yahoo))
print(companies[where_is_yahoo] == 'Yahoo')
