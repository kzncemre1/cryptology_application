import sys

def read_embedded_context(file, p):
    print("Reading audio file...")
    with (open(file, "rb") as f):
        iter = p+4
        f.seek(iter)

        input_size = f.read(1)

        iter += 1
        f.seek(iter)

        bytes_list = []
        for i in range(input_size[0]):
            data = f.read(1)
            bytes_list.append(data)
            iter += 1
            f.seek(iter)

        merged_bytes = b"".join(bytes_list)
        print(f"Embedded text:{merged_bytes.decode()}")

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

if __name__ == "__main__":
    file = sys.argv[1]
    p = find_data_chunk_id(file)
    read_embedded_context(file, p)