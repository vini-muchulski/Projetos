nota_1 = float(input("Qual a primeira nota? "))
nota_2 = float(input("Qual a segunda nota? "))

media = (nota_1+nota_2)/2



if 5<=media<7:
    print("Você ficou de RECUPERAÇÃO! Sua média foi {:.1f}".format(media))

elif 7<=media:
    print("Você foi APROVADO! Sua média foi {:.1f}".format(media))

else:
    print("Você foi REPROVADO! Sua média foi {:.1f}".format(media))