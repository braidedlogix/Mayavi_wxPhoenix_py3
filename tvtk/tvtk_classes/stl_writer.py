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


class STLWriter(Writer):
    """
    STLWriter - write stereo lithography files
    
    Superclass: Writer
    
    STLWriter writes stereo lithography (.stl) files in either ASCII
    or binary form. Stereo lithography files only contain triangles. If
    polygons with more than 3 vertices are present, only the first 3
    vertices are written.  Use TriangleFilter to convert polygons to
    triangles.
    
    @warning
    Binary files written on one system may not be readable on other
    systems. STLWriter uses VAX or PC byte ordering and swaps bytes on
    other systems.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSTLWriter, obj, update, **traits)
    
    file_type = traits.Trait('ascii',
    tvtk_base.TraitRevPrefixMap({'ascii': 1, 'binary': 2}), help=\
        """
        Specify file type (ASCII or BINARY) for vtk data file.
        """
    )

    def _file_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileType,
                        self.file_type_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify file name of vtk polygon data file to write.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

    header = traits.String('Visualization Toolkit generated SLA File                                        ', enter_set=True, auto_set=False, help=\
        """
        Set the header for the file.
        """
    )

    def _header_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeader,
                        self.header)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('header', 'GetHeader'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_type', 'file_name', 'header',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(STLWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit STLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['file_type'], ['file_name', 'header']),
            title='Edit STLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit STLWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

