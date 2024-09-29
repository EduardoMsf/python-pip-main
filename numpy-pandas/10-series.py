import pandas as pd 


psg_players =  pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'], index=[1, 7, 10, 30])

print(psg_players)
print(pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi']))

dict = {1:'Navas', 7:'Mbappe', 10:'Neymar', 30:'Messi'}

print(pd.Series(dict))

dict2 ={
    'jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
    'altura': [185, 178, 175, 170],
    'goles': [2,200,200,200]
}

psg_players2 = pd.DataFrame(dict2,index=[1, 7, 10, 30] )
print(psg_players2)
print(psg_players2.columns)
print(psg_players2.index)
