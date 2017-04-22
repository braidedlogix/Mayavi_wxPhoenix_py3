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


class BooleanOperationPolyDataFilter(PolyDataAlgorithm):
    """
    BooleanOperationPolyDataFilter - Computes the boundary of the
    union, intersection, or difference volume computed from the volumes
    defined by two input surfaces.
    
    Superclass: PolyDataAlgorithm
    
    The two surfaces do not need to be manifold, but if they are not,
    unexpected results may be obtained. The resulting surface is
    available in the first output of the filter. The second output
    contains a set of polylines that represent the intersection between
    the two input surfaces.
    
    This code was contributed in the VTK Journal paper: "Boolean Operations on Surfaces in VTK Without External
    Libraries" by Cory Quammen, Chris Weigle C., Russ Taylor
    http://hdl.handle.net/10380/3262
    http://www.midasjournal.org/browse/publication/797
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBooleanOperationPolyDataFilter, obj, update, **traits)
    
    reorient_difference_cells = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off cell reorientation of the intersection portion of the
        surface when the operation is set to DIFFERENCE. Defaults to on.
        """
    )

    def _reorient_difference_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReorientDifferenceCells,
                        self.reorient_difference_cells_)

    operation = traits.Trait('union',
    tvtk_base.TraitRevPrefixMap({'union': 0, 'difference': 2, 'intersection': 1}), help=\
        """
        Set the boolean operation to perform. Defaults to union.
        """
    )

    def _operation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOperation,
                        self.operation_)

    tolerance = traits.Float(1e-06, enter_set=True, auto_set=False, help=\
        """
        Set/get the tolerance used to determine when a point's absolute
        distance is considered to be zero. Defaults to 1e-6.
        """
    )

    def _tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTolerance,
                        self.tolerance)

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
    (('reorient_difference_cells', 'GetReorientDifferenceCells'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('operation',
    'GetOperation'), ('tolerance', 'GetTolerance'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reorient_difference_cells', 'operation',
    'progress_text', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BooleanOperationPolyDataFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BooleanOperationPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['reorient_difference_cells'], ['operation'], ['tolerance']),
            title='Edit BooleanOperationPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BooleanOperationPolyDataFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

