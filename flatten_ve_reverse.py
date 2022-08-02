"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#input için liste

output = []
#output için liste

#sorunun çözümü için kullanacağımız fonksiyon
def flatten(l):
    for i in l:
        #liste içerisindeki tüm elemanları elden geçiriyoruz
        if type(i)==list:
            #eğer liste içinde liste varsa fonksiyonu tekrar çağırıp liste elemanlarını teker teker elden geçiriyoruz
            flatten(i)
            #elden geçmemiş listeleri elemek için kullanıyoruz
            continue
        #elden geçirilen her elemanı teker teker output listesine ekliyoruz
        output.append(i)

#fonksiyonu çağırıp outputu bastırıyoruz
flatten(liste)
print(output)

"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

inp = [[1, 2], [3, 4], [5, 6, 7]]
#input için liste
out = []
#output için liste
for i in inp:
    #liste içindeki her listeyi sıralamak adına döngü kullanıyoruz
    i.reverse()
    out.append(i)
#alt listeleri sıraladıktan sonra tüm listeyi tekrardan sıralayıp bastırıyoruz
out.reverse()
print(out)


