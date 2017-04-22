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

from tvtk.tvtk_classes.object import Object


class MeanValueCoordinatesInterpolator(Object):
    """
    MeanValueCoordinatesInterpolator - compute interpolation computes
    for closed triangular mesh
    
    Superclass: Object
    
    MeanValueCoordinatesInterpolator computes interpolation weights
    for a closed, manifold polyhedron mesh.  Once computed, the
    interpolation weights can be used to interpolate data anywhere
    interior or exterior to the mesh. This work implements two MVC
    algorithms. The first one is for triangular meshes which is
    documented in the Siggraph 2005 paper by Tao Ju, Scot Schaefer and
    Joe Warren from Rice University "Mean Value Coordinates for Closed
    Triangular Meshes". The second one is for general polyhedron mesh
    which is documented in the Eurographics Symposium on Geometry
    Processing 2006 paper by Torsten Langer, Alexander Belyaev and
    Hans-Peter Seidel from MPI Informatik "Spherical Barycentric
    Coordinates". The filter will automatically choose which algorithm to
    use based on whether the input mesh is triangulated or not.
    
    In VTK this class was initially created to interpolate data across
    polyhedral cells. In addition, the class can be used to interpolate
    data values from a polyhedron mesh, and to smoothly deform a mesh
    from an associated control mesh.
    
    @sa
    PolyhedralCell
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMeanValueCoordinatesInterpolator, obj, update, **traits)
    
    def compute_interpolation_weights(self, *args):
        """
        V.compute_interpolation_weights([float, float, float], Points,
            IdList, [float, ...])
        C++: static void ComputeInterpolationWeights(double x[3],
            Points *pts, IdList *tris, double *weights)
        V.compute_interpolation_weights([float, float, float], Points,
            CellArray, [float, ...])
        C++: static void ComputeInterpolationWeights(double x[3],
            Points *pts, CellArray *tris, double *weights)
        Method to generate interpolation weights for a point x[3] from a
        list of triangles.  In this version of the method, the triangles
        are defined by a Points array plus a IdList, where the
        IdList is organized such that three ids in order define a
        triangle.  Note that number of weights must equal the number of
        points.
        """
        my_args = deref_array(args, [(['float', 'float', 'float'], 'vtkPoints', 'vtkIdList', 'tuple'), (['float', 'float', 'float'], 'vtkPoints', 'vtkCellArray', 'tuple')])
        ret = self._wrap_call(self._vtk_obj.ComputeInterpolationWeights, *my_args)
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
            return super(MeanValueCoordinatesInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MeanValueCoordinatesInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

