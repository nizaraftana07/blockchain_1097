import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # ATRIBUT BARU: Angka tebakan miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # ATRIBUT BARU: nonce ikut dimasukkan ke dalam perhitungan hash
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Membuat target awalan nol, misal difficulty 3 -> "000"
        target = "0" * difficulty

        # Looping (PoW): Terus tebak nonce sampai hash diawali dengan "000"
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Block Mined! Nonce: {self.nonce} | Hash: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3  # ATRIBUT BARU: Tingkat kesulitan mining

    def create_genesis_block(self):
        return Block(0, "Genesis Block - Rantai Dimulai", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        # ATRIBUT BARU: Panggil fungsi mining sebelum blok ditambahkan ke rantai
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Fungsi untuk mengecek apakah ada data yang dimanipulasi
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # 1. Cek apakah hash block saat ini masih valid (data tidak diubah)
            if current_block.hash != current_block.calculate_hash():
                return False

            # 2. Cek apakah pointer ke block sebelumnya masih akurat
            if current_block.previous_hash != previous_block.hash:
                return False

        return True