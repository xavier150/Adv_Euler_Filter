# SPDX-FileCopyrightText: 2024-2025 Xavier Loux (BleuRaven)
#
# SPDX-License-Identifier: GPL-3.0-or-later

# ----------------------------------------------
#  Adv Euler Filter
#  https://github.com/xavier150/Adv_Euler_Filter
# ----------------------------------------------

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

