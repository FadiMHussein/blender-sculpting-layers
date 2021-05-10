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
import textwrap

from bpy.types import Operator
from . import callbacks


class EnableMultiResolutionOperator(Operator):
    """
    Operator to Decrease Resolution
    """
    bl_label = "Enable MultiResollution"
    bl_description = "Enable Multi Resolution"
    bl_idname = "object.enable_multi_res"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.enable_multi_resolution(context)
        return {'FINISHED'}

    def draw(self, context):
        warning_lines = textwrap.wrap("Warning: This will clear all layers and configurations for the current object!", 50)
        for line in warning_lines:
            self.layout.label(text=line)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class DisableMultiResolutionOperator(Operator):
    """
    Operator to Decrease Resolution
    """
    bl_label = "Disable MultiResollution"
    bl_description = "Disable Multi Resolution"
    bl_idname = "object.disable_multi_res"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.disable_multi_resolution(context)
        return {'FINISHED'}

    def draw(self, context):
        warning_lines = textwrap.wrap("Warning: This will clear all layers and configurations for the current object!", 50)
        for line in warning_lines:
            self.layout.label(text=line)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class IncreaseResolutionOperator(Operator):
    """
    Operator to Increase Resolution
    """
    bl_label = "Increase"
    bl_description = "Subdivide mesh to increase resolution"
    bl_idname = "object.increase_resolution"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.increase_resolution_callback(context)
        return {'FINISHED'}


class DecreaseResolutionOperator(Operator):
    """
    Operator to Decrease Resolution
    """
    bl_label = "Decrease"
    bl_description = "Decrease higher resolution"
    bl_idname = "object.decrease_resolution"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.decrease_resolution_callback(context)
        return {'FINISHED'}


class UnSubdivideOperator(Operator):
    """
    Operator to Un-Subdivide Resolution
    """
    bl_label = "Unsubdivide"
    bl_description = "Un-Subdivide mesh to create lower Resolution mesh"
    bl_idname = "object.un_subdivide_mesh"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.un_subdivide_mesh_callback(context)
        return {'FINISHED'}


class ApplyResolutionConfigOperator(Operator):
    """
    Operator to Apply MultiResolution Configs
    """
    bl_label = "Apply Resolution Configs"
    bl_description = "Apply Configurations to Start Adding Layers ( Does not apply the actual modifier )"
    bl_idname = "object.apply_resolution_config"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.apply_resolution_config_callback(context)
        return {'FINISHED'}


class ClearResolutionConfigOperator(Operator):
    """
    Operator to Clear MultiResolution Configs
    """
    bl_label = "Clear Resolution Configs"
    bl_description = "Clear Configurations to Reconfigure Multi Resolution"
    bl_idname = "object.clear_resolution_config"
    # TODO: Add Undo Action
    # bl_options = {"UNDO"}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        callbacks.clear_resolution_config_callback(context)
        return {'FINISHED'}

    def draw(self, context):
        warning_lines = textwrap.wrap("Warning: This will clear all layers and configurations for the current object!", 50)
        for line in warning_lines:
            self.layout.label(text=line)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

