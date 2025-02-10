# 1- m
# print(" Sonlarni kvadiratini chiqarib beradigan dastur ")
# yegindi = " "
# while yegindi != "tohta" :
#     yegindi =input(" Istol gan son kiriting yoki (dasturni tohtatish uchun tohta deb yozing) : ")
#     if yegindi != "tohta":
#         print(float(yegindi)**2)
# print(" Dastur tugadi ")
# 2 - m
# print("#Istalgan soni kivadiratini topadigan dastur ")
# yegindi = " "
# ishora = True
# while ishora:
#     yegindi= input("Istalgan son kiriting (dasturni tohtatish uchun tohta deb yozing )")
#     if yegindi =="tohta":
#         ishora = False
#     else:
#         print(float(yegindi)**2)
# print("Dastur tugadi")
# 3 - m
# print("#Istlagan soni kivadiratini chiqarib beradigan dastur ")
# yegindi = " "
# while True:
#     yegindi = input("Istalgan son kiriting (datsturni tohtatish uchun tohta deb yozing )")
#     if yegindi == "tohta":
#         break
#     else:
#         print(float(yegindi)**2)
# print("Dastur tohtadi ")
# 4- m
# sonlare =(range(1,11))
# for son in sonlare:
#     if son ==4:
#         break
#     else:
#         print(f"{son } bu soni kivadirati {son **2 }")
# 5-m
# salom= {"apple":"olma","banana":"banan"}
# soz = input("soz kiriting").lower()
# tarijama=salom.get(soz)
# if tarijama==None:
#     print("bunday soz yoq ")
# else:
#     print(f'{soz.title()} bu sozni tarjimasi {tarijama}')
# 6-m
# logot = {"if":"shart aperatori agar degani ","int":"butunson degani ","str":"yozuli malumot turi","else":"shart opertori agar degani "}
# for n,k in sorted(logot.items()):
#     print(n,"-",k)
# 7-m
# mevalar = {"olma":"qizil","shaftoli":"suvli","behi":"qatiq","gilos":"kichikna","banan":"sariq"}
# for k,n in sorted(mevalar.items()):
#     print(k,"-",n)
# 8-m
# davlatlar = {"o'zbekiston":"toshkent","hindiston":"dehli","rossiya":"maskiva","italya":"rim"}
# for key in sorted(davlatlar):
#     print(key.title())
# 9-m
# davlatlar = {"o'zbekiston":"toshkent","hindiston":"dehli","rossiya":"maskiva","italya":"rim"}
# for soz,key in sorted(davlatlar.items()):
#     print(key.title())
# 10-M
# davlatlar = {"o'zbekiston":"toshkent","hindiston":"dehli","rossiya":"maskiva","italya":"rim"}
# sorov =str(input("qayis davlatni poytahtini bishni holaysiz>> ")).lower()
# sorovnoma= davlatlar.get(sorov)
# if sorovnoma:
#     print(f"{sorov.title()} bu davlatni poytaxti {sorovnoma.title()}")
# else:
#     print("bizda bunday malumot yoq ")
# 11-m
# malumotlar ={"osh":20000,"shorva":15000,"non":3000,"choy":2000}
# kerak = input("3 ta narsa buyurtma qiling >>  ").strip().lower()
# buyurtmlar=[]
# for n in range(3):
#     buyurtmlar.append(input(f"{n+1}-tavom").lower())
# for buyurtma in buyurtmlar:
#     if buyurtma in malumotlar:
#         print(f"{buyurtma.title()}  {malumotlar[buyurtma]} som")
#     else:
#         print(f"kechirasiz ,bizda {buyurtma} yoq")
#
# mahsulotlar = {
#     "olma": 3000,
#     "behi": 5000,
#     "gilos": 2000,
#     "banan": 15000
# }
# yordam = []
# for n in range(2):
#     meva = input(f"{n+1}-buyurtma: ").strip().lower()
#     yordam.append(meva)
# for a in yordam:
#     if a in mahsulotlar:
#         print(f"{a.title()} - {mahsulotlar[a]} so'm")
#     else:
#         print(f"{a.title()} bizda bunday meva yo‘q")
