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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ParticleReader(PolyDataAlgorithm):
    """
    ParticleReader - Read ASCII or binary particle
                               data and (optionally) one scalar
                               value associated with each particle.
    
    Superclass: PolyDataAlgorithm
    
    ParticleReader reads either a binary or a text file of
     particles. Each particle can have associated with it an optional
     scalar value. So the format is: x, y, z, scalar
     (all floats or doubles). The text file can consist of a comma
     delimited set of values. In most cases ParticleReader can
     automatically determine whether the file is text or binary.
     The data can be either float or double.
     Progress updates are provided.
     With respect to binary files, random access into the file to read
     pieces is supported.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParticleReader, obj, update, **traits)
    
    has_scalar = tvtk_base.true_bool_trait(help=\
        """
        Default: 1. If 1 then each particle has a value associated with
        it.
        """
    )

    def _has_scalar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHasScalar,
                        self.has_scalar_)

    swap_bytes = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the byte swapping to explicitly swap the bytes of a file.
        Not used when reading text files.
        """
    )

    def _swap_bytes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSwapBytes,
                        self.swap_bytes_)

    data_byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'little_endian': 1, 'big_endian': 0}), help=\
        """
        These methods should be used instead of the swap_bytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a big_endian file on a big_endian
        machine will result in no swapping. Trying to read the same file
        on a little_endian machine will result in swapping. As a quick
        note most UNIX machines are big_endian while PC's and VAX tend to
        be little_endian. So if the file you are reading in was generated
        on a VAX or PC, set_data_byte_order_to_little_endian otherwise
        set_data_byte_order_to_big_endian. Not used when reading text files.
        """
    )

    def _data_byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataByteOrder,
                        self.data_byte_order_)

    data_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'float': 10, 'double': 11}), help=\
        """
        Get/Set the data type.  The options are:
        - VTK_FLOAT (default) single precision floating point.
        - VTK_DOUBLE double precision floating point.
        """
    )

    def _data_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataType,
                        self.data_type_)

    file_type = traits.Trait('unknown',
    tvtk_base.TraitRevPrefixMap({'unknown': 0, 'binary': 2, 'text': 1}), help=\
        """
        Get/Set the file type.  The options are:
        - FILE_TYPE_IS_UNKNOWN (default) the class will attempt to
          determine the file type. If this fails then you should set the
          file type yourself.
        - FILE_TYPE_IS_TEXT the file type is text.
        - FILE_TYPE_IS_BINARY the file type is binary.
        """
    )

    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name.
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

    _updateable_traits_ = \
    (('has_scalar', 'GetHasScalar'), ('swap_bytes', 'GetSwapBytes'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('data_byte_order', 'GetDataByteOrder'), ('data_type', 'GetDataType'),
    ('file_type', 'GetFileType'), ('file_name', 'GetFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'has_scalar',
    'release_data_flag', 'swap_bytes', 'data_byte_order', 'data_type',
    'file_type', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParticleReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParticleReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['has_scalar', 'swap_bytes'], ['data_byte_order', 'data_type',
            'file_type'], ['file_name']),
            title='Edit ParticleReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParticleReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

