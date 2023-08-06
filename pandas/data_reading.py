"""
meraba,

bu dosyada pandas kütüphanesini kullanarak veri okuma işlemlerini göreceğiz.
verilerle ilgili istatistiksel bilgileri göreceğiz.
herhangi bir veriyi nasıl okuyacağımızı ve üstünde nesaıl istatiksel bilgiye ulaşabileceğimizi inceleyeceğiz.
bu dosyada pandasın bir çok metodunu kullanacağız

en/
hi,
in this file, we will see how to read data using the pandas library.
we will see statistical information about the data.
we will examine how to read any data and how to access statistical information on it.
we will use many methods of pandas in this file

"""
import pandas as pd
import seaborn as sns


# df = pd.read_csv("\pandas\pd1.csv")
# print(df.head())


df = sns .load_dataset("titanic")
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.columns)  
# print(df.index)  # istatistiksel bilgileri verir
# print(df.describe().T)
# df.isnull().values.any  # boş değer var mı yok mu

# print(df.isnull().sum())  # boş değerlerin toplamı

# print(df) 


# print(df['sex'].head().tail(2))
print(df['sex'].value_counts()) # cinsiyetlerin sayısı 