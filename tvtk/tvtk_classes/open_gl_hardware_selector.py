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

from tvtk.tvtk_classes.hardware_selector import HardwareSelector


class OpenGLHardwareSelector(HardwareSelector):
    """
    OpenGLHardwareSelector - implements the device specific code of
     OpenGLHardwareSelector.
    
    Superclass: HardwareSelector
    
    Implements the device specific code of OpenGLHardwareSelector.
    
    @sa
    HardwareSelector
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLHardwareSelector, obj, update, **traits)
    
    def begin_selection(self):
        """
        V.begin_selection()
        C++: virtual void BeginSelection()"""
        ret = self._vtk_obj.BeginSelection()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('area', 'GetArea'), ('field_association',
    'GetFieldAssociation'), ('process_id', 'GetProcessID'),
    ('prop_color_value', 'GetPropColorValue'),
    ('use_process_id_from_data', 'GetUseProcessIdFromData'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ('prop_color_value',)
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'area', 'field_association',
    'process_id', 'prop_color_value', 'use_process_id_from_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLHardwareSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLHardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['area', 'field_association', 'process_id',
            'prop_color_value', 'use_process_id_from_data']),
            title='Edit OpenGLHardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLHardwareSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

