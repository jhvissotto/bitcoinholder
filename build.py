# Gera index.html a partir de template.html + CSVs mensais.
# Uso: python downloader.py (atualiza CSVs)  ->  python build.py
import pandas as pd, json
f={'btc':'btc_usd_mensal.csv','sp':'sp500_mensal.csv','dj':'dowjones_mensal.csv','rut':'russell2000_mensal.csv'}
d=None
for k,v in f.items():
    x=pd.read_csv(v,usecols=['Date','Close']).rename(columns={'Close':k})
    d=x if d is None else d.merge(x,on='Date')
D={'d':[s[:7] for s in d.Date]}
for k in f: D[k]=[round(v,2) for v in d[k]]
html=open('template.html',encoding='utf-8').read().replace('__DATA__',json.dumps(D,separators=(',',':')))
open('index.html','w',encoding='utf-8').write(html)
print('index.html gerado:',len(d),'meses',D['d'][0],'->',D['d'][-1])
