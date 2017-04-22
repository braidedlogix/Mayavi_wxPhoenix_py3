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


class DiagonalMatrixSource(ArrayDataAlgorithm):
    """
    DiagonalMatrixSource - generates a sparse or dense square matrix
    with user-specified values for the diagonal, superdiagonal, and
    subdiagonal.
    
    Superclass: ArrayDataAlgorithm
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDiagonalMatrixSource, obj, update, **traits)
    
    array_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _array_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayType,
                        self.array_type)

    column_label = traits.String('columns', enter_set=True, auto_set=False, help=\
        """
        Controls the output matrix column dimension label. Default:
        "columns"
        """
    )

    def _column_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetColumnLabel,
                        self.column_label)

    diagonal = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to diagonal elements
        (default: 1)
        """
    )

    def _diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDiagonal,
                        self.diagonal)

    extents = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Stores the extents of the output matrix (which is square)
        """
    )

    def _extents_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtents,
                        self.extents)

    row_label = traits.String('rows', enter_set=True, auto_set=False, help=\
        """
        Controls the output matrix row dimension label. Default: "rows"
        """
    )

    def _row_label_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRowLabel,
                        self.row_label)

    sub_diagonal = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to subdiagonal elements
        (default: 0)
        """
    )

    def _sub_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubDiagonal,
                        self.sub_diagonal)

    super_diagonal = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Stores the value that will be assigned to superdiagonal elements
        (default: 0)
        """
    )

    def _super_diagonal_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSuperDiagonal,
                        self.super_diagonal)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('array_type',
    'GetArrayType'), ('column_label', 'GetColumnLabel'), ('diagonal',
    'GetDiagonal'), ('extents', 'GetExtents'), ('row_label',
    'GetRowLabel'), ('sub_diagonal', 'GetSubDiagonal'), ('super_diagonal',
    'GetSuperDiagonal'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_type', 'column_label', 'diagonal',
    'extents', 'progress_text', 'row_label', 'sub_diagonal',
    'super_diagonal'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DiagonalMatrixSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['array_type', 'column_label', 'diagonal', 'extents',
            'row_label', 'sub_diagonal', 'super_diagonal']),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DiagonalMatrixSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

