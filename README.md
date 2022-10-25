# P1_Komnum_B10

## Nama Anggota Kelompok 10 :

- M. Dafian Zaki Akhdan &ensp;&ensp;&ensp;&ensp;&nbsp; - 5025211108
- Dewangga Dika Darmawan &nbsp; - 5025211109
- Urdhanaka Aptanagi &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&nbsp; - 5025211123

<br >

## Screenshot & Penjelasan :

```python
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
```

Disini kami menggunakan 3 library yaitu matplotlib dan numpy untuk membuat grafik dari fungsi, kemudian tabulate untuk membuat tabel dari array data yang telah didapat.

<br >

```python
function = input("function : ")
a = input("lower root boundary: ")
b = input("upper root boundary: ")
iteration = input("how many iteration: ")

x = np.linspace(-10,10,num = 1000)
y = eval(function)
plt.plot(x, y)
plt.show()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

bolzano_method(function, float(a), float(b), float(iteration))
```

Input yang diminta adalah `function`, `lower root boundary`, `upper root boundary`, dan `iteration`. function yang diminta adalah fungsi dalam bentuk python, misal kita menginginkan fungsi $x^3 + x^2 - 3x - 3$ maka kita menginputkan `(x ** 3) + (x ** 2) - (3 * x) - 3`. Lalu untuk lower root boundary dan upper root boundary merupakan akar dari fungsi yang terletak diantara batas atas dan batas bawah. Kemudian untuk iteration merupakan berapa banyak iterasi kita ingin inginkan dalam menghitung akar persamaan menggunakan bolzano. Pertama kita buat grafik dari fungsi menggunakan library `matplotlib`, kemudian akan memanggil fungsi `bolzano_method`.

<br >

```python
def bolzano_method(func, a, b, iteration):
    i = 1
    ite = int(iteration)
    def f(x):
        f = eval(func)
        return f

    data = [['iterasi', 'x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']]
    while iteration > 0:
        c = (b+a)/2
        data.append([i,a,b,c,f(a),f(b),f(c)])
        i = i + 1
        if f(a) * f(b) >= 0:
            print("No root or multiple roots present")
            quit()

        elif f(c) * f(a) < 0:
            b = c

        elif f(c) * f(b) < 0:
            a = c
        else:
            print("Error happens")
            quit()
        ans = (b+a)/2
        iteration -= 1


    print(tabulate(data, headers="firstrow", tablefmt="github"))

    print(f"The lower boundary is {a} and upper boundary is {b}")
    print(f"The root after {ite} iteration is {ans}")
```

Pertama ada fungsi `eval()` yang berfungsi untuk mengubah fungsi input tadi dari string menjadi python expression. Lalu ada array `data` yang menampung semua hasil iterasi bolzano. Selanjutnya akan masuk loop dengan total iterasi yang diinputkan, pada loop ini akan dilakukan perhitungan bolzano. pertama `a` merupakan lower root boundary, `b` merupakan upper root boundary, dan `c` adalah hasil dari (a+b)/2. Selanjutnya masuk ke percabangan yang mana jika `f(c) * f(a) < 0` maka `b = c` atau jika `f(c) * f(b) < 0` maka `a = c`. Proses ini dilanjut hingga iterasi selesai, kemudian hasil pada tiap iterasi akan di append kedalam array data. Setelah loop selesai maka array data akan dioutputkan untuk tiap iterasi dan di outputkan juga `lower root boundary`, `upper root boundary`, dan `root` setelah iterasi.

<br >

Contoh Input dan Output :

![image](https://user-images.githubusercontent.com/91055469/197852694-bd637101-594f-4d17-9e24-fdef5cd74c0c.png)
