# P1_Komnum_E10

## Nama Anggota Kelompok 10 :

- M. Dafian Zaki Akhdan &ensp;&ensp;&ensp;&ensp;&nbsp; - 5025211108
- Dewangga Dika Darmawan &nbsp; - 5025211109
- Urdhanaka Aptanagi &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&nbsp; - 5025211123

<br >

## Screenshot & Penjelasan :

![image](https://user-images.githubusercontent.com/91055469/197847234-c9ef9113-439a-45e0-b815-74d9a2cf43ad.png)

Input yang diminta adalah `function`, `lower root boundary`, `upper root boundary`, dan `iteration`. function yang diminta adalah fungsi dalam bentuk python, misal kita menginginkan fungsi $x^3 + x^2 - 3x - 3$ maka kita menginputkan `(x ** 3) + (x ** 2) - (3 * x) - 3`. Lalu untuk lower root boundary dan upper root boundary merupakan akar dari fungsi yang terletak diantara batas atas dan batas bawah. Kemudian untuk iteration merupakan berapa banyak iterasi kita ingin inginkan dalam menghitung akar persamaan menggunakan bolzano. Pertama kita buat grafik dari fungsi menggunakan library `matplotlib`, kemudian akan memanggil fungsi `bolzano_method`.

<br >

![image](https://user-images.githubusercontent.com/91055469/197848859-9a62a1c3-b6ed-46c1-861a-afcdebc2d955.png)

Pertama ada fungsi `eval()` yang berfungsi untuk mengubah fungsi input tadi dari string menjadi python expression. Lalu ada array `data` yang menampung semua hasil iterasi bolzano. Selanjutnya akan masuk loop dengan total iterasi yang diinputkan, pada loop ini akan dilakukan perhitungan bolzano, kemudian hasilnya akan di append kedalam array data. Setelah loop selesai maka array data akan dioutputkan untuk tiap iterasi dan di outputkan juga `lower root boundary` dan `upper root boundary` setelah iterasi.

<br >

Contoh Input dan Output :

![image](https://user-images.githubusercontent.com/91055469/197850548-05d6cb41-ef0f-4822-b541-f1b08e25a698.png)
