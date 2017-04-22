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

from tvtk.tvtk_classes.abstract_image_interpolator import AbstractImageInterpolator


class ImageInterpolator(AbstractImageInterpolator):
    """
    ImageInterpolator - interpolate data values from images
    
    Superclass: AbstractImageInterpolator
    
    ImageInterpolator provides a simple interface for interpolating
    image data.  It provides linear, cubic, and nearest-neighbor
    interpolation.@par Thanks: Thanks to David Gobbi at the Seaman Family
    MR Centre and Dept. of Clinical Neurosciences, Foothills Medical
    Centre, Calgary, for providing this class.
    @sa
    ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageInterpolator, obj, update, **traits)
    
    interpolation_mode = traits.Trait('linear',
    tvtk_base.TraitRevPrefixMap({'linear': 1, 'cubic': 2, 'nearest': 0}), help=\
        """
        The interpolation mode for point scalars (default: linear). 
        Subclasses will provide additional interpolation modes, so this
        is a virtual method.
        """
    )

    def _interpolation_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInterpolationMode,
                        self.interpolation_mode_)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('interpolation_mode',
    'GetInterpolationMode'), ('border_mode', 'GetBorderMode'),
    ('component_count', 'GetComponentCount'), ('component_offset',
    'GetComponentOffset'), ('out_value', 'GetOutValue'), ('tolerance',
    'GetTolerance'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'border_mode',
    'interpolation_mode', 'component_count', 'component_offset',
    'out_value', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['border_mode', 'interpolation_mode'], ['component_count',
            'component_offset', 'out_value', 'tolerance']),
            title='Edit ImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

