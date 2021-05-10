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
from bpy.types import MultiresModifier
from ..single_res import callbacks as single_res_callbacks
from ..common.properties import LayerProperties
from ..common import helpers


# TODO: Document Multi Resolution Callbacks


def disable_sculpting_layers_callback(context):
    """
    Disable Sculpting Layers

    :param context: Current Context
    :type context: bpy.context
    """
    # delete_all_layers_callback(context)
    single_res_callbacks.delete_all_layers_callback(context)
    context.object.sculpting_layers.is_enabled_status = False


# TODO: Fix Update Modifier Name When Change By User
def enable_multi_resolution(context):
    """
    Enable Multi Resolution

    :param context: Current Context
    :type context: bpy.context
    """
    # Clear Sculpting Layers
    # delete_all_layers_callback(context)
    single_res_callbacks.delete_all_layers_callback(context)

    # Clear Shape Keys
    context.object.shape_key_clear()

    # Add MutiRes Modifier
    bpy.ops.object.modifier_add(type='MULTIRES')
    modifier: MultiresModifier = context.object.modifiers["Multires"]
    # Name the Modifier
    modifier.name = "Sculpting Layers"
    # Copy the name to the Addon Properties and Store it in Object
    context.object.sculpting_layers.multi_res_modifier_name = "Sculpting Layers"

    context.object.sculpting_layers.multi_resolution_enabled_status = True


# TODO: Fix Update Modifier Name When Change By User
def disable_multi_resolution(context):
    """
    Disable Multi Resolution

    :param context: Current Context
    :type context: bpy.context
    """
    # Clear Sculpting Layers
    # delete_all_layers_callback(context)
    single_res_callbacks.delete_all_layers_callback(context)

    # Clear Configurations
    clear_resolution_config_callback(context)

    # Remove Modifier
    modifier = context.object.modifiers[context.object.sculpting_layers.multi_res_modifier_name]
    context.object.modifiers.remove(modifier)

    context.object.sculpting_layers.multi_resolution_enabled_status = False


def increase_resolution_callback(context):
    """
    Subdivide Mesh to Increase Resolution

    :param context:
    :type context: bpy.context

    :return:
    """
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers.multi_res_modifier_name

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
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers.multi_res_modifier_name

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
    # Get Modifier Name
    modifier_name = context.object.sculpting_layers.multi_res_modifier_name

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
    # Get the Sculpting Original Object
    sculpting_object_ref: bpy.types.Object = context.object

    # Copy Object Data to new Object and Save the reference
    context.object.sculpting_layers.multi_res_object = context.object.copy()
    object_ref: bpy.types.Object = context.object.sculpting_layers.multi_res_object
    object_ref.data = context.object.data.copy()

    # Add Fake User To New Object To Preserve on Save
    object_ref.use_fake_user = True

    # Get Modifier Name
    modifier_name = context.object.sculpting_layers.multi_res_modifier_name
    # Get Modifier on New Object
    modifier = object_ref.modifiers[modifier_name]

    # Set the Modifier on New Object to Highest Level
    modifier.levels = modifier.total_levels
    modifier.sculpt_levels = modifier.total_levels
    modifier.render_levels = modifier.total_levels

    # Link New Object to Collection
    context.collection.objects.link(object_ref)
    # Set the New Object as Active
    context.view_layer.objects.active = object_ref

    # Change New Object Mode to OBJECT
    bpy.ops.object.mode_set(mode='OBJECT')
    # Apply Modifier on New Object
    bpy.ops.object.modifier_apply(modifier=modifier_name)

    # Reset the Active Object to The Original Sculpting Object
    context.view_layer.objects.active = sculpting_object_ref
    # Unselect Object
    object_ref.select_set(False)
    # Unlink New Object from Collection
    if not helpers.is_debug():
        context.collection.objects.unlink(object_ref)
    # Reset the Original Object Mode to SCULPT
    # bpy.ops.object.mode_set(mode='SCULPT')


def clear_resolution_config_callback(context):
    """
    Decrease Resolution

    :param context: Current Context
    :type context: bpy.context

    :return:
    """
    # TODO: Purge Object Mesh Data
    # bpy.data.meshes.remove(context.object.sculpting_layers.multi_res_object.data,  do_unlink=True)
    if context.object.sculpting_layers.multi_res_object is None:
        return
    # Delete the Duplicate Object
    bpy.data.objects.remove(context.object.sculpting_layers.multi_res_object,  do_unlink=True)


