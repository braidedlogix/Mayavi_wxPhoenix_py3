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

from tvtk.tvtk_classes.poly_data_contour_line_interpolator import PolyDataContourLineInterpolator


class PolygonalSurfaceContourLineInterpolator(PolyDataContourLineInterpolator):
    """
    PolygonalSurfaceContourLineInterpolator - Contour interpolator for
    to place points on polygonal surfaces.
    
    Superclass: PolyDataContourLineInterpolator
    
    PolygonalSurfaceContourLineInterpolator interpolates and places
    contour points on polygonal surfaces. The class interpolates nodes by
    computing a graph geodesic laying on the polygonal data. By \em graph
    Geodesic, we mean that the line interpolating the two end points
    traverses along on the mesh edges so as to form the shortest path. A
    Dijkstra algorithm is used to compute the path. See
    DijkstraGraphGeodesicPath.
    
    The class is mean to be used in conjunction with
    PolygonalSurfacePointPlacer. The reason for this weak coupling is
    a performance issue, both classes need to perform a cell pick, and
    coupling avoids multiple cell picks (cell picks are slow).
    
    @warning
    You should have computed cell normals for the input polydata.
    
    @sa
    DijkstraGraphGeodesicPath, PolyDataNormals
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolygonalSurfaceContourLineInterpolator, obj, update, **traits)
    
    distance_offset = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Height offset at which points may be placed on the polygonal
        surface. If you specify a non-zero value here, be sure to have
        computed vertex normals on your input polygonal data. (easily
        done with PolyDataNormals).
        """
    )

    def _distance_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistanceOffset,
                        self.distance_offset)

    def get_contour_point_ids(self, *args):
        """
        V.get_contour_point_ids(ContourRepresentation, IdList)
        C++: void GetContourPointIds(ContourRepresentation *rep,
            IdList *idList)
        Get the contour point ids. These point ids correspond to those on
        the polygonal surface
        """
        my_args = deref_array(args, [('vtkContourRepresentation', 'vtkIdList')])
        ret = self._wrap_call(self._vtk_obj.GetContourPointIds, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('distance_offset', 'GetDistanceOffset'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'distance_offset'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PolygonalSurfaceContourLineInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolygonalSurfaceContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['distance_offset']),
            title='Edit PolygonalSurfaceContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolygonalSurfaceContourLineInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

