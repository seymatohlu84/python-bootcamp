from collections import Counter

def cift_toplam(liste):
    toplam=0
    for sayi in liste:
        if sayi%2==0:
            toplam=toplam+sayi
    return toplam

print(cift_toplam([1,2,3,4]))


def kelime_say(cumle):
    sozluk={}
    for kelime in cumle.split():
        if kelime in sozluk:
            sozluk[kelime]=sozluk[kelime]+1
        else:
            sozluk[kelime]=1
    return sozluk

print(kelime_say("ali ata bak ali"))

def en_sik(liste):
    sayac= {}
    for eleman in liste:
        if eleman in sayac:
            sayac[eleman]=sayac[eleman]+1
        else:
            sayac[eleman]=1
    en_sik_eleman = None
    en_buyuk_sayi = 0
    for eleman in sayac:
        if sayac[eleman]> en_buyuk_sayi:
            en_buyuk_sayi=sayac[eleman]
            en_sik_eleman=eleman
    return en_sik_eleman
print(en_sik([1,2,2,3]))

print (Counter("ali ata bak ali".split()))
print (dict(Counter("ali ata bak ali".split())))
print(Counter([1,2,2,3]))
print(dict(Counter([1,2,2,3])))
print(Counter([1,2,2,3]).most_common(1))
print(dict(Counter([1,2,2,3]).most_common(1)))
print(Counter([1, 2, 2, 3]).most_common(1)[0][0])
print(Counter([1,2,2,3]).most_common(2))