def add_layer_callback(context):
    """
    Add New Layer

    :param context: Current Context
    :type context: bpy.context
    """
    # Get the Sculpting Original Object
    sculpting_object_ref: bpy.types.Object = context.object
    # bpy.ops.object.mode_set(mode='OBJECT')
    # bpy.ops.object.select_all(action='DESELECT')

    # If No Shape Keys Present Create Base Shape Key
    if context.object.sculpting_layers.multi_res_object.data.shape_keys is None:
        # Select Proxy Object
        # context.view_layer.objects.active = context.object.sculpting_layers.multi_res_object
        # Add Shape Key
        context.object.sculpting_layers.multi_res_object.shape_key_add(name="SL_MORPH")
        # Reset Selection
        # context.view_layer.objects.active = sculpting_object_ref
        # context.object.sculpting_layers.last_mix_relative_key_name = "SL_MORPH"

    # bpy.ops.object.mode_set(mode='SCULPT')
    # Create New Layer
    new_layer: LayerProperties = context.object.sculpting_layers.layers.add()
    new_layer.shape_key_name = "NEW"


def delete_layer_callback(context, layer_index):
    """
    Delete a Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Get the Layer From Index
    layer: LayerProperties = context.object.sculpting_layers.layers[layer_index]

    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Mute the shape Key
    morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = True
    # Remove Layer
    context.object.sculpting_layers.layers.remove(layer_index)

    reshape_object(context, morph_object)

    # TODO: Fix Applying Layer To Improve Performance
    # Temporary Solution For Not Actually Applying Layer
    if len(context.object.sculpting_layers.layers) == 0:
        apply_all_layers_callback(context)


def delete_all_layers_callback(context):
    """
    Delete All Layers

    :param context: Current Context
    :type context: bpy.context
    """
    for index in reversed(range(len(context.object.sculpting_layers.layers))):
        delete_layer_callback(context, index)


def apply_layer_callback(context, layer_index):
    """
    Apply A Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Temporary Fix (Just Remove the Layer and Leave the ShapeKey)
    context.object.sculpting_layers.layers.remove(layer_index)

    # Temporary Solution For Not Actually Applying Layer
    if len(context.object.sculpting_layers.layers) == 0:
        apply_all_layers_callback(context)


def apply_all_layers_callback(context):
    """
    Apply All Layers

    :param context: Current Context
    :type context: bpy.context
    """
    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Add New Shape From Mix (Saves the Mesh Data)
    new_shape_key = morph_object.shape_key_add(name="SL_MORPH_0", from_mix=True)

    # Delete All Shape Keys except last
    for key_to_remove in morph_object.data.shape_keys.key_blocks[0:-1]:
        # Remove the Shape Key
        morph_object.shape_key_remove(key_to_remove)

    # Remove Layers
    context.object.sculpting_layers.layers.clear()

    # Set New Shape Key and Value
    new_shape_key.name = "SL_MORPH"  # Could Be Removed
    new_shape_key.value = 1
    # Clear All ShapeKeys
    morph_object.shape_key_clear()

    reshape_object(context, morph_object)


def reshape_object(context, morph_object):
    sculpting_object_ref: bpy.types.Object = context.object

    # Get Modifier Name
    modifier_name = sculpting_object_ref.sculpting_layers.multi_res_modifier_name
    # Get Modifier on New Object
    modifier = sculpting_object_ref.modifiers[modifier_name]

    # Set the Modifier on Object to Highest Level
    modifier.levels = modifier.total_levels

    if not helpers.is_debug():
        context.collection.objects.link(morph_object)
    morph_object.select_set(True)

    # Reshape Object
    bpy.ops.object.multires_reshape(modifier=modifier_name)

    # Unlink Morph Object
    if not helpers.is_debug():
        context.collection.objects.unlink(morph_object)


def hide_layer_callback(context, layer_index):
    """
    Hide A Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Get the Selected Layer
    layer: LayerProperties = context.object.sculpting_layers.layers[layer_index]

    if layer.shape_key_name == "NEW":
        return

    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Mute the Shape Key which is Connected to Layer
    morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = True
    # Disable Layer
    context.object.sculpting_layers.layers[layer_index].is_enabled = False

    reshape_object(context, morph_object)


def show_layer_callback(context, layer_index):
    """
    Show A Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Get the Selected Layer
    layer: LayerProperties = context.object.sculpting_layers.layers[layer_index]

    if layer.shape_key_name == "NEW":
        return

    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Mute the Shape Key which is Connected to Layer
    morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = False
    # Disable Layer
    context.object.sculpting_layers.layers[layer_index].is_enabled = True

    reshape_object(context, morph_object)


