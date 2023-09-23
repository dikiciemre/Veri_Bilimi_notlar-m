import pandas as pd

# Örnek veri çerçevesi
data = {'Cinsiyet': ['Erkek', 'Kadın', 'Diğer', 'Erkek', 'Kadın']}
df = pd.DataFrame(data)
print(df)

# Kategorik değişkenleri nümerik değerlere dönüştürme
df_encoded = pd.get_dummies(df, columns=['Cinsiyet'])


# Sonuçları görüntüleme
print(df_encoded)
