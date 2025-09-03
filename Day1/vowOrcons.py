#vowel or consonant check
def vowOrcons(a):
    return (a=='a' or a=='e' or a=='i' or a=='o' or a=='u')
x=input().lower()
if vowOrcons(x):
    print(f'{x} is a vowel')
else:
    print(f'{x} is not a vowel')