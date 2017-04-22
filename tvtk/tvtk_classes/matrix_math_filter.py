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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class MatrixMathFilter(DataSetAlgorithm):
    """
    MatrixMathFilter - Calculate functions of quality of the elements
     of a mesh
    
    Superclass: DataSetAlgorithm
    
    MatrixMathFilter computes one or more functions of mathematical
    quality for the cells or points in a mesh. The per-cell or per-point
    quality is added to the mesh's cell data or point data, in an array
    with names varied with different quality being queried. Note this
    filter always assume the data associate with the cells or points are
    3 by 3 matrix.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMatrixMathFilter, obj, update, **traits)
    
    def get_operation(self):
        """
        V.get_operation() -> int
        C++: int GetOperation()
        Set/Get the particular estimator used to function the quality of
        query.
        """
        ret = self._vtk_obj.GetOperation()
        return ret
        

    def set_operation_to_eigenvalue(self):
        """
        V.set_operation_to_eigenvalue()
        C++: void SetOperationToEigenvalue()
        Set/Get the particular estimator used to function the quality of
        query.
        """
        self._vtk_obj.SetOperationToEigenvalue()

    def set_operation_to_eigenvector(self):
        """
        V.set_operation_to_eigenvector()
        C++: void SetOperationToEigenvector()
        Set/Get the particular estimator used to function the quality of
        query.
        """
        self._vtk_obj.SetOperationToEigenvector()

    def set_operation_to_inverse(self):
        """
        V.set_operation_to_inverse()
        C++: void SetOperationToInverse()
        Set/Get the particular estimator used to function the quality of
        query.
        """
        self._vtk_obj.SetOperationToInverse()

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MatrixMathFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MatrixMathFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MatrixMathFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MatrixMathFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

