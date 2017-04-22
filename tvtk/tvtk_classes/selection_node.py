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

from tvtk.tvtk_classes.object import Object


class SelectionNode(Object):
    """
    SelectionNode - A node in a selection tree.
    
    Superclass: Object
    
    Used to store selection results.
    
    SelectionNode stores selection parameters for a selection (or part
    of a selection). It stores a list of properties (in a Information)
    and a list of selection values (in a AbstractArray). The
    properties provide information about what the selection values mean.
    For example the CONTENT_TYPE property gives information about what is
    stored by the node. If the CONTENT_TYPE is GLOBALIDS, the
    selection_list array should contain a list of cell or point ids, which
    identify the particular cells or points that have matching values in
    the GLOBALID DataSetAttribute array. If the CONTENT_TYPE is
    PEDIGREEIDS, the selection_list array should contain a list of cell or
    point ids, which identify the particular cells or points that have
    matching values in the PEDIGREEID DataSetAttribute array. The
    FIELD_TYPE property designates whether the selection refers to cells
    or points.
    
    Usually, each node under the root is a selection from one data
    object. SOURCE or SOURCE_ID properties point to this object. If the
    selection was performed on a renderer, PROP or PROP_ID point to the
    prop the selection was made on. Selection nodes corresponding to
    composite datasets may contain child nodes. Each child node of a
    composite dataset should have COMPOSITE_INDEX set. This is the
    flat-index to identify a node with in the composite dataset to which
    the selection applies.
    
    @warning
    No selection_list is created by default. It should be assigned.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSelectionNode, obj, update, **traits)
    
    content_type = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get or set the content type of the selection. This is the same as
        setting the CONTENT_TYPE() key on the property.
        """
    )

    def _content_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetContentType,
                        self.content_type)

    field_type = traits.Int(-1, enter_set=True, auto_set=False, help=\
        """
        Get or set the field type of the selection. This is the same as
        setting the FIELD_TYPE() key on the property.
        """
    )

    def _field_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFieldType,
                        self.field_type)

    query_string = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the query expression string.
        """
    )

    def _query_string_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetQueryString,
                        self.query_string)

    def _get_selection_data(self):
        return wrap_vtk(self._vtk_obj.GetSelectionData())
    def _set_selection_data(self, arg):
        old_val = self._get_selection_data()
        self._wrap_call(self._vtk_obj.SetSelectionData,
                        deref_vtk(arg))
        self.trait_property_changed('selection_data', old_val, arg)
    selection_data = traits.Property(_get_selection_data, _set_selection_data, help=\
        """
        Sets the selection table.
        """
    )

    def _get_selection_list(self):
        return wrap_vtk(self._vtk_obj.GetSelectionList())
    def _set_selection_list(self, arg):
        old_val = self._get_selection_list()
        my_arg = deref_array([arg], [['vtkAbstractArray']])
        self._wrap_call(self._vtk_obj.SetSelectionList,
                        my_arg[0])
        self.trait_property_changed('selection_list', old_val, arg)
    selection_list = traits.Property(_get_selection_list, _set_selection_list, help=\
        """
        Sets the selection list.
        """
    )

    def _get_properties(self):
        return wrap_vtk(self._vtk_obj.GetProperties())
    properties = traits.Property(_get_properties, help=\
        """
        Returns the property map.
        """
    )

    def COMPONENT_NUMBER(self):
        """
        V.component__number() -> InformationIntegerKey
        C++: static InformationIntegerKey *COMPONENT_NUMBER()
        When content_type==_thresholds  or content_type==_values i.e.
        threshold and value based selections, it is possible pick the
        component number using this key. If none is specified, the 0th
        component is used. If any number less than 0 is specified, then
        the magnitude is used.
        """
        ret = wrap_vtk(self._vtk_obj.COMPONENT_NUMBER())
        return ret
        

    def COMPOSITE_INDEX(self):
        """
        V.composite__index() -> InformationIntegerKey
        C++: static InformationIntegerKey *COMPOSITE_INDEX()
        Used to identify a node in composite datasets.
        """
        ret = wrap_vtk(self._vtk_obj.COMPOSITE_INDEX())
        return ret
        

    def CONTAINING_CELLS(self):
        """
        V.containing__cells() -> InformationIntegerKey
        C++: static InformationIntegerKey *CONTAINING_CELLS()
        This flag tells the extraction filter, when FIELD_TYPE==POINT,
        that it should also extract the cells that contain any of the
        extracted points.
        """
        ret = wrap_vtk(self._vtk_obj.CONTAINING_CELLS())
        return ret
        

    def CONTENT_TYPE(self):
        """
        V.content__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *CONTENT_TYPE()
        Get the (primary) property that describes the content of a
        selection node's data. Other auxiliary description properties
        follow. GLOBALIDS means that the selection list contains values
        from the DataSetAttribute array of the same name. PEDIGREEIDS
        means that the selection list contains values from the
        DataSetAttribute array of the same name. VALUES means the the
        selection list contains values from an arbitrary attribute array
        (ignores any globalids attribute) INDICES means that the
        selection list contains indexes into the cell or point arrays.
        FRUSTUM means the set of points and cells inside a frustum
        LOCATIONS means the set of points and cells near a set of
        positions THRESHOLDS means the points and cells with values
        within a set of ranges get_content_type() returns -1 if the content
        type is not set.
        """
        ret = wrap_vtk(self._vtk_obj.CONTENT_TYPE())
        return ret
        

    def convert_attribute_type_to_selection_field(self, *args):
        """
        V.convert_attribute_type_to_selection_field(int) -> int
        C++: static int ConvertAttributeTypeToSelectionField(int val)
        Methods to convert SelectionNode::SelectionField to
        DataSetAttribute::AttributeTypes and vice-versa.
        """
        ret = self._wrap_call(self._vtk_obj.ConvertAttributeTypeToSelectionField, *args)
        return ret

    def convert_selection_field_to_attribute_type(self, *args):
        """
        V.convert_selection_field_to_attribute_type(int) -> int
        C++: static int ConvertSelectionFieldToAttributeType(int val)
        Methods to convert SelectionNode::SelectionField to
        DataSetAttribute::AttributeTypes and vice-versa.
        """
        ret = self._wrap_call(self._vtk_obj.ConvertSelectionFieldToAttributeType, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(SelectionNode)
        C++: virtual void DeepCopy(SelectionNode *src)
        Copy properties, selection list and children of the input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def EPSILON(self):
        """
        V.epsilon() -> InformationDoubleKey
        C++: static InformationDoubleKey *EPSILON()
        For location selection of points, if distance is greater than
        this reject.
        """
        ret = wrap_vtk(self._vtk_obj.EPSILON())
        return ret
        

    def equal_properties(self, *args):
        """
        V.equal_properties(SelectionNode, bool) -> bool
        C++: bool EqualProperties(SelectionNode *other,
            bool fullcompare=true)
        Compares Properties of self and other to ensure that they are
        exactly same.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.EqualProperties, *my_args)
        return ret

    def FIELD_TYPE(self):
        """
        V.field__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_TYPE()
        Controls whether cell, point, or field data determine what is
        inside and out. The default is CELL. Vertex and edge types are
        also available for graph classes. get_field_type() returns -1 if
        the field type is not set.
        """
        ret = wrap_vtk(self._vtk_obj.FIELD_TYPE())
        return ret
        

    def HIERARCHICAL_INDEX(self):
        """
        V.hierarchical__index() -> InformationIntegerKey
        C++: static InformationIntegerKey *HIERARCHICAL_INDEX()
        Used to identify a dataset in a hiererchical box dataset.
        """
        ret = wrap_vtk(self._vtk_obj.HIERARCHICAL_INDEX())
        return ret
        

    def HIERARCHICAL_LEVEL(self):
        """
        V.hierarchical__level() -> InformationIntegerKey
        C++: static InformationIntegerKey *HIERARCHICAL_LEVEL()
        Used to identify a dataset in a hiererchical box dataset.
        """
        ret = wrap_vtk(self._vtk_obj.HIERARCHICAL_LEVEL())
        return ret
        

    def INDEXED_VERTICES(self):
        """
        V.indexed__vertices() -> InformationIntegerKey
        C++: static InformationIntegerKey *INDEXED_VERTICES()
        This key is used when making visible vertex selection. It means
        that the cell ID selection has data about which vertices for each
        cell are visible.
        """
        ret = wrap_vtk(self._vtk_obj.INDEXED_VERTICES())
        return ret
        

    def INVERSE(self):
        """
        V.inverse() -> InformationIntegerKey
        C++: static InformationIntegerKey *INVERSE()
        This flag tells the extraction filter to exclude the selection.
        """
        ret = wrap_vtk(self._vtk_obj.INVERSE())
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Restore data object to initial state,
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def PIXEL_COUNT(self):
        """
        V.pixel__count() -> InformationIntegerKey
        C++: static InformationIntegerKey *PIXEL_COUNT()
        A helper for visible cell selector, this is the number of pixels
        covered by the actor whose cells are listed in the selection.
        """
        ret = wrap_vtk(self._vtk_obj.PIXEL_COUNT())
        return ret
        

    def PROCESS_ID(self):
        """
        V.process__id() -> InformationIntegerKey
        C++: static InformationIntegerKey *PROCESS_ID()
        Process id the selection is on.
        """
        ret = wrap_vtk(self._vtk_obj.PROCESS_ID())
        return ret
        

    def PROP(self):
        """
        V.prop() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *PROP()
        Pointer to the prop the selection belongs to.
        """
        ret = wrap_vtk(self._vtk_obj.PROP())
        return ret
        

    def PROP_ID(self):
        """
        V.prop__id() -> InformationIntegerKey
        C++: static InformationIntegerKey *PROP_ID()
        ID of the prop the selection belongs to. What ID means is
        application specific.
        """
        ret = wrap_vtk(self._vtk_obj.PROP_ID())
        return ret
        

    def SOURCE(self):
        """
        V.source() -> InformationObjectBaseKey
        C++: static InformationObjectBaseKey *SOURCE()
        Pointer to the data or algorithm the selection belongs to.
        """
        ret = wrap_vtk(self._vtk_obj.SOURCE())
        return ret
        

    def SOURCE_ID(self):
        """
        V.source__id() -> InformationIntegerKey
        C++: static InformationIntegerKey *SOURCE_ID()
        ID of the data or algorithm the selection belongs to. What ID
        means is application specific.
        """
        ret = wrap_vtk(self._vtk_obj.SOURCE_ID())
        return ret
        

    def shallow_copy(self, *args):
        """
        V.shallow_copy(SelectionNode)
        C++: virtual void ShallowCopy(SelectionNode *src)
        Copy properties, selection list and children of the input. This
        is a shallow copy: selection lists and pointers in the properties
        are passed by reference.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def subtract_selection_list(self, *args):
        """
        V.subtract_selection_list(SelectionNode)
        C++: void SubtractSelectionList(SelectionNode *other)
        Subtracts the items in the selection list, other, from this
        selection list. Assumes that both selections have identical
        properties (i.e., test with equal_properties before using).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SubtractSelectionList, *my_args)
        return ret

    def union_selection_list(self, *args):
        """
        V.union_selection_list(SelectionNode)
        C++: void UnionSelectionList(SelectionNode *other)
        Merges the selection list between self and the other. Assumes
        that both has identical properties.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UnionSelectionList, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('content_type', 'GetContentType'),
    ('field_type', 'GetFieldType'), ('query_string', 'GetQueryString'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'content_type', 'field_type',
    'query_string'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SelectionNode, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SelectionNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['content_type', 'field_type', 'query_string']),
            title='Edit SelectionNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SelectionNode properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

