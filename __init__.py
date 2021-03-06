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

import bpy
from bpy.props import PointerProperty

from .multi_res.operators import IncreaseResolutionOperator, DecreaseResolutionOperator, UnSubdivideOperator, \
    ApplyResolutionConfigOperator, ClearResolutionConfigOperator, EnableMultiResolutionOperator, \
    DisableMultiResolutionOperator
from .multi_res.panels import MultiResolutionPanel
from .basic.operators import AddLayerOperator, ApplyAllLayerOperator, DeleteAllLayerOperator, ApplyLayerOperator, \
    DeleteLayerOperator, ToggleLayerVisibilityOperator, ToggleLayerRecordingOperator, DisableSculptingLayersOperator, \
    EnableSculptingLayersOperator, UpdateLayerWeighOperator
from .common.properties import LayerProperties, SculptingLayersProperties
from .basic.panels import BasicPanel, LayersPanel

bl_info = {
    "name": "Sculpting Layers",
    "author": "Fadi Hussein",
    "version": (0, 4, 0),
    "blender": (2, 83, 0),
    "location": "Sculpting > Sidebar > Sculpting Layers",
    "description": "Sculpting Layers for Non-Destructive Sculpting Workflow",
    "warning": "Still in Development (May Experience Bugs and Performance Issues)",
    "wiki_url": "https://github.com/FadiMHussein/blender-sculpting-layers/wiki",
    "category": "Sculpting",
    "tracker_url": "https://github.com/FadiMHussein/blender-sculpting-layers/issues",
    "support": "COMMUNITY",
}

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

"""
Classes List to Register/Unregister
"""
classes = (
    # Properties
    LayerProperties,
    SculptingLayersProperties,

    # Operators
    EnableSculptingLayersOperator,
    DisableSculptingLayersOperator,

    EnableMultiResolutionOperator,
    DisableMultiResolutionOperator,

    AddLayerOperator,
    ApplyAllLayerOperator,
    DeleteAllLayerOperator,
    ApplyLayerOperator,
    DeleteLayerOperator,
    ToggleLayerVisibilityOperator,
    ToggleLayerRecordingOperator,
    IncreaseResolutionOperator,
    DecreaseResolutionOperator,
    UnSubdivideOperator,
    ApplyResolutionConfigOperator,
    ClearResolutionConfigOperator,
    UpdateLayerWeighOperator,
    # Menus

    # Panels
    BasicPanel,
    MultiResolutionPanel,
    LayersPanel
)


def register():
    """
    Register addon components
    """
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    # Add Sculpting Layers Properties to Object Type
    bpy.types.Object.sculpting_layers = PointerProperty(type=SculptingLayersProperties)


def unregister():
    """
    Unregister addon components
    """
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)

    # Delete Sculpting Layers Properties from Object Type
    del bpy.types.Object.sculpting_layers


if __name__ == "__main__":
    register()
