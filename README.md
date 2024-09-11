# SecondChance

SecondChance adalah platform e-commerce yang menjual barang preloved dengan fokus pada keberlanjutan dan penghematan.

## tugas 2

### tautan ke aplikasi

`http://makarim-zufar-secondchance.pbp.cs.ui.ac.id/`

### membuat project django baru dan install semua requirements

saya membuat project di direktori yang saya tentukan, lalu saya menjalankan perintah untuk membuat virtual environtment

```bash
python -m venv env
```

lalu mengaktifkan virtual environtment dengan command

```bash
env/Sripts/Scripts/activate.bat
```

setelah terbentuk folder env saya akan memastikan ulang apakah requirements sudah terinstal maka saya membuat file bernama requirements.txt di file yang sama berisi

```txt
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

lalu menjalankan perintah ini untuk menginstall semua yang tertulis di requirements.txt

```bash
pip install -r requirements.txt
```

lalu saya menjalankan perintah untuk membuat project

```bash
django-admin startproject SecondChance .
```

### membuat aplikasi main pada project

untuk membuat project baru saya mengetikan command berikut

```bash
python manage.py startapp main
```

### melakukan routing pada proyek agar dapat menjalankan main

setelah saya berhasil membuat aplikasi main, saya melakukan routing pada SecondChance agar bisa berjalan di `setting.py`
![Installed Apps](images_readme/routing_main_apps.png)

### membuat models

untuk model saya membuat dengan 5 varibel:
model memiliki beberapa atribut sebagai berikut:

- `name` dengan tipe `CharField`.
 Atribut itu akan menjelaskan nama dari model

- `description` dengan tipe `TextField`.
 Atribut itu akan menjelaskan deskripsi dari model

- `price` dengan tipe `IntegerrField`.
 Atribut itu akan menjelaskan harga dari model

- `stock` dengan tipe `IntegerField`.
 Atribut itu akan menjelaskan ketersediaan dari model

- `category` dengan tipe `CharField`.
 Atribut itu akan menjelaskan kelompok/kategori dari model

setelah itu saya melakukan migrate agar semua perubahan dapat diterapkan:

```python
python manage.py makemigrations
python manage.py migrate
```

### membuat fungsi `show_main` pada `views.py` untuk dikembalikan ke dalam template HTML

```pyhton
from django.shortcuts import render
from .models import Product

def show_main(request):
    context = {
        "products":[
            {
                "nama": "Makarim Zufar Prambudyo",
                "npm": "2306241751",
                "kelas": "PBP D",
            }
        ]
    }
    return render(request, 'main.html', context)  
```

pada context yang berupa dict saya membuat sebuah dict bernama product yang nantinya akan di panggil di HTML

### membuat routing pada `urls.py`

Pada langkah ini Saya membuat `urls.py` pada direktori aplikasi `main` dan gunanya untuk memetakan fungsi yang telah dibuat pada `views.py` tadi.

```pyhton
from django.urls import path
from main.views import show_main

app_name = "main"

urlpatterns = [
    path('', show_main, name="show_main"),
]
```

Di dalam fungsi `path`, Saya membuat parameter pertama sebagai `''` supaya halaman aplikasi tersebut muncul pada halaman utama localpath. Parameter kedua berisikan fungsi yang telah dibuat pada `views.py` dan parameter `name` adalah untuk pengakses fungsi tersebut.

selain itu saya juga melakukan routing pada `urls.py` yang ada pada folder proyek yaitu SecondChance agar bisa terhubung

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]
```

### persiapan upload ke pws

untuk allowed host di `setting.py` saya setting agar bisa di akses juga oleh pws

```python
ALLOWED_HOSTS = ["localhost","127.0.0.1","makarim-zufar-SecondChance.pbp.cs.ui.ac.id"]
```

### bagan yang berisi request client ke web

![flowchart](images_readme/Flowchart.png)

### fungsi git

