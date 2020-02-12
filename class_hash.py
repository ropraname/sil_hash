class hash_table:
    def __init__(self):
        self.hash_mass = [[] for i in range(10000)]

    def add(self, hashing_name):
        if self.hash_mass[hash(hashing_name) % len(self.hash_mass)] != hashing_name:
            self.hash_mass[hash(hashing_name) % len(self.hash_mass)].append(hash(hashing_name))
        print(self.hash_mass)

    def remove(self, removing_name):
        for sl in self.hash_mass[hash(removing_name) % len(self.hash_mass)]:
            if sl == hash(removing_name):
                self.hash_mass[hash(removing_name) % len(self.hash_mass)].remove(hash(removing_name))
                break
        print(self.hash_mass)

    def len(self):
        len_el = 0
        for hashes_m in self.hash_mass:
            for hashes in hashes_m:
                len_el += 1
        return len_el


h = hash_table()
h.add('KOSTYA:qwertyuiop')
h.remove('KOSTYA:qwertyuiop')
print(h.len())