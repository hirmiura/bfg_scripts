#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura (https://github.com/hirmiura)
from __future__ import annotations

import os
import sys

# fmt:off
sys.path.append(os.path.abspath('./src'))
from BMFC import BMFC  # noqa: E402
# fmt:on

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test_applyDict():
    d = {
        'fontName': 'test',
        'aa': 4,
        'widthPaddingFactor': 0.1,
        'chars': '12,13-21,33',
        'notInClass': 'nothing'
    }
    t = BMFC()
    t.apply_dict(d)
    assert t.fontName == d['fontName']
    assert t.aa == d['aa']
    assert t.widthPaddingFactor == d['widthPaddingFactor']
    assert t.chars[0].begin == 12
    assert t.chars[1].begin == 13
    assert t.chars[1].end == 21
    assert t.chars[2].begin == 33


def test_load():
    f = os.path.join(__location__, 'test.bmfc')
    t = BMFC.load(f)
    assert t is not None
    assert t.fileVersion == 1
    assert t.fontName == 'TamaTou'
    assert t.fontFile == 'TamaTou-Regular.otf'
    assert t.charSet == 0
    assert t.fontSize == 20
    assert t.aa == 4
    assert t.scaleH == 100
    assert t.useSmoothing == 1
    assert t.isBold == 0
    assert t.isItalic == 0
    assert t.useUnicode == 1
    assert t.disableBoxChars == 1
    assert t.outputInvalidCharGlyph == 0
    assert t.dontIncludeKerningPairs == 0
    assert t.useHinting == 1
    assert t.renderFromOutline == 0
    assert t.useClearType == 1
    assert t.autoFitNumPages == 0
    assert t.autoFitFontSizeMin == 0
    assert t.autoFitFontSizeMax == 0
