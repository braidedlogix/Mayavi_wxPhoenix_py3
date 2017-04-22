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

from tvtk.tvtk_classes.array_data_algorithm import ArrayDataAlgorithm


class NormalizeMatrixVectors(ArrayDataAlgorithm):
    """
    NormalizeMatrixVectors - given a sparse input matrix, produces a
    sparse output matrix with each vector normalized to unit length with
    respect to a p-norm (default p=2).
    
    Superclass: ArrayDataAlgorithm
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkNormalizeMatrixVectors, obj, update, **traits)
    
    p_value = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Value of p in p-norm normalization, subject to p >= 1.  Default
        is p=2 (Euclidean norm).
        """
    )

    def _p_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPValue,
                        self.p_value)

    vector_dimension = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Controls whether to normalize row-vectors or column-vectors.  0 =
        rows, 1 = columns.
        """
    )

    def _vector_dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetVectorDimension,
                        self.vector_dimension)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('p_value',
    'GetPValue'), ('vector_dimension', 'GetVectorDimension'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'p_value', 'progress_text', 'vector_dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(NormalizeMatrixVectors, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit NormalizeMatrixVectors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['p_value', 'vector_dimension']),
            title='Edit NormalizeMatrixVectors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit NormalizeMatrixVectors properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

