class Node:
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.first_child = None
        self.next_sibling = None


class OrganizationTree:

    def __init__(self, root):
        self.root = root

    # Memeriksa ID pegawai agar tidak duplikat
    def _contains_id(self, node, id_pegawai):

        if node is None:
            return False

        if node.id_pegawai == id_pegawai:
            return True

        return (
            self._contains_id(node.first_child, id_pegawai)
            or
            self._contains_id(node.next_sibling, id_pegawai)
        )

    # Operasi pencarian pegawai
    def search_node(self, keyword):

        keyword = keyword.strip().lower()

        if not keyword:
            return None

        def _search(node):

            if node is None:
                return None

            if (keyword in node.nama.lower()
                or keyword in node.jabatan.lower()):

                return node

            hasil = _search(node.first_child)

            if hasil is not None:
                return hasil

            return _search(node.next_sibling)

        return _search(self.root)

    # Operasi penambahan pegawai
    def insert_node(self, nama_atasan, id_pegawai, nama, jabatan):

        if self._contains_id(self.root, id_pegawai):
            print("Gagal: ID pegawai sudah digunakan.")
            return False

        atasan = self.search_node(nama_atasan)

        if atasan is None:
            print("Gagal: Atasan tidak ditemukan.")
            return False

        node_baru = Node(id_pegawai, nama, jabatan)

        if atasan.first_child is None:
            atasan.first_child = node_baru

        else:
            saudara = atasan.first_child

            while saudara.next_sibling is not None:
                saudara = saudara.next_sibling

            saudara.next_sibling = node_baru

        print(
            f"Berhasil menambahkan {nama} "
            f"({jabatan}) di bawah {atasan.nama}."
        )

        return True

    # Preorder Traversal
    def preorder(self):

        hasil = []

        def _preorder(node):

            if node is None:
                return

            hasil.append(
                f"{node.nama} ({node.jabatan})"
            )

            _preorder(node.first_child)
            _preorder(node.next_sibling)

        _preorder(self.root)

        return hasil

    # Inorder Traversal
    def inorder(self):

        hasil = []

        def _inorder(node):

            if node is None:
                return

            _inorder(node.first_child)

            hasil.append(
                f"{node.nama} ({node.jabatan})"
            )

            _inorder(node.next_sibling)

        _inorder(self.root)

        return hasil

    # Postorder Traversal
    def postorder(self):

        hasil = []

        def _postorder(node):

            if node is None:
                return

            _postorder(node.first_child)
            _postorder(node.next_sibling)

            hasil.append(
                f"{node.nama} ({node.jabatan})"
            )

        _postorder(self.root)

        return hasil

    # Menampilkan struktur organisasi
    def tampilkan_struktur(self):

        def _tampil(node, level=0):

            if node is None:
                return

            print(
                "  " * level
                + f"- {node.nama} ({node.jabatan})"
            )

            anak = node.first_child

            while anak is not None:
                _tampil(anak, level + 1)
                anak = anak.next_sibling

        _tampil(self.root)


# ==========================================
# MEMBUAT ROOT ORGANISASI
# ==========================================

rektor = Node(
    "ORG001",
    "Dr. Ahmad",
    "Rektor"
)

organisasi = OrganizationTree(rektor)


# ==========================================
# MENAMBAHKAN DATA ORGANISASI
# ==========================================


organisasi.insert_node(
    "Dr. Ahmad", "ORG002",
    "Dr. Siti", "Dekan Fakultas Sains dan Teknologi"
)

organisasi.insert_node(
    "Dr. Ahmad", "ORG003",
    "Dr. Budi", "Dekan Fakultas Ekonomi dan Ilmu Sosial"
)

organisasi.insert_node(
    "Dr. Siti", "ORG004",
    "Andi", "Ketua Prodi Teknik Informatika"
)

organisasi.insert_node(
    "Dr. Siti", "ORG005",
    "Rina", "Ketua Prodi Sistem Informasi"
)

organisasi.insert_node(
    "Andi", "ORG006",
    "Dewi", "Dosen Teknik Informatika"
)

organisasi.insert_node(
    "Andi", "ORG007",
    "Fajar", "Dosen Teknik Informatika"
)

organisasi.insert_node(
    "Rina", "ORG008",
    "Nadia", "Dosen Sistem Informasi"
)

organisasi.insert_node(
    "Dr. Budi", "ORG009",
    "Citra", "Ketua Prodi Manajemen"
)

organisasi.insert_node(
    "Dr. Budi", "ORG010",
    "Rizal", "Ketua Prodi Akuntansi"
)


# ==========================================
# PENGUJIAN PENCARIAN
# ==========================================

print("\n=== HASIL PENCARIAN ===")

cari = organisasi.search_node("Teknik Informatika")

if cari:
    print("Data ditemukan:")
    print("ID:", cari.id_pegawai)
    print("Nama:", cari.nama)
    print("Jabatan:", cari.jabatan)
else:
    print("Data tidak ditemukan.")


# ==========================================
# PENGUJIAN PENAMBAHAN DATA
# ==========================================

print("\n=== PENAMBAHAN DATA ===")

organisasi.insert_node(
    "Dr. Ahmad",
    "ORG011",
    "Dr. Maya",
    "Kepala Biro Akademik"
)


# ==========================================
# MENAMPILKAN STRUKTUR ORGANISASI
# ==========================================

print("\n=== STRUKTUR ORGANISASI ===")

organisasi.tampilkan_struktur()


# ==========================================
# PREORDER TRAVERSAL
# ==========================================

print("\n=== PREORDER TRAVERSAL ===")

for data in organisasi.preorder():
    print(data)


# ==========================================
# INORDER TRAVERSAL
# ==========================================

print("\n=== INORDER TRAVERSAL ===")

for data in organisasi.inorder():
    print(data)


# ==========================================
# POSTORDER TRAVERSAL
# ==========================================

print("\n=== POSTORDER TRAVERSAL ===")

for data in organisasi.postorder():
    print(data)