# SPDX-FileCopyrightText: 2024-2025 Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  Adv Euler Filter
#  https://github.com/xavier150/Adv_Euler_Filter
# ----------------------------------------------


import bpy
import fnmatch
import mathutils
import math
import time
import sys

if "bpy" in locals():
    import importlib
    if "aef_basics" in locals():
        importlib.reload(aef_basics)
from . import aef_basics
from .aef_basics import *


def LayoutSection(layout, PropName, PropLabel):
    scene = bpy.context.scene
    expanded = eval("scene."+PropName)
    tria_icon = "TRIA_DOWN" if expanded else "TRIA_RIGHT"
    layout.row().prop(scene, PropName, icon=tria_icon, icon_only=True, text=PropLabel, emboss=False)
    return expanded
