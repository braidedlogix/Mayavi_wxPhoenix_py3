# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui.item import Item, spring
from traitsui.group import HGroup
from traitsui.view import View

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk


def InstanceEditor(*args, **kw):
    from traitsui.editors.api import InstanceEditor as Editor
    return Editor(view_name="handler.view")

try:
    long
except NameError:
    # Silly workaround for Python3.
    long = int

from tvtk.tvtk_classes.reslice_cursor_representation import ResliceCursorRepresentation


class ResliceCursorLineRepresentation(ResliceCursorRepresentation):
    """
    ResliceCursorLineRepresentation - represent the
    ResliceCursorWidget
    
    Superclass: ResliceCursorRepresentation
    
    This class provides a representation for the reslice cursor widget.
    It consists of two cross sectional hairs, with an optional thickness.
    The hairs may have a hole in the center. These may be translated or
    rotated independent of each other in the view. The result is used to
    reslice the data along these cross sections. This allows the user to
    perform multi-planar thin or thick reformat of the data on an image
    view, rather than a 3d view.
    @sa
    ResliceCursorWidget ResliceCursor
    ResliceCursorPolyDataAlgorithm ResliceCursorRepresentation
    ResliceCursorThickLineRepresentation ResliceCursorActor
    ImagePlaneWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorLineRepresentation, obj, update, **traits)
    
    def _get_reslice_cursor_actor(self):
        return wrap_vtk(self._vtk_obj.GetResliceCursorActor())
    reslice_cursor_actor = traits.Property(_get_reslice_cursor_actor, help=\
        """
        Get the reslice cursor actor. You must set the reslice cursor on
        this class
        """
    )

    def set_user_matrix(self, *args):
        """
        V.set_user_matrix(Matrix4x4)
        C++: virtual void SetUserMatrix(Matrix4x4 *matrix)
        Set the user matrix on all the internal actors.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUserMatrix, *my_args)
        return ret

    _updateable_traits_ = \
    (('display_text', 'GetDisplayText'), ('restrict_plane_to_volume',
    'GetRestrictPlaneToVolume'), ('show_resliced_image',
    'GetShowReslicedImage'), ('use_image_actor', 'GetUseImageActor'),
    ('need_to_render', 'GetNeedToRender'), ('picking_managed',
    'GetPickingManaged'), ('dragable', 'GetDragable'), ('pickable',
    'GetPickable'), ('use_bounds', 'GetUseBounds'), ('visibility',
    'GetVisibility'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('manipulation_mode',
    'GetManipulationMode'), ('thickness_label_format',
    'GetThicknessLabelFormat'), ('tolerance', 'GetTolerance'),
    ('handle_size', 'GetHandleSize'), ('place_factor', 'GetPlaceFactor'),
    ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'display_text', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'picking_managed',
    'restrict_plane_to_volume', 'show_resliced_image', 'use_bounds',
    'use_image_actor', 'visibility', 'estimated_render_time',
    'handle_size', 'manipulation_mode', 'place_factor',
    'render_time_multiplier', 'thickness_label_format', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResliceCursorLineRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['display_text', 'need_to_render', 'picking_managed',
            'restrict_plane_to_volume', 'show_resliced_image', 'use_bounds',
            'use_image_actor', 'visibility'], [], ['estimated_render_time',
            'handle_size', 'manipulation_mode', 'place_factor',
            'render_time_multiplier', 'thickness_label_format', 'tolerance']),
            title='Edit ResliceCursorLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

