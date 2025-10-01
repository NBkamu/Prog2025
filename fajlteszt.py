try:
    with open("F1-2024dec.csv" ,encoding="utf-8") as fajl:
        n = 4 / 0
        f = fajl.read()
    print(f)
    print(n)
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")
except ZeroDivisionError:
    print("Ne ossz 0-val!")
except Exception:
    print("Halihóóóó!")
print("Itt a program vége!")
