# Argumenty przyjmujące tekst i klucz który definiuje o ile zmieniają się litery
def Cezar(tekst: str, klucz: str) -> str:
    rezultat = ""
    #Ogranicza wartość klucza
    klucz = klucz % 26
    # Przechodzimy po każdym znaku w tekście
    for litera in tekst:
        # Jeśli znak jest małą literą
        if 'a' <= litera <= 'z':
            # Zmienia literę na jej numer w alfabecie, przesuwa go o wartość klucz,
            # zwija wynik w zakresie 0-25, a następnie przekstałca z powrotem na znak i dopisuje do wyniku
            rezultat += chr((ord(litera) - ord('a') + klucz) % 26 + ord('a'))
        # Jeśli znak jest dużą literą:
        elif 'A' <= litera <= 'Z':
            #Anlalogicznie to samo tylko dla dużych liter
            rezultat += chr((ord(litera) - ord('A') + klucz) % 26 + ord('A')) #
        else:
            # Jeśli znak nie jest literą to go nie szyfrujemy tylko dodajemy do wyniku bez zmian
            rezultat += litera
    return rezultat

if __name__ == '__main__':
    print(Cezar("abc", 2))