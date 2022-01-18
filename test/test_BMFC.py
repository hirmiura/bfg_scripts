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
