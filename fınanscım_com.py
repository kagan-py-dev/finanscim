### FİNANSIMCOM ###

import datetime as dt, random as rd, json as js

kullanicilar = []

def motivesozler():

    motive_sozler = [

        {"Warren Buffett": "Risk, ne yaptığını bilmediğin zaman ortaya çıkar."},
        {"Warren Buffett": "Bugün biri gölgede oturuyorsa, bunun sebebi uzun zaman önce birinin ağaç dikmiş olmasıdır."},
        {"Warren Buffett": "Fiyat ödediğin şeydir, değer ise aldığın."},

        {"Charlie Munger": "Tersine düşün. Daima tersine düşün."},
        {"Charlie Munger": "Büyük para, alım satımda değil beklemede kazanılır."},

        {"Benjamin Graham": "Yatırımcıların en büyük düşmanı, kendileridir."},
        {"Benjamin Graham": "Akıllı yatırımcı, piyasaya değil mantığa güvenir."},

        {"Peter Lynch": "Bildiğin işe yatırım yap."},
        {"Peter Lynch": "Hisse senetleri, sabrı olmayanlardan sabırlılara para transfer eder."},

        {"Ray Dalio": "Acı + düşünme = ilerleme."},
        {"Ray Dalio": "Gerçekle yüzleşmezsen, gerçek seni bulur."},

        {"Jim Rohn": "Disiplin, hedeflerle başarı arasındaki köprüdür."},
        {"Jim Rohn": "Geliriniz nadiren kişisel gelişiminizin üzerine çıkar."},

        {"Napoleon Hill": "Zenginlik, düşünceyle başlar."},
        {"Napoleon Hill": "Vazgeçmeyenler sonunda kazanır."},

        {"Peter Drucker": "En iyi gelecek, onu yaratanındır."},
        {"Peter Drucker": "Planlamayan, başarısız olmayı planlamıştır."},

        {"Robert Kiyosaki": "Zenginler para için çalışmaz, parayı kendileri için çalıştırır."},
        {"Robert Kiyosaki": "Finansal özgürlük bir zihniyet meselesidir."},

        {"John D. Rockefeller": "Para kazanmak, her meslekten daha asil bir sanattır."},
        {"John D. Rockefeller": "Disiplinli tasarruf, büyük servetlerin temelidir."},

        {"George S. Clason": "Altın, onu tutmayı bilenlere gider."},
        {"George S. Clason": "Kazancının bir kısmını kendine ayır."},

        {"Howard Marks": "İkinci seviyede düşünmeden büyük başarı olmaz."},
        {"Howard Marks": "Risk, çoğu zaman aşırı özgüvenden doğar."},

        {"Elon Musk": "Uzun vadede önemli olan, vazgeçmemektir."},
        {"Elon Musk": "Sürekli gelişmeyen bir sistem çökmeye mahkûmdur."},

        {"Jeff Bezos": "Uzun vadeli düşünmek, kısa vadede cesaret ister."},
        {"Jeff Bezos": "Müşteri güveni, en değerli varlıktır."},

        {"Bill Gates": "Başarı kötü bir öğretmendir."},
        {"Bill Gates": "Kendine yatırım, en yüksek getiriyi sağlar."},

        {"Henry Ford": "İster yapabileceğine inan, ister inanma; her iki durumda da haklısın."},
        {"Henry Ford": "Birlikte çalışmak başarıyı getirir."},

        {"Jack Ma": "Bugün zor olan şeyler, yarının fırsatlarıdır."},
        {"Jack Ma": "Vazgeçmeyenler sonunda kazanır."},

        {"Paul Tudor Jones": "Sermayeni koru, kazanç kendiliğinden gelir."},
        {"Paul Tudor Jones": "Disiplin olmadan strateji işe yaramaz."}

    ]
    
    soz = rd.choice(motive_sozler) 

    for yazar, metin in soz.items(): 
        print(f"{yazar}: {metin}")

def giris():
    ad = input("Adınızı Giriniz: ")
    soyad = input("Soyadınızı Giriniz: ")
    kullaniciadi = input("Kullanıcı Adınızı Giriniz(Lütfen kullanıcı adınızda en az 1 adet rakam, özel karakter ve büyük harf olsun): ")
    sifre = input("Şifrenizi Giriniz (Lütfen şifrenizde en az 1 adet rakam, özel karakter ve büyük harf olsun): ")
    gmail = input("Gmailinizi Giriniz: ").strip()
    yas = input("Yaşınızı Giriniz: ")
    meslek = input("Mesleğinizi Giriniz: ")
    aylik_gelir = int(input("Lütfen Aylık Net Gelirinizi Girin(Maaş, Harçlık, Pasif gelir vb.): "))
    return ad, soyad, kullaniciadi, sifre, gmail, yas, meslek, aylik_gelir

