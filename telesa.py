#!/usr/bin/env python3

print ("1-objem, 2-obsah, 3-obvod")
vypocet = int (input("Co chcete počítat?"))

if vypocet == 1:
    print ("1-krychle, 2-kvádr, 3-koule")
    objem = int (input("Vyberte těleso: "))
    if objem == 1:
        a = float (input ("Délka hrany krychle: "))
        vkrychle = a*a*a
        print (vkrychle)
    if objem == 2:
        a = float (input ("Délka hrany a: "))
        b = float (input ("Délka hrany b: "))
        c = float (input ("Délka hrany c: "))
        vkvadru = a*b*c
        print (vkvadru)
    if objem == 3:
        r = float (input ("Poloměr koule: "))
        vkoule = 4/3*3.1415*r*r*r
        print (vkoule)

if vypocet == 2:
    print ("1-čtverec, 2-obdélník, 3-kruh")
    obsah = int (input ("Vyberte tvar: "))
    if obsah == 1:
        a = float (input ("Délka hrany čtverce:"))
        sctverce = a*a
        print (sctverce)
    if obsah == 2:
        a = float (input ("Délka hrany a: "))
        b = float (input ("Délka hrany b: "))
        sobdelniku = a*b
        print (sobdelniku)
    if obsah == 3:
        r = float (input ("Poloměr kruhu: "))
        skruhu = 3.1415*r*r
        print (skruhu)

if vypocet == 3:
    print ("1-čtverec, 2-obdélník, 3-kruh")
    obvod = int (input ("Vyberte tvar: "))
    if obvod == 1:
        a = float (input ("Délka hrany čtverce:"))
        octverce = 4*a
        print (octverce)
    if obvod == 2:
        a = float (input ("Délka hrany a: "))
        b = float (input ("Délka hrany b: "))
        oobdelniku = 2 * (a+b)
        print (oobdelniku)
    if obvod == 3:
        r = float (input ("Poloměr kruhu: "))
        okruhu = 3.1415*r*2
        print (okruhu)
