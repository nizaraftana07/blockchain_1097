import hashlib
import time
from datetime import datetime, timezone


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = prev_hash
        self.hash = self.calculate_hash()

    @property
    def timestamp_readable(self):
        # Konversi timestamp UNIX ke format tanggal lokal yang mudah dibaca
        dt = datetime.fromtimestamp(self.timestamp, tz=timezone.utc)
        return dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

    def calculate_hash(self):
        # Menggabungkan seluruh data blok menjadi satu string untuk di-hash dengan SHA-256
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Blok pertama dalam blockchain (Genesis Block)
        genesis_block = Block(
            1, "Genesis Block — Inisialisasi Ledger RoastChain", "0"
        )
        self.chain.append(genesis_block)

    def add_block(self, data):
        # Mengambil blok terakhir sebagai acuan hash sebelumnya
        last_block = self.chain[-1]
        new_block = Block(last_block.index + 1, data, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Memeriksa validitas setiap blok dari blok ke-2 hingga akhir
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1. Cek apakah isi data atau hash blok saat ini telah diubah
            if current_block.hash != current_block.calculate_hash():
                return False

            # 2. Cek apakah pointer previous_hash cocok dengan hash blok sebelumnya
            if current_block.previous_hash != previous_block.hash:
                return False

        return True