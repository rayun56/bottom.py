import argparse


def encode(in_str: str):
    mapping = prepare()

    if not in_str.isascii():
        raise ValueError('Input string must be ASCII')

    in_bytes = in_str.encode('ascii')

    out_str = '👉👈'.join([mapping[char] for char in in_bytes]) + '👉👈'

    return out_str


def decode(in_str: str):
    vals = {
        '🫂': 200,
        '💖': 50,
        '✨': 10,
        '🥺': 5,
        ',': 1,
        '❤️': 0
    }

    out_bytes = bytearray()
    in_list = in_str.split('👉👈')
    for byte in in_list:
        b = 0
        for char in byte:
            if char not in vals.keys():
                raise ValueError(f"Invalid character: {char}")
            b += vals[char]
        out_bytes += b.to_bytes()

    return out_bytes.decode('ascii')[:-1]


def prepare() -> list[str]:
    vals = {
        200: '🫂',
        50: '💖',
        10: '✨',
        5: '🥺',
        1: ','
    }

    mapping = ['❤️']

    for i in range(1, 256):
        map_str = ''
        for val, char in vals.items():
            if i // val >= 1:
                map_str += char * (i // val)
                i %= val
        mapping.append(map_str)

    return mapping


def main():
    args = argparse.ArgumentParser()
    args.add_argument('mode', choices=['encode', 'decode'])
    args.add_argument('input')
    args = args.parse_args()
    if args.mode == 'encode':
        print(encode(args.input))
    elif args.mode == 'decode':
        print(decode(args.input))


if __name__ == '__main__':
    main()
