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

from tvtk.tvtk_classes.object import Object


class XMLHierarchicalBoxDataFileConverter(Object):
    """
    XMLHierarchicalBoxDataFileConverter - converts older *.vth, *.vthb
    files to newer format.
    
    Superclass: Object
    
    XMLHierarchicalBoxDataFileConverter is a utility class to convert
    v0.1 and v1.0 of the VTK XML hierarchical file format to the v1.1.
    Users can then use XMLUniformGridAMRReader to read the dataset
    into VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXMLHierarchicalBoxDataFileConverter, obj, update, **traits)
    
    input_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the input filename.
        """
    )

    def _input_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputFileName,
                        self.input_file_name)

    output_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the output filename.
        """
    )

    def _output_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputFileName,
                        self.output_file_name)

    def convert(self):
        """
        V.convert() -> bool
        C++: bool Convert()
        Converts the input file to new format and writes out the output
        file.
        """
        ret = self._vtk_obj.Convert()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('input_file_name', 'GetInputFileName'),
    ('output_file_name', 'GetOutputFileName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'input_file_name',
    'output_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XMLHierarchicalBoxDataFileConverter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XMLHierarchicalBoxDataFileConverter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['input_file_name', 'output_file_name']),
            title='Edit XMLHierarchicalBoxDataFileConverter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XMLHierarchicalBoxDataFileConverter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

