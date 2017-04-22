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


class PLYWriter(Writer):
    """
    PLYWriter - write Stanford PLY file format
    
    Superclass: Writer
    
    PLYWriter writes polygonal data in Stanford University PLY format
    (see http://graphics.stanford.edu/data/_3dscanrep/). The data can be
    written in either binary (little or big endian) or ASCII
    representation. As for point_data and cell_data, PLYWriter cannot
    handle normals or vectors. It only handles RGB point_data and
    cell_data. You need to set the name of the array (using set_name for
    the array and set_array_name for the writer). If the array is not a
    UnsignedCharArray with 3 or 4 components, you need to specify a
    LookupTable to map the scalars to RGB.
    
    @warning
    PLY does not handle big endian versus little endian correctly.
    
    @sa
    PLYReader
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPLYWriter, obj, update, **traits)
    
    color_mode = traits.Trait('default',
    tvtk_base.TraitRevPrefixMap({'default': 0, 'off': 4, 'uniform_cell_color': 1, 'uniform_color': 3, 'uniform_point_color': 2}), help=\
        """
        These methods enable the user to control how to add color into
        the PLY output file. The default behavior is as follows. The user
        provides the name of an array and a component number. If the type
        of the array is three components, unsigned char, then the data is
        written as three separate "red", "green" and "blue" properties.
        If the type of the array is four components, unsigned char, then
        the data is written as three separate "red", "green" and "blue"
        properties, dropping the "alpha". If the type is not unsigned
        char, and a lookup table is provided, then the array/component
        are mapped through the table to generate three separate "red",
        "green" and "blue" properties in the PLY file. The user can also
        set the color_mode to specify a uniform color for the whole part
        (on a vertex colors, face colors, or both. (Note: vertex colors
        or cell colors may be written, depending on where the named array
        is found. If points and cells have the arrays with the same name,
        then both colors will be written.)
        """
    )

    def _color_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColorMode,
                        self.color_mode_)

    data_byte_order = traits.Trait('little_endian',
    tvtk_base.TraitRevPrefixMap({'little_endian': 0, 'big_endian': 1}), help=\
        """
        If the file type is binary, then the user can specify which byte
        order to use (little versus big endian).
        """
    )

    def _data_byte_order_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataByteOrder,
                        self.data_byte_order_)

    file_type = traits.Trait('binary',
    tvtk_base.TraitRevPrefixMap({'binary': 2, 'ascii': 1}), help=\
        """
        Specify file type (ASCII or BINARY) for vtk data file.
        """
    )

    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    texture_coordinates_name = traits.Trait('uv',
    tvtk_base.TraitRevPrefixMap({'uv': 0, 'texture_uv': 1}), help=\
        """
        Choose the name used for the texture coordinates. (u, v) or
        (texture_u, texture_v)
        """
    )

    def _texture_coordinates_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureCoordinatesName,
                        self.texture_coordinates_name_)

    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Specify the array name to use to color the data.
        """
    )

    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    color = tvtk_base.vtk_color_trait((255, 255, 255), help=\
        """
        
        """
    )

    def _color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColor,
                        self.color, False)

    component = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the array component to use to color the data.
        """
    )

    def _component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComponent,
                        self.component)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of vtk polygon data file to write.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        A lookup table can be specified in order to convert data arrays
        to RGBA colors.
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
        V.get_input() -> PolyData
        C++: PolyData *GetInput()
        V.get_input(int) -> PolyData
        C++: PolyData *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def add_comment(self, *args):
        """
        V.add_comment(string)
        C++: void AddComment(const std::string &comment)
        Add a comment in the header part.
        """
        ret = self._wrap_call(self._vtk_obj.AddComment, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('color_mode',
    'GetColorMode'), ('data_byte_order', 'GetDataByteOrder'),
    ('file_type', 'GetFileType'), ('texture_coordinates_name',
    'GetTextureCoordinatesName'), ('array_name', 'GetArrayName'),
    ('color', 'GetColor'), ('component', 'GetComponent'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'color_mode', 'data_byte_order', 'file_type',
    'texture_coordinates_name', 'array_name', 'color', 'component',
    'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PLYWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['color_mode', 'data_byte_order', 'file_type',
            'texture_coordinates_name'], ['array_name', 'color', 'component',
            'file_name']),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PLYWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

