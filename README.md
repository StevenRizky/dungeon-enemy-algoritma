# Dungeon Enemy Algoritma

Nama: Ananda Rizky Muntazar Muthahhari

Tugas algoritma Enemy pada dungeon

## 1. Identifikasi Algoritma

Algoritma yang digunakan adalah **Breadth-First Search (BFS)** untuk mencari jalur terpendek dari Enemy menuju Player pada dungeon berbentuk grid

Proses :
1. Enemy mendeteksi posisi Player
2. Program menghitung jarak Enemy dengan Player
3. Jika Player berada dalam jangkauan, Enemy mencari jalur
4. BFS mencari jalur yang dapat dilewati tanpa melewati dinding
5. Jika jalur ditemukan, Enemy bergerak satu langkah menuju Player
6. Jika Player di luar jangkauan atau tidak ada jalur, Enemy tetap diam

BFS cocok digunakan karena dungeon pada contoh ini berbentuk grid dan setiap langkah memiliki biaya yang sama

## 2. Flowchart

```text
START
  |
  v
Deteksi posisi Enemy dan Player
  |
  v
Apakah Player dalam jangkauan?
  |
  +---- TIDAK ----> Enemy diam
  |
  +---- YA -------> Cari jalur dengan BFS
                         |
                         v
                  Apakah jalur ditemukan?
                         |
                 +-------+-------+
                 |               |
                TIDAK            YA
                 |               |
                 v               v
             Enemy diam     Enemy bergerak
                              menuju Player
                 |               |
                 +-------+-------+
                         |
                         v
                        END
```
<img width="656" height="1015" alt="flowchart" src="https://github.com/user-attachments/assets/731674dd-11e8-4e0c-9e61-530ca8df1cea" />

## 3. Code Snippet Python

Implementasi lengkap terdapat pada file `enemy_ai.py`.

### Cara menjalankan

```bash
python enemy_ai.py
```

## 4. Game Map

```text
        x
      0 1 2 3 4 5 6 7
    +-----------------
y 0 | # # # # # # # #
y 1 | # E . . . . . #
y 2 | # . # # # . . #
y 3 | # . . . # P . #
y 4 | # # # # # # # #
```

## Struktur Project

- `README.md` - Penjelasan tugas dan flowchart
- `enemy_ai.py` - Implementasi algoritma menggunakan Python
- `flowchart.md` - Flowchart dan keterangan algoritma
