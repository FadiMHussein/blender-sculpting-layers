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
from bpy.props import StringProperty, IntProperty, PointerProperty
from bpy.types import Operator
from .properties import SculptingLayersProperties, LayerProperties


# ------------------------------------------------------------------------
#    Layers Operators
# ------------------------------------------------------------------------

class AddLayerOperator(Operator):
    """
    Operator to Add new Layer
    """
    bl_label = "Add Layer"
    bl_idname = "wm.add_layer"

    def execute(self, context):
        properties: SculptingLayersProperties = context.object.sculpting_layers_properties
        properties.layers.add()

        return {'FINISHED'}


class DeleteAllLayerOperator(Operator):
    """
    Operator to Delete All Layers
    """
    bl_label = "Delete All"
    bl_idname = "object.delete_all_layers"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        return {'FINISHED'}


class ApplyAllLayerOperator(Operator):
    """
    Operator to Apply All Layers
    """
    bl_label = "Apply All"
    bl_idname = "object.apply_all_layers"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        return {'FINISHED'}


class ApplyLayerOperator(Operator):
    """
    Operator to Apply a Layer
    """
    bl_label = "Apply"
    bl_description = "Apply Layer to Base Mesh"
    bl_idname = "object.apply_layer"

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print(context.object.sculpting_layers_properties.layers[self.layer_index])
        return {'FINISHED'}


class DeleteLayerOperator(Operator):
    """
    Operator to Delete a Layer
    """
    bl_label = "Delete"
    bl_description = "Delete Layer"
    bl_idname = "object.delete_layer"

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print(context.object.sculpting_layers_properties.layers[self.layer_index])
        return {'FINISHED'}


class ToggleLayerVisibilityOperator(Operator):
    """
    Operator to Hide/Show a Layer
    """
    bl_label = "Toggle"
    bl_description = "Toggle Layer Visibility"
    bl_idname = "object.toggle_layer_visibility"

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        if(context.object.sculpting_layers_properties.layers[self.layer_index].is_enabled):
            context.object.sculpting_layers_properties.layers[self.layer_index].is_enabled = False
        else:
            context.object.sculpting_layers_properties.layers[self.layer_index].is_enabled = True

        return {'FINISHED'}