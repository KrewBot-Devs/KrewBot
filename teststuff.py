'''        embed=discord.Embed(title='Goods Prices', color=discord.Color.orange())
        embed.add_field(name='Brazil', value='Rum: 60\nCoffee: 26\nSpice: 25 \nSilk: 150', inline=True)
        embed.add_field(name='Guinea', value='Rum: 38\nCoffee: 22\nSpice: 22\nSilk: 310', inline=True)
        embed.add_field(name='Labrador', value='Rum: 48\nCoffee: 40\nSpice: 14\nSilk: 230', inline=True)
        embed.add_field(name='Spain', value='Rum: 52\nCoffee: 65 \nSpice: 53\nSilk: 180', inline=True)
        embed.add_field(name='Jamaica', value='Rum: 32\nCoffee: 70\nSpice: 40\nSilk: 240', inline=True)
'''
goods = {
'Brazil': {
        'Rum': '60',
        'Coffee': '26',
        'Spice': '25',
        'Silk': '150'
        },
'Guinea': {
        'Rum': '38',
        'Coffee': '22',
        'Spice': '22',
        'Silk': '310'
        },
'Labrador': {
        'Rum': '48',
        'Coffee': '40',
        'Spice': '14',
        'Silk': '230'
        },
'Spain': {
        'Rum': '60',
        'Coffee': '26',
        'Spice': '53',
        'Silk': '180'
        },
'Brazil': {
        'Rum': '32',
        'Coffee': '70',
        'Spice': '40',
        'Silk': '240'
        }

}
Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},
         'Dict2': {'name': 'Bob', 'age': '25'}}
for i in goods:
    print(i,':')
    for k, v in goods[i].items():
        print(k,': ',v)
