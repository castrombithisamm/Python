def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bounjour'
    else:
        return 'Hello'

print (greet('es'), 'Glen')
print(greet('fr'), 'Josh')
print(greet('en'), 'Kalenjin')
