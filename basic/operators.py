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
import textwrap

from bpy.props import IntProperty, StringProperty, FloatProperty
from bpy.types import Operator
from ..common.properties import SculptingLayersProperties, LayerProperties
from ..single_res import callbacks as single_res_callbacks
from ..multi_res import callbacks as multi_res_callbacks


class EnableSculptingLayersOperator(Operator):
    """
    Enable Sculpting Layers
    """
    bl_label = "Enable Sculpting Layers"
    bl_idname = "object.enable_sculpting_layers"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    def execute(self, context):
        context.object.sculpting_layers.is_enabled_status = True
        return {'FINISHED'}

    def draw(self, context):
        warning_lines = textwrap.wrap("Warning: This will clear all layers and configurations for the current object!", 50)
        for line in warning_lines:
            self.layout.label(text=line)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class DisableSculptingLayersOperator(Operator):
    """
    Disable Sculpting Layers
    """
    bl_label = "Disable Sculpting Layers"
    bl_idname = "object.disable_sculpting_layers"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.disable_sculpting_layers_callback(context)
        else:
            single_res_callbacks.disable_sculpting_layers_callback(context)
        return {'FINISHED'}

    def draw(self, context):
        warning_lines = textwrap.wrap("Warning: This will clear all layers and configurations for the current object!", 50)
        for line in warning_lines:
            self.layout.label(text=line)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class AddLayerOperator(Operator):
    """
    Operator to Add new Layer
    """
    bl_label = "Add Layer"
    bl_idname = "object.add_layer"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.add_layer_callback(context)
        else:
            single_res_callbacks.add_layer_callback(context)
        return {'FINISHED'}


class DeleteAllLayerOperator(Operator):
    """
    Operator to Delete All Layers
    """
    bl_label = "Delete All"
    bl_idname = "object.delete_all_layers"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.delete_all_layers_callback(context)
        else:
            single_res_callbacks.delete_all_layers_callback(context)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ApplyAllLayerOperator(Operator):
    """
    Operator to Apply All Layers
    """
    bl_label = "Apply All"
    bl_idname = "object.apply_all_layers"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.apply_all_layers_callback(context)
        else:
            single_res_callbacks.apply_all_layers_callback(context)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ApplyLayerOperator(Operator):
    """
    Operator to Apply a Layer
    """
    bl_label = "Apply"
    bl_description = "Apply Layer to Base Mesh"
    bl_idname = "object.apply_layer"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.apply_layer_callback(context, self.layer_index)
        else:
            single_res_callbacks.apply_layer_callback(context, self.layer_index)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class DeleteLayerOperator(Operator):
    """
    Operator to Delete a Layer
    """
    bl_label = "Delete"
    bl_description = "Delete Layer"
    bl_idname = "object.delete_layer"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.delete_layer_callback(context, self.layer_index)
        else:
            single_res_callbacks.delete_layer_callback(context, self.layer_index)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class ToggleLayerVisibilityOperator(Operator):
    """
    Operator to Hide/Show a Layer
    """
    bl_label = "Toggle"
    bl_description = "Toggle Layer Visibility"
    bl_idname = "object.toggle_layer_visibility"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.layers[self.layer_index].is_enabled:
            if context.object.sculpting_layers.multi_resolution_enabled_status:
                multi_res_callbacks.hide_layer_callback(context, self.layer_index)
            else:
                single_res_callbacks.hide_layer_callback(context, self.layer_index)
        else:
            if context.object.sculpting_layers.multi_resolution_enabled_status:
                multi_res_callbacks.show_layer_callback(context, self.layer_index)
            else:
                single_res_callbacks.show_layer_callback(context, self.layer_index)

        return {'FINISHED'}


class ToggleLayerRecordingOperator(Operator):
    """
    Operator to Toggle Layer Recording
    """
    bl_label = "Record"
    bl_description = "Toggle Layer Recording"
    bl_idname = "object.toggle_layer_recording"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    layer_index: IntProperty(
        name='Layer Index',
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.layers[self.layer_index].is_recording:
            if context.object.sculpting_layers.multi_resolution_enabled_status:
                multi_res_callbacks.stop_layer_recording_callback(context, self.layer_index)
            else:
                single_res_callbacks.stop_layer_recording_callback(context, self.layer_index)
        else:
            if context.object.sculpting_layers.multi_resolution_enabled_status:
                multi_res_callbacks.start_layer_recording_callback(context, self.layer_index)
            else:
                single_res_callbacks.start_layer_recording_callback(context, self.layer_index)
        return {'FINISHED'}


class UpdateLayerWeighOperator(Operator):
    """
    Operator to Update Layer Weight
    """
    bl_label = "Apply All"
    bl_idname = "object.update_layer_weight"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    shape_key_name = StringProperty(
        name="shape_key_name"
    )

    weight = FloatProperty(
        name="weight"
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if context.object.sculpting_layers.multi_resolution_enabled_status:
            multi_res_callbacks.update_layer_weight_callback(context, self.shape_key_name, self.weight)
        else:
            single_res_callbacks.update_layer_weight_callback(context, self.shape_key_name, self.weight)
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
