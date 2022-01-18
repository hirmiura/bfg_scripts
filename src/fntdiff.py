#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura <https://github.com/hirmiura>
from __future__ import annotations

import argparse
import io
import re
import sys

RE_MATCH_NAME = 'id'
CHAR_REX = re.compile(rf'^char\s+id=(?P<{RE_MATCH_NAME}>\d+)\s')


def pargs() -> None:
    global args
    parser = argparse.ArgumentParser(
        description='2つのfntファイルを比較して使用している文字コードの差を出力する')
    parser.add_argument('-a', action='store_true', help='追加された文字コードを表示する')
    parser.add_argument('-s', action='store_true', help='削除された文字コードを表示する')
    parser.add_argument('-i', action='store_true', help='共通の文字コードを表示する')
    parser.add_argument('-x', action='store_true', help='文字コードを16進数で表示する')
    parser.add_argument('-c', action='store_true', help='文字コードを文字として表示する')
    parser.add_argument('file1', help='入力ファイル1')
    parser.add_argument('file2', help='入力ファイル2')
    parser.add_argument('--version', action='version', version='%(prog)s 0.2.0')
    args = parser.parse_args()


def parse_file(file: str) -> set:
    assert file is not None
    ids = set()
    with open(file) as f:
        for line in f:
            match = CHAR_REX.match(line)
            if match:
                ids.add(int(match.group(RE_MATCH_NAME)))
    return ids


def print_codes(codes) -> None:
    assert codes is not None
    if len(codes) == 0:
        return
    codes = sorted(codes)
    if args.c:
        convert = map(chr, codes)
    else:
        convert = map(lambda i: format(i, 'x'), codes) if args.x else map(str, codes)
    result = ', '.join(convert)
    print(result)


def process() -> None:
    lids = []
    for file in [args.file1, args.file2]:
        # print(f'{file} を処理中...', flush=True)
        ids = parse_file(file)
        lids.append(ids)
    # 和/差/共通
    add = lids[1] - lids[0]
    sub = lids[0] - lids[1]
    inter = lids[0] & lids[1]
    # 右寄せのための桁計算
    anum = len(add)
    snum = len(sub)
    inum = len(inter)
    astr = f'{anum:,}'
    sstr = f'{snum:,}'
    istr = f'{inum:,}'
    keta = (max(len(astr), len(sstr), len(istr)))
    # 結果表示
    print(f'追加: {astr: >{keta}}')
    if args.a:
        print_codes(add)
    print(f'削除: {sstr: >{keta}}')
    if args.s:
        print_codes(sub)
    print(f'共通: {istr: >{keta}}')
    if args.i:
        print_codes(inter)


def main():
    pargs()
    process()
    return 0


if __name__ == '__main__':
    # MSYS2での文字化け対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    sys.exit(main())
