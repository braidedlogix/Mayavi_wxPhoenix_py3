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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class TransferAttributes(PassInputTypeAlgorithm):
    """
    TransferAttributes - transfer data from a graph representation to
    a tree representation using direct mapping or pedigree ids.
    
    Superclass: PassInputTypeAlgorithm
    
    The filter requires both a Graph and Tree as input.  The tree
    vertices must be a superset of the graph vertices.  A common example
    is when the graph vertices correspond to the leaves of the tree, but
    the internal vertices of the tree represent groupings of graph
    vertices.  The algorithm matches the vertices using the array
    "_pedigree_id".  The user may alternately set the direct_mapping flag to
    indicate that the two structures must have directly corresponding
    offsets (i.e. node i in the graph must correspond to node i in the
    tree).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTransferAttributes, obj, update, **traits)
    
    direct_mapping = tvtk_base.false_bool_trait(help=\
        """
        If on, uses direct mapping from tree to graph vertices. If off,
        both the graph and tree must contain pedigree_id arrays which are
        used to match graph and tree vertices. Default is off.
        """
    )

    def _direct_mapping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirectMapping,
                        self.direct_mapping_)

    source_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The field name to use for storing the source array.
        """
    )

    def _source_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSourceArrayName,
                        self.source_array_name)

    source_field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The source field type for accessing the source array. Valid
        values are those from enum DataObject::FieldAssociations.
        """
    )

    def _source_field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSourceFieldType,
                        self.source_field_type)

    target_array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        The field name to use for storing the source array.
        """
    )

    def _target_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetArrayName,
                        self.target_array_name)

    target_field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The target field type for accessing the target array. Valid
        values are those from enum DataObject::FieldAssociations.
        """
    )

    def _target_field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTargetFieldType,
                        self.target_field_type)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
        Set the input type of the algorithm to Graph.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    _updateable_traits_ = \
    (('direct_mapping', 'GetDirectMapping'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('source_array_name',
    'GetSourceArrayName'), ('source_field_type', 'GetSourceFieldType'),
    ('target_array_name', 'GetTargetArrayName'), ('target_field_type',
    'GetTargetFieldType'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'direct_mapping',
    'global_warning_display', 'release_data_flag', 'progress_text',
    'source_array_name', 'source_field_type', 'target_array_name',
    'target_field_type'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TransferAttributes, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TransferAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['direct_mapping'], [], ['source_array_name',
            'source_field_type', 'target_array_name', 'target_field_type']),
            title='Edit TransferAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TransferAttributes properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

