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

from tvtk.tvtk_classes.molecule_reader_base import MoleculeReaderBase


class XYZMolReader(MoleculeReaderBase):
    """
    XYZMolReader - read Molecular Data files
    
    Superclass: MoleculeReaderBase
    
    XYZMolReader is a source object that reads Molecule files The
    file_name must be specified
    
    @par Thanks: Dr. Jean M. Favre who developed and contributed this
    class
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkXYZMolReader, obj, update, **traits)
    
    time_step = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the current time step. It should be greater than 0 and
        smaller than max_time_step.
        """
    )

    def _time_step_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTimeStep,
                        self.time_step)

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

    def _get_max_time_step(self):
        return self._vtk_obj.GetMaxTimeStep()
    max_time_step = traits.Property(_get_max_time_step, help=\
        """
        Get the maximum time step.
        """
    )

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: virtual int CanReadFile(const char *name)
        Test whether the file with the given name can be read by this
        reader.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('time_step',
    'GetTimeStep'), ('b_scale', 'GetBScale'), ('file_name',
    'GetFileName'), ('hb_scale', 'GetHBScale'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'b_scale', 'file_name', 'hb_scale',
    'progress_text', 'time_step'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(XYZMolReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit XYZMolReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['b_scale', 'file_name', 'hb_scale', 'time_step']),
            title='Edit XYZMolReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit XYZMolReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

