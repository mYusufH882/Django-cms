# webcms
Web blog sederhana untuk mengelola konten dengan framework django

# Installasi atau setup projek
1. Buat sebuah direktori kosong 
2. Buat virtual environment dengan perintah : <code>python3 -m venv env</code>
3. kloning aplikasi : git clone <link_github_repository>
4. masuk kedalam proyek yang sudah dibuat : <code>cd webcms/</code>
5. pindah branch main ke master dengan perintah : <code>git checkout master</code>
6. lalu jalankan perintah : <code>pip install -r requirements.txt</code>
7. buat database dan sesuaikan nama database pada file settings.py di webcms/webcms/settings.py
8. lalu jalankan perintah : <code>./manage.py runserver</code>

Jika langkah diatas berhasil dijalankan silahakan akses:
1. Halaman Admin : http://127.0.0.1:8000/admin/
2. Halaman User : http://127.0.0.1:8000/blog/
