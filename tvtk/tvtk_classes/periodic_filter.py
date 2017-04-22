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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class PeriodicFilter(MultiBlockDataSetAlgorithm):
    """
    PeriodicFilter - A filter to produce mapped  periodic multiblock
    dataset from a single block
    
    Superclass: MultiBlockDataSetAlgorithm
    
    Generate periodic dataset by transforming points, vectors, tensors
    data arrays from an original data array. The generated dataset is of
    the same type than the input (float or double). This is an abstract
    class wich do not implement the actual transformation. Point
    coordinates are transformed, as well as all vectors (3-components)
    and tensors (9 components) in points and cell data arrays. The
    generated multiblock will have the same tree architecture than the
    input, except transformed leaves are replaced by a
    MultipieceDataSet. Supported input leaf dataset type are:
    PolyData, StructuredGrid and UnstructuredGrid. Other data
    objects are transformed using the transform filter (at a high cost!).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPeriodicFilter, obj, update, **traits)
    
    iteration_mode = traits.Trait('max',
    tvtk_base.TraitRevPrefixMap({'max': 1, 'direct_nb': 0}), help=\
        """
        Set/Get Iteration mode. VTK_ITERATION_MODE_DIRECT_NB to specify
        the number of periods, VTK_ITERATION_MODE_MAX to generate a full
        period (default).
        """
    )

    def _iteration_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIterationMode,
                        self.iteration_mode_)

    number_of_periods = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get Number of periods. Used only with
        ITERATION_MODE_DIRECT_NB.
        """
    )

    def _number_of_periods_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPeriods,
                        self.number_of_periods)

    def add_index(self, *args):
        """
        V.add_index(int)
        C++: virtual void AddIndex(unsigned int index)
        Select the periodic pieces indices. Each node in the multi -
        block tree is identified by an index. The index can be obtained
        by performing a preorder traversal of the tree (including empty
        nodes). eg. A(B (D, E), C(F, G)). Inorder traversal yields: A, B,
        D, E, C, F, G Index of A is 0, while index of C is 4.
        """
        ret = self._wrap_call(self._vtk_obj.AddIndex, *args)
        return ret

    def remove_all_indices(self):
        """
        V.remove_all_indices()
        C++: virtual void RemoveAllIndices()
        Clear selected indices tree
        """
        ret = self._vtk_obj.RemoveAllIndices()
        return ret
        

    def remove_index(self, *args):
        """
        V.remove_index(int)
        C++: virtual void RemoveIndex(unsigned int index)
        Remove an index from selected indices tress
        """
        ret = self._wrap_call(self._vtk_obj.RemoveIndex, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('iteration_mode', 'GetIterationMode'), ('number_of_periods',
    'GetNumberOfPeriods'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'iteration_mode', 'number_of_periods',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PeriodicFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['iteration_mode'], ['number_of_periods']),
            title='Edit PeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PeriodicFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

