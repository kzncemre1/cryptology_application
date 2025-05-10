import struct
import sys


def find_data_chunk_id(file):
    with open(file, "rb") as f:
        iter = 36
        f.seek(iter)
        data_chunk_id = b'data'
        while True:
            data = f.read(4)
            if data == data_chunk_id :
                return iter
            else:
                iter += 1
                f.seek(iter)

def change_context(file, p,  input):
        baslangic = p+4
        with open(file, "r+b") as f:
            f.seek(baslangic)
            f.write(len(input).to_bytes(1, byteorder='little'))

            baslangic += 1
            f.seek(baslangic)

            for i in range(len(input)):
                byte = input[i]
                f.write(byte)
                baslangic += 1
                f.seek(baslangic)



if __name__ == "__main__":
    file = sys.argv[1]
    data_chunk_id = find_data_chunk_id(file)

    context = input("Please enter context : (Max. 160 characters):")
    if len(context) > 160:
        context = context[:160]


    bytes_list = []
    for char in context:
        bytes_list.append(char.encode())

    change_context(file, data_chunk_id,  bytes_list)

