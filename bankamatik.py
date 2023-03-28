halilHesap ={
    'ad' : 'Halil Orak',
    'hesapNo' : '1236546',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

mucoHesap ={
    'ad' : 'Mücahit Orak',
    'hesapNo' : '1236897',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
        hesapSorgula(halilHesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if toplam >= miktar:
            ekHesapkullanimi = input('ek hesap kullanmak ister misiniz ?(evet/hayır): ')
            if ekHesapkullanimi == 'evet':
                ekhesapKullanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakmiktar
                print('paranızı alabilirsiniz')
                hesapSorgula(halilHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} miktar para vardır.")
        else:
            print('yetersiz bakiye')
            hesapSorgula(halilHesap)

def hesapSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır ve ek hesabınızda {hesap['ekHesap']} tl bulunmaktadır.")

    
paraCek(halilHesap,3000)

paraCek(halilHesap,2000)
