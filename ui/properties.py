#  Copyright (C) 2021 Fadi Hussein
#  This file is part of blender-sculpting-layers <https://github.com/FadiMHussein/blender-sculpting-layers>.
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

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty, CollectionProperty,
                       )

from bpy.types import PropertyGroup
from ..helpers import callbacks as callback


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
        update=callback.enable_sculpting_layers_callback
    )

    weight: FloatProperty(
        name="Weight",
        description="Layer Weight",
        default=1,
        min=-1,
        max=1
    )


class SculptingLayersProperties(PropertyGroup):
    """
    Class to define Sculpting Layers Properties
    """
    is_enabled: BoolProperty(
        name="Enable Sculpting Layers",
        description="Enable Sculpting Layers for None-Destructive Sculpting Workflow",
        default=False,
        update=callback.enable_sculpting_layers_callback
    )

    layers: CollectionProperty(
        type=LayerProperties
    )

# ------------------------------------------------------------------------
#    Multi Resolution Properties
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
#    Layers Properties
# ------------------------------------------------------------------------
