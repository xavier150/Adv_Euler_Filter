# SPDX-FileCopyrightText: 2024-2025 Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  Adv Euler Filter
#  https://github.com/xavier150/Adv_Euler_Filter
# ----------------------------------------------

'''
This addons allows to easily add filter in graph editor.

Addon for Blender by Xavier Loux (BleuRaven)
xavierloux.com
xavierloux.loux@gmail.com
'''

import os
import bpy
import fnmatch
import time
import addon_utils
import importlib

from . import bpl
from . import bbpl
from . import aef_addon_pref
from . import aef_ui
from . import aef_basics
from . import aef_utils
from . import aef_eulerfilter_utils
from . import aef_types


if "bpl" in locals():
    importlib.reload(bpl)
if "bbpl" in locals():
    importlib.reload(bbpl)
if "aef_addon_pref" in locals():
    importlib.reload(aef_addon_pref)
if "aef_ui" in locals():
    importlib.reload(aef_ui)
if "aef_basics" in locals():
    importlib.reload(aef_basics)
if "aef_utils" in locals():
    importlib.reload(aef_utils)
if "aef_eulerfilter_utils" in locals():
    importlib.reload(aef_eulerfilter_utils)
if "aef_types" in locals():
    importlib.reload(aef_types)

classes = (
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bbpl.register()
    aef_addon_pref.register()
    aef_ui.register()


def unregister():
    from bpy.utils import unregister_class

    for cls in classes:
        unregister_class(cls)

    aef_addon_pref.unregister()
    aef_ui.unregister()
    bbpl.unregister()