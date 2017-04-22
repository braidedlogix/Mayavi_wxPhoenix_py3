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

from tvtk.tvtk_classes.open_foam_reader import OpenFOAMReader


class POpenFOAMReader(OpenFOAMReader):
    """
    POpenFOAMReader - reads a decomposed dataset in open_foam format
    
    Superclass: OpenFOAMReader
    
    POpenFOAMReader creates a multiblock dataset. It reads
    parallel-decomposed mesh information and time dependent data.  The
    poly_mesh folders contain mesh information. The time folders contain
    transient data for the cells. Each folder can contain any number of
    data files.
    
    @par Thanks: This class was developed by Takuya Oshima at Niigata
    University, Japan (oshima@eng.niigata-u.ac.jp).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPOpenFOAMReader, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Set and get the controller.
        """
    )

    _updateable_traits_ = \
    (('add_dimensions_to_array_names', 'GetAddDimensionsToArrayNames'),
    ('cache_mesh', 'GetCacheMesh'), ('create_cell_to_point',
    'GetCreateCellToPoint'), ('decompose_polyhedra',
    'GetDecomposePolyhedra'), ('list_time_steps_by_control_dict',
    'GetListTimeStepsByControlDict'), ('positions_is_in13_format',
    'GetPositionsIsIn13Format'), ('read_zones', 'GetReadZones'),
    ('use64_bit_labels', 'GetUse64BitLabels'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('file_name', 'GetFileName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'add_dimensions_to_array_names', 'cache_mesh',
    'create_cell_to_point', 'debug', 'decompose_polyhedra',
    'global_warning_display', 'list_time_steps_by_control_dict',
    'positions_is_in13_format', 'read_zones', 'release_data_flag',
    'use64_bit_labels', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(POpenFOAMReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit POpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['add_dimensions_to_array_names', 'cache_mesh',
            'create_cell_to_point', 'decompose_polyhedra',
            'list_time_steps_by_control_dict', 'positions_is_in13_format',
            'read_zones', 'use64_bit_labels'], [], ['file_name']),
            title='Edit POpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit POpenFOAMReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

