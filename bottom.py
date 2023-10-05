import argparse
import os

from urllib.parse import urlparse
from urllib.request import urlopen
from time import perf_counter


def encode(in_str: str) -> str:
    mapping = prepare()

    if not in_str:
        return ''

    in_bytes = in_str.encode('utf-8')

    out_str = '👉👈'.join([mapping[char] for char in in_bytes]) + '👉👈'

    return out_str


def decode(in_str: str) -> str:
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

    return out_bytes.decode('utf-8')[:-1]


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


def infile(location: str) -> str:
    url = urlparse(location)
    if url.scheme in ['file', '']:
        if not os.path.exists(url.path):
            raise FileNotFoundError(f"File not found: {url.path}")
        with open(url.path, 'r', encoding='utf-8') as f:
            return encode(f.read())
    else:
        try:
            r = urlopen(location)
        except ValueError:
            raise ValueError(f"Invalid URL: {location}")
        return encode(r.read().decode('utf-8'))


def outfile(location: str) -> str:
    url = urlparse(location)
    if url.scheme in ['file', '']:
        if not os.path.exists(url.path):
            raise FileNotFoundError(f"File not found: {url.path}")
        with open(url.path, 'r', encoding='utf-8') as f:
            return decode(f.read())
    else:
        try:
            r = urlopen(location)
        except ValueError:
            raise ValueError(f"Invalid URL: {location}")
        return decode(r.read().decode('utf-8'))


def main():
    args = argparse.ArgumentParser()
    args.add_argument('mode', choices=['encode', 'decode', 'infile', 'outfile'])
    args.add_argument('--output-file', '-o', help="Location of a file to print the output to. If no "
                                                  "output file is specified, the result will be printed to console")
    args.add_argument('input')
    args = args.parse_args()
    result = None
    st = perf_counter()
    if args.mode == 'encode':
        result = encode(args.input)

    if args.mode == 'decode':
        result = decode(args.input)

    if args.mode == 'infile':
        result = infile(args.input)

    if args.mode == 'outfile':
        result = outfile(args.input)

    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(result)
    else:
        print(result)
    et = perf_counter()
    print(f"Time taken: {(et - st) * 1000:.2f}ms")


if __name__ == '__main__':
    main()
