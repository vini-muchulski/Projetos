""""

Maximum Number of Vowels in a Substring of Given Length - Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

"""
palavra = "aabciiidef"

vogais = {
    "a": 0, "e": 0, "i": 0, "o": 0, "u": 0,
}


for letra in palavra:
    if(letra in vogais.keys()):
        vogais[letra] +=1

print(vogais)