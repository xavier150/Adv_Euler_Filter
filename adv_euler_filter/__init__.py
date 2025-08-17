# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.	 If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================

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