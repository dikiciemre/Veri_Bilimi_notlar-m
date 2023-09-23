"""
    İsim         Boy
0   Ahmet        175
1   Ayşe         NaN
2   Mehmet       182
3   Fatma        NaN
4   Emre         178
5   Zeynep       NaN
6   Gökçe        185
7   Elif         170
8   Can          NaN
9   Esra         169
"""

import pandas as pd
import numpy as np

# Örnek veri seti
veri = {'İsim': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma', 'Emre', 'Zeynep', 'Gökçe', 'Elif', 'Can', 'Esra'],
        'Boy': [175, np.nan, 182, np.nan, 178, np.nan, 185, 170, np.nan, 169]}

# Veri setini DataFrame'e dönüştürme
df = pd.DataFrame(veri)
print(df)
print("\n\n*****************\n\n")

# Eksik değerleri dolduran fonksiyon
def fix_missing(df, col_name):
    if col_name in df.columns:
        median = df[col_name].median()
        df[col_name].fillna(median, inplace=True)

# "Boy" sütunundaki eksik değerleri doldur
fix_missing(df, "Boy")

# Eksik değerlerin doldurulduğunu kontrol etme
print(df)
