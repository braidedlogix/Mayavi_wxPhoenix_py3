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

from tvtk.tvtk_classes.selection_algorithm import SelectionAlgorithm


class LinearSelector(SelectionAlgorithm):
    """
    LinearSelector - select cells intersecting a line (possibly broken)
    
    Superclass: SelectionAlgorithm
    
    This filter takes a CompositeDataSet as input and a line segment
    as parameter. It outputs a Selection identifying all the cells
    intersecting the given line segment.
    
    @par Thanks: This class has been initially developed in the frame of
    CEA's Love visualization software development
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Modified and integrated into VTK, Kitware SAS 2012 This class was
    implemented by Thierry Carrard, Charles Pignerol, and Philippe Pebay.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLinearSelector, obj, update, **traits)
    
    include_vertices = tvtk_base.true_bool_trait(help=\
        """
        Set/Get whether lines vertice are included in selection
        """
    )

    def _include_vertices_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncludeVertices,
                        self.include_vertices_)

    end_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _end_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEndPoint,
                        self.end_point)

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        Set/Get the list of points defining the intersecting broken line
        """
    )

    start_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _start_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStartPoint,
                        self.start_point)

    tolerance = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get tolerance to be used by intersection algorithm
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

    vertex_elimination_tolerance = traits.Trait(1e-06, traits.Range(0.0, 0.1, enter_set=True, auto_set=False), help=\
        """
        Set/Get relative tolerance for vertex elimination
        """
    )

    def _vertex_elimination_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVertexEliminationTolerance,
                        self.vertex_elimination_tolerance)

    _updateable_traits_ = \
    (('include_vertices', 'GetIncludeVertices'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('end_point', 'GetEndPoint'),
    ('start_point', 'GetStartPoint'), ('tolerance', 'GetTolerance'),
    ('vertex_elimination_tolerance', 'GetVertexEliminationTolerance'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'include_vertices', 'release_data_flag', 'end_point', 'progress_text',
    'start_point', 'tolerance', 'vertex_elimination_tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LinearSelector, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LinearSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['include_vertices'], [], ['end_point', 'start_point',
            'tolerance', 'vertex_elimination_tolerance']),
            title='Edit LinearSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LinearSelector properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

