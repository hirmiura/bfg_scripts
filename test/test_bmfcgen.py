#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura (https://github.com/hirmiura)
from __future__ import annotations

import os
import sys

# fmt:off
sys.path.append(os.path.abspath('./src'))
import bmfcgen  # noqa: E402
# fmt:on

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test_init_config():
    os.chdir('test')
    bmfcgen.init_config()
    assert len(bmfcgen.bmf_config) == 3
    c = bmfcgen.bmf_config[0]
    assert c.outputfile == 'Sika15aa'
    assert c.fontName == 'Cica'
    assert c.fontFile == 'Cica-Regular.otf'
    assert c.fontSize == -15
    assert c.aa == 4
    assert c.renderFromOutline == 0
    assert c.outWidth == 4096
    assert c.outHeight == 2048
    assert len(c.nameInStarsector) == 1
    assert c.nameInStarsector[0] == "insignia15LTaa"
