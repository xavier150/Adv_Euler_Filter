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
from typing import Dict

class EulerFrame:
    def __init__(self, frame: float):
        self.frame = frame
        self.euler = mathutils.Euler()

    def get_key_str(self):
        return f"({self.frame}) ->  X{self.euler.x}, Y{self.euler.y}, Z{self.euler.z}"
    
    def get_euler(self):
        return self.euler

class EulerGroup:
    def __init__(self, source_data):
        self.source_data = source_data
        self.selected_data_path = None
        self.euler_frames: Dict[float, EulerFrame] = {}

    def try_add_new_key(self, fcurve: bpy.types.FCurve, keyframe: bpy.types.Keyframe):
        if self.selected_data_path is None:
            # Set the target data path
            self.selected_data_path = fcurve.data_path
        else:
            # Add only curve from the same data path
            if fcurve.data_path != self.selected_data_path:
                return
            

        array_index = fcurve.array_index
        frame = keyframe.co[0]
        value = keyframe.co[1]

        if frame not in self.euler_frames:
            new_euler_frame = self.euler_frames[frame] = EulerFrame(frame)

        if array_index == 0:
            self.euler_frames[frame].euler.x = value
        elif array_index == 1:
            self.euler_frames[frame].euler.y = value
        elif array_index == 2:
            self.euler_frames[frame].euler.z = value

    def apply_euler_on_frame(self, frame, new_euler: mathutils.Euler) -> bool:
        frame_data = self.euler_frames[frame] 
        for fcurve in self.source_data.fcurves:
            fcurve: bpy.types.FCurve
            array_index = fcurve.array_index
            if fcurve.data_path == self.selected_data_path:
                for keyframe in fcurve.keyframe_points:
                    if keyframe.co[0] == frame: 
                        if array_index == 0:
                            offset = new_euler.x - self.euler_frames[frame].euler.x
                            keyframe.co[1] += offset
                            keyframe.handle_left.y += offset
                            keyframe.handle_right.y += offset
                            print("s1")
                        elif array_index == 1:
                            offset = new_euler.y - self.euler_frames[frame].euler.y
                            keyframe.co[1] += offset
                            keyframe.handle_left.y += offset
                            keyframe.handle_right.y += offset
                            print("s2")
                        elif array_index == 2:
                            offset = new_euler.z - self.euler_frames[frame].euler.z
                            keyframe.co[1] += offset
                            keyframe.handle_left.y += offset
                            keyframe.handle_right.y += offset
                            print("s3")
        return False

    def print_all_keys(self):
        for frame_key in self.euler_frames:
            frame_data = self.euler_frames[frame_key]
            frame_data_str = frame_data.get_key_str()
            print(f"[{frame_data.frame}] {frame_data_str}")


