#---------------------------Hashing transactions---------------------------#
def sha256(b):
        b = preprocess(b)

        # split message into 512-bit blocks, with 16 32-bit words
        blocks = []
        for i in range (len(b)//64): 
                words = []
                for k in range(16): 
                        words.append(b[64*i+4*k:64*i+4*(k+1)])
                        print(f"word: {words[k]}")
                blocks.append(words)
        print(blocks)

def preprocess(b):
        og_len = len(b) * 8

        # append 1 bit + seven 0 bits
        b.append(0x80)
        # append zeros until 64-bit length field fits
        while len(b) % 64 != 56:
                b.append(0x00)
        # append original length as 64-bit big endian
        b += og_len.to_bytes(8, "big")

        for byte in b:
                print(f"{byte:08b}", end="")
        print()
        print(f"padded size:{len(b)*8}")

        return b
