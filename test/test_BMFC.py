#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura (https://github.com/hirmiura)
from __future__ import annotations

import os
import sys

# fmt:off
sys.path.append(os.path.abspath('./src'))
from BMFC import BMFC, NumRange  # noqa: E402
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
    assert t.paddingDown == 0
    assert t.paddingUp == 0
    assert t.paddingRight == 0
    assert t.paddingLeft == 0
    assert t.spacingHoriz == 1
    assert t.spacingVert == 1
    assert t.useFixedHeight == 0
    assert t.forceZero == 0
    assert t.widthPaddingFactor == 0.00
    assert t.outWidth == 2048
    assert t.outHeight == 2048
    assert t.outBitDepth == 32
    assert t.fontDescFormat == 0
    assert t.fourChnlPacked == 0
    assert t.textureFormat == 'png'
    assert t.textureCompression == 0
    assert t.alphaChnl == 1
    assert t.redChnl == 0
    assert t.greenChnl == 0
    assert t.blueChnl == 0
    assert t.invA == 0
    assert t.invR == 0
    assert t.invG == 0
    assert t.invB == 0
    assert t.outlineThickness == 0
    cds = [
        NumRange(32, 126),
        NumRange(160, 172),
        NumRange(174, 259),
        NumRange(272, 275),
        NumRange(282, 283),
        NumRange(296, 299),
        NumRange(305),
        NumRange(323, 324),
        NumRange(327, 328),
        NumRange(332, 335),
        NumRange(338, 339),
        NumRange(352, 353),
        NumRange(360, 365),
        NumRange(376),
        NumRange(381, 382),
        NumRange(402),
        NumRange(416, 417),
        NumRange(431, 432),
        NumRange(461, 476),
        NumRange(504, 505),
        NumRange(593),
        NumRange(609),
        NumRange(710, 711),
        NumRange(713, 715),
        NumRange(728, 732),
        NumRange(746, 747),
        NumRange(768, 772), ]
    for tc, sc in zip(t.chars, cds):
        assert tc == sc
