# SecondChance

SecondChance adalah platform e-commerce yang menjual barang preloved dengan fokus pada keberlanjutan dan penghematan.

## tugas 2

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