Git dalam Pengembangan Perangkat Lunak
Git adalah sistem pengontrol versi terdistribusi yang berfungsi untuk melacak perubahan kode sumber selama pengembangan perangkat lunak. Sistem ini sangat penting untuk kolaborasi tim dan pengelolaan kode dalam proyek perangkat lunak.

Fungsi Utama Git

1.Pelacakan Perubahan (Version Control)
Git melacak setiap perubahan yang dilakukan pada kode. Setiap kali perubahan dikomit, Git menyimpan snapshot dari keadaan proyek saat itu. Ini memungkinkan pengembang untuk melihat riwayat perubahan, termasuk siapa yang mengubah apa dan kapan.

2.Kolaborasi Tim
Git memungkinkan kolaborasi antara banyak pengembang. Setiap pengembang dapat bekerja di cabang (branch) mereka sendiri tanpa mengganggu pekerjaan orang lain. Setelah perubahan siap, mereka bisa digabungkan (merge) ke cabang utama. Ini sangat membantu dalam proyek-proyek besar di mana banyak orang bekerja pada fitur yang berbeda.

3.Branching dan Merging
Fitur branching Git memungkinkan pengembang membuat jalur kerja paralel untuk berbagai fitur atau perbaikan bug. Setiap cabang bisa dikembangkan secara terpisah dan digabungkan kembali ke cabang utama setelah selesai, membantu menjaga stabilitas kode utama.

4.Revisi dan Rollback
Git memungkinkan pengembang untuk kembali ke versi kode sebelumnya jika ada masalah. Jika ditemukan bug atau masalah pada fitur baru, pengembang dapat dengan mudah membatalkan perubahan atau memperbaikinya dengan melihat riwayat perubahan.

5.Distribusi Kode
Git adalah sistem terdistribusi, yang berarti setiap pengembang memiliki salinan lengkap dari seluruh repositori di komputer mereka. Ini memungkinkan pekerjaan offline dan sinkronisasi perubahan ketika koneksi tersedia.

6.Integrasi dengan Platform CI/CD
Git terintegrasi dengan berbagai alat Continuous Integration/Continuous Deployment (CI/CD) seperti Jenkins, GitLab CI, dan GitHub Actions. Ini memungkinkan pengujian otomatis dan penerapan kode secara cepat dan berulang setiap kali ada perubahan di repositori.

7.Penyimpanan Aman
Git menyimpan semua perubahan dengan aman di repositori, memastikan bahwa data kode selalu terjaga. Ini juga mengurangi risiko kehilangan data atau kesalahan kode yang disebabkan oleh perubahan yang tidak disengaja.

8.Pengembangan Open Source
Git sangat populer di komunitas open source dan digunakan pada platform seperti GitHub, GitLab, dan Bitbucket. Pengembang di seluruh dunia dapat berkolaborasi pada proyek besar, mengirim pull request, dan melakukan review kode.

9.Integrasi dengan Manajemen Proyek
Git terintegrasi dengan alat manajemen proyek seperti Jira dan Trello, memungkinkan setiap perubahan kode terkait langsung dengan tugas atau masalah spesifik, sehingga memudahkan pelacakan kemajuan proyek.

### kenapa django di pilih sebagai media pembelajaran

Django sering dipilih sebagai framework pertama untuk dipelajari dalam pengembangan perangkat lunak, terutama untuk pengembangan web, karena beberapa alasan berikut:

1. Django Mengikuti Prinsip "Batteries-Included"
Django menyediakan banyak fitur bawaan yang memudahkan pengembang dalam membangun aplikasi web tanpa harus mencari atau mengonfigurasi banyak alat tambahan. Fitur-fitur seperti otentikasi pengguna, pengelolaan database, routing URL, dan template rendering semuanya sudah ada sejak awal. Ini membantu pemula memahami konsep-konsep dasar pengembangan web secara lebih komprehensif tanpa harus memikirkan integrasi komponen tambahan.

