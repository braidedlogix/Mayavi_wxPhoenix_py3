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

from tvtk.tvtk_classes.planes import Planes


class PlanesIntersection(Planes):
    """
    PlanesIntersection - A PlanesIntersection object is a
       Planes object that can compute whether the arbitrary convex
    region
       bounded by it's planes intersects an axis-aligned box.
    
    Superclass: Planes
    
    A subclass of Planes, this class determines whether it
       intersects an axis aligned box.   This is motivated by the
       need to intersect the axis aligned region of a spacial
       decomposition of volume data with various other regions.
       It uses the algorithm from Graphics Gems IV, page 81.
    
    @par Caveat:
       An instance of Planes can be redefined by changing the planes,
       but this subclass then will not know if the region vertices are
       up to date.  (Region vertices can be specified in
    set_region_vertices
       or computed by the subclass.)  So Delete and recreate if you want
       to change the set of planes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPlanesIntersection, obj, update, **traits)
    
    def get_region_vertices(self, *args):
        """
        V.get_region_vertices([float, ...], int) -> int
        C++: int GetRegionVertices(double *v, int nvertices)"""
        ret = self._wrap_call(self._vtk_obj.GetRegionVertices, *args)
        return ret

    def set_region_vertices(self, *args):
        """
        V.set_region_vertices(Points)
        C++: void SetRegionVertices(Points *pts)
        V.set_region_vertices([float, ...], int)
        C++: void SetRegionVertices(double *v, int nvertices)
        It helps if you know the vertices of the convex region. If you
        don't, we will calculate them.  Region vertices are 3-tuples.
        """
        my_args = deref_array(args, [['vtkPoints'], ('tuple', 'int')])
        ret = self._wrap_call(self._vtk_obj.SetRegionVertices, *my_args)
        return ret

    def _get_num_region_vertices(self):
        return self._vtk_obj.GetNumRegionVertices()
    num_region_vertices = traits.Property(_get_num_region_vertices, help=\
        """
        
        """
    )

    def _get_number_of_region_vertices(self):
        return self._vtk_obj.GetNumberOfRegionVertices()
    number_of_region_vertices = traits.Property(_get_number_of_region_vertices, help=\
        """
        
        """
    )

    def convert3d_cell(self, *args):
        """
        V.convert3d_cell(Cell) -> PlanesIntersection
        C++: static PlanesIntersection *Convert3DCell(Cell *cell)
        Another convenience function provided by this class, returns the
        PlanesIntersection object representing a 3d cell.  The point
        IDs for each face must be given in counter-clockwise order from
        the outside of the cell.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Convert3DCell, *my_args)
        return wrap_vtk(ret)

    def intersects_region(self, *args):
        """
        V.intersects_region(Points) -> int
        C++: int IntersectsRegion(Points *R)
        Return 1 if the axis aligned box defined by R intersects the
        region defined by the planes, or 0 otherwise.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.IntersectsRegion, *my_args)
        return ret

    def polygon_intersects_b_box(self, *args):
        """
        V.polygon_intersects_b_box([float, float, float, float, float,
            float], Points) -> int
        C++: static int PolygonIntersectsBBox(double bounds[6],
            Points *pts)
        A convenience function provided by this class, returns 1 if the
        polygon defined in pts intersects the bounding box defined in
        bounds, 0 otherwise.
        
        * The points must define a planar polygon.
        """
        my_args = deref_array(args, [(['float', 'float', 'float', 'float', 'float', 'float'], 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.PolygonIntersectsBBox, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PlanesIntersection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PlanesIntersection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PlanesIntersection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PlanesIntersection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

