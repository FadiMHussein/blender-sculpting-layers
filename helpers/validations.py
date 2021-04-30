#  Copyright (C) 2021 Fadi Hussein
#  This file is part of blender-sculpting-layers <https://github.com/FadiMHussein/blender-sculpting-layers.git>.
#
#  blender-sculpting-layers is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  blender-sculpting-layers is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with blender-sculpting-layers.  If not, see <http://www.gnu.org/licenses/>.
#
#

def addon_is_enabled(context):
    """
    Validate if sculpting layers option is enabled
    :param bpy.context context: Current Context
    :return:
        bool: Validation Results
    """
    return context.object.sculpting_layers_properties.is_enabled


def can_add_layers(context):
    """
    Validate if sculpting layers can be added
    :param bpy.context context: Current Context
    :return:
        bool: Validation Results
    """
    return True


def can_enable_multires(context):
    """
    Validate if MultiResolution can be enabled
    :param bpy.context context: Current Context
    :return:
        bool: Validation Results
    """
    return True
