"""
================================================
BACKEND — Logika Queue & Audio
File    : logic.py
Dikerjakan oleh: Farhan & Naila
================================================
"""

from gtts import gTTS
from datetime import datetime
import os
import tempfile
import base64

MENIT_PER_PELANGGAN = 5   # asumsi 1 pelanggan dilayani dalam 5 menit


# ─────────────────────────────────────────────
# CLASS NODE
# Menyimpan data pelanggan + timestamp masuk
# ─────────────────────────────────────────────

class Node:
    def __init__(self, nama: str, pesanan: str):
        self.nama         = nama
        self.pesanan      = pesanan
        self.waktu_masuk  = datetime.now()   # timestamp saat enqueue
        self.next         = None             # pointer ke node berikutnya


# ─────────────────────────────────────────────
# CLASS QUEUE (User-Defined)
# Implementasi manual menggunakan Linked List
# FIFO: enqueue dari rear, dequeue dari front
# ─────────────────────────────────────────────

class Queue:
    def __init__(self):
        self.head  = None   # pointer ke depan (front)
        self.tail  = None   # pointer ke belakang (rear)
        self._size = 0

    def enqueue(self, nama: str, pesanan: str):
        """Tambah node baru ke belakang antrian. O(1)"""
        node = Node(nama, pesanan)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def dequeue(self) -> dict | None:
        """Hapus & ambil node dari depan antrian. O(1)"""
        if self.is_empty():
            return None
        data = {
            "nama": self.head.nama,
            "pesanan": self.head.pesanan,
            "waktu_masuk": self.head.waktu_masuk,
        }
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return data

    def front(self) -> dict | None:
        """Lihat node paling depan tanpa menghapus."""
        if self.is_empty():
            return None
        return {"nama": self.head.nama, "pesanan": self.head.pesanan,
                "waktu_masuk": self.head.waktu_masuk}

    def rear(self) -> dict | None:
        """Lihat node paling belakang tanpa menghapus."""
        if self.is_empty():
            return None
        return {"nama": self.tail.nama, "pesanan": self.tail.pesanan,
                "waktu_masuk": self.tail.waktu_masuk}

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def to_list(self) -> list:
        """Traversal seluruh antrian → kembalikan sebagai list."""
        result, current = [], self.head
        while current:
            result.append({
                "nama": current.nama,
                "pesanan": current.pesanan,
                "waktu_masuk": current.waktu_masuk,
            })
            current = current.next
        return result

    def reset(self):
        self.head = self.tail = None
        self._size = 0


# ─────────────────────────────────────────────
# FUNGSI ESTIMASI WAKTU TUNGGU
# ─────────────────────────────────────────────

def estimasi_tunggu(posisi: int) -> str:
    """
    Hitung estimasi waktu tunggu berdasarkan posisi antrian.
    posisi 0 = depan (segera dipanggil).
    """
    menit = posisi * MENIT_PER_PELANGGAN
    if menit == 0:
        return "Segera dipanggil"
    return f"± {menit} menit"


# ─────────────────────────────────────────────
# FUNGSI AUDIO (gTTS)
# ─────────────────────────────────────────────

def buat_audio(teks: str) -> str:
    """Generate MP3 dari teks, kembalikan sebagai base64 string."""
    tts = gTTS(text=teks, lang="id")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        tmp_path = tmp.name
    with open(tmp_path, "rb") as f:
        audio_bytes = f.read()
    os.remove(tmp_path)
    return base64.b64encode(audio_bytes).decode()
