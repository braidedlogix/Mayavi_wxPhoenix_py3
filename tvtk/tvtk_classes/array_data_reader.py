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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class ArrayDataReader(ArrayDataAlgorithm):
    """
    ArrayDataReader - Reads ArrayData written by ArrayDataWriter.
    
    Superclass: ArrayDataAlgorithm
    
    Reads ArrayData data written with ArrayDataWriter.
    
    Outputs:
      Output port 0: ArrayData containing a collection of Arrays.
    
    @sa
    ArrayDataWriter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayDataReader, obj, update, **traits)
    
    read_from_input_string = tvtk_base.false_bool_trait(help=\
        """
        Whether to read from an input string as opposed to a file, which
        is the default.
        """
    )

    def _read_from_input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadFromInputString,
                        self.read_from_input_string_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Set the filesystem location from which data will be read.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    input_string = traits.String('', enter_set=True, auto_set=False, help=\
        """
        The input string to parse. If you set the input string, you must
        also set the read_from_input_string flag to parse the string instead
        of a file.
        """
    )

    def _input_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputString,
                        self.input_string)

    def read(self, *args):
        """
        V.read(string) -> ArrayData
        C++: static ArrayData *Read(StdString str)
        Read an arbitrary array from a string.
        """
        ret = self._wrap_call(self._vtk_obj.Read, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('read_from_input_string', 'GetReadFromInputString'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('input_string', 'GetInputString'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_from_input_string', 'release_data_flag', 'file_name',
    'input_string', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayDataReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_from_input_string'], [], ['file_name', 'input_string']),
            title='Edit ArrayDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayDataReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

