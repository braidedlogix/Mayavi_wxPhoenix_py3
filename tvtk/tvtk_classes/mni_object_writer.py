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


class MNIObjectWriter(Writer):
    """
    MNIObjectWriter - A writer for MNI surface mesh files.
    
    Superclass: Writer
    
    The MNI .obj file format is used to store geometrical data.  This
    file format was developed at the mc_connell Brain Imaging Centre at
    the Montreal Neurological Institute and is used by their software.
    Only polygon and line files are supported by this writer.  For these
    formats, all data elements are written including normals, colors, and
    surface properties.  ASCII and binary file types are supported.
    @sa
    MINCImageReader MNIObjectReader MNITransformReader@par
    Thanks: Thanks to David Gobbi for writing this class and Atamai Inc.
    for contributing it to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMNIObjectWriter, obj, update, **traits)
    
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

    def _get_lookup_table(self):
        return wrap_vtk(self._vtk_obj.GetLookupTable())
    def _set_lookup_table(self, arg):
        old_val = self._get_lookup_table()
        self._wrap_call(self._vtk_obj.SetLookupTable,
                        deref_vtk(arg))
        self.trait_property_changed('lookup_table', old_val, arg)
    lookup_table = traits.Property(_get_lookup_table, _set_lookup_table, help=\
        """
        Set the lookup table associated with the object.  This will be
        used to convert scalar values to colors, if a mapper is not set.
        """
    )

    def _get_mapper(self):
        return wrap_vtk(self._vtk_obj.GetMapper())
    def _set_mapper(self, arg):
        old_val = self._get_mapper()
        self._wrap_call(self._vtk_obj.SetMapper,
                        deref_vtk(arg))
        self.trait_property_changed('mapper', old_val, arg)
    mapper = traits.Property(_get_mapper, _set_mapper, help=\
        """
        Set the mapper associated with the object.  Optional. This is
        useful for exporting an actor with the same colors that are used
        to display the actor within VTK.
        """
    )

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set the property associated with the object.  Optional. This is
        useful for exporting an actor.
        """
    )

    def _get_descriptive_name(self):
        return self._vtk_obj.GetDescriptiveName()
    descriptive_name = traits.Property(_get_descriptive_name, help=\
        """
        Get the name of this file format.
        """
    )

    def _get_file_extensions(self):
        return self._vtk_obj.GetFileExtensions()
    file_extensions = traits.Property(_get_file_extensions, help=\
        """
        Get the entension for this file format.
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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_type',
    'GetFileType'), ('file_name', 'GetFileName'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'file_type', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MNIObjectWriter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['file_type'], ['file_name']),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MNIObjectWriter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

