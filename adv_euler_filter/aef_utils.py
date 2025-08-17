# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================


import bpy
import mathutils
from . import aef_types
from . import aef_eulerfilter_utils


def create_euler_group_from_select() -> aef_types.EulerGroup:
    obj = bpy.context.object
    action = obj.animation_data.action

    euler_group = aef_types.EulerGroup(action)
    # Get euler data from selected curves
    for fcurve in action.fcurves:
        for keyframe in fcurve.keyframe_points:
            if keyframe.select_control_point:
                euler_group.try_add_new_key(fcurve, keyframe)

    return euler_group

def apply_euler_filer_first_to_last(euler_group: aef_types.EulerGroup):
    euler_values = list(euler_group.euler_frames.values())
    first_key = euler_values[0]
    last_key = euler_values[-1]

    new_euler = aef_eulerfilter_utils.calculate_euler_filter(first_key.get_euler(), last_key.get_euler())
    euler_group.apply_euler_on_frame(last_key.frame, new_euler)

def apply_euler_filer_last_to_first(euler_group: aef_types.EulerGroup):
    euler_values = list(euler_group.euler_frames.values())
    first_key = euler_values[0]
    last_key = euler_values[-1]

    new_euler = aef_eulerfilter_utils.calculate_euler_filter(last_key.get_euler(), first_key.get_euler())
    euler_group.apply_euler_on_frame(first_key.frame, new_euler)

