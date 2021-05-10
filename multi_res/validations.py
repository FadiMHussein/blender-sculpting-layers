#   Copyright (C) 2021 Fadi Hussein
#   This file is part of blender-sculpting-layers <https://github.com/FadiMHussein/blender-sculpting-layers>.
#
#   blender-sculpting-layers is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   blender-sculpting-layers is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with blender-sculpting-layers.  If not, see <http://www.gnu.org/licenses/>.
#
import bpy
from ..common import validations


def can_modify_layers(active_object):
    """
    Validate if sculpting layers can be added

    :param active_object: bpy.types.Object
    :type active_object: bpy.types.Object

    :return: Validation Results
    :rtype: bool
    """
    return validations.addon_is_enabled(active_object) and not can_modify_multi_res_configs(active_object)


def has_multi_res_modifier(active_object):
    """
    Validate if Object Has MultiRes Modifier

    :param active_object: Current Active Object
    :type active_object: bpy.context.object

    :return: Validation Results
    :rtype: bool
    """
    for modifier in active_object.modifiers:
        if modifier.type == "MULTIRES":
            return True
    return False


def can_enable_multires(active_object):
    """
    Validate if MultiResolution can be enabled

    :param active_object: Current Active Object
    :type active_object: bpy.context.object

    :return: Validation Results
    :rtype: bool
    """
    return validations.addon_is_enabled(active_object)  # and not has_multi_res_modifier(active_object)


def can_modify_multi_res_configs(active_object):
    """
    Validate if MultiResolution modifier is added and can start increasing/decreasing resolution

    :param active_object: Current Active Object
    :type active_object: bpy.context.object

    :return: Validation Results
    :rtype: bool
    """
    return active_object.sculpting_layers.multi_resolution_enabled and active_object.sculpting_layers.multi_res_object is None


def can_change_res(active_object):
    """
    Validate if MultiResolution Config is Enabled and you Can Change Resolution

    :param active_object: Current Active Object
    :type active_object: bpy.context.object

    :return: Validation Results
    :rtype: bool
    """
    return active_object.sculpting_layers.multi_resolution_enabled and has_multi_res_modifier(active_object)
