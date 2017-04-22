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

from tvtk.tvtk_classes.overlapping_amr_algorithm import OverlappingAMRAlgorithm


class AMRBaseReader(OverlappingAMRAlgorithm):
    """
    AMRBaseReader - An abstract class that encapsulates common
    functionality for all AMR readers.
    
    Superclass: OverlappingAMRAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAMRBaseReader, obj, update, **traits)
    
    enable_caching = tvtk_base.false_bool_trait(help=\
        """
        Set/Get Reader caching property
        """
    )

    def _enable_caching_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEnableCaching,
                        self.enable_caching_)

    def get_cell_array_status(self, *args):
        """
        V.get_cell_array_status(string) -> int
        C++: int GetCellArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayStatus, *args)
        return ret

    def set_cell_array_status(self, *args):
        """
        V.set_cell_array_status(string, int)
        C++: void SetCellArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetCellArrayStatus, *args)
        return ret

    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set/Get a multiprocess-controller for reading in parallel. By
        default this parameter is set to NULL by the constructor.
        """
    )

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set/Get the filename. Concrete instances of this class must
        implement the set_file_name method accordingly.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def get_point_array_status(self, *args):
        """
        V.get_point_array_status(string) -> int
        C++: int GetPointArrayStatus(const char *name)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayStatus, *args)
        return ret

    def set_point_array_status(self, *args):
        """
        V.set_point_array_status(string, int)
        C++: void SetPointArrayStatus(const char *name, int status)
        Get/Set whether the point or cell array with the given name is to
        be read.
        """
        ret = self._wrap_call(self._vtk_obj.SetPointArrayStatus, *args)
        return ret

    def get_cell_array_name(self, *args):
        """
        V.get_cell_array_name(int) -> string
        C++: const char *GetCellArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellArrayName, *args)
        return ret

    def _get_cell_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetCellDataArraySelection())
    cell_data_array_selection = traits.Property(_get_cell_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def _get_number_of_blocks(self):
        return self._vtk_obj.GetNumberOfBlocks()
    number_of_blocks = traits.Property(_get_number_of_blocks, help=\
        """
        Returns the total number of blocks. Implemented by concrete
        instances.
        """
    )

    def _get_number_of_cell_arrays(self):
        return self._vtk_obj.GetNumberOfCellArrays()
    number_of_cell_arrays = traits.Property(_get_number_of_cell_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def _get_number_of_levels(self):
        return self._vtk_obj.GetNumberOfLevels()
    number_of_levels = traits.Property(_get_number_of_levels, help=\
        """
        Returns the total number of levels. Implemented by concrete
        instances.
        """
    )

    def _get_number_of_point_arrays(self):
        return self._vtk_obj.GetNumberOfPointArrays()
    number_of_point_arrays = traits.Property(_get_number_of_point_arrays, help=\
        """
        Get the number of point or cell arrays available in the input.
        """
    )

    def get_point_array_name(self, *args):
        """
        V.get_point_array_name(int) -> string
        C++: const char *GetPointArrayName(int index)
        Get the name of the point or cell array with the given index in
        the input.
        """
        ret = self._wrap_call(self._vtk_obj.GetPointArrayName, *args)
        return ret

    def _get_point_data_array_selection(self):
        return wrap_vtk(self._vtk_obj.GetPointDataArraySelection())
    point_data_array_selection = traits.Property(_get_point_data_array_selection, help=\
        """
        Get the data array selection tables used to configure which data
        arrays are loaded by the reader.
        """
    )

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Initializes the AMR reader. All concrete instances must call this
        method in their constructor.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def is_caching_enabled(self):
        """
        V.is_caching_enabled() -> bool
        C++: bool IsCachingEnabled()
        Set/Get Reader caching property
        """
        ret = self._vtk_obj.IsCachingEnabled()
        return ret
        

    def set_max_level(self, *args):
        """
        V.set_max_level(int)
        C++: void SetMaxLevel(int a)
        Set the level, up to which the blocks are loaded.
        """
        ret = self._wrap_call(self._vtk_obj.SetMaxLevel, *args)
        return ret

    _updateable_traits_ = \
    (('enable_caching', 'GetEnableCaching'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'enable_caching',
    'global_warning_display', 'release_data_flag', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AMRBaseReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AMRBaseReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['enable_caching'], [], ['file_name']),
            title='Edit AMRBaseReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AMRBaseReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

