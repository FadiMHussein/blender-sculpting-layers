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
import bpy.types
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatProperty,
                       PointerProperty, CollectionProperty,
                       )

from bpy.types import PropertyGroup
from . import callbacks


# ------------------------------------------------------------------------
#    Basic Properties
# ------------------------------------------------------------------------

class LayerProperties(PropertyGroup):
    """
    Class to define a Single Sculpting Layer
    """
    label: StringProperty(
        name="",
        description="",
        default="New Layer",
        maxlen=1024,
    )

    is_enabled: BoolProperty(
        name="Enable",
        description="Enable Layer",
        default=True,
    )

    is_recording: BoolProperty(
        name="Recording",
        description="Layer is Recording",
        default=False,
    )

    weight: FloatProperty(
        name="Weight",
        description="Layer Weight",
        default=1,
        min=-1,
        max=1
    )

    shape_key_pointer: PointerProperty(
        type=bpy.types.Key,
        name="Shape Key",
        description="Pointer to Shape Key"
    )


class SculptingLayersProperties(PropertyGroup):
    """
    Class to define Sculpting Layers Properties
    """
    is_enabled_status: BoolProperty(
        name="Enable Sculpting Layers",
        description="Enable Sculpting Layers for None-Destructive Sculpting Workflow",
        default=False,
    )

    is_enabled: BoolProperty(
        name="Enable Sculpting Layers",
        description="Enable Sculpting Layers for None-Destructive Sculpting Workflow",
        default=False,
        set=callbacks.is_enabled_set,
        get=callbacks.is_enabled_get
    )

    multi_resolution_enabled_status: BoolProperty(
        name="Enable Multi Resolution",
        description="Enable Multi Resolution with Sculpting Layers",
        default=False,
    )

    multi_resolution_enabled: BoolProperty(
        name="Enable Multi Resolution",
        description="Enable Multi Resolution with Sculpting Layers",
        default=False,
        set=callbacks.is_multi_res_enabled_set,
        get=callbacks.is_multi_res_enabled_get
    )

    multi_res_object: PointerProperty(
        type=bpy.types.Object,
        name="Multi Res Object",
        description="Pointer to Multi Res Object"
    )

    multi_res_modifier_name: StringProperty()

    layers: CollectionProperty(
        type=LayerProperties
    )

# ------------------------------------------------------------------------
#    Multi Resolution Properties
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
#    Layers Properties
# ------------------------------------------------------------------------
