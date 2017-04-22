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


class SelectionSource(SelectionAlgorithm):
    """
    SelectionSource - Generate selection from given set of ids
    SelectionSource generates a Selection from a set of (piece id,
    cell id) pairs.
    
    Superclass: SelectionAlgorithm
    
    It will only generate the selection values that match
    UPDATE_PIECE_NUMBER (i.e. piece == UPDATE_PIECE_NUMBER).
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectionSource, obj, update, **traits)
    
    array_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Access to the component number for the array specified by
        array_name. Default is component 0. Use -1 for magnitude.
        """
    )

    def _array_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayComponent,
                        self.array_component)

    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Access to the name of the selection's subset description array.
        """
    )

    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    composite_index = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If composite_index < 0 then COMPOSITE_INDEX() is not added to the
        output.
        """
    )

    def _composite_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCompositeIndex,
                        self.composite_index)

    containing_cells = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        When extracting by points, extract the cells that contain the
        passing points.
        """
    )

    def _containing_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContainingCells,
                        self.containing_cells)

    content_type = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set the content type for the generated selection. Possible values
        are as defined by Selection::SelectionContent.
        """
    )

    def _content_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContentType,
                        self.content_type)

    field_type = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set the field type for the generated selection. Possible values
        are as defined by Selection::SelectionField.
        """
    )

    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    hierarchical_index = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If hierarchical_level or hierarchical_index < 0 , then
        HIERARCHICAL_LEVEL() and HIERARCHICAL_INDEX() keys are not added
        to the output.
        """
    )

    def _hierarchical_index_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHierarchicalIndex,
                        self.hierarchical_index)

    hierarchical_level = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        If hierarchical_level or hierarchical_index < 0 , then
        HIERARCHICAL_LEVEL() and HIERARCHICAL_INDEX() keys are not added
        to the output.
        """
    )

    def _hierarchical_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHierarchicalLevel,
                        self.hierarchical_level)

    inverse = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Determines whether the selection describes what to include or
        exclude. Default is 0, meaning include.
        """
    )

    def _inverse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInverse,
                        self.inverse)

    query_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the query expression string.
        """
    )

    def _query_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQueryString,
                        self.query_string)

    def add_block(self, *args):
        """
        V.add_block(int)
        C++: void AddBlock(IdType blockno)
        Add the flat-index/composite index for a block.
        """
        ret = self._wrap_call(self._vtk_obj.AddBlock, *args)
        return ret

    def add_id(self, *args):
        """
        V.add_id(int, int)
        C++: void AddID(IdType piece, IdType id)
        Add a (piece, id) to the selection set. The source will generate
        only the ids for which piece == UPDATE_PIECE_NUMBER. If piece ==
        -1, the id applies to all pieces.
        """
        ret = self._wrap_call(self._vtk_obj.AddID, *args)
        return ret

    def add_location(self, *args):
        """
        V.add_location(float, float, float)
        C++: void AddLocation(double x, double y, double z)
        Add a point in world space to probe at.
        """
        ret = self._wrap_call(self._vtk_obj.AddLocation, *args)
        return ret

    def add_string_id(self, *args):
        """
        V.add_string_id(int, string)
        C++: void AddStringID(IdType piece, const char *id)
        Add a (piece, id) to the selection set. The source will generate
        only the ids for which piece == UPDATE_PIECE_NUMBER. If piece ==
        -1, the id applies to all pieces.
        """
        ret = self._wrap_call(self._vtk_obj.AddStringID, *args)
        return ret

    def add_threshold(self, *args):
        """
        V.add_threshold(float, float)
        C++: void AddThreshold(double min, double max)
        Add a value range to threshold within.
        """
        ret = self._wrap_call(self._vtk_obj.AddThreshold, *args)
        return ret

    def remove_all_blocks(self):
        """
        V.remove_all_blocks()
        C++: void RemoveAllBlocks()
        Remove all blocks added with add_block.
        """
        ret = self._vtk_obj.RemoveAllBlocks()
        return ret
        

    def remove_all_i_ds(self):
        """
        V.remove_all_i_ds()
        C++: void RemoveAllIDs()
        Removes all IDs.
        """
        ret = self._vtk_obj.RemoveAllIDs()
        return ret
        

    def remove_all_locations(self):
        """
        V.remove_all_locations()
        C++: void RemoveAllLocations()
        Remove all locations added with add_location.
        """
        ret = self._vtk_obj.RemoveAllLocations()
        return ret
        

    def remove_all_string_i_ds(self):
        """
        V.remove_all_string_i_ds()
        C++: void RemoveAllStringIDs()
        Removes all IDs.
        """
        ret = self._vtk_obj.RemoveAllStringIDs()
        return ret
        

    def remove_all_thresholds(self):
        """
        V.remove_all_thresholds()
        C++: void RemoveAllThresholds()
        Remove all thresholds added with add_threshold.
        """
        ret = self._vtk_obj.RemoveAllThresholds()
        return ret
        

    def set_frustum(self, *args):
        """
        V.set_frustum([float, ...])
        C++: void SetFrustum(double *vertices)
        Set a frustum to choose within.
        """
        ret = self._wrap_call(self._vtk_obj.SetFrustum, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('array_component', 'GetArrayComponent'), ('array_name',
    'GetArrayName'), ('composite_index', 'GetCompositeIndex'),
    ('containing_cells', 'GetContainingCells'), ('content_type',
    'GetContentType'), ('field_type', 'GetFieldType'),
    ('hierarchical_index', 'GetHierarchicalIndex'), ('hierarchical_level',
    'GetHierarchicalLevel'), ('inverse', 'GetInverse'), ('query_string',
    'GetQueryString'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_component', 'array_name',
    'composite_index', 'containing_cells', 'content_type', 'field_type',
    'hierarchical_index', 'hierarchical_level', 'inverse',
    'progress_text', 'query_string'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectionSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['array_component', 'array_name', 'composite_index',
            'containing_cells', 'content_type', 'field_type',
            'hierarchical_index', 'hierarchical_level', 'inverse',
            'query_string']),
            title='Edit SelectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectionSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

