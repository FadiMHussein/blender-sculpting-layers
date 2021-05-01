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


def addon_is_enabled(properties):
    """
    Validate if sculpting layers option is enabled

    :param properties: Current Context Properties
    :type properties: SculptingLayersProperties

    :return: Validation Results
    :rtype: bool
    """
    return properties.is_enabled_status


def can_add_layers(context):
    """
    Validate if sculpting layers can be added

    :param context: Current Context
    :type context: bpy.context

    :return: Validation Results
    :rtype: bool
    """
    return True


def can_enable_multires(context):
    """
    Validate if MultiResolution can be enabled

    :param context: Current Context
    :type context: bpy.context

    :return: Validation Results
    :rtype: bool
    """
    return True


def can_modify_multi_res_configs(properties):
    """
    Validate if MultiResolution modifier is added and can start increasing/decreasing resolution

    :param properties: Current Context Properties
    :type properties: SculptingLayersProperties

    :return: Validation Results
    :rtype: bool
    """
    return properties.multi_resolution_enabled and properties.multi_res_object is None


def can_change_res(properties):
    """
    Validate if MultiResolution Config is Enabled and you Can Change Resolution

    :param properties: Current Context Properties
    :type properties: SculptingLayersProperties

    :return: Validation Results
    :rtype: bool
    """
    return properties.multi_resolution_enabled and bpy.context.object.modifiers[properties.multi_res_modifier_name] is not None


def has_sculpting_layers(properties):
    """
    Validate if Sculpting Layers are Present

    :param properties: Current Context Properties
    :type properties: SculptingLayersProperties

    :return: Validation Results
    :rtype: bool
    """
    return len(properties.layers) != 0


def has_shape_keys(sculpting_object):
    """
    Validate if Object has Shape Keys

    :param sculpting_object: bpy.types.Object
    :type sculpting_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return sculpting_object.data.shape_keys is not None
