# SPDX-FileCopyrightText: 2024-2025 Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  Adv Euler Filter
#  https://github.com/xavier150/Adv_Euler_Filter
# ----------------------------------------------

import os
import bpy
import addon_utils

from . import aef_basics
from .aef_basics import *
from . import aef_utils
from .aef_utils import *
from . import aef_ui_utils
from . import languages
from .languages import *


if "bpy" in locals():
    import importlib
    if "aef_export_asset" in locals():
        importlib.reload(aef_export_asset)
    if "aef_write_text" in locals():
        importlib.reload(aef_write_text)
    if "aef_basics" in locals():
        importlib.reload(aef_basics)
    if "aef_utils" in locals():
        importlib.reload(aef_utils)
    if "aef_check_potential_error" in locals():
        importlib.reload(aef_check_potential_error)
    if "aef_ui_utils" in locals():
        importlib.reload(aef_ui_utils)
    if "languages" in locals():
        importlib.reload(languages)


from bpy.props import (
        StringProperty,
        BoolProperty,
        EnumProperty,
        IntProperty,
        FloatProperty,
        FloatVectorProperty,
        PointerProperty,
        CollectionProperty,
        )

from bpy.types import (
        Operator,
        )


class AEF_AP_AddonPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout


classes = (

)


def menu_func(self, context):
    layout = self.layout
    col = layout.column()
    col.separator(factor=1.0)
    col.operator(AEF_PT_CorrectAndImprov.AEF_OT_CorrectExtremUV.bl_idname)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)

    bpy.types.VIEW3D_MT_uv_map.remove(menu_func)
