
# f(x) fonksiyonunun tanımlayalım
def f(x):
    return x**4 - 4*x

# Riemann toplamını hesaplayan fonksiyon
def riemann(a, b, n):
    # Δx hesaplanması
    delta_x = (b-a)/n
    result = 0
    # Her dikdörtgen için result değişkeninin güncellenmesi
    for i in range(n):
        result += f(a + i*delta_x)*delta_x
    # Sonuç olarak result değişkeninin döndürülmesi
    return result

# Kullanıcıdan a, b ve n değerlerinin alınması
a = int(input("a değeri: "))
b = int(input("b değeri: "))
n = int(input("n değeri: "))
# Riemann toplamının hesaplanması
result = riemann(a, b, n)
# Sonuçun 4 basamaklı virgülden sonra sayılarla yazdırılması
print("Sonuç: {:.4f}".format(result))
