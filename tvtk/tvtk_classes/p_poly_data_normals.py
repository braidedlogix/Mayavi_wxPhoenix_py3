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

from tvtk.tvtk_classes.poly_data_normals import PolyDataNormals


class PPolyDataNormals(PolyDataNormals):
    """
    PPolyDataNormals - compute normals for polygonal mesh
    
    Superclass: PolyDataNormals
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPPolyDataNormals, obj, update, **traits)
    
    piece_invariant = tvtk_base.true_bool_trait(help=\
        """
        To get piece invariance, this filter has to request an extra
        ghost level.  By default piece invariance is on.
        """
    )

    def _piece_invariant_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPieceInvariant,
                        self.piece_invariant_)

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
    (('piece_invariant', 'GetPieceInvariant'), ('auto_orient_normals',
    'GetAutoOrientNormals'), ('compute_cell_normals',
    'GetComputeCellNormals'), ('compute_point_normals',
    'GetComputePointNormals'), ('consistency', 'GetConsistency'),
    ('flip_normals', 'GetFlipNormals'), ('non_manifold_traversal',
    'GetNonManifoldTraversal'), ('splitting', 'GetSplitting'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('feature_angle', 'GetFeatureAngle'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'auto_orient_normals', 'compute_cell_normals',
    'compute_point_normals', 'consistency', 'debug', 'flip_normals',
    'global_warning_display', 'non_manifold_traversal', 'piece_invariant',
    'release_data_flag', 'splitting', 'feature_angle',
    'output_points_precision', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PPolyDataNormals, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PPolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['auto_orient_normals', 'compute_cell_normals',
            'compute_point_normals', 'consistency', 'flip_normals',
            'non_manifold_traversal', 'piece_invariant', 'splitting'], [],
            ['feature_angle', 'output_points_precision']),
            title='Edit PPolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PPolyDataNormals properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