def giriskt(ad, soyad, kullaniciadi, sifre, gmail):
    ozelktkrer = "!-*"
    hatalar = []

    k_rakamvar = False
    k_ozelvar = False
    k_buyukharf = False

    s_rakamvar = False
    s_ozelvar = False
    s_buyukharf = False

    if not ad.isalpha():
        hatalar.append("AD_HATA")

    if not soyad.isalpha():
        hatalar.append("SOYAD_HATA")

    for i in kullaniciadi:
        if i in ozelktkrer:
            k_ozelvar = True

        if i.isdigit():
            k_rakamvar = True

        if i.isupper():
            k_buyukharf = True

    
    if not k_ozelvar or not k_rakamvar or not k_buyukharf:
        hatalar.append("KULLANICIADI_HATA")

    if len(sifre) < 10:
        hatalar.append("SIFRE_UZUNLUK_HATA")

    for i in sifre:

        if i in ozelktkrer:
            s_ozelvar = True

        if i.isdigit():
            s_rakamvar = True

        if i.isupper():
            s_buyukharf = True

    if not s_ozelvar or not s_rakamvar or not s_buyukharf:
        hatalar.append("SIFRE_KARAKTER_HATA")

    if not gmail.endswith("@gmail.com"):
        hatalar.append("GMAIL_HATA")

    if kullaniciadi == sifre:
        hatalar.append("KULLANİCİADİ_SİFRE_AYNI_HATASI")

    return hatalar

def db():
    while True:
        ad, soyad, kullaniciadi, sifre, gmail, yas, meslek, aylik_gelir = giris()
        hata = giriskt(ad, soyad, kullaniciadi, sifre, gmail)

        if hata:
            if "AD_HATA" in hata:
                print("Ad sadece harflerden oluşmalı")

            if "SOYAD_HATA" in hata:
                print("Soyad sadece harflerden oluşmalı")

            if "KULLANICIADI_HATA" in hata:
                print("Kullanıcı adı büyük harf, rakam ve özel karakter içermeli")

            if "SIFRE_UZUNLUK_HATA" in hata:
                print("Şifre en az 10 karakter olmalı")

            if "SIFRE_KARAKTER_HATA" in hata:
                print("Şifre büyük harf, rakam ve özel karakter içermeli")

            if "GMAIL_HATA" in hata:
                print("Geçerli bir gmail giriniz")

            if "KULLANICIADI_SIFRE_AYNI_HATA" in hata:
                print("Kullanıcı adı ile şifre aynı olmamalı")

            print("Lütfen Tekrar Giriniz\n")
            continue

        for k in kullanicilar:
            if k["kullaniciadi"] == kullaniciadi:
                print("Kullanıcı adı daha önce kaydolmuş")
                break
        else:
            aktif_ay = dt.datetime.now().strftime("%Y-%m")
            kullanicilar.append({
                "ad": ad,
                "soyad": soyad,
                "kullaniciadi": kullaniciadi,
                "sifre": sifre,
                "gmail": gmail,
                "yas": yas,
                "meslek": meslek,
                "aylik_gelir": aylik_gelir,
                
                "aktif_ay": aktif_ay,
                
                "harcama_arsivi": {
                    aktif_ay: {
                "Mecburi Harcamalar":[],
                "Acil İhtiyaç Harcamaları": [],
                "Yatırım Harcamaları": [],
                "Kişisel Harcamalar": [],
                "Keyfi Harcamalar" : [] 
                    }    
                }
            })
            kullanicilari_kaydet()
            
            break
        
def kullanicilari_yukle():
    global kullanicilar
    try:
        with open("kullanicilar.json", "r", encoding="utf-8") as f:
            kullanicilar = js.load(f)
    except FileNotFoundError:
        kullanicilar = []
        
def kullanicilari_kaydet():
    with open("kullanicilar.json", "w", encoding="utf-8") as f:
        js.dump(kullanicilar, f, ensure_ascii=False, indent=4)
               
def login():
    kullaniciadi = input("Kullanıcı Adı: ")
    sifre = input("Şifre: ")
    gmail = input("Gmail: ")
    
    for k in kullanicilar:
        if k["kullaniciadi"] == kullaniciadi and k["sifre"] == sifre and k["gmail"] ==gmail:
            print("Giriş Başarılı.")
        
            if "harcama_arsivi" not in k:
                ay = dt.datetime.now().strftime("%Y-%m")
                k["aktif_ay"] = ay
                k["harcama_arsivi"] = {
                    ay: {
                    "Mecburi Harcamalar": [],
                    "Acil İhtiyaç Harcamaları": [],
                    "Yatırım Harcamaları": [],
                    "Kişisel Harcamalar": [],
                    "Keyfi Harcamalar": []
                    }
                }
                kullanicilari_kaydet()
            return k
    print("Hatalı Giriş lütfen tekrar deneyiniz veya kayıtlı değilseniz kaydolunuz.")
    return None

def ay_sonu():
    bugun = dt.datetime.now()
    yarin = bugun + dt.timedelta(days= 1)
    return bugun.month != yarin.month ## True or False

def ay_kontrol(kullanici):
    mevcut_ay = dt.datetime.now().strftime("%Y-%m")

    if kullanici["aktif_ay"] != mevcut_ay:
        kullanici["aktif_ay"] = mevcut_ay
        kullanici["harcama_arsivi"][mevcut_ay] = {
            "Mecburi Harcamalar": [],
            "Acil İhtiyaç Harcamaları": [],
            "Yatırım Harcamaları": [],
            "Kişisel Harcamalar": [],
            "Keyfi Harcamalar": []
        }
        kullanicilari_kaydet()

