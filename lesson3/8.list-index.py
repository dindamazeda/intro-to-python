kompanije = ['Google', 'Facebook', 'Yahoo', 'Microsoft', 'AirBnb']

pozicija_google_u_listi = kompanije.index('Google')

print(pozicija_google_u_listi)
print(kompanije[pozicija_google_u_listi] == 'Google')

gde_je_yahoo = kompanije.index('Yahoo', 0, len(kompanije))

print('Yahoo je na poziciji {}'.format(gde_je_yahoo))
print(kompanije[gde_je_yahoo] == 'Yahoo')