2. Mendukung Pembelajaran Secara Bertahap
Django mempromosikan struktur kode yang terorganisir dan mendukung pemisahan tanggung jawab antara logika aplikasi, presentasi, dan data. Ini membantu pemula memahami MVC/MVT (Model-View-Controller/Model-View-Template) dengan baik. Pengembang pemula dapat melihat bagaimana setiap bagian aplikasi bekerja sama tanpa bingung dengan arsitektur yang rumit.

3. Fokus pada Keamanan
Django memiliki banyak fitur keamanan bawaan untuk membantu pengembang menghindari kesalahan umum yang sering terjadi pada aplikasi web. Misalnya, Django melindungi dari serangan SQL Injection, Cross-Site Scripting (XSS), dan Cross-Site Request Forgery (CSRF). Dengan belajar Django, pengembang pemula juga belajar untuk mengutamakan keamanan sejak awal dalam pengembangan perangkat lunak.

4. Dokumentasi yang Luar Biasa
Dokumentasi Django sangat lengkap dan ramah pengguna, membuatnya ideal untuk pengembang pemula. Ini termasuk tutorial yang mendetail serta penjelasan yang baik untuk setiap fitur. Dokumentasi ini membantu pelajar memahami cara membangun aplikasi nyata, mulai dari hal-hal sederhana hingga yang lebih kompleks.

5. Komunitas yang Besar dan Aktif
Django memiliki komunitas yang besar dan sangat aktif. Dengan banyaknya tutorial, forum, dan dokumentasi komunitas, pemula memiliki banyak sumber daya untuk mendapatkan dukungan saat belajar. Django juga sering diperbarui oleh komunitas, memastikan bahwa framework ini tetap relevan dan sesuai dengan perkembangan teknologi terbaru.

6. Konsep DRY (Don't Repeat Yourself)
Django mengikuti prinsip DRY yang mendorong pengembang untuk menulis kode yang lebih efisien dan tidak mengulangi hal yang sama berkali-kali. Bagi pemula, ini membantu memahami pentingnya reusabilitas kode dan manajemen proyek yang lebih baik.

7. Kemudahan Integrasi dengan Teknologi Lain
Django mudah diintegrasikan dengan berbagai teknologi seperti PostgreSQL, MySQL, SQLite, Redis, dan banyak lagi. Ini memungkinkan pengembang pemula untuk mempelajari cara kerja berbagai sistem basis data dan teknologi lainnya dalam konteks pengembangan web.

8. Berbasis Python
Django dibangun menggunakan Python, salah satu bahasa pemrograman yang paling mudah dipelajari dan terstruktur dengan baik. Karena Python banyak digunakan di dunia pemrograman (termasuk dalam pengembangan perangkat lunak, data science, dan kecerdasan buatan), belajar Django membantu pemula memahami Python lebih mendalam sambil mengaplikasikannya pada proyek web.

9. Cepat untuk Membuat Prototipe
Django memudahkan pengembang untuk membuat prototipe aplikasi dengan cepat. Dalam waktu singkat, pemula bisa membangun aplikasi web dasar yang berfungsi penuh, yang memotivasi mereka untuk terus belajar dan mengembangkan proyek-proyek yang lebih kompleks.

10. Populer di Industri
Banyak perusahaan besar, termasuk Instagram, Pinterest, Mozilla, dan Disqus, menggunakan Django. Dengan belajar Django, pemula mendapatkan keterampilan yang relevan dengan dunia industri, yang bisa membuka peluang kerja atau pengembangan karir di masa depan.

### Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk menghubungkan dan memetakan antara objek di dalam kode Python dengan tabel di dalam basis data relasional. ORM bertujuan untuk menghindari penulisan langsung query SQL dengan menggunakan bahasa pemrograman Python, yang lebih mudah dipahami dan digunakan oleh pengembang.
