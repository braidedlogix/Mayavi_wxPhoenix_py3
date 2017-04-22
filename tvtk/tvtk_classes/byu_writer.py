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


class BYUWriter(Writer):
    """
    BYUWriter - write MOVIE.BYU files
    
    Superclass: Writer
    
    BYUWriter writes MOVIE.BYU polygonal files. These files consist of
    a geometry file (.g), a scalar file (.s), a displacement or vector
    file (.d), and a 2d texture coordinate file (.t). These files must be
    specified to the object, the appropriate boolean variables must be
    true, and data must be available from the input for the files to be
    written. WARNING: this writer does not currently write triangle
    strips. Use TriangleFilter to convert strips to triangles.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBYUWriter, obj, update, **traits)
    
    write_displacement = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the displacement file.
        """
    )

    def _write_displacement_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteDisplacement,
                        self.write_displacement_)

    write_scalar = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the scalar file.
        """
    )

    def _write_scalar_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteScalar,
                        self.write_scalar_)

    write_texture = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off writing the texture file.
        """
    )

    def _write_texture_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWriteTexture,
                        self.write_texture_)

    displacement_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the displacement file to write.
        """
    )

    def _displacement_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplacementFileName,
                        self.displacement_file_name)

    geometry_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the geometry file to write.
        """
    )

    def _geometry_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGeometryFileName,
                        self.geometry_file_name)

    scalar_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the scalar file to write.
        """
    )

    def _scalar_file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarFileName,
                        self.scalar_file_name)

    texture_file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify the name of the texture file to write.
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
        V.get_input() -> PolyData
        C++: PolyData *GetInput()
        V.get_input(int) -> PolyData
        C++: PolyData *GetInput(int port)
        Get the input to this writer.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('write_displacement', 'GetWriteDisplacement'), ('write_scalar',
    'GetWriteScalar'), ('write_texture', 'GetWriteTexture'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('displacement_file_name', 'GetDisplacementFileName'),
    ('geometry_file_name', 'GetGeometryFileName'), ('scalar_file_name',
    'GetScalarFileName'), ('texture_file_name', 'GetTextureFileName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'write_displacement', 'write_scalar',
    'write_texture', 'displacement_file_name', 'geometry_file_name',
    'progress_text', 'scalar_file_name', 'texture_file_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BYUWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['write_displacement', 'write_scalar', 'write_texture'], [],
            ['displacement_file_name', 'geometry_file_name', 'scalar_file_name',
            'texture_file_name']),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BYUWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

