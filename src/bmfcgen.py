#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura <https://github.com/hirmiura>
#
# 使い方
# $ENV:Path="bmfont.exeのパス;"+$ENV:Path
# bmfcgen.py
# のんびり待つ
from __future__ import annotations

import copy
import io
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field

from BMFC import BMFC


BMFONT_EXE = 'bmfont64.exe'
BMFCGEN_JSON_FILE = 'bmfcgen.json'


@dataclass
class BmfGenConf(BMFC):
    outputfile: str = ''
    nameInStarsector: list[str] = field(default_factory=list)

    @property
    def bmfc_file(self):
        return self.outputfile + '.bmfc'

    @property
    def fnt_file(self):
        return self.outputfile + '.fnt'

    @property
    def png_file(self):
        return self.outputfile + '_0.png'

    def apply_dict(self, d: dict) -> None:
        super().apply_dict(d)
        if 'nameInStarsector' in d:
            self.nameInStarsector = d['nameInStarsector']


def read_jsonc(file: str) -> dict:
    """Cコメント付きJSONファイルを読み込む

    Args:
        file (str): JSONファイル

    Returns:
        dict: JOSNオブジェクト
    """
    with open(file, encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'/\*[\s\S]*?\*/|//.*', '', text)
    return json.loads(text)


def init_config():
    TEMP_KEY = 'template'
    CONFIG_KEY = 'config'

    # 設定リスト
    global bmf_config
    bmf_config = []

    # JSON設定ファイルを読み込む
    jobj = read_jsonc(BMFCGEN_JSON_FILE)

    # 全体用テンプレートを読み込む
    world_temp = BmfGenConf.load(jobj[TEMP_KEY]) if TEMP_KEY in jobj else BmfGenConf()

    # 設定リストを読み込む
    if CONFIG_KEY in jobj:
        for c in jobj[CONFIG_KEY]:
            cdict = c
            # 全体用テンプレートからコピーする
            citem = copy.copy(world_temp)
            if TEMP_KEY in cdict:
                # 個別テンプレートがあれば読み込む
                citem.load(c[TEMP_KEY])
                del cdict[TEMP_KEY]
            # 残りの設定を読み込む
            citem.apply_dict(cdict)
            # 設定リストに追加する
            bmf_config.append(citem)


def generate_bmfc():
    print('bmfcファイルを生成中...', flush=True)
    count: int = 0
    for conf in bmf_config:
        count += 1
        conf.save(conf.bmfc_file)
        print('==>' + conf.bmfc_file, flush=True)
    print(f'{count} ファイル生成完了', flush=True)


def generate_font():
    print('ビットマップフォントを生成中...', flush=True)
    count: int = 0
    for conf in bmf_config:
        count += 1
        print('==>' + conf.fnt_file, flush=True)
        com = [BMFONT_EXE, '-c', conf.bmfc_file, '-o', conf.fnt_file]
        subprocess.run(com, shell=True)
    print(f'{count} フォント生成完了', flush=True)


def main():
    print('bmfcgen.py', flush=True)
    init_config()
    generate_bmfc()
    print()
    generate_font()
    return 0


if __name__ == '__main__':
    # MSYS2での文字化け対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    sys.exit(main())
