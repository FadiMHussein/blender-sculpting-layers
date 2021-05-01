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
import bpy
from bpy.types import MultiresModifier


# TODO: Fix Update Modifier Name When Change By User
def enable_multi_resolution(context):
    # Clear Sculpting Layers
    delete_all_layers_callback(context)

    # Clear Shape Keys
    context.object.shape_key_clear()

    # Add MutiRes Modifier
    bpy.ops.object.modifier_add(type='MULTIRES')
    modifier: MultiresModifier = context.object.modifiers["Multires"]
    # Name the Modifier
    modifier.name = "Sculpting Layers"
    # Copy the name to the Addon Properties and Store it in Object
    context.object.sculpting_layers_properties.multi_res_modifier_name = "Sculpting Layers"

    context.object.sculpting_layers_properties.multi_resolution_enabled_status = True


# TODO: Fix Update Modifier Name When Change By User
def disable_multi_resolution(context):
    # Clear Sculpting Layers
    delete_all_layers_callback(context)

    # Clear Configurations
    clear_resolution_config_callback(context)

    # Remove Modifier
    modifier = context.object.modifiers[context.object.sculpting_layers_properties.multi_res_modifier_name]
    context.object.modifiers.remove(modifier)

    context.object.sculpting_layers_properties.multi_resolution_enabled_status = False


def increase_resolution_callback(context):
    """
    Subdivide Mesh to Increase Resolution

    :param context:
    :type context: bpy.context

    :return:
    """
    # TODO: Move Function To Multi Resolution Module
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers_properties.multi_res_modifier_name

    # Apply Subdivisions
    bpy.ops.object.multires_subdivide(modifier=modifier_name)

    # Set All Levels of Modifier to the Highest Available Level
    modifier = context.object.modifiers[modifier_name]
    modifier.levels = modifier.total_levels
    modifier.sculpt_levels = modifier.total_levels
    modifier.render_levels = modifier.total_levels


def decrease_resolution_callback(context):
    """
    Decrease Resolution

    :param context:
    :type context: bpy.context

    :return:
    """
    # TODO: Move Function To Multi Resolution Module
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers_properties.multi_res_modifier_name

    # Set All Levels of Modifier to the Highest Available Level - 1
    modifier = context.object.modifiers[modifier_name]
    modifier.levels = modifier.total_levels - 1
    modifier.sculpt_levels = modifier.total_levels - 1
    modifier.render_levels = modifier.total_levels - 1

    # Apply New Lower Subdivisions
    bpy.ops.object.multires_higher_levels_delete(modifier=modifier_name)


def un_subdivide_mesh_callback(context):
    """
    Subdivide Mesh

    :param context:
    :type context: bpy.context

    :return:
    """
    # TODO: Move Function To Multi Resolution Module
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers_properties.multi_res_modifier_name

    # Apply Un-Subdivision
    bpy.ops.object.multires_unsubdivide(modifier=modifier_name)

    # Set All Levels of Modifier to the Highest Available Level - 1
    modifier = context.object.modifiers[modifier_name]
    modifier.levels = modifier.total_levels
    modifier.sculpt_levels = modifier.total_levels
    modifier.render_levels = modifier.total_levels


def apply_resolution_config_callback(context):
    """
    Decrease Resolution

    :param context: Current Context
    :type context: bpy.context

    :return:
    """
    # TODO: Move Function To Multi Resolution Module
    # Get the Sculpting Original Object
    sculpting_object_ref: bpy.types.Object = context.object

    # Copy Object Data to new Object and Save the reference
    context.object.sculpting_layers_properties.multi_res_object = context.object.copy()
    object_ref: bpy.types.Object = context.object.sculpting_layers_properties.multi_res_object
    object_ref.data = context.object.data.copy()

    # Add Fake User To New Object To Preserve on Save
    object_ref.use_fake_user = True

    # Get Modifier Name
    modifier_name = context.object.sculpting_layers_properties.multi_res_modifier_name
    # Get Modifier on New Object
    modifier = object_ref.modifiers[modifier_name]

    # Set the Modifier on New Object to Highest Level
    modifier.levels = modifier.total_levels
    modifier.sculpt_levels = modifier.total_levels
    modifier.render_levels = modifier.total_levels

    # Link New Object to Collection
    bpy.context.collection.objects.link(object_ref)
    # Set the New Object as Active
    bpy.context.view_layer.objects.active = object_ref

    # Change New Object Mode to OBJECT
    bpy.ops.object.mode_set(mode='OBJECT')
    # Apply Modifier on New Object
    bpy.ops.object.modifier_apply(modifier=modifier_name)

    # Reset the Active Object to The Original Sculpting Object
    bpy.context.view_layer.objects.active = sculpting_object_ref
    # Unlink New Object from Collection
    bpy.context.collection.objects.unlink(object_ref)
    # Reset the Original Object Mode to SCULPT
    bpy.ops.object.mode_set(mode='SCULPT')


def clear_resolution_config_callback(context):
    """
    Decrease Resolution

    :param context: Current Context
    :type context: bpy.context

    :return:
    """
    # TODO: Move Function To Multi Resolution Module
    # TODO: Purge Object Mesh Data
    # bpy.data.meshes.remove(context.object.sculpting_layers_properties.multi_res_object.data,  do_unlink=True)
    if context.object.sculpting_layers_properties.multi_res_object is None:
        return
    # Delete the Duplicate Object
    bpy.data.objects.remove(context.object.sculpting_layers_properties.multi_res_object,  do_unlink=True)


def add_layer_callback(context):
    context.object.sculpting_layers_properties.layers.add()


def delete_layer_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers.remove(layer_index)


def delete_all_layers_callback(context):
    context.object.sculpting_layers_properties.layers.clear()


def apply_layer_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers.remove(layer_index)


def apply_all_layers_callback(context):
    context.object.sculpting_layers_properties.layers.clear()


def hide_layer_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers[layer_index].is_enabled = False


def show_layer_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers[layer_index].is_enabled = True


def start_layer_recording_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers[layer_index].is_recording = True


def stop_layer_recording_callback(context, layer_index):
    context.object.sculpting_layers_properties.layers[layer_index].is_recording = False

