"""
   İsim     Soyisim      Tarih       Derece
0  Ahmet    Yılmaz      1990-05-15   Lisans
1  Ayşe     Demir       1985-09-22   Yüksek Lisans
2  Mehmet   Kaya        1995-03-10   Doktora
3  Fatma    Şahin       1988-12-03   Lisans
4  Emre     Arslan      1992-07-18   Yüksek Lisans
5  Zeynep   Öztürk      1997-01-25   Lisans
6  Gökçe    Erdoğan     1984-11-30   Doktora
7  Elif     Karadeniz   1993-08-12   Yüksek Lisans
8  Can      Özdemir    1989-06-07   Lisans
9  Esra     Aksoy       1991-04-05   Yüksek Lisans
"""

import pandas as pd

# yukarıda veri setinde derece değerlerini kategorikten nümeriğe çevirdi.

# Örnek veri çerçevesi
data = {'İsim': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma', 'Emre'],
        'Soyisim': ['Yılmaz', 'Demir', 'Kaya', 'Şahin', 'Arslan'],
        'Tarih': ['1990-05-15', '1985-09-22', '1995-03-10', '1988-12-03', '1992-07-18'],
        'Derece': ['Lisans', 'Yüksek Lisans', 'Doktora', 'Lisans', 'Yüksek Lisans']}

df = pd.DataFrame(data)

# Derece sütununu sıralı nümerik değerlere dönüştürme
degree_mapping = {'Lisans': 1, 'Yüksek Lisans': 2, 'Doktora': 3}
df['Derece'] = df['Derece'].map(degree_mapping)

# Sonuçları görüntüleme
print(df)
