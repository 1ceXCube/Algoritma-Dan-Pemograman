#program mencari nilai FPB dan KPK
print ("tampilkan pilihan")
print ("1.FPB  ")
print ("2.KPK  ") 

pilihan = input("pilih opsi : ")
if pilihan == "1":
 print("anda memilih opsi FPB ")
elif pilihan == "2":
 print("anda memilih opsi KPK ")
else:
   print("invalid / error ")

bil1 = int (input ("masukkan bilangan pertama : ") )
bil2 = int (input ("masukkan bilangan kedua : ") )
if bil1 > bil2:
       bilangan_terkecil = bil1
else: 
 bilangan_terkecil = bil2
for i in range (1, bilangan_terkecil + 1):
 if (bil1 % i == 0) and (bil2 % i == 0):
  fpb = i
  kpk = int (bil1*bil2/(fpb))

if pilihan == "1":
  hasil_fpb = fpb
  print (f"bilangan FPB dari {bil1} dan {bil2} adalah : {fpb} ")  
elif pilihan == "2":
  hasil_kpk = kpk 
  print (f"bilangan FPB dari {bil1} dan {bil2} adalah : {kpk} ")    

  
  
