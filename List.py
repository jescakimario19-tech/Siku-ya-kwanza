print ("TO-DO LIST YA BOOM")
matumizi = [] # Hii ndio list itakayo hifadhi matumizi yote
while True:
  print ("/n chagua namba:")
  print (" 1. ongeza tumizi jipya ")
  print (" 2. onyesha matumizi yote")
  print (" 3. Hesabu ya jumla ya boom")
  print (" 4. Toka")
  chaguo = input ("Andika namba 1-4:")
  if chaguo == "1":
    jina = input ("Andika tumizi: mfano chakula: ")
    kiasi = int(input ("kiasi Tsh:"))
    matumizi.append("jina+ "-" + str(kiasi))
    print ("umehifadhi!")
                    elif chaguo == "2":
    print ("/n --- MATUMIZI YAKO ---")
    for tumizi in matumizi
    print(tumizi)
                    elif chaguo == "3":
  jumla = 0
for tumizi in matumizi
#Tunataka sehemu ya kiasi kutoka "chakula -5000"
kiasi_cha_tumizi = tumizi.slit("-")
 jumla = jumla + int(kiasi_cha_tumizi)  
print ("/n --- JUMLA YA BOOM --- ")
print (" umetumia jumla ya Tsh:",jumla)
elif chaguo == "4":
print ("kwaheri.Dhibiti boom yako!")
break
    else:
print("chaguo sio sahihi mkuu")
