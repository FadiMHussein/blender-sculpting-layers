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
import bpy
from ..common.properties import LayerProperties
from ..common import helpers


def disable_sculpting_layers_callback(context):
    """
    Disable Sculpting Layers

    :param context: Current Context
    :type context: bpy.context
    """
    delete_all_layers_callback(context)
    context.object.sculpting_layers.is_enabled_status = False


def add_layer_callback(context):
    """
    Add New Layer

    :param context: Current Context
    :type context: bpy.context
    """
    # If No Shape Keys Present Create Base Shape Key
    if context.object.data.shape_keys is None:
        context.object.shape_key_add(name="SL_MORPH")
        context.object.sculpting_layers.last_mix_relative_key_name = "SL_MORPH"

    # TODO: Fix Applying Layer To Improve Performance
    # relative_key_name = context.object.sculpting_layers.last_mix_relative_key_name
    # Create New ShapeKey
    name = "SL"
    new_shape_key = context.object.shape_key_add(name=name, from_mix=False)
    # Related to Applying Layer Fix
    # new_shape_key.relative_key = context.object.data.shape_keys.key_blocks[relative_key_name]
    # Apply Shape Key Value to Enable Sculpting
    new_shape_key.value = 1
    # Extend Shape Key Min to -1
    new_shape_key.slider_min = -1
    # Create New Layer and Assign ShapeKey
    new_layer: LayerProperties = context.object.sculpting_layers.layers.add()
    # TODO: Fix Key Name Stored in Layer if Related Shape Key Name has Changed
    new_layer.shape_key_name = new_shape_key.name


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
    # Get the ShapeKey to Remove
    key_to_remove = context.object.data.shape_keys.key_blocks[layer.shape_key_name]
    # Remove the Shape Key
    context.object.shape_key_remove(key_to_remove)
    # Remove Layer
    context.object.sculpting_layers.layers.remove(layer_index)

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
    # TODO: Fix Applying Layer (Actually Applying to Morph Mesh)

    """
    layer_to_apply: LayerProperties = context.object.sculpting_layers.layers[layer_index]

    for layer in context.object.sculpting_layers.layers:
        if layer.shape_key_name != layer_to_apply.shape_key_name:
            context.object.data.shape_keys.key_blocks[layer.shape_key_name].mute = True

    new_shape_key = context.object.shape_key_add(name="SL_MORPH", from_mix=True)
    delete_layer_callback(context, layer_index)

    for layer in context.object.sculpting_layers.layers:
        context.object.data.shape_keys.key_blocks[layer.shape_key_name].mute = False

    new_shape_key.value = 1

    context.object.sculpting_layers.last_mix_relative_key_name = new_shape_key.name
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
    # Add New Shape From Mix (Saves the Mesh Data)
    new_shape_key = context.object.shape_key_add(name="SL_MORPH_0", from_mix=True)
    # Delete All Layers
    delete_all_layers_callback(context)
    # Remove the Original ShapeKey (Previous Mesh Base)
    key_to_remove = context.object.data.shape_keys.key_blocks["SL_MORPH"]
    context.object.shape_key_remove(key_to_remove)
    # Set New Shape Key and Value
    new_shape_key.name = "SL_MORPH"  # Could Be Removed
    new_shape_key.value = 1
    # Clear All ShapeKeys
    context.object.shape_key_clear()


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
    # Mute the Shape Key which is Connected to Layer
    context.object.data.shape_keys.key_blocks[layer.shape_key_name].mute = True
    # Disable Layer
    context.object.sculpting_layers.layers[layer_index].is_enabled = False


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
    # Unmute the Shape Key which is Connected to Layer
    context.object.data.shape_keys.key_blocks[layer.shape_key_name].mute = False
    # Enable Layer
    context.object.sculpting_layers.layers[layer_index].is_enabled = True


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
    # Get Shape Key Index which is Connected to Layer
    _, index = helpers.get_shape_key_by_name(context, layer.shape_key_name)
    # Select Shape Key
    context.object.active_shape_key_index = index
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
    # Select Base Mesh Shape Key
    context.object.active_shape_key_index = 0
    # Stop Layer Recording
    context.object.sculpting_layers.layers[layer_index].is_recording = False


def update_layer_weight_callback(context, shape_key_name, weight):
    """
    Update Layer Weight
    :param context: Current Context
    :type context: bpy.context
    """
    # TODO: Allow Changing Weight Max (Needs to Change Layer Weight Slider Also Using Setter Function)
    """
    if weight > context.object.data.shape_keys.key_blocks[shape_key_name].slider_max:
        context.object.data.shape_keys.key_blocks[shape_key_name].slider_max = weight
        context.object.data.shape_keys.key_blocks[shape_key_name].slider_min = -weight

    if weight < context.object.data.shape_keys.key_blocks[shape_key_name].slider_min:
        context.object.data.shape_keys.key_blocks[shape_key_name].slider_min = weight
        context.object.data.shape_keys.key_blocks[shape_key_name].slider_max = -weight
    """
    # Change ShapeKey Value
    context.object.data.shape_keys.key_blocks[shape_key_name].value = weight
