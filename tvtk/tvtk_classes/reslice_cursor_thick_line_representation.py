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

from tvtk.tvtk_classes.reslice_cursor_line_representation import ResliceCursorLineRepresentation


class ResliceCursorThickLineRepresentation(ResliceCursorLineRepresentation):
    """
    ResliceCursorThickLineRepresentation - represents a thick slab of
    the reslice cursor widget
    
    Superclass: ResliceCursorLineRepresentation
    
    This class respresents a thick reslice cursor, that can be used to
    perform interactive thick slab MPR's through data. The class
    internally uses ImageSlabReslice to do its reslicing. The slab
    thickness is set interactively from the widget. The slab resolution
    (ie the number of blend points) is set as the minimum spacing along
    any dimension from the dataset.
    @sa
    ImageSlabReslice ResliceCursorLineRepresentation
    ResliceCursorWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResliceCursorThickLineRepresentation, obj, update, **traits)
    
    def create_default_reslice_algorithm(self):
        """
        V.create_default_reslice_algorithm()
        C++: virtual void CreateDefaultResliceAlgorithm()
        INTERNAL - Do not use Create the thick reformat class. This
        overrides the superclass implementation and creates a
        ImageSlabReslice instead of a ImageReslice.
        """
        ret = self._vtk_obj.CreateDefaultResliceAlgorithm()
        return ret
        

    def set_reslice_parameters(self, *args):
        """
        V.set_reslice_parameters(float, float, int, int)
        C++: virtual void SetResliceParameters(double outputSpacingX,
            double outputSpacingY, int extentX, int extentY)
        INTERNAL - Do not use Reslice parameters which are set from
        ResliceCursorWidget based on user interactions.
        """
        ret = self._wrap_call(self._vtk_obj.SetResliceParameters, *args)
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
            return super(ResliceCursorThickLineRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResliceCursorThickLineRepresentation properties', scrollable=True, resizable=True,
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
            title='Edit ResliceCursorThickLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResliceCursorThickLineRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

