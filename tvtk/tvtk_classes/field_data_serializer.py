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


class FieldDataSerializer(Object):
    """
    FieldDataSerializer -  A concrete instance of Object which
    provides functionality for
     serializing and de-serializing field data, primarily used for the
    purpose
     of preparing the data for transfer over MPI or other communication
     mechanism.
    
    Superclass: Object
    
    @sa
    FieldData PointData CellData MultiProcessStream
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFieldDataSerializer, obj, update, **traits)
    
    def de_serialize_to_sub_extent(self, *args):
        """
        V.de_serialize_to_sub_extent([int, int, int, int, int, int], [int,
            int, int, int, int, int], FieldData, MultiProcessStream)
        C++: static void DeSerializeToSubExtent(int subext[6],
            int gridExtent[6], FieldData *fieldData,
            MultiProcessStream &bytestream)
        Deserializes the field data from a bytestream to a the given
        sub-extent. The field data can be either cell-centered or
        node-centered depending on what subext and grid_extent actually
        represent.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeSerializeToSubExtent, *my_args)
        return ret

    def deserialize(self, *args):
        """
        V.deserialize(MultiProcessStream, FieldData)
        C++: static void Deserialize(MultiProcessStream &bytestream,
            FieldData *fieldData)
        Deserializes the field data from a bytestream.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Deserialize, *my_args)
        return ret

    def deserialize_meta_data(self, *args):
        """
        V.deserialize_meta_data(MultiProcessStream, StringArray,
            IntArray, IntArray)
        C++: static void DeserializeMetaData(
            MultiProcessStream &bytestream, StringArray *names,
            IntArray *datatypes, IntArray *dimensions)
        Given the serialized field metadata in a bytestream, this method
        extracts the name, datatype and dimensions of each array. The
        metadata is deserialized on user-supplied, pre-allocated data
        structures. (1) names -- an array of strings wherein, each
        element, names[i], corresponds to the name of array i. (2)
        datatypes -- an array of ints where each element corresponds to
        the actual primitive type of each array, e.g.,VTK_DOUBLE,VTK_INT,
        etc. (3) dimensions -- a 2-component array of  integers where the
        first component corresponds to the number of tuples of and the
        second component corresponds to the number components of array i.
        """
        my_args = deref_array(args, [('vtkMultiProcessStream', 'vtkStringArray', 'vtkIntArray', 'vtkIntArray')])
        ret = self._wrap_call(self._vtk_obj.DeserializeMetaData, *my_args)
        return ret

    def serialize(self, *args):
        """
        V.serialize(FieldData, MultiProcessStream)
        C++: static void Serialize(FieldData *fieldData,
            MultiProcessStream &bytestream)
        Serializes the given field data (all the field data) into a
        bytestream.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Serialize, *my_args)
        return ret

    def serialize_meta_data(self, *args):
        """
        V.serialize_meta_data(FieldData, MultiProcessStream)
        C++: static void SerializeMetaData(FieldData *fieldData,
            MultiProcessStream &bytestream)
        Serializes the metadata of the given field data instance, i.e.,
        the number of arrays, the name of each array and their
        dimensions.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SerializeMetaData, *my_args)
        return ret

    def serialize_sub_extent(self, *args):
        """
        V.serialize_sub_extent([int, int, int, int, int, int], [int, int,
            int, int, int, int], FieldData, MultiProcessStream)
        C++: static void SerializeSubExtent(int subext[6],
            int gridExtent[6], FieldData *fieldData,
            MultiProcessStream &bytestream)
        Serializes the given sub-extent of field data of a structured
        grid in a byte-stream. The field data can be either cell-centered
        or node-centered depending on what subext and grid_extent actually
        represents.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SerializeSubExtent, *my_args)
        return ret

    def serialize_tuples(self, *args):
        """
        V.serialize_tuples(IdList, FieldData, MultiProcessStream)
        C++: static void SerializeTuples(IdList *tupleIds,
            FieldData *fieldData, MultiProcessStream &bytestream)
        Serializes the selected tuples from the the field data in a
        byte-stream.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkFieldData', 'vtkMultiProcessStream')])
        ret = self._wrap_call(self._vtk_obj.SerializeTuples, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FieldDataSerializer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FieldDataSerializer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit FieldDataSerializer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FieldDataSerializer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

