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

from tvtk.tvtk_classes.image_stencil_source import ImageStencilSource


class ROIStencilSource(ImageStencilSource):
    """
    ROIStencilSource - create simple mask shapes
    
    Superclass: ImageStencilSource
    
    ROIStencilSource will create an image stencil with a simple shape
    like a box, a sphere, or a cylinder.  Its output can be used with
    ImageStecil or other vtk classes that apply a stencil to an image.
    @sa
    ImplicitFunctionToImageStencil LassoStencilSource@par Thanks:
    Thanks to David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkROIStencilSource, obj, update, **traits)
    
    shape = traits.Trait('box',
    tvtk_base.TraitRevPrefixMap({'box': 0, 'cylinder_x': 2, 'cylinder_y': 3, 'cylinder_z': 4, 'ellipsoid': 1}), help=\
        """
        The shape of the region of interest.  Cylinders can be oriented
        along the X, Y, or Z axes.  The default shape is "Box".
        """
    )

    def _shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShape,
                        self.shape_)

    bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBounds,
                        self.bounds)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('shape',
    'GetShape'), ('bounds', 'GetBounds'), ('output_origin',
    'GetOutputOrigin'), ('output_spacing', 'GetOutputSpacing'),
    ('output_whole_extent', 'GetOutputWholeExtent'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'shape', 'bounds', 'output_origin',
    'output_spacing', 'output_whole_extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ROIStencilSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['shape'], ['bounds', 'output_origin', 'output_spacing',
            'output_whole_extent']),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ROIStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