def start_layer_recording_callback(context, layer_index):
    """
    Start Recording on a Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Get the Selected Layer
    layer: LayerProperties = context.object.sculpting_layers.layers[layer_index]

    # Get the Sculpting Original Object
    sculpting_object_ref: bpy.types.Object = context.object

    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Reset Shape Keys values
    for layer in context.object.sculpting_layers.layers:
        # Update Morph Object Shape Key Weight
        if layer.shape_key_name != "NEW":
            morph_object.data.shape_keys.key_blocks[layer.shape_key_name].value = 1
            morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = False

    reshape_object(context, morph_object)

    # Start Layer Recording
    layer.is_recording = True


def stop_layer_recording_callback(context, layer_index):
    """
    Stop Recording on a Layer

    :param context: Current Context
    :type context: bpy.context

    :param layer_index: Selected Layer Index
    :type layer_index: int
    """
    # Get the Sculpting Original Object
    sculpting_object_ref: bpy.types.Object = context.object

    # Change Sculpting Object Mode to OBJECT
    bpy.ops.object.mode_set(mode='OBJECT')

    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Copy Object Data to new Object
    object_ref: bpy.types.Object = context.object.copy()
    object_ref.data = context.object.data.copy()

    # Get Modifier Name
    modifier_name = sculpting_object_ref.sculpting_layers.multi_res_modifier_name
    # Get Modifier on New Object
    modifier = object_ref.modifiers[modifier_name]

    # Set the Modifier on New Object to Highest Level
    modifier.levels = modifier.total_levels
    # modifier.sculpt_levels = modifier.total_levels
    # modifier.render_levels = modifier.total_levels

    # Link New & Morph Objects to Collection
    if not helpers.is_debug():
        context.collection.objects.link(morph_object)
    context.collection.objects.link(object_ref)
    # Set the New Object as Active
    context.view_layer.objects.active = object_ref

    # Change New Object Mode to OBJECT
    bpy.ops.object.mode_set(mode='OBJECT')

    # Select Original Object
    sculpting_object_ref.select_set(True)

    # Reshape Object
    bpy.ops.object.multires_reshape(modifier=modifier_name)

    # Apply Modifier on New Object
    bpy.ops.object.modifier_apply(modifier=modifier_name)

    sculpting_object_ref.select_set(False)

    object_ref.shape_key_add(from_mix=True)
    # object_ref.active_shape_key_index = 0

    morph_object.select_set(True)
    context.view_layer.objects.active = morph_object

    bpy.ops.object.join_shapes()

    bpy.data.objects.remove(object_ref, do_unlink=True)

    temp_shape_key = morph_object.data.shape_keys.key_blocks[-1]
    temp_shape_key.value = 1
    temp_shape_key.slider_min = -1

    # temp_key_name = object_ref.active_shape_key.name

    for key in morph_object.data.shape_keys.key_blocks[0:-1]:
        layer = sculpting_object_ref.sculpting_layers.layers[layer_index]
        if layer.shape_key_name != key.name:
            key.mute = True

    morph_object.shape_key_add(from_mix=True)
    new_shape_key = morph_object.data.shape_keys.key_blocks[-1]
    new_shape_key.name = "SL"
    new_shape_key.value = 1
    new_shape_key.slider_min = -1

    morph_object.shape_key_remove(temp_shape_key)
    new_shape_key.relative_key = morph_object.data.shape_keys.key_blocks[-2]

    if sculpting_object_ref.sculpting_layers.layers[layer_index].shape_key_name != "NEW":
        morph_object.data.shape_keys.key_blocks[sculpting_object_ref.sculpting_layers.layers[layer_index].shape_key_name].mute = True

    sculpting_object_ref.sculpting_layers.layers[layer_index].shape_key_name = new_shape_key.name
    sculpting_object_ref.sculpting_layers.layers[layer_index].is_recording = False

    for layer in sculpting_object_ref.sculpting_layers.layers:
        morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = False

    # Reset the Active Object to The Original Sculpting Object
    sculpting_object_ref.select_set(True)
    context.view_layer.objects.active = sculpting_object_ref
    bpy.ops.object.mode_set(mode='SCULPT')

    # Unlink Morph Object
    if not helpers.is_debug():
        context.collection.objects.unlink(morph_object)

    # Reapply Shape Keys values
    for layer in context.object.sculpting_layers.layers:
        # Update Morph Object Shape Key Weight
        if layer.shape_key_name != "NEW":
            morph_object.data.shape_keys.key_blocks[layer.shape_key_name].value = layer.weight
            morph_object.data.shape_keys.key_blocks[layer.shape_key_name].mute = not layer.is_enabled

    reshape_object(context, morph_object)


def update_layer_weight_callback(context, shape_key_name, weight):
    """
    Update Layer Weight
    :param context: Current Context
    :type context: bpy.context
    """
    if shape_key_name == "NEW":
        return

    # Get the Sculpting & Morph Object
    morph_object: bpy.types.Object = context.object.sculpting_layers.multi_res_object

    # Update Morph Object Shape Key Weight
    morph_object.data.shape_keys.key_blocks[shape_key_name].value = weight

    reshape_object(context, morph_object)
