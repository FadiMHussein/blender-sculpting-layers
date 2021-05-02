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
from bpy.types import Panel

from . import validations as multi_res_validations
from .operators import IncreaseResolutionOperator, DecreaseResolutionOperator, UnSubdivideOperator, \
    ApplyResolutionConfigOperator, ClearResolutionConfigOperator
from ..common import validations

from ..common.properties import SculptingLayersProperties


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
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        # Get Addon Properties
        properties: SculptingLayersProperties = context.object.sculpting_layers
        # Check if Layout Should be Enabled and Assign
        enabled = validations.addon_is_enabled(context.object)
        layout.enabled = enabled

        # Spit Validation Message
        if not enabled:
            layout.label(text="Enable Sculpting Layers First")

        enable_row = layout.row(align=True)
        enable_row.enabled = multi_res_validations.can_enable_multires(context.object)
        enable_row.prop(properties, "multi_resolution_enabled")

        can_init = multi_res_validations.can_modify_multi_res_configs(context.object)
        can_change_res = multi_res_validations.can_change_res(context.object)

        res_col = layout.row(align=True)
        res_col.enabled = can_init
        res_col.row().operator(IncreaseResolutionOperator.bl_idname)
        res_col.row().operator(DecreaseResolutionOperator.bl_idname)
        res_col.row().operator(UnSubdivideOperator.bl_idname)

        init_row = layout.row(align=True)
        init_row.enabled = can_init
        init_row.operator(ApplyResolutionConfigOperator.bl_idname, icon="CHECKMARK")

        clear_row = layout.row(align=True)
        clear_row.enabled = not can_init
        clear_row.operator(ClearResolutionConfigOperator.bl_idname, icon="CANCEL")

        if multi_res_validations.can_change_res(context.object):
            viewport_level_row = layout.row(align=True)
            viewport_level_row.enabled = can_change_res
            viewport_level_row.prop(context.object.modifiers["Sculpting Layers"], "levels")

            sculpt_level_row = layout.row(align=True)
            sculpt_level_row.enabled = can_change_res
            sculpt_level_row.prop(context.object.modifiers["Sculpting Layers"], "sculpt_levels")

            render_level_row = layout.row(align=True)
            render_level_row.enabled = can_change_res
            render_level_row.prop(context.object.modifiers["Sculpting Layers"], "render_levels")

