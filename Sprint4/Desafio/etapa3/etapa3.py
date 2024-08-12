import hashlib


def mascara():
    while True:
        texto = input("Digite uma palavra, ou 'N' para encerrar: ")
        if texto.lower() == 'n':
            break
        hash_str = hashlib.sha1(texto.encode())
        hash_hex = hash_str.hexdigest()
        print(f'Hash: {hash_hex}')


if __name__ == "__main__":
    mascara()
