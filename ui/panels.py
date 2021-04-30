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

from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )
from .properties import SculptingLayersProperties
from ..helpers import validations
from .operators import ApplyAllLayerOperator, DeleteAllLayerOperator, AddLayerOperator, ApplyLayerOperator, \
    ToggleLayerVisibilityOperator, DeleteLayerOperator


# ------------------------------------------------------------------------
#    Basic Panel
# ------------------------------------------------------------------------
class BasicPanel(Panel):
    """
    Panel Class to Define Basic Panel UI
    """
    bl_label = "Basic"
    bl_idname = "SCULPT_PT_BasicPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sculpting Layers"
    bl_context = "sculpt_mode"

    @classmethod
    def poll(cls, context):
        """
        Basic Panel Activation Function
        :param bpy.context context: Current Context
        :return: bool: object is active or not
        """
        return context.object is not None

    def draw(self, context):
        """
        Sculpting Layers Panel Drawing Function
        :param bpy.context context: current context
        """
        layout = self.layout
        # active_object = context.object
        properties: SculptingLayersProperties = context.object.sculpting_layers_properties

        layout.prop(properties, "is_enabled")


# ------------------------------------------------------------------------
#    Multi Resolution Panel
# ------------------------------------------------------------------------
class MultiResolutionPanel(Panel):
    """
    Panel Class to Define MultiResollution Panel UI
    """
    bl_label = "MultiResolution Options"
    bl_idname = "SCULPT_PT_MultiResolution"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sculpting Layers"
    bl_context = "sculpt_mode"

    @classmethod
    def poll(cls, context):
        """
        MultiResolution Panel Activation Function
        :param bpy.context context: Current Context
        :return: bool: object is active or not
        """
        return context.object is not None

    def draw(self, context):
        """
        Sculpting Layers Panel Drawing Function
        :param bpy.context context: current context
        """
        layout = self.layout

        properties: SculptingLayersProperties = context.object.sculpting_layers_properties

        if not validations.addon_is_enabled(context):
            layout.label(text="Enable Sculpting Layers First")


# ------------------------------------------------------------------------
#    Layers Panel
# ------------------------------------------------------------------------
class LayersPanel(Panel):
    """
    Panel Class to Define Sculpting Layers Panel UI
    """
    bl_label = "Layers"
    bl_idname = "SCULPT_PT_Layers"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sculpting Layers"
    bl_context = "sculpt_mode"

    @classmethod
    def poll(cls, context):
        """
        Sculpting Layers Panel Activation Function
        :param bpy.context context: Current Context
        :return: bool: object is active or not
        """
        return context.object is not None

    def draw(self, context):
        """
        Sculpting Layers Panel Drawing Function
        :param bpy.context context: current context
        """
        layout = self.layout

        # Check if Layout Should be Enabled and Assign
        enabled = validations.addon_is_enabled(context)
        layout.enabled = enabled
        # Get Addon Properties
        properties: SculptingLayersProperties = context.object.sculpting_layers_properties

        # Spit Validation Message
        if not enabled:
            layout.label(text="Enable Sculpting Layers First")

        # Add Layer Operator
        layout.row(align=True).operator(AddLayerOperator.bl_idname, icon="PLUS")

        # Layer List
        layer_box = layout.box()

        # Draw Three Empty Rows if No Layers
        if len(properties.layers) == 0:
            layer_box.separator()
            layer_box.separator()
            layer_box.separator()

        # Draw Layers
        layer_index = 0
        for layer in properties.layers:
            layer_rows = layer_box.row(align=True)
            layer_rows.column().prop(layer, "label")

            # Apply Layer Operator
            layer_rows.column().operator(ApplyLayerOperator.bl_idname, text="", icon="CHECKMARK").layer_index = layer_index

            # Toggle Layer Visibility Operator
            if layer.is_enabled:
                layer_rows.column().operator(ToggleLayerVisibilityOperator.bl_idname, text="", icon="HIDE_OFF").layer_index = layer_index
            else:
                layer_rows.column().operator(ToggleLayerVisibilityOperator.bl_idname, text="", icon="HIDE_ON").layer_index = layer_index

            # Delete Layer Operator
            layer_rows.column().operator(DeleteLayerOperator.bl_idname, text="", icon="CANCEL").layer_index = layer_index

            # Layer Weight
            layer_box.row(align=True).prop(layer, "weight")

            layer_index += 1

        # Global Layers Operators
        global_row = layout.row()
        global_row.split()
        # Apply All Layers Operator
        global_row.operator(ApplyAllLayerOperator.bl_idname, icon="CHECKMARK")
        # Delete All Layers Operator
        global_row.operator(DeleteAllLayerOperator.bl_idname, icon="CANCEL")
