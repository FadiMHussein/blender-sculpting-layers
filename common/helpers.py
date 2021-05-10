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


def get_shape_key_by_name(context, name):
    """
    Get Shape Key By Name
    :param context: Current Context
    :type context: bpy.context

    :param name: Shape Key Name
    :type name: str

    :return: Shape Key

    """
    index = 0
    for key in context.object.data.shape_keys.key_blocks:
        if key.name == name:
            return key, index
        index += 1

    return None, None


def is_debug():
    return True
