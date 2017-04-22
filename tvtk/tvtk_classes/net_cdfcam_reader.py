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

from tvtk.tvtk_classes.unstructured_grid_algorithm import UnstructuredGridAlgorithm


class NetCDFCAMReader(UnstructuredGridAlgorithm):
    """
    NetCDFCAMReader - Read unstructured net_cdf CAM files.
    
    Superclass: UnstructuredGridAlgorithm
    
    Reads in a net_cdf CAM (Community Atmospheric Model) file and produces
    and unstructured grid.  The grid is actually unstructured in the X
    and Y directions and rectilinear in the Z direction with all hex
    cells.  The reader requires 2 net_cdf files.  The first is the cell
    connectivity file which has the quad connectivity in the plane. The
    other connectivity file has all of the point and field information.
    Currently this reader ignores time that may exist in the points file.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNetCDFCAMReader, obj, update, **traits)
    
    single_level = tvtk_base.false_bool_trait(help=\
        """
        Set whether or not to read a single level.  A value of one
        indicates that only a single level will be read in. The net_cdf
        variables loaded will then be ones with dimensions of (time,
        ncols).  This will result in a surface grid. Otherwise a
        volumetric grid will be created (if lev > 1) and the variables
        with dimensions of (time, lev, ncols) will be read in. By
        default, single_level = 0.
        """
    )

    def _single_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSingleLevel,
                        self.single_level_)

    cell_layer_right = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify which "side" of the domain to add the connecting cells
        at.  0 indicates left side and 1 indicates right side. The
        default is the right side.@deprecated This method is no longer
        supported. The reader automatically decides which side to pad
        cells on. Using this method has no effect.
        """
    )

    def _cell_layer_right_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCellLayerRight,
                        self.cell_layer_right)

    connectivity_file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )

    def _connectivity_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConnectivityFileName,
                        self.connectivity_file_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_single_level_max_value(self):
        return self._vtk_obj.GetSingleLevelMaxValue()
    single_level_max_value = traits.Property(_get_single_level_max_value, help=\
        """
        Set whether or not to read a single level.  A value of one
        indicates that only a single level will be read in. The net_cdf
        variables loaded will then be ones with dimensions of (time,
        ncols).  This will result in a surface grid. Otherwise a
        volumetric grid will be created (if lev > 1) and the variables
        with dimensions of (time, lev, ncols) will be read in. By
        default, single_level = 0.
        """
    )

    def _get_single_level_min_value(self):
        return self._vtk_obj.GetSingleLevelMinValue()
    single_level_min_value = traits.Property(_get_single_level_min_value, help=\
        """
        Set whether or not to read a single level.  A value of one
        indicates that only a single level will be read in. The net_cdf
        variables loaded will then be ones with dimensions of (time,
        ncols).  This will result in a surface grid. Otherwise a
        volumetric grid will be created (if lev > 1) and the variables
        with dimensions of (time, lev, ncols) will be read in. By
        default, single_level = 0.
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *fileName)
        Returns 1 if this file can be read and 0 if the file cannot be
        read. Because net_cdf CAM files come in pairs and we only check
        one of the files, the result is not definitive.  Invalid files
        may still return 1 although a valid file will never return 0.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    _updateable_traits_ = \
    (('single_level', 'GetSingleLevel'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('cell_layer_right', 'GetCellLayerRight'),
    ('connectivity_file_name', 'GetConnectivityFileName'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'single_level', 'cell_layer_right',
    'connectivity_file_name', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NetCDFCAMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NetCDFCAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['single_level'], [], ['cell_layer_right',
            'connectivity_file_name', 'file_name']),
            title='Edit NetCDFCAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NetCDFCAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

