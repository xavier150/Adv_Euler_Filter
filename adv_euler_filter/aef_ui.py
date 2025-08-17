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

import os
import bpy
import addon_utils
import time
import mathutils

from . import bbpl
from . import aef_basics
from . import aef_utils
from . import aef_ui_utils
from . import languages
from . import aef_types


class AEF_PT_GraphCurveFilter(bpy.types.Panel):
    # Graph Curve Filter panel

    bl_idname = "AEF_PT_GraphCurveFilter"
    bl_label = "Curbe Filter"
    bl_space_type = "GRAPH_EDITOR"
    bl_region_type = "UI"
    bl_category = "Curbe Filter"

    class AEF_OT_ApplyFilterLeftRight(bpy.types.Operator):
        bl_label = "Apply (Left -> Right)"
        bl_idname = "object.aef_apply_filter_left_right"
        bl_description = "Clic to apply filter (Left -> Right)"

        def execute(self, context):
            euler_group = aef_utils.create_euler_group_from_select()
            aef_utils.apply_euler_filer_first_to_last(euler_group)
            return {'FINISHED'}
        
    class AEF_OT_ApplyFilterRightLeft(bpy.types.Operator):
        bl_label = "Apply (Right -> Left)"
        bl_idname = "object.aef_apply_filter_right_left"
        bl_description = "Clic to apply filter (Right -> Left)"

        def execute(self, context):
            euler_group = aef_utils.create_euler_group_from_select()
            aef_utils.apply_euler_filer_last_to_first(euler_group)
            return {'FINISHED'}

    def draw(self, contex):
        layout = self.layout

        # Extension details
        if bpy.app.version >= (4, 2, 0):
            version_str = 'Version '+ str(bbpl.blender_extension.extension_utils.get_package_version())
        else:
            version_str = 'Version '+ bbpl.blender_addon.addon_utils.get_addon_version_str("Unreal Engine Assets Exporter")

        credit_box = layout.box()
        credit_box.label(text=languages.ti('intro'))
        credit_box.label(text=version_str)
        bbpl.blender_layout.layout_doc_button.functions.add_doc_page_operator(
            layout = layout,
            url = "https://github.com/xavier150/Adv-Euler-Filter",
            text = "Open Github page",
            icon="HELP"
            )
        
        obj = bpy.context.object
        if not obj or not obj.animation_data or not obj.animation_data.action:
            return None

        preview = False
        if preview:
            print("ssssssssssssssssssss")
            euler_group = aef_utils.create_euler_group_from_select()
            euler_group.print_all_keys()
            euler_values = list(euler_group.euler_frames.values())
            derniere = euler_values[-1]
            avant_derniere = euler_values[-2]

            new_euler = aef_utils.calculate_euler_filter(avant_derniere.get_euler(), derniere.get_euler())
            print(f"(FIXED {derniere.frame}) ->  X{new_euler.x}, Y{new_euler.y}, Z{new_euler.z}")
        
        new_filter_button = layout.operator("object.aef_apply_filter_left_right")
        new_filter_button = layout.operator("object.aef_apply_filter_right_left")

        return None

classes = (
    AEF_PT_GraphCurveFilter,
    AEF_PT_GraphCurveFilter.AEF_OT_ApplyFilterLeftRight,
    AEF_PT_GraphCurveFilter.AEF_OT_ApplyFilterRightLeft,
)


def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
