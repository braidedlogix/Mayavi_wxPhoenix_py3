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

from tvtk.tvtk_classes.cell import Cell


class PolyLine(Cell):
    """
    PolyLine - cell represents a set of 1d lines
    
    Superclass: Cell
    
    PolyLine is a concrete implementation of Cell to represent a
    set of 1d lines.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPolyLine, obj, update, **traits)
    
    def generate_sliding_normals(self, *args):
        """
        V.generate_sliding_normals(Points, CellArray, DataArray)
            -> int
        C++: static int GenerateSlidingNormals(Points *,
            CellArray *, DataArray *)
        V.generate_sliding_normals(Points, CellArray, DataArray,
            [float, ...]) -> int
        C++: static int GenerateSlidingNormals(Points *,
            CellArray *, DataArray *, double *firstNormal)
        Given points and lines, compute normals to lines. These are not
        true normals, they are "orientation" normals used by classes like
        TubeFilter that control the rotation around the line. The
        normals try to stay pointing in the same direction as much as
        possible (i.e., minimal rotation) w.r.t the first_normal (computed
        if NULL). Allways returns 1 (success).
        """
        my_args = deref_array(args, [('vtkPoints', 'vtkCellArray', 'vtkDataArray'), ('vtkPoints', 'vtkCellArray', 'vtkDataArray', 'tuple')])
        ret = self._wrap_call(self._vtk_obj.GenerateSlidingNormals, *my_args)
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
            return super(PolyLine, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PolyLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PolyLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PolyLine properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

