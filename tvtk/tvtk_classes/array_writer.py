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

from tvtk.tvtk_classes.writer import Writer


class ArrayWriter(Writer):
    """
    ArrayWriter - Serialize sparse and dense arrays to a file or
    stream.
    
    Superclass: Writer
    
    ArrayWriter serializes sparse and dense array data using a
    text-based format that is human-readable and easily parsed (default
    option).  The write_binary array option can be used to serialize the
    sparse and dense array data using a binary format that is optimized
    for rapid throughput.
    
    ArrayWriter can be used in two distinct ways: first, it can be
    used as a normal pipeline filter, which writes its inputs to a file. 
    Alternatively, static methods are provided for writing Array
    instances to files or arbitrary c++ streams.
    
    Inputs:
      Input port 0: (required) ArrayData object containing a single
    sparse or dense
                               array.
    
    Output Format:
      See
    http://www.kitware.com/_infovis_wiki/index.php/_n-_way__array__file__formats
    for
      details on how ArrayWriter encodes data.
    
    @sa
    ArrayReader
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkArrayWriter, obj, update, **traits)
    
    binary = tvtk_base.false_bool_trait(help=\
        """
        Get / set whether data will be written in binary format (when
        used as a filter).
        """
    )

    def _binary_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBinary,
                        self.binary_)

    write_to_output_string = tvtk_base.false_bool_trait(help=\
        """
        Whether to output to a string instead of to a file, which is the
        default.
        """
    )

    def _write_to_output_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteToOutputString,
                        self.write_to_output_string_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Get / set the filename where data will be stored (when used as a
        filter).
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_output_string(self):
        return self._vtk_obj.GetOutputString()
    output_string = traits.Property(_get_output_string, help=\
        """
        The output string. This is only set when write_to_output_string is
        set.
        """
    )

    _updateable_traits_ = \
    (('binary', 'GetBinary'), ('write_to_output_string',
    'GetWriteToOutputString'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'binary', 'debug', 'global_warning_display',
    'release_data_flag', 'write_to_output_string', 'file_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ArrayWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['binary', 'write_to_output_string'], [], ['file_name']),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ArrayWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

