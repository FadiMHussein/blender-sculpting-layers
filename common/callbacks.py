#   Copyright (C) 2021 Fadi Hussein
#   This file is part of BlenderSculptingLayers <https://github.com/FadiMHussein/blender-sculpting-layers>.
#
#   BlenderSculptingLayers is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   BlenderSculptingLayers is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with BlenderSculptingLayers.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   BlenderSculptingLayers is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   BlenderSculptingLayers is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with BlenderSculptingLayers.  If not, see <http://www.gnu.org/licenses/>.
#
import bpy
from bpy.types import PointerProperty


def is_enabled_get(self):
    return bpy.context.object.sculpting_layers.is_enabled_status


def is_enabled_set(self, value):
    if value:
        bpy.ops.object.enable_sculpting_layers()
    else:
        bpy.ops.object.disable_sculpting_layers()
        bpy.ops.object.disable_multi_res()


def is_multi_res_enabled_get(self):
    return bpy.context.object.sculpting_layers.multi_resolution_enabled_status


def is_multi_res_enabled_set(self, value):
    if value:
        bpy.ops.object.enable_multi_res()
    else:
        bpy.ops.object.disable_multi_res()


def update_layer_weight_callback(self, context):
    bpy.ops.object.update_layer_weight(shape_key_name=self.shape_key_name, weight=self.weight)
