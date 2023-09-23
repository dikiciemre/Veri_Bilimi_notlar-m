import langs as langs
import pandas as pd
import numpy as np


numbers = pd.Series([35.798, 64.436, 76.678, 12.380])
print(numbers)
"""
0    35.798
1    64.436
2    76.678
3    12.380
dtype: float64
"""



numbers.name = "Pandas Series Numbers"
print(numbers.name)
"""
Pandas Series Numbers
"""



print(numbers.dtype)
"""
float64
"""



print(numbers[0]," ",numbers[3])
"""
35.798   12.38
"""


print(numbers.index)
"""
RangeIndex(start=0, stop=4, step=1)
"""




numbers.index = [

    "Istanbul",
    "Turkiye",
    "Canada",
    "Los Angeles"]
print(numbers)
"""
Istanbul       35.798
Turkiye        64.436
Canada         76.678
Los Angeles    12.380
Name: Pandas Series Numbers, dtype: float64
"""


print(numbers["Los Angeles"])
"""
12.38
"""


print(numbers.iloc[3])
"""
12.38
"""



print(numbers.iloc[[3,1]])
"""
Los Angeles    12.380
Turkiye        64.436
Name: Pandas Series Numbers, dtype: float64
"""


print(numbers[["Canada","Turkiye"]])
"""
Canada     76.678
Turkiye    64.436
Name: Pandas Series Numbers, dtype: float64
"""

print("--------------------------\n")



print(numbers > 30)
"""
Istanbul        True
Turkiye         True
Canada          True
Los Angeles    False
Name: Pandas Series Numbers, dtype: bool
"""




print(numbers.mean())
"""
47.323
"""



print(numbers.std())
"""
28.91602593718577
"""


print(numbers*1_000_000)
"""
Istanbul       35798000.0
Turkiye        64436000.0
Canada         76678000.0
Los Angeles    12380000.0
Name: Pandas Series Numbers, dtype: float64
"""




data_frame = pd.DataFrame({
    "Population" : [35.798, 64.436,76.678,12.380],
    "GDP": [2341342,2341342,64564356,68679732],
    "Surface": [1234,5678,368396,1235890],
    "HDI": [0.923,0.453,0.756,0.534],
    "Continent": ["Turkiye","Turkiye","America","America"]},
    columns=["Population","GDP","Surface","HDI","Continent"])

print(data_frame)
"""
   Population       GDP  Surface    HDI Continent
0      35.798   2341342     1234  0.923   Turkiye
1      64.436   2341342     5678  0.453   Turkiye
2      76.678  64564356   368396  0.756   America
3      12.380  68679732  1235890  0.534   America
"""




print(data_frame.index)
"""
RangeIndex(start=0, stop=4, step=1)
"""


print(data_frame.columns)
"""
Index(['Population', 'GDP', 'Surface', 'HDI', 'Continent'], dtype='object')
"""


