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

from tvtk.tvtk_classes.data_representation import DataRepresentation


class GeoAlignedImageRepresentation(DataRepresentation):
    """
    GeoAlignedImageRepresentation - A multi-resolution image tree
    
    Superclass: DataRepresentation
    
    GeoAlignedImageRepresentation represents a high resolution image
    over the globle. It has an associated GeoSource which is
    responsible for fetching new data. This class keeps the fetched data
    in a quad-tree structure organized by latitude and longitude.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoAlignedImageRepresentation, obj, update, **traits)
    
    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    def _set_source(self, arg):
        old_val = self._get_source()
        self._wrap_call(self._vtk_obj.SetSource,
                        deref_vtk(arg))
        self.trait_property_changed('source', old_val, arg)
    source = traits.Property(_get_source, _set_source, help=\
        """
        The source for this representation. This must be set first before
        calling get_best_image_for_bounds.
        """
    )

    def get_best_image_for_bounds(self, *args):
        """
        V.get_best_image_for_bounds([float, float, float, float])
            -> GeoImageNode
        C++: virtual GeoImageNode *GetBestImageForBounds(
            double bounds[4])
        Retrieve the most refined image patch that covers the specified
        latitude and longitude bounds (lat-min, lat-max, long-min,
        long-max).
        """
        ret = self._wrap_call(self._vtk_obj.GetBestImageForBounds, *args)
        return wrap_vtk(ret)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def save_database(self, *args):
        """
        V.save_database(string)
        C++: void SaveDatabase(const char *path)
        Serialize the database to the specified directory. Each image is
        stored as a .vti file. The Origin and Spacing of the saved image
        contain (lat-min, long-min) and (lat-max, long-max),
        respectively. Files are named based on their level and id within
        that level.
        """
        ret = self._wrap_call(self._vtk_obj.SaveDatabase, *args)
        return ret

    _updateable_traits_ = \
    (('selectable', 'GetSelectable'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('selection_array_name',
    'GetSelectionArrayName'), ('selection_type', 'GetSelectionType'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'selectable', 'progress_text',
    'selection_array_name', 'selection_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoAlignedImageRepresentation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoAlignedImageRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['selectable'], [], ['selection_array_name', 'selection_type']),
            title='Edit GeoAlignedImageRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoAlignedImageRepresentation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

