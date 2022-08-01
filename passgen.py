from random import *
def EngLetters(register):
    a = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    if register == 'up': return choice(a[:26])
    if register == 'low': return choice(a[26:])
    if register == 'uplow': return choice(a)
def RusLetter(register):
    a = [chr(i) for i in range(1040, 1105 + 1)]
    a.insert(5, 'Ё')
    a.insert(39, 'ё')
    if register == 'up': return choice(a[:33])
    if register == 'low': return choice(a[33:])
    if register == 'uplow': return choice(a)

def PassGen(language, len, register):
    GenPassword = ''
    for i in range(len):
        Digit_or_Letter = randint(0, 2)
        if Digit_or_Letter:
            GenPassword += str(randint(0, 10))
        else:
            if language == 'rus':
                GenPassword += RusLetter(register)
            elif language == 'eng':
                GenPassword += EngLetters(register)
            else:
                if randint(0, 2):
                    GenPassword += RusLetter(register)
                else:
                    GenPassword += EngLetters(register)
    print(f'Вот твой пароль: {GenPassword}')

print("Привет! Меня зовут PassGenerator, я сгенерирую тебе пароль!", "Какой язык будет использоваться? Напиши: 'rus', если русский, 'eng' - если нужен английский, иначе 'ruseng', если нужно и то, и то", sep = '\n')
lang = input()
print("Какой длины будет пароль?")
lenght = int(input())
print("Буквы заглавные или строчные? Напиши 'up', если нужны заглавные, 'low' - если нужны строчные, иначе 'uplow', чтобы и то, и то")
register = input()
PassGen(lang, lenght, register)