# 🚀 Workflow-CI

[![CI](https://github.com/jihankusumaww/Workflow-CI/actions/workflows/ci.yml/badge.svg)](https://github.com/jihankusumaww/Workflow-CI/actions/workflows/ci.yml)

Deskripsi singkat
-----------------
Workflow-CI adalah template repository yang menunjukkan pola terbaik untuk Continuous Integration (CI) menggunakan GitHub Actions. Repositori ini fokus pada automasi langkah build, lint, test, caching dependency, dan publikasi artefak untuk mempercepat feedback loop pengembangan. Cocok sebagai starting point untuk proyek Node.js, Python, Go, atau bahasa lainnya. 🧩✨

Fitur utama
-----------
- ✅ Trigger otomatis pada push dan pull request
- ✅ Matrix build untuk menjalankan job di beberapa versi runtime
- ✅ Caching dependency untuk mengurangi waktu build
- ✅ Linting + unit tests dijalankan di CI
- ✅ Uploading artifacts / test reports (opsional)
- ✅ Contoh konfigurasi .github/workflows/ci.yml untuk referensi

Struktur repo
-------------
- .github/workflows/ci.yml — konfigurasi workflow CI (lihat file ini untuk detail)
- src/ — kode sumber (struktur contoh)
- tests/ — test unit / integrasi
- README.md — dokumentasi (file ini)
- LICENSE — lisensi proyek (jika ditambahkan)

Mengapa pakai workflow ini? 🤔
-----------------------------
- Konsistensi: Semua contributor mendapat environment testing yang sama.
- Kecepatan: Caching dan parallel job mengurangi waktu feedback.
- Keamanan: Rahasia (Secrets) dikelola melalui GitHub, bukan file repo.
- Skalabilitas: Mudah menambah matrix job untuk berbagai versi runtime.

Prasyarat (lokal)
-----------------
- Git
- Bahasa/runtime sesuai proyek (mis. Node.js, Python, Go)
- Pengelola paket (npm/yarn/pnpm, pip, go mod)
- (Opsional) act — menjalankan GitHub Actions secara lokal (https://github.com/nektos/act)

Contoh instruksi menjalankan proyek secara lokal
-----------------------------------------------
Contoh Node.js:
```bash
git clone https://github.com/jihankusumaww/Workflow-CI.git
cd Workflow-CI
npm install
npm run lint
npm test
```

Contoh Python (venv + pytest):
```bash
git clone https://github.com/jihankusumaww/Workflow-CI.git
cd Workflow-CI
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Contoh Go:
```bash
git clone https://github.com/jihankusumaww/Workflow-CI.git
cd Workflow-CI
go test ./...
```

Menjalankan workflow CI secara lokal (opsional)
----------------------------------------------
- Install act: https://github.com/nektos/act
- Jalankan job (ganti nama job sesuai .github/workflows/ci.yml):
```bash
act -j ci
```
Catatan: act bukan pengganti sempurna GitHub-hosted runners tapi berguna untuk debugging cepat.

Penjelasan file workflow (.github/workflows/ci.yml)
--------------------------------------------------
- Trigger: push, pull_request (dapat disesuaikan)
- Jobs umum:
  - checkout: checkout/cek kode
  - setup: setup runtime (setup-node, setup-python, setup-go)
  - install: install dependencies
  - lint: jalankan linter (eslint/flake8/gofmt)
  - test: jalankan unit/integration tests
  - cache: cache dependencies (npm cache, pip cache, go/pkg/mod)
  - upload-artifact: (opsional) unggah hasil test/coverage
- Matrix: jalankan job di beberapa versi runtime (contoh: Node 14/16/18)

Contoh snippet matrix (di workflow):
```yaml
strategy:
  matrix:
    node-version: [14, 16, 18]
```

Tips mengoptimalkan CI ⚡
------------------------
- Cache dependency dengan key yang mencakup file lock (package-lock.json / Pipfile.lock / go.sum).
- Jalankan linting sebelum test agar kegagalan cepat terlihat.
- Split job heavy (build) dan ringan (lint) supaya parallelism optimal.
- Gunakan artifacts untuk menyimpan laporan coverage atau hasil build.

Handling secrets dan environment
--------------------------------
- Jangan letakkan secrets dalam repo.
- Tambahkan Secrets di GitHub: Settings → Secrets and variables → Actions.
- Di workflow, akses secrets via: ${{ secrets.MY_SECRET }}

Badge status CI
--------------
Gunakan badge di bagian atas README untuk menampilkan status workflow. Jika Anda mengganti nama file workflow, perbarui URL badge:
https://github.com/<owner>/<repo>/actions/workflows/<workflow-file>.yml/badge.svg

Troubleshooting umum 🛠️
-----------------------
- Job timed out: tingkatkan timeout atau pecah job jadi lebih kecil.
- Dependency cache conflict: ubah key cache untuk mem-bust cache lama.
- Test lulus lokal tapi gagal di CI: periksa env var, versi runtime, atau dependensi native.
- Permission error: pastikan token / secrets dikonfigurasi untuk akses yang diperlukan.

Cara berkontribusi
------------------
1. Fork repo 🔀
2. Buat branch fitur: feature/<deskripsi-singkat>
3. Commit perubahan dan buka Pull Request ke main
4. Sertakan deskripsi perubahan dan langkah reproduksi bila perlu
5. Pastikan CI lulus sebelum merge ✅

Contoh template commit / PR
- Judul: feat(ci): tambah caching npm untuk job test
- Deskripsi: Menambahkan action cache dengan key berbasis package-lock.json untuk mempercepat instalasi dependency.

Roadmap & ide fitur tambahan
----------------------------
- Menambahkan job linting security (Snyk / Dependabot)
- Matrix OS (ubuntu, windows, macos)
- Auto release artifacts on tag (GitHub Releases)

License
-------
Tambahkan file LICENSE sesuai lisensi yang diinginkan (mis. MIT) di root repository.

Kontak
------
Pemilik repo: @jihankusumaww  
Butuh bantuan penyesuaian CI untuk stack spesifik? Buka issue atau mention saya di PR. 📬

Changelog singkat
-----------------
- v0.1.0 — Template awal workflow CI dengan lint/test/cache dan dokumentasi README.

Catatan akhir ✨
--------------
README ini dibuat sebagai panduan lengkap dan ramah-contributor untuk konfigurasi CI. Sesuaikan perintah dan contoh dengan stack proyek Anda (mis. package manager dan perintah test yang dipakai).
