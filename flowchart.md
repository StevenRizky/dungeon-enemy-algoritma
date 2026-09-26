# Flowchart Enemy AI

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

## Keterangan
- Deteksi: mencari posisi Enemy dan Player.
- Jangkauan: menggunakan Manhattan Distance.
- Pathfinding: menggunakan Breadth-First Search (BFS).
- Movement: Enemy mengambil posisi berikutnya dari jalur BFS.