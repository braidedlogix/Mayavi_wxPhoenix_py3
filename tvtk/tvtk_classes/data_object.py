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


class DataObject(Object):
    """
    DataObject - general representation of visualization data
    
    Superclass: Object
    
    DataObject is an general representation of visualization data. It
    serves to encapsulate instance variables and methods for
    visualization network execution, as well as representing data
    consisting of a field (i.e., just an unstructured pile of data). This
    is to be compared with a DataSet, which is data with geometric
    and/or topological structure.
    
    DataObjects are used to represent arbitrary repositories of data
    via the FieldData instance variable. These data must be eventually
    mapped into a concrete subclass of DataSet before they can
    actually be displayed.
    
    @sa
    DataSet FieldData DataObjectToDataSetFilter
    FieldDataToAttributeDataFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkDataObject, obj, update, **traits)
    
    global_release_data_flag = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off flag to control whether every object releases its
        data after being used by a filter.
        """
    )

    def _global_release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGlobalReleaseDataFlag,
                        self.global_release_data_flag_)

    def _get_field_data(self):
        return wrap_vtk(self._vtk_obj.GetFieldData())
    def _set_field_data(self, arg):
        old_val = self._get_field_data()
        self._wrap_call(self._vtk_obj.SetFieldData,
                        deref_vtk(arg))
        self.trait_property_changed('field_data', old_val, arg)
    field_data = traits.Property(_get_field_data, _set_field_data, help=\
        """
        Assign or retrieve a general field data to this data object.
        """
    )

    def _get_information(self):
        return wrap_vtk(self._vtk_obj.GetInformation())
    def _set_information(self, arg):
        old_val = self._get_information()
        self._wrap_call(self._vtk_obj.SetInformation,
                        deref_vtk(arg))
        self.trait_property_changed('information', old_val, arg)
    information = traits.Property(_get_information, _set_information, help=\
        """
        Set/Get the information object associated with this data object.
        """
    )

    def get_active_field_information(self, *args):
        """
        V.get_active_field_information(Information, int, int)
            -> Information
        C++: static Information *GetActiveFieldInformation(
            Information *info, int fieldAssociation, int attributeType)
        Return the information object within the input information
        object's field data corresponding to the specified association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS) and
        attribute (SCALARS, VECTORS, NORMALS, TCOORDS, or TENSORS)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetActiveFieldInformation, *my_args)
        return wrap_vtk(ret)

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the actual size of the data in kibibytes (1024 bytes).
        This number is valid only after the pipeline has updated. The
        memory size returned is guaranteed to be greater than or equal to
        the memory required to represent the data (e.g., extra space in
        arrays, etc. are not included in the return value).
        """
    )

    def get_association_type_as_string(self, *args):
        """
        V.get_association_type_as_string(int) -> string
        C++: static const char *GetAssociationTypeAsString(
            int associationType)
        Given an integer association type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Points").
        """
        ret = self._wrap_call(self._vtk_obj.GetAssociationTypeAsString, *args)
        return ret

    def get_association_type_from_string(self, *args):
        """
        V.get_association_type_from_string(string) -> int
        C++: static int GetAssociationTypeFromString(
            const char *associationType)
        Given an integer association type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Points").
        """
        ret = self._wrap_call(self._vtk_obj.GetAssociationTypeFromString, *args)
        return ret

    def get_attribute_type_for_array(self, *args):
        """
        V.get_attribute_type_for_array(AbstractArray) -> int
        C++: virtual int GetAttributeTypeForArray(AbstractArray *arr)
        Retrieves the attribute type that an array came from. This is
        useful for obtaining which attribute type a input array to an
        algorithm came from (retrieved from
        get_input_abstract_array_to_processs).
        """
        my_args = deref_array(args, [['vtkAbstractArray']])
        ret = self._wrap_call(self._vtk_obj.GetAttributeTypeForArray, *my_args)
        return ret

    def get_attributes(self, *args):
        """
        V.get_attributes(int) -> DataSetAttributes
        C++: virtual DataSetAttributes *GetAttributes(int type)
        Returns the attributes of the data object of the specified
        attribute type. The type may be:  POINT  - Defined in DataSet
        subclasses. CELL   - Defined in DataSet subclasses. VERTEX -
        Defined in Graph subclasses. EDGE   - Defined in Graph
        subclasses. ROW    - Defined in Table.  The other attribute
        type, FIELD, will return NULL since field data is stored as a
        FieldData instance, not a DataSetAttributes instance. To
        retrieve field data, use get_attributes_as_field_data.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributes, *args)
        return wrap_vtk(ret)

    def get_attributes_as_field_data(self, *args):
        """
        V.get_attributes_as_field_data(int) -> FieldData
        C++: virtual FieldData *GetAttributesAsFieldData(int type)
        Returns the attributes of the data object as a FieldData. This
        returns non-null values in all the same cases as get_attributes,
        in addition to the case of FIELD, which will return the field
        data for any DataObject subclass.
        """
        ret = self._wrap_call(self._vtk_obj.GetAttributesAsFieldData, *args)
        return wrap_vtk(ret)

    def get_data(self, *args):
        """
        V.get_data(Information) -> DataObject
        C++: static DataObject *GetData(Information *info)
        V.get_data(InformationVector, int) -> DataObject
        C++: static DataObject *GetData(InformationVector *v,
            int i=0)
        Retrieve an instance of this class from an information object.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetData, *my_args)
        return wrap_vtk(ret)

    def _get_data_object_type(self):
        return self._vtk_obj.GetDataObjectType()
    data_object_type = traits.Property(_get_data_object_type, help=\
        """
        Return class name of data type. This is one of
        VTK_STRUCTURED_GRID, VTK_STRUCTURED_POINTS,
        VTK_UNSTRUCTURED_GRID, VTK_POLY_DATA, or VTK_RECTILINEAR_GRID
        (see SetGet.h for definitions). THIS METHOD IS THREAD SAFE
        """
    )

    def _get_data_released(self):
        return self._vtk_obj.GetDataReleased()
    data_released = traits.Property(_get_data_released, help=\
        """
        Get the flag indicating the data has been released.
        """
    )

    def _get_extent_type(self):
        return self._vtk_obj.GetExtentType()
    extent_type = traits.Property(_get_extent_type, help=\
        """
        The extent_type will be left as VTK_PIECES_EXTENT for data objects
        such as PolyData and UnstructuredGrid. The extent_type will
        be changed to vtk__3d__extent for data objects with 3d structure
        such as ImageData (and its subclass StructuredPoints),
        RectilinearGrid, and StructuredGrid. The default is the
        have an extent in pieces, with only one piece (no streaming
        possible).
        """
    )

    def get_named_field_information(self, *args):
        """
        V.get_named_field_information(Information, int, string)
            -> Information
        C++: static Information *GetNamedFieldInformation(
            Information *info, int fieldAssociation, const char *name)
        Return the information object within the input information
        object's field data corresponding to the specified association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS) and name.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetNamedFieldInformation, *my_args)
        return wrap_vtk(ret)

    def get_number_of_elements(self, *args):
        """
        V.get_number_of_elements(int) -> int
        C++: virtual IdType GetNumberOfElements(int type)
        Get the number of elements for a specific attribute type (POINT,
        CELL, etc.).
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfElements, *args)
        return ret

    def _get_update_time(self):
        return self._vtk_obj.GetUpdateTime()
    update_time = traits.Property(_get_update_time, help=\
        """
        Used by Threaded ports to determine if they should initiate an
        asynchronous update (still in development).
        """
    )

    def ALL_PIECES_EXTENT(self):
        """
        V.all__pieces__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *ALL_PIECES_EXTENT()"""
        ret = wrap_vtk(self._vtk_obj.ALL_PIECES_EXTENT())
        return ret
        

    def BOUNDING_BOX(self):
        """
        V.bounding__box() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *BOUNDING_BOX()"""
        ret = wrap_vtk(self._vtk_obj.BOUNDING_BOX())
        return ret
        

    def CELL_DATA_VECTOR(self):
        """
        V.cell__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *CELL_DATA_VECTOR()"""
        ret = wrap_vtk(self._vtk_obj.CELL_DATA_VECTOR())
        return ret
        

    def copy_information_from_pipeline(self, *args):
        """
        V.copy_information_from_pipeline(Information)
        C++: virtual void CopyInformationFromPipeline(
            Information *info)
        Copy from the pipeline information to the data object's own
        information. Called right before the main execution pass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformationFromPipeline, *my_args)
        return ret

    def copy_information_to_pipeline(self, *args):
        """
        V.copy_information_to_pipeline(Information)
        C++: virtual void CopyInformationToPipeline(Information *info)
        Copy information from this data object to the pipeline
        information. This is used by the TrivialProducer that is
        created when someone calls set_input_data() to connect a data
        object to a pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyInformationToPipeline, *my_args)
        return ret

    def crop(self, *args):
        """
        V.crop((int, ...))
        C++: virtual void Crop(const int *updateExtent)
        This method crops the data object (if necessary) so that the
        extent matches the update extent.
        """
        ret = self._wrap_call(self._vtk_obj.Crop, *args)
        return ret

    def DATA_EXTENT(self):
        """
        V.data__extent() -> InformationIntegerPointerKey
        C++: static InformationIntegerPointerKey *DATA_EXTENT()"""
        ret = wrap_vtk(self._vtk_obj.DATA_EXTENT())
        return ret
        

    def DATA_EXTENT_TYPE(self):
        """
        V.data__extent__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_EXTENT_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.DATA_EXTENT_TYPE())
        return ret
        

    def DATA_NUMBER_OF_GHOST_LEVELS(self):
        """
        V.data__number__of__ghost__levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_NUMBER_OF_GHOST_LEVELS(
            )"""
        ret = wrap_vtk(self._vtk_obj.DATA_NUMBER_OF_GHOST_LEVELS())
        return ret
        

    def DATA_NUMBER_OF_PIECES(self):
        """
        V.data__number__of__pieces() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_NUMBER_OF_PIECES()"""
        ret = wrap_vtk(self._vtk_obj.DATA_NUMBER_OF_PIECES())
        return ret
        

    def DATA_OBJECT(self):
        """
        V.data__object() -> InformationDataObjectKey
        C++: static InformationDataObjectKey *DATA_OBJECT()"""
        ret = wrap_vtk(self._vtk_obj.DATA_OBJECT())
        return ret
        

    def DATA_PIECE_NUMBER(self):
        """
        V.data__piece__number() -> InformationIntegerKey
        C++: static InformationIntegerKey *DATA_PIECE_NUMBER()"""
        ret = wrap_vtk(self._vtk_obj.DATA_PIECE_NUMBER())
        return ret
        

    def DATA_TIME_STEP(self):
        """
        V.data__time__step() -> InformationDoubleKey
        C++: static InformationDoubleKey *DATA_TIME_STEP()"""
        ret = wrap_vtk(self._vtk_obj.DATA_TIME_STEP())
        return ret
        

    def DATA_TYPE_NAME(self):
        """
        V.data__type__name() -> InformationStringKey
        C++: static InformationStringKey *DATA_TYPE_NAME()"""
        ret = wrap_vtk(self._vtk_obj.DATA_TYPE_NAME())
        return ret
        

    def data_has_been_generated(self):
        """
        V.data_has_been_generated()
        C++: void DataHasBeenGenerated()
        This method is called by the source when it executes to generate
        data. It is sort of the opposite of release_data. It sets the
        data_released flag to 0, and sets a new update_time.
        """
        ret = self._vtk_obj.DataHasBeenGenerated()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(DataObject)
        C++: virtual void DeepCopy(DataObject *src)
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def EDGE_DATA_VECTOR(self):
        """
        V.edge__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *EDGE_DATA_VECTOR()"""
        ret = wrap_vtk(self._vtk_obj.EDGE_DATA_VECTOR())
        return ret
        

    def FIELD_ACTIVE_ATTRIBUTE(self):
        """
        V.field__active__attribute() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ACTIVE_ATTRIBUTE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ACTIVE_ATTRIBUTE())
        return ret
        

    def FIELD_ARRAY_TYPE(self):
        """
        V.field__array__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ARRAY_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ARRAY_TYPE())
        return ret
        

    def FIELD_ASSOCIATION(self):
        """
        V.field__association() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ASSOCIATION()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ASSOCIATION())
        return ret
        

    def FIELD_ATTRIBUTE_TYPE(self):
        """
        V.field__attribute__type() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_ATTRIBUTE_TYPE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_ATTRIBUTE_TYPE())
        return ret
        

    def FIELD_NAME(self):
        """
        V.field__name() -> InformationStringKey
        C++: static InformationStringKey *FIELD_NAME()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NAME())
        return ret
        

    def FIELD_NUMBER_OF_COMPONENTS(self):
        """
        V.field__number__of__components() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_NUMBER_OF_COMPONENTS()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NUMBER_OF_COMPONENTS())
        return ret
        

    def FIELD_NUMBER_OF_TUPLES(self):
        """
        V.field__number__of__tuples() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_NUMBER_OF_TUPLES()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_NUMBER_OF_TUPLES())
        return ret
        

    def FIELD_OPERATION(self):
        """
        V.field__operation() -> InformationIntegerKey
        C++: static InformationIntegerKey *FIELD_OPERATION()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_OPERATION())
        return ret
        

    def FIELD_RANGE(self):
        """
        V.field__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *FIELD_RANGE()"""
        ret = wrap_vtk(self._vtk_obj.FIELD_RANGE())
        return ret
        

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Restore data object to initial state,
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def ORIGIN(self):
        """
        V.origin() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *ORIGIN()"""
        ret = wrap_vtk(self._vtk_obj.ORIGIN())
        return ret
        

    def PIECE_EXTENT(self):
        """
        V.piece__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *PIECE_EXTENT()"""
        ret = wrap_vtk(self._vtk_obj.PIECE_EXTENT())
        return ret
        

    def POINT_DATA_VECTOR(self):
        """
        V.point__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *POINT_DATA_VECTOR(
            )"""
        ret = wrap_vtk(self._vtk_obj.POINT_DATA_VECTOR())
        return ret
        

    def prepare_for_new_data(self):
        """
        V.prepare_for_new_data()
        C++: virtual void PrepareForNewData()
        make the output data ready for new data to be inserted. For most
        objects we just call Initialize. But for ImageData we leave
        the old data in case the memory can be reused.
        """
        ret = self._vtk_obj.PrepareForNewData()
        return ret
        

    def release_data(self):
        """
        V.release_data()
        C++: void ReleaseData()
        Release data back to system to conserve memory resource. Used
        during visualization network execution.  Releasing this data does
        not make down-stream data invalid, so it does not modify the
        MTime of this data object.
        """
        ret = self._vtk_obj.ReleaseData()
        return ret
        

    def remove_named_field_information(self, *args):
        """
        V.remove_named_field_information(Information, int, string)
        C++: static void RemoveNamedFieldInformation(Information *info,
             int fieldAssociation, const char *name)
        Remove the info associated with an array
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveNamedFieldInformation, *my_args)
        return ret

    def SIL(self):
        """
        V.sil() -> InformationDataObjectKey
        C++: static InformationDataObjectKey *SIL()"""
        ret = wrap_vtk(self._vtk_obj.SIL())
        return ret
        

    def SPACING(self):
        """
        V.spacing() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *SPACING()"""
        ret = wrap_vtk(self._vtk_obj.SPACING())
        return ret
        

    def set_active_attribute(self, *args):
        """
        V.set_active_attribute(Information, int, string, int)
            -> Information
        C++: static Information *SetActiveAttribute(
            Information *info, int fieldAssociation,
            const char *attributeName, int attributeType)
        Set the named array to be the active field for the specified type
        (SCALARS, VECTORS, NORMALS, TCOORDS, or TENSORS) and association
        (FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS).  Returns
        the active field information object and creates on entry if one
        not found.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetActiveAttribute, *my_args)
        return wrap_vtk(ret)

    def set_active_attribute_info(self, *args):
        """
        V.set_active_attribute_info(Information, int, int, string, int,
            int, int)
        C++: static void SetActiveAttributeInfo(Information *info,
            int fieldAssociation, int attributeType, const char *name,
            int arrayType, int numComponents, int numTuples)
        Set the name, array type, number of components, and number of
        tuples within the passed information object for the active
        attribute of type attribute_type (in specified association,
        FIELD_ASSOCIATION_POINTS or FIELD_ASSOCIATION_CELLS).  If there
        is not an active attribute of the specified type, an entry in the
        information object is created.  If array_type, num_components, or
        num_tuples equal to -1, or name=NULL the value is not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetActiveAttributeInfo, *my_args)
        return ret

    def set_point_data_active_scalar_info(self, *args):
        """
        V.set_point_data_active_scalar_info(Information, int, int)
        C++: static void SetPointDataActiveScalarInfo(
            Information *info, int arrayType, int numComponents)
        Convenience version of previous method for use (primarily) by the
        Imaging filters. If array_type or num_components == -1, the value
        is not changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetPointDataActiveScalarInfo, *my_args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(DataObject)
        C++: virtual void ShallowCopy(DataObject *src)
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def VERTEX_DATA_VECTOR(self):
        """
        V.vertex__data__vector() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *VERTEX_DATA_VECTOR(
            )"""
        ret = wrap_vtk(self._vtk_obj.VERTEX_DATA_VECTOR())
        return ret
        

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(DataObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit DataObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

