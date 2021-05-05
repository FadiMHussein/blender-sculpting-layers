#    Copyright (C) 2021 Fadi Hussein
#    This file is part of blender-sculpting-layers <https://github.com/FadiMHussein/blender-sculpting-layers>.
#
#    blender-sculpting-layers	 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    blender-sculpting-layers	 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with blender-sculpting-layers.  If not, see <http://www.gnu.org/licenses/>.
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
    return validations.addon_is_enabled(active_object) and not active_object.sculpting_layers.multi_resolution_enabled_status