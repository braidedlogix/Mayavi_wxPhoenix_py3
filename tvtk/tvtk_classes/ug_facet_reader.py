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


class UGFacetReader(PolyDataAlgorithm):
    """
    UGFacetReader - read EDS Unigraphics facet files
    
    Superclass: PolyDataAlgorithm
    
    UGFacetReader is a source object that reads Unigraphics facet
    files. Unigraphics is a solid modeling system; facet files are the
    polygonal plot files it uses to create 3d plots.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUGFacetReader, obj, update, **traits)
    
    merging = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off merging of points/triangles.
        """
    )

    def _merging_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMerging,
                        self.merging_)

    file_name = tvtk_base.vtk_file_name("", help=\
        """
        Specify Unigraphics file name.
        """
    )

    def _file_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFileName,
                        self.file_name)

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

    part_number = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Specify the desired part to extract. The part number must range
        between [_0,_number_of_parts-_1]. If the value is =(-1), then all
        parts will be extracted. If the value is <(-1), then no parts
        will be  extracted but the part colors will be updated.
        """
    )

    def _part_number_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPartNumber,
                        self.part_number)

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

    def _get_number_of_parts(self):
        return self._vtk_obj.GetNumberOfParts()
    number_of_parts = traits.Property(_get_number_of_parts, help=\
        """
        Special methods for interrogating the data file.
        """
    )

    def get_part_color_index(self, *args):
        """
        V.get_part_color_index(int) -> int
        C++: short GetPartColorIndex(int partId)
        Retrieve color index for the parts in the file.
        """
        ret = self._wrap_call(self._vtk_obj.GetPartColorIndex, *args)
        return ret

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

    _updateable_traits_ = \
    (('merging', 'GetMerging'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('file_name',
    'GetFileName'), ('part_number', 'GetPartNumber'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display', 'merging',
    'release_data_flag', 'file_name', 'part_number', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UGFacetReader, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UGFacetReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['merging'], [], ['file_name', 'part_number']),
            title='Edit UGFacetReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UGFacetReader properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

