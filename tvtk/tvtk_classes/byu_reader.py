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


class BYUReader(PolyDataAlgorithm):
    """
    BYUReader - read MOVIE.BYU polygon files
    
    Superclass: PolyDataAlgorithm
    
    BYUReader is a source object that reads MOVIE.BYU polygon files.
    These files consist of a geometry file (.g), a scalar file (.s), a
    displacement or vector file (.d), and a 2d texture coordinate file
    (.t).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBYUReader, obj, update, **traits)
    
    read_displacement = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the displacement file.
        """
    )

    def _read_displacement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadDisplacement,
                        self.read_displacement_)

    read_scalar = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the scalar file.
        """
    )

    def _read_scalar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadScalar,
                        self.read_scalar_)

    read_texture = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the reading of the texture coordinate file. Specify
        name of geometry file_name.
        """
    )

    def _read_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReadTexture,
                        self.read_texture_)

    displacement_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of displacement file_name.
        """
    )

    def _displacement_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementFileName,
                        self.displacement_file_name)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of geometry file_name (alias).
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    geometry_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of geometry file_name.
        """
    )

    def _geometry_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryFileName,
                        self.geometry_file_name)

    part_number = traits.Trait(0, traits.Range(0, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get the part number to be read.
        """
    )

    def _part_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPartNumber,
                        self.part_number)

    scalar_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of scalar file_name.
        """
    )

    def _scalar_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFileName,
                        self.scalar_file_name)

    texture_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify name of texture coordinates file_name.
        """
    )

    def _texture_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureFileName,
                        self.texture_file_name)

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

    def can_read_file(self, *args):
        """
        V.can_read_file(string) -> int
        C++: static int CanReadFile(const char *filename)
        Returns 1 if this file can be read and 0 if the file cannot be
        read. Because BYU files do not have anything in the header
        specifying the file type, the result is not definitive.  Invalid
        files may still return 1 although a valid file will never return
        0.
        """
        ret = self._wrap_call(self._vtk_obj.CanReadFile, *args)
        return ret

    _updateable_traits_ = \
    (('read_displacement', 'GetReadDisplacement'), ('read_scalar',
    'GetReadScalar'), ('read_texture', 'GetReadTexture'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('displacement_file_name', 'GetDisplacementFileName'), ('file_name',
    'GetFileName'), ('geometry_file_name', 'GetGeometryFileName'),
    ('part_number', 'GetPartNumber'), ('scalar_file_name',
    'GetScalarFileName'), ('texture_file_name', 'GetTextureFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'read_displacement', 'read_scalar', 'read_texture',
    'release_data_flag', 'displacement_file_name', 'file_name',
    'geometry_file_name', 'part_number', 'progress_text',
    'scalar_file_name', 'texture_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BYUReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['read_displacement', 'read_scalar', 'read_texture'], [],
            ['displacement_file_name', 'file_name', 'geometry_file_name',
            'part_number', 'scalar_file_name', 'texture_file_name']),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BYUReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

