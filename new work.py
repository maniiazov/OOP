flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue', 'yellow'},
    'ch': {'red', 'yellow'},
    'jp': {'white', 'red'},
    'fr': {'blue', 'white', 'red'}
}  

while True:
    Gad = input("\nВведите цвет на Англ,да по братски (или 'exit' для выхода из мощной игры по цветам): ").lower().strip()
    
    if Gad == 'exit':
        print('Конец игры (хахахахха)')
        break

    colors = set(Gad.split())
    result = [domain for domain, flag_colors in flags.items() if colors.issubset(flag_colors)]

    if result:
        print("Такой цвет есть у доменов:", ", ".join(result))
    else:
        print("Такого цвета нет")