print(data_frame.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   Population  4 non-null      float64
 1   GDP         4 non-null      int64  
 2   Surface     4 non-null      int64  
 3   HDI         4 non-null      float64
 4   Continent   4 non-null      object 
dtypes: float64(2), int64(2), object(1)
memory usage: 288.0+ bytes
None
"""



print(data_frame.size)
"""
20
"""


print(data_frame.shape)
"""
(4, 5)
"""


print(data_frame.describe())
"""
       Population           GDP       Surface       HDI
count    4.000000  4.000000e+00  4.000000e+00  4.000000
mean    47.323000  3.448169e+07  4.027995e+05  0.666500
std     28.916026  3.715049e+07  5.814303e+05  0.213652
min     12.380000  2.341342e+06  1.234000e+03  0.453000
25%     29.943500  2.341342e+06  4.567000e+03  0.513750
50%     50.117000  3.345285e+07  1.870370e+05  0.645000
75%     67.496500  6.559320e+07  5.852695e+05  0.797750
max     76.678000  6.867973e+07  1.235890e+06  0.923000
"""



print(data_frame.dtypes)
"""
Population    float64
GDP             int64
Surface         int64
HDI           float64
Continent      object
dtype: object
"""


print(data_frame.dtypes.value_counts())
"""
float64    2
int64      2
object     1
Name: count, dtype: int64
"""



print(data_frame.loc[0])
"""
Population     35.798
GDP           2341342
Surface          1234
HDI             0.923
Continent     Turkiye
Name: 0, dtype: object
"""


print(data_frame["Population"])
"""
0    35.798
1    64.436
2    76.678
3    12.380
Name: Population, dtype: float64
"""



print(data_frame["Population"] > 40)
"""
0    False
1     True
2     True
3    False
Name: Population, dtype: bool
"""


print(data_frame.loc[data_frame["Population"] > 40])
"""
   Population       GDP  Surface    HDI Continent
1      64.436   2341342     5678  0.453   Turkiye
2      76.678  64564356   368396  0.756   America
"""


print(data_frame.loc[data_frame["Population"] > 40, ["Population","GDP"]])
"""
   Population       GDP
1      64.436   2341342
2      76.678  64564356
"""




print(data_frame.drop(0))
"""
   Population       GDP  Surface    HDI Continent
1      64.436   2341342     5678  0.453   Turkiye
2      76.678  64564356   368396  0.756   America
3      12.380  68679732  1235890  0.534   America
"""



print(data_frame.drop(columns=["Population","HDI"]))
"""
       GDP  Surface Continent
0   2341342     1234   Turkiye
1   2341342     5678   Turkiye
2  64564356   368396   America
3  68679732  1235890   America
"""





langs = pd.Series(
    ["Turkish","Turkish","English","English"],
    index= [0,1,2,3],
    name="Language"
)

data_frame["Languages"] = langs
print(data_frame)
"""
   Population       GDP  Surface    HDI Continent Languages
0      35.798   2341342     1234  0.923   Turkiye   Turkish
1      64.436   2341342     5678  0.453   Turkiye   Turkish
2      76.678  64564356   368396  0.756   America   English
3      12.380  68679732  1235890  0.534   America   English
"""





data_frame = pd.read_csv('veriler.csv')
print(data_frame)
"""
   ulke  boy  kilo  yas cinsiyet
0    tr  130    30   10        e
1    tr  125    36   11        e
2    tr  135    34   10        k
3    tr  133    30    9        k
4    tr  129    38   12        e
5    tr  180    90   30        e
6    tr  190    80   25        e
7    tr  175    90   35        e
8    tr  177    60   22        k
9    us  185   105   33        e
10   us  165    55   27        k
11   us  155    50   44        k
12   us  160    58   39        k
13   us  162    59   41        k
14   us  167    62   55        k
15   fr  174    70   47        e
16   fr  193    90   23        e
17   fr  187    80   27        e
18   fr  183    88   28        e
19   fr  159    40   29        k
20   fr  164    66   32        k
21   fr  166    56   42       k"
"""




print(data_frame.head())
"""
  ulke  boy  kilo  yas cinsiyet
0   tr  130    30   10        e
1   tr  125    36   11        e
2   tr  135    34   10        k
3   tr  133    30    9        k
4   tr  129    38   12        e
"""



print(data_frame.tail())
"""
   ulke  boy  kilo  yas cinsiyet
17   fr  187    80   27        e
18   fr  183    88   28        e
19   fr  159    40   29        k
20   fr  164    66   32        k
21   fr  166    56   42       k"
"""



print(data_frame.columns)
"""
Index(['ulke', 'boy', 'kilo', 'yas', 'cinsiyet'], dtype='object')
"""


print(data_frame.shape)
"""
(22, 5)
"""


print(data_frame.dtypes)
"""
ulke        object
boy          int64
kilo         int64
yas          int64
cinsiyet    object
dtype: object
"""





print(data_frame.isnull())
"""
    ulke    boy   kilo    yas  cinsiyet
0   False  False  False  False     False
1   False  False  False  False     False
2   False  False  False  False     False
3   False  False  False  False     False
4   False  False  False  False     False
5   False  False  False  False     False
6   False  False  False  False     False
7   False  False  False  False     False
8   False  False  False  False     False
9   False  False  False  False     False
10  False  False  False  False     False
11  False  False  False  False     False
12  False  False  False  False     False
13  False  False  False  False     False
14  False  False  False  False     False
15  False  False  False  False     False
16  False  False  False  False     False
17  False  False  False  False     False
18  False  False  False  False     False
19  False  False  False  False     False
20  False  False  False  False     False
21  False  False  False  False     False
"""





data_frame1 = pd.DataFrame({
    "Column A" : [3,np.nan,4,np.nan],
    "Column B": [234,545,657,np.nan],
    "Column C": [np.nan,56,23,78]},
    columns=["Column A","Column B","Column C"])

print(data_frame1)
"""
   Column A  Column B  Column C
0       3.0     234.0       NaN
1       NaN     545.0      56.0
2       4.0     657.0      23.0
3       NaN       NaN      78.0

"""



print(data_frame1.dropna() )
"""
   Column A  Column B  Column C
2       4.0     657.0      23.0
"""



print(data_frame1.dropna(thresh=2))
"""
   Column A  Column B  Column C
0       3.0     234.0       NaN
1       NaN     545.0      56.0
2       4.0     657.0      23.0
"""




elciler = pd.Series([ 'France', 'United Kingdom', 'United Kingdom', 'Italy', 'Germany', 'Germany', 'Germany', ],
index=['Gérard Araud', 'Kim Darroch', 'Peter Westmacott', 'Armando Varricchio', 'Peter Wittig', 'Peter Ammon', 'Klaus Scharioth ' ])




print(elciler.duplicated())
"""
Gérard Araud          False
Kim Darroch           False
Peter Westmacott       True
Armando Varricchio    False
Peter Wittig          False
Peter Ammon            True
Klaus Scharioth        True
dtype: bool
"""





print("------------------\n")
print(elciler.duplicated(keep="last"))
"""
Gérard Araud          False
Kim Darroch            True
Peter Westmacott      False
Armando Varricchio    False
Peter Wittig           True
Peter Ammon            True
Klaus Scharioth       False
dtype: bool
"""





print("------------------\n")
print(elciler.duplicated(keep=False))
"""
Gérard Araud          False
Kim Darroch            True
Peter Westmacott       True
Armando Varricchio    False
Peter Wittig           True
Peter Ammon            True
Klaus Scharioth        True
dtype: bool
"""




print("------------------\n")
# keep=False diyerek bu serideki tekrarlanan tüm verileri silelim
print(elciler.drop_duplicates(keep=False))
"""
Gérard Araud          France
Armando Varricchio     Italy
dtype: object
"""




print("------------------\n")
#"keep" parametresine "first" değerini verirsek tekrarlanan verilerin ilkleri dışındakileri siler:
print(elciler.drop_duplicates(keep="first"))
"""
Gérard Araud                  France
Kim Darroch           United Kingdom
Armando Varricchio             Italy
Peter Wittig                 Germany
dtype: object
"""




print("------------------\n")
df = pd.DataFrame({ 'Veri': [ '1987_E_ABD _1', '1990?_E_ING_1', '1992_K_ABD_2', '1970?_E_ IT_1', '1985_K_I T_2' ]})
print(df)
"""
            Veri
0  1987_E_ABD _1
1  1990?_E_ING_1
2   1992_K_ABD_2
3  1970?_E_ IT_1
4   1985_K_I T_2
"""


print("------------------\n")
print(df["Veri"].str.split("_"))
#Bu verideki sütunların sırasıyla yıl, cinsiyet, ülke ve çocuk sayısı verilerini içerdiğini biliyoruz. Örneğin; "E" erkek, "K" kız anlamına geliyor. Bu bilgileri ayırıp farklı sütunlar haline getireceğiz. Pandas "str" arayüzü ile string metotlarını kullanmamızı sağlar. "split" metodunu kullanalım:
"""
0    [1987, E, ABD , 1]
1    [1990?, E, ING, 1]
2     [1992, K, ABD, 2]
3    [1970?, E,  IT, 1]
4     [1985, K, I T, 2]
Name: Veri, dtype: object
"""



print("------------------\n")
print(df["Veri"].str.split("_", expand=True)) # "expand" parametresini True yaparak parçalanan verileri sütunlara ayırabiliriz:
"""
       0  1     2  3
0   1987  E  ABD   1
1  1990?  E   ING  1
2   1992  K   ABD  2
3  1970?  E    IT  1
4   1985  K   I T  2
"""




print("------------------\n")
df = df["Veri"].str.split("_", expand=True)# sütunlara ayıralım
df.columns = ["Yıl", "Cinsiyet", "Ülke", "Çocuk Sayısı"] # sütun isimlerini değiştirelim
print(df)# dataframe'i yazdıralım
"""
     Yıl Cinsiyet  Ülke Çocuk Sayısı
0   1987        E  ABD             1
1  1990?        E   ING            1
2   1992        K   ABD            2
3  1970?        E    IT            1
4   1985        K   I T            2
"""



print("------------------\n")
print(df["Yıl"].str.contains("\?")) # Verilerde herhangi bir metin ya da karakter bulunuyor mu diye kontrol etmek için "contains" metodunu kullanabiliriz. Örneğin; soru işareti (?) içeren verilere bakalım
"""
0    False
1     True
2    False
3     True
4    False
Name: Yıl, dtype: bool
"""



print("------------------\n")
#Burada soru işaretinden önce "" karakterini koyduk çünkü bu metot regex metni alıyor ve "?" karakterinin özel bir anlamı var. Bu özel anlamı baskılamak için "" karakteri koyduk. Burada iki tane yıl verisi "?" içeriyor, bu işaretleri silmemiz lazım. "replace" metodu ile bu işaretleri boş string ("") ile değiştirerek silebiliriz:
df["Yıl"] = df["Yıl"].str.replace("\?", "") # "?" karakterlerini silelim
print(df["Yıl"]) # Yıl verilerini yazdıralım
"""
0     1987
1    1990?
2     1992
3    1970?
4     1985
Name: Yıl, dtype: object
"""



print("------------------\n")
#Ülke isimlerindeki boşlukları (" ") da kaldıralım:
df["Ülke"] = df["Ülke"].str.replace(" ", "") # " " karakterlerini silelim
print(df["Ülke"])
"""
0    ABD
1    ING
2    ABD
3     IT
4     IT
Name: Ülke, dtype: object
"""


print("------------------\n")
#Son olarak temizlenmiş olan tüm verimizi yazdıralım:
print(df)
"""
     Yıl Cinsiyet Ülke Çocuk Sayısı
0   1987        E  ABD            1
1  1990?        E  ING            1
2   1992        K  ABD            2
3  1970?        E   IT            1
4   1985        K   IT            2
"""

