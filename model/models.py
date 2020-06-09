# coding:utf-8
import numpy as np
import pandas as pd


def data():
    df = pd.read_csv("./data.csv")
    df.columns = ['Date', 'M2', 'M1']
    df['Date'] = df['Date'].astype(np.datetime64)
    df['Date'] = df['Date'].map(lambda x: x.strftime("%Y-%m"))
    date = df['Date']
    date = list(date.values)

    # 'M2g','M1g','M1g-M2g'
    df.insert(3, 'M2g', None)
    df.insert(4, 'M1g', None)
    df.insert(5, 'M1g-M2g', None)
    df = df.set_index('Date')

    df['M2g'] = df['M2'].pct_change(periods=12)
    df['M1g'] = df['M1'].pct_change(periods=12)
    df['M1g-M2g'] = df['M1g'] - df['M2g']

    df.fillna(0, inplace=True)

    m2g = df['M2g'].map(lambda x: '%.4f' % x).astype(float)
    m1g = df['M1g'].map(lambda x: '%.4f' % x).astype(float)
    m1g_m2g = df['M1g-M2g'].map(lambda x: '%.4f' % x).astype(float)
    m2g = list(m2g.values)
    m1g = list(m1g.values)
    m1g_m2g = list(m1g_m2g.values)

    m2g_date = []
    for tpl in zip(date, m2g):
        m2g_date.append(list(tpl))

    m1g_date = []
    for tpl in zip(date, m1g):
        m1g_date.append(list(tpl))

    m1g_m2g_date = []
    for tpl in zip(date, m1g_m2g):
        m1g_m2g_date.append(list(tpl))

    df['M2'] = df['M2'].map(lambda x: '%.2f' % x)
    df['M1'] = df['M1'].map(lambda x: '%.2f' % x)
    df['M2g'] = df['M2g'].map(lambda x: format(x, '.2%'))
    df['M1g'] = df['M1g'].map(lambda x: format(x, '.2%'))
    df['M1g-M2g'] = df['M1g-M2g'].map(lambda x: format(x, '.2%'))

    return date, m2g_date, m1g_date, m1g_m2g_date, df
