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

from tvtk.tvtk_classes.abstract_poly_data_reader import AbstractPolyDataReader


class STLReader(AbstractPolyDataReader):
    """
    STLReader - read ASCII or binary stereo lithography files
    
    Superclass: AbstractPolyDataReader
    
    STLReader is a source object that reads ASCII or binary stereo
    lithography files (.stl files). The file_name must be specified to
    STLReader. The object automatically detects whether the file is
    ASCII or binary.
    
    .stl files are quite inefficient since they duplicate vertex
    definitions. By setting the Merging boolean you can control whether
    the point data is merged after reading. Merging is performed by
    default, however, merging requires a large amount of temporary
    storage since a 3d hash table must be constructed.
    
    @warning
    Binary files written on one system may not be readable on other
    systems. STLWriter uses VAX or PC byte ordering and swaps bytes on
    other systems.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSTLReader, obj, update, **traits)
    
    merging = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off merging of points/triangles.
        """
    )

    def _merging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMerging,
                        self.merging_)

    scalar_tags = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off tagging of solids with scalars.
        """
    )

    def _scalar_tags_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarTags,
                        self.scalar_tags_)

    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Specify a spatial locator for merging points. By default an
        instance of MergePoints is used.
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
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('merging', 'GetMerging'), ('scalar_tags', 'GetScalarTags'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'merging',
    'release_data_flag', 'scalar_tags', 'file_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(STLReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['merging', 'scalar_tags'], [], ['file_name']),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit STLReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

