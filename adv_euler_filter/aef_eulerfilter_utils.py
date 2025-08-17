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


import math
import mathutils

euler_methods = ["QUAD", "UNWRAP", "QUAD_UNWRAP"]
euler_method = "UNWRAP"

def calculate_euler_filter(prev_euler: mathutils.Euler, current_euler: mathutils.Euler) -> mathutils.Euler:
    if euler_method == "QUAD":
        return calculate_euler_filter_quat(prev_euler, current_euler)
    elif euler_method == "UNWRAP":
        return calculate_euler_filter_unwrap(prev_euler, current_euler)
    elif euler_method == "QUAD_UNWRAP":
        corrected_euler = calculate_euler_filter_quat(prev_euler, current_euler)
        return calculate_euler_filter_quat(prev_euler, corrected_euler)



def calculate_euler_filter_quat(prev_euler: mathutils.Euler, current_euler: mathutils.Euler) -> mathutils.Euler:
    """
    Corrige edit_euler pour éviter les flips (Euler breaks), en gardant la continuité visuelle avec target_euler.
    L’ordre des Euler est respecté.
    """
    assert prev_euler.order == current_euler.order, "Euler orders must match"

    # Convert both Euler angles to quaternions
    quat_prev = prev_euler.to_quaternion()
    quat_current = current_euler.to_quaternion()

    # Compute relative rotation
    delta_quat = quat_prev.rotation_difference(quat_current)

    # Apply the delta to the target to keep orientation similar
    corrected_quat = quat_prev @ delta_quat

    # Convert back to Euler using the desired order
    corrected_euler = corrected_quat.to_euler(current_euler.order)

    return corrected_euler

def unwrap_radian(target: float, value: float) -> float:
    """Unwrap `value` to be as close as possible to `target`, modulo 2π."""
    delta = value - target
    while delta > math.pi:
        value -= 2 * math.pi
        delta = value - target
    while delta < -math.pi:
        value += 2 * math.pi
        delta = value - target
    return value

def calculate_euler_filter_unwrap(prev_euler: mathutils.Euler, current_euler: mathutils.Euler) -> mathutils.Euler:
    """
    Corrige edit_euler pour conserver la continuité avec target_euler,
    en restant proche des valeurs angulaires originales (ex: -720 reste -720, pas +0).
    """
    assert prev_euler.order == current_euler.order, "Euler orders must match"

    # 1. Convert edit to quaternion
    quat = current_euler.to_quaternion()

    # 2. Convert back to euler using same order
    filtered = quat.to_euler(current_euler.order)

    # 3. Unwrap each angle to stay numerically close to target_euler
    filtered.x = unwrap_radian(prev_euler.x, filtered.x)
    filtered.y = unwrap_radian(prev_euler.y, filtered.y)
    filtered.z = unwrap_radian(prev_euler.z, filtered.z)

    return filtered