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


