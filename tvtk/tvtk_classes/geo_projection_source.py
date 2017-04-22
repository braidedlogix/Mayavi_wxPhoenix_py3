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

from tvtk.tvtk_classes.geo_source import GeoSource


class GeoProjectionSource(GeoSource):
    """
    GeoProjectionSource - A 2d geographic geometry source
    
    Superclass: GeoSource
    
    GeoProjectionSource is a GeoSource suitable for use in
    Terrain2D. This source uses the libproj4 library to produce
    geometry patches at multiple resolutions. Each patch covers a
    specific region in projected space.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoProjectionSource, obj, update, **traits)
    
    min_cells_per_node = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        The minimum number of cells per node.
        """
    )

    def _min_cells_per_node_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinCellsPerNode,
                        self.min_cells_per_node)

    projection = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The projection ID defining the projection. Initial value is 0.
        """
    )

    def _projection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjection,
                        self.projection)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('min_cells_per_node',
    'GetMinCellsPerNode'), ('projection', 'GetProjection'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'min_cells_per_node',
    'projection'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoProjectionSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoProjectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['min_cells_per_node', 'projection']),
            title='Edit GeoProjectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoProjectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

