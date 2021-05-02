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
from bpy.types import Panel
from ..common.properties import SculptingLayersProperties
from ..common.validations import *
from .operators import AddLayerOperator, ToggleLayerRecordingOperator, ApplyLayerOperator, \
    ToggleLayerVisibilityOperator, DeleteLayerOperator, ApplyAllLayerOperator, DeleteAllLayerOperator


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
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        # active_object = context.object
        properties: SculptingLayersProperties = context.object.sculpting_layers

        layout.prop(properties, "is_enabled")


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
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        # Get Addon Properties
        properties: SculptingLayersProperties = context.object.sculpting_layers
        # Check if Layout Should be Enabled and Assign
        enabled = addon_is_enabled(context.object) and can_add_layers(context.object)
        layout.enabled = enabled

        can_rec = can_record(context.object)

        # Spit Validation Message
        if not enabled:
            layout.label(text="Enable Sculpting Layers First")

        # Add Layer Operator
        add_row = layout.row(align=True)
        add_row.enabled = can_rec
        add_row.operator(AddLayerOperator.bl_idname, icon="PLUS")

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
            layer_row = layer_box.row(align=True)
            layer_row.column().prop(layer, "label")

            layer_row.enabled = can_rec or layer.is_recording

            # Toggle Layer Recording Operator
            if layer.is_recording:
                layer_row.column().operator(
                    ToggleLayerRecordingOperator.bl_idname, text="", icon="PAUSE"
                ).layer_index = layer_index
            else:
                layer_row.column().operator(
                    ToggleLayerRecordingOperator.bl_idname, text="", icon="PLAY"
                ).layer_index = layer_index

            # Apply Layer Operator
            layer_row.column().operator(
                ApplyLayerOperator.bl_idname, text="", icon="CHECKMARK"
            ).layer_index = layer_index

            # Toggle Layer Visibility Operator
            if layer.is_enabled:
                layer_row.column().operator(
                    ToggleLayerVisibilityOperator.bl_idname, text="", icon="HIDE_OFF"
                ).layer_index = layer_index
            else:
                layer_row.column().operator(
                    ToggleLayerVisibilityOperator.bl_idname, text="", icon="HIDE_ON"
                ).layer_index = layer_index

            # Delete Layer Operator
            layer_row.column().operator(
                DeleteLayerOperator.bl_idname, text="", icon="REMOVE"
            ).layer_index = layer_index

            # Layer Weight
            layer_box.row(align=True).prop(layer, "weight")

            layer_index += 1

        # Global Layers Operators
        global_row = layout.row()
        global_row.enabled = can_rec
        global_row.split()
        # Apply All Layers Operator
        global_row.operator(ApplyAllLayerOperator.bl_idname, icon="CHECKMARK")
        # Delete All Layers Operator
        global_row.operator(DeleteAllLayerOperator.bl_idname, icon="REMOVE")