def aylikharcama(kullanici):
    ay_kontrol(kullanici)
    aktif_ay = kullanici["aktif_ay"]
    sec = input("""
          1- Mecburi Harcamalar
          2- Acil İhtiyaç Harcamaları
          3- Yatırım Harcamaları
          4- Kişisel Harcamalar
          5- Keyfi Harcamalar
          **Lütfen 5 Seçenekten Birini Tuşlayınız: 
          
          """)
    
    kategoriler = {
    "1": "Mecburi Harcamalar",
    "2": "Acil İhtiyaç Harcamaları",
    "3": "Yatırım Harcamaları",
    "4": "Kişisel Harcamalar",
    "5": "Keyfi Harcamalar"
}
    
    if sec not in kategoriler:
        print("Hatalı Seçim Yaptınız.")
        return
    
    kategori = kategoriler[sec]
    tutar = float(input("Harcama Tutarınızı Girin: "))
    
    
    tarih = dt.datetime.now().strftime("%Y-%m-%d")
    
    kullanici["harcama_arsivi"][aktif_ay][kategori].append({
        "tarih": tarih,
        "tutar": tutar
        
    })
    
    kullanicilari_kaydet()
    
    print("Harcama başarıyla kaydedildi.")
    
    kategori_yuzdelik(kullanici)
    
    if ay_sonu():
        kategori_toplamlari(kullanici)
        uyariver(kullanici)    

def aylik_toplam_harcama(kullanici):
    aktif_ay=kullanici["aktif_ay"]
    toplama = 0
    
    for kategori in kullanici["harcama_arsivi"][aktif_ay]:
        if kategori == "Yatırım Harcamaları":
            continue
        
        for harcama in kullanici["harcama_arsivi"][aktif_ay][kategori]:
            toplama += harcama["tutar"]
    return toplama

def kategori_toplamlari(kullanici):
    aktif_ay = kullanici["aktif_ay"]
    sonuc = {}
    
    for kategori, harcamalar in kullanici["harcama_arsivi"][aktif_ay].items():
        sonuc[kategori] = sum(h["tutar"] for h in harcamalar)
        
        
    if ay_sonu():
        print("Ay Sonu Harcama Raporunuz: ")
        for k,v in sonuc.items():
            print(f"{k} : {v} TL")
            
    return sonuc

def kategori_yuzdelik(kullanici):
    aktif_ay = kullanici["aktif_ay"]
    gelir = kullanici["aylik_gelir"]

    if gelir == 0:
        print("Gelir girilmediği için yüzdelik hesaplanamaz.")
        return

    print("\n📊 Kategori Bazlı Harcamaların Gelire Oranı:")

    for kategori, harcamalar in kullanici["harcama_arsivi"][aktif_ay].items():
        toplam = sum(h["tutar"] for h in harcamalar)

        yuzde = (toplam / gelir) * 100

        #print(f"- {kategori}: %{yuzde:.1f}")

        
        if kategori == "Keyfi Harcamalar" and yuzde > 20:
            print("DİKKAT: Keyfi harcamalar gelirinizin %20'sini geçti!")

        
        if kategori == "Yatırım Harcamaları" and yuzde < 10:
            print("ÖNERİ: Gelirinizin en az %10'unu yatırıma ayırmanız önerilir.")

def uyariver(kullanici):
    gelir = kullanici["aylik_gelir"]
    toplam = aylik_toplam_harcama(kullanici)
    
    oran = toplam / gelir
    
    if gelir == 0:
        print("Gelir girilmemiştir.")
    
    if oran >= 1:
        print("Gelirinizin TAMAMINI Aştınız!")
        
    elif oran >= 0.8:
        print("Gelirinizin %80'inden fazlasını harcadınız!") 
    else:
        print("Harcamalar kontrol altında!")

    print(f"Toplam Harcama : {toplam} TL / Gelir : {gelir} TL")

def main():
    kullanicilari_yukle()

    aktif_kullanici = None 

    while True:
        
        if not aktif_kullanici:
            secim = input("""
1- Kayıt Ol
2- Giriş Yap
Seçim (1 veya 2): """)

            if secim == "1":
                db()
                print("Kayıt tamamlandı. Şimdi giriş yap.")
                continue

            elif secim == "2":
                aktif_kullanici = login()
                if not aktif_kullanici:
                    print("Giriş başarısız.")
                    continue
            else:
                print("Geçersiz seçim.")
                continue

        
        print(f"\nHoş geldin {aktif_kullanici['ad']}")

        aylikharcama(aktif_kullanici)

        devam = input("Başka harcama eklemek ister misin? (Eklemek İçin (e) - Çıkmak İçin(h) tuşlayınız): ")
        if devam.lower() != "e":
            print("Oturum kapatıldı.")
            aktif_kullanici = None

if __name__ == "__main__":
    motivesozler()
    main()
