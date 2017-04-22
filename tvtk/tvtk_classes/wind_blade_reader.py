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

from tvtk.tvtk_classes.structured_grid_algorithm import StructuredGridAlgorithm


class WindBladeReader(StructuredGridAlgorithm):
    """
    WindBladeReader - class for reading wind_blade data files
    
    Superclass: StructuredGridAlgorithm
    
    WindBladeReader is a source object that reads wind_blade files
    which are block binary files with tags before and after each block
    giving the number of bytes within the block.  The number of data
    variables dumped varies.  There are 3 output ports with the first
    being a structured grid with irregular spacing in the Z dimension.
    The second is an unstructured grid only read on on process 0 and used
    to represent the blade.  The third is also a structured grid with
    irregular spacing on the Z dimension.  Only the first and second
    output ports have time dependent data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWindBladeReader, obj, update, **traits)
    
    filename = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        
        """
    )

    def _filename_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFilename,
                        self.filename)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)"""
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    sub_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(1851859053, 1886284064, 1948284021, 544503909, 1769108595, 170813294), cols=3, help=\
        """
        
        """
    )

    def _sub_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubExtent,
                        self.sub_extent)

    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(1701257332, 1634887022, 544433524, 2037149520, 1635017028, 1869768224), cols=3, help=\
        """
        
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    def _get_blade_output(self):
        return wrap_vtk(self._vtk_obj.GetBladeOutput())
    blade_output = traits.Property(_get_blade_output, help=\
        """
        
        """
    )

    def _get_field_output(self):
        return wrap_vtk(self._vtk_obj.GetFieldOutput())
    field_output = traits.Property(_get_field_output, help=\
        """
        Get the reader's output
        """
    )

    def _get_ground_output(self):
        return wrap_vtk(self._vtk_obj.GetGroundOutput())
    ground_output = traits.Property(_get_ground_output, help=\
        """
        
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        The following methods allow selective reading of solutions
        fields. By default, ALL data fields on the nodes are read, but
        this can be modified.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def disable_all_point_arrays(self):
        """
        V.disable_all_point_arrays()
        C++: void DisableAllPointArrays()"""
        ret = self._vtk_obj.DisableAllPointArrays()
        return ret
        

    def enable_all_point_arrays(self):
        """
        V.enable_all_point_arrays()
        C++: void EnableAllPointArrays()"""
        ret = self._vtk_obj.EnableAllPointArrays()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('filename',
    'GetFilename'), ('sub_extent', 'GetSubExtent'), ('whole_extent',
    'GetWholeExtent'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'filename', 'progress_text', 'sub_extent',
    'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WindBladeReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit WindBladeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['filename', 'sub_extent', 'whole_extent']),
            title='Edit WindBladeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WindBladeReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

