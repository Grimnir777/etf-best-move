# Présentation

Ce projet consiste à répondre à la question : quelle est la meilleur période du mois pour investir sur un ETF, en prenant en considération des données historiques.


## Idée

L'idée est de prendre pour chaque mois plusieurs scénarios possibles. Dans tous les cas dans ce scénario j'investis 100€ par mois sur le S&P500 entre janvier 2020 et décembre 2021 (période covid).

Je ne prends pas en compte les frais qui seront les mêmes pour les 4 scénarios. Aussi, je considère qu'il est possible d'acheter des fractions d'ETF (possible en compte titres spécifique mais dans la majorité des cas et sur le PEA, il s'agira d'un nombre entier d'ETF acheté).

Scénarios :

- J'investis le 1er jour ouvré de chaque mois peu importe la valeur
- J'investis en milieu de mois : le 14, 15 ou 16 (le premier jour ouvré dans ces 3, sur la période choisie il n'y a pas de problème)
- J'investis le dernier jour ouvré de chaque mois peu importe la valeur
- J'essaie d'optimiser mes entrées, en achetant après une baisse de plus de 1% n'importe quel jour du mois (mais toujours une fois par mois) à défaut, le dernier jour ouvré du mois



## Résultats

### Achat en début de mois

Voici les résultats:

```
Total investi : 2400.00
Nombre d'ETF possédé : 39.14
Valeur totale du portefeuille au 31 décembre 2021 : 2918.79
Plus value : 518.79
```

### Achat en milieu de mois

Voici les résultats:

```
Total investi : 2400.00
Nombre d'ETF possédé : 38.76
Valeur totale du portefeuille au 31 décembre 2021 : 2890.76
Plus value : 490.76
```


### Achat en fin de mois

Voici les résultats:

```
Total investi : 2400.00
Nombre d'ETF possédé : 38.87
Valeur totale du portefeuille au 31 décembre 2021 : 2899.03
Plus value : 499.03
```

### Achat optimisé

Voici les résultats:

```
Achat d'etf le 27 1 2020 diff -1.58
Achat d'etf le 21 2 2020 diff -1.07
Achat d'etf le 3 3 2020 diff -2.82
Achat d'etf le 1 4 2020 diff -4.44
Achat d'etf le 1 5 2020 diff -2.82
Achat d'etf le 11 6 2020 diff -5.89
Achat d'etf le 7 7 2020 diff -1.08
Achat d'etf le 31 8 2020 diff -0.22
Achat d'etf le 3 9 2020 diff -3.51
Achat d'etf le 6 10 2020 diff -1.40
Achat d'etf le 18 11 2020 diff -1.14
Achat d'etf le 16 12 2020 diff -11.84
Achat d'etf le 4 1 2021 diff -1.48
Achat d'etf le 25 2 2021 diff -2.44
Achat d'etf le 3 3 2021 diff -1.32
Achat d'etf le 30 4 2021 diff -0.72
Achat d'etf le 10 5 2021 diff -1.04
Achat d'etf le 18 6 2021 diff -1.33
Achat d'etf le 19 7 2021 diff -1.59
Achat d'etf le 18 8 2021 diff -1.05
Achat d'etf le 20 9 2021 diff -1.71
Achat d'etf le 4 10 2021 diff -1.30
Achat d'etf le 26 11 2021 diff -2.28
Achat d'etf le 1 12 2021 diff -1.19
Total investi : 2400.00
Nombre d'ETF possédé : 39.23
Valeur totale du portefeuille au 31 décembre 2021 : 2926.13
Plus value : 526.13
```

A noter, qu'après plusieurs tentatives sur différentes valeurs de seuil j'ai choisi de garder le seuil de -1%, car pour des seuils inférieurs, l'option choix en fin de mois reste la plus choisie.

## Conclusion

Tout d'abord, on remarque des différences négligeables entre tous les scénarios. Cependant, cela reste à nuancer car la période choisie est courte (2 ans) ainsi que le montant investi chaque mois (100€).

Par contre, pour une approche totalement désintéressé des marchés (entre les 3 premiers scénarios), il paraît préférable de choisir l'investissement en début de mois. C'est d'ailleurs ce qui est souvent conseillé sur les forums et site internet d'investissement.

Pour les plus friands de performance, et d'après mes intuitions j'ai pu vérifier que l'achat après une baisse importante permet de booster un petit peu sa performance.