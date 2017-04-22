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

from tvtk.tvtk_classes.graph_algorithm import GraphAlgorithm


class TreeDifferenceFilter(GraphAlgorithm):
    """
    TreeDifferenceFilter - compare two trees
    
    Superclass: GraphAlgorithm
    
    TreeDifferenceFilter compares two trees by analyzing a
    DoubleArray. Each tree must have a copy of this array.  A user of
    this filter should call set_comparison_array_name to specify the array
    that should be used as the basis of coparison.  This array can either
    be part of the trees' edge_data or vertex_data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTreeDifferenceFilter, obj, update, **traits)
    
    comparison_array_is_vertex_data = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Specify whether the comparison array is within the trees' vertex
        data or not.  By default, we assume that the array to compare is
        within the trees' edge_data().
        """
    )

    def _comparison_array_is_vertex_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComparisonArrayIsVertexData,
                        self.comparison_array_is_vertex_data)

    comparison_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the array that we're comparing between the
        two trees. The named array must be a DoubleArray.
        """
    )

    def _comparison_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComparisonArrayName,
                        self.comparison_array_name)

    id_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of the identifier array in the trees'
        vertex_data. This array is used to find corresponding vertices in
        the two trees. If this array name is not set, then we assume that
        the vertices in the two trees to compare have corresponding
        IdTypes. Otherwise, the named array must be a StringArray.
        The identifier array does not necessarily have to specify a name
        for each vertex in the tree.  If some vertices are unnamed, then
        this filter will assign correspondence between ancestors of named
        vertices.
        """
    )

    def _id_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIdArrayName,
                        self.id_array_name)

    output_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the name of a new DoubleArray that will contain the
        results of the comparison between the two trees.  This new array
        will be added to the input tree's vertex_data or edge_data, based
        on the value of comparison_array_is_vertex_data.  If this method is
        not called, the new DoubleArray will be named "difference" by
        default.
        """
    )

    def _output_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputArrayName,
                        self.output_array_name)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('comparison_array_is_vertex_data', 'GetComparisonArrayIsVertexData'),
    ('comparison_array_name', 'GetComparisonArrayName'), ('id_array_name',
    'GetIdArrayName'), ('output_array_name', 'GetOutputArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'comparison_array_is_vertex_data',
    'comparison_array_name', 'id_array_name', 'output_array_name',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TreeDifferenceFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TreeDifferenceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['comparison_array_is_vertex_data',
            'comparison_array_name', 'id_array_name', 'output_array_name']),
            title='Edit TreeDifferenceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TreeDifferenceFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

