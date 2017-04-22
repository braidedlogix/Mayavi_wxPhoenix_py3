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

from tvtk.tvtk_classes.cell3d import Cell3D


class Polyhedron(Cell3D):
    """
    Polyhedron - a 3d cell defined by a set of polygonal faces
    
    Superclass: Cell3D
    
    Polyhedron is a concrete implementation that represents a 3d cell
    defined by a set of polygonal faces. The polyhedron should be
    watertight, non-self-intersecting and manifold (each edge is used
    twice).
    
    Interpolation functions and weights are defined / computed using the
    method of Mean Value Coordinates (MVC). See the VTK class
    MeanValueCoordinatesInterpolator for more information.
    
    The class does not require the polyhedron to be convex. However, the
    polygonal faces must be planar. Non-planar polygonal faces will
    definitely cause problems, especially in severely warped situations.
    
    @sa
    Cell3D ConvecPointSet MeanValueCoordinatesInterpolator
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyhedron, obj, update, **traits)
    
    def _get_faces(self):
        return self._vtk_obj.GetFaces()
    def _set_faces(self, arg):
        old_val = self._get_faces()
        self._wrap_call(self._vtk_obj.SetFaces,
                        arg)
        self.trait_property_changed('faces', old_val, arg)
    faces = traits.Property(_get_faces, _set_faces, help=\
        """
        Methods supporting the definition of faces. Note that the
        get_faces() returns a list of faces in CellArray form; use the
        method get_number_of_faces() to determine the number of faces in the
        list. The set_faces() method is also in CellArray form, except
        that it begins with a leading count indicating the total number
        of faces in the list.
        """
    )

    def _get_poly_data(self):
        return wrap_vtk(self._vtk_obj.GetPolyData())
    poly_data = traits.Property(_get_poly_data, help=\
        """
        Construct polydata if no one exist, then return this->_poly_data
        """
    )

    def is_convex(self):
        """
        V.is_convex() -> bool
        C++: bool IsConvex()
        Determine whether or not a polyhedron is convex. This method is
        adapted from Devillers et al., "Checking the Convexity of
        Polytopes and the Planarity of Subdivisions", Computational
        Geometry, Volume 11, Issues 3 – 4, December 1998, Pages 187 –
        208.
        """
        ret = self._vtk_obj.IsConvex()
        return ret
        

    def is_inside(self, *args):
        """
        V.is_inside([float, float, float], float) -> int
        C++: int IsInside(double x[3], double tolerance)
        A method particular to Polyhedron. It determines whether a
        point x[3] is inside the polyhedron or not (returns 1 is the
        point is inside, 0 otherwise). The tolerance is expressed in
        normalized space; i.e., a fraction of the size of the bounding
        box.
        """
        ret = self._wrap_call(self._vtk_obj.IsInside, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('merge_tolerance', 'GetMergeTolerance'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'merge_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Polyhedron, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['merge_tolerance']),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Polyhedron properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

