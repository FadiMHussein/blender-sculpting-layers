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
#  BlenderSculptingLayers is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  BlenderSculptingLayers is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with BlenderSculptingLayers.  If not, see <http://www.gnu.org/licenses/>.
#
#
import bpy
from .properties import SculptingLayersProperties


def addon_is_enabled(active_object):
    """
    Validate if sculpting layers option is enabled

    :param active_object: bpy.types.Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return active_object.sculpting_layers.is_enabled_status


def can_add_layers(active_object):
    """
    Validate if sculpting layers can be added

    :param active_object: bpy.types.Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return True


def can_record(active_object):
    """
    Validate if sculpting layers can be added

    :param active_object: Active Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    for layer in active_object.sculpting_layers.layers:
        if layer.is_recording:
            return False

    return True


def has_sculpting_layers(active_object):
    """
    Validate if Sculpting Layers are Present

    :param active_object: bpy.types.Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return len(active_object.sculpting_layers.layers) != 0


def has_shape_keys(active_object):
    """
    Validate if Object has Shape Keys

    :param active_object: bpy.types.Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return active_object.data.shape_keys is not None
