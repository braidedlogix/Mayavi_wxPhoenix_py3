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


class Algorithm(Object):
    """
    Algorithm - Superclass for all sources, filters, and sinks in VTK.
    
    Superclass: Object
    
    Algorithm is the superclass for all sources, filters, and sinks in
    VTK.  It defines a generalized interface for executing data
    processing algorithms.  Pipeline connections are associated with
    input and output ports that are independent of the type of data
    passing through the connections.
    
    Instances may be used independently or within pipelines with a
    variety of architectures and update mechanisms.  Pipelines are
    controlled by instances of Executive.  Every Algorithm instance
    has an associated Executive when it is used in a pipeline.  The
    executive is responsible for data flow.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAlgorithm, obj, update, **traits)
    
    abort_execute = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the abort_execute flag for the process object. Process
        objects may handle premature termination of execution in
        different ways.
        """
    )

    def _abort_execute_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAbortExecute,
                        self.abort_execute_)

    release_data_flag = tvtk_base.false_bool_trait(help=\
        """
        Turn release data flag on or off for all output ports.
        """
    )

    def _release_data_flag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReleaseDataFlag,
                        self.release_data_flag_)

    def _get_executive(self):
        return wrap_vtk(self._vtk_obj.GetExecutive())
    def _set_executive(self, arg):
        old_val = self._get_executive()
        self._wrap_call(self._vtk_obj.SetExecutive,
                        deref_vtk(arg))
        self.trait_property_changed('executive', old_val, arg)
    executive = traits.Property(_get_executive, _set_executive, help=\
        """
        Get this algorithm's executive.  If it has none, a default
        executive will be created.
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
        Set/Get the information object associated with this algorithm.
        """
    )

    def _get_input_connection(self):
        if self._vtk_obj.GetTotalNumberOfInputConnections():
            return wrap_vtk(self._vtk_obj.GetInputConnection(0, 0))
        else:
            return None
    
    def _set_input_connection(self, obj):
        old_val = self._get_input_connection()
        self._wrap_call(self._vtk_obj.SetInputConnection, deref_vtk(obj))
        self.trait_property_changed('input_connection', old_val, obj)
    input_connection = traits.Property(_get_input_connection,
                                       _set_input_connection,
                                       help="The first input connection for this object, i.e. the result of `get_input_connection(0, 0)`.")
    
    def get_input_connection(self, *args):
        """
        V.get_input_connection(int, int) -> AlgorithmOutput
        C++: AlgorithmOutput *GetInputConnection(int port, int index)
        Get the algorithm output port connected to an input port.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputConnection, *args)
        return wrap_vtk(ret)

    def set_input_connection(self, *args):
        """
        V.set_input_connection(int, AlgorithmOutput)
        C++: virtual void SetInputConnection(int port,
            AlgorithmOutput *input)
        V.set_input_connection(AlgorithmOutput)
        C++: virtual void SetInputConnection(AlgorithmOutput *input)
        Set the connection for the given input port index.  Each input
        port of a filter has a specific purpose.  A port may have zero or
        more connections and the required number is specified by each
        filter.  Setting the connection with this method removes all
        other connections from the port.  To add more than one connection
        use add_input_connection().
        
        * The input for the connection is the output port of another
        * filter, which is obtained with get_output_port().  Typical usage
          is
        
        * filter_2->_set_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputConnection, *my_args)
        return ret

    def get_input_data_object(self, *args):
        """
        V.get_input_data_object(int, int) -> DataObject
        C++: DataObject *GetInputDataObject(int port, int connection)
        Get the data object that will contain the algorithm input for the
        given port and given connection.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputDataObject, *args)
        return wrap_vtk(ret)

    def set_input_data_object(self, *args):
        """
        V.set_input_data_object(int, DataObject)
        C++: virtual void SetInputDataObject(int port,
            DataObject *data)
        V.set_input_data_object(DataObject)
        C++: virtual void SetInputDataObject(DataObject *data)
        Sets the data-object as an input on the given port index. Setting
        the input with this method removes all other connections from the
        port. Internally, this method creates a TrivialProducer
        instance and sets that as the input-connection for the given
        port. It is safe to call this method repeatedly with the same
        input data object. The MTime of the Algorithm will not change
        unless the data object changed.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputDataObject, *my_args)
        return ret

    progress = traits.Trait(0.0, traits.Range(0.0, 1.0, enter_set=True, auto_set=False), help=\
        """
        Set/Get the execution progress of a process object.
        """
    )

    def _progress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgress,
                        self.progress)

    def _get_progress_observer(self):
        return wrap_vtk(self._vtk_obj.GetProgressObserver())
    def _set_progress_observer(self, arg):
        old_val = self._get_progress_observer()
        self._wrap_call(self._vtk_obj.SetProgressObserver,
                        deref_vtk(arg))
        self.trait_property_changed('progress_observer', old_val, arg)
    progress_observer = traits.Property(_get_progress_observer, _set_progress_observer, help=\
        """
        If an progress_observer is set, the algorithm will report progress
        through it rather than directly. This means that it will call
        update_progress() on the progress_observer rather than itself
        report it and set progress. This is most useful in situations
        where multiple threads are executing an algorithm at the same
        time and want to handle progress locally.
        """
    )

    progress_text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the current text message associated with the progress state.
        This may be used by a calling process/GUI. Note: Because
        set_progress_text() is called from inside request_data() it does not
        modify the algorithm object. Algorithms are not allowed to modify
        themselves from inside request_data().
        """
    )

    def _progress_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProgressText,
                        self.progress_text)

    def get_update_extent(self, *args):
        """
        V.get_update_extent() -> (int, int, int, int, int, int)
        C++: int *GetUpdateExtent()
        V.get_update_extent(int) -> (int, int, int, int, int, int)
        C++: int *GetUpdateExtent(int port)
        V.get_update_extent(int, int, int, int, int, int)
        C++: void GetUpdateExtent(int &x0, int &x1, int &y0, int &y1,
            int &z0, int &z1)
        V.get_update_extent(int, int, int, int, int, int, int)
        C++: void GetUpdateExtent(int port, int &x0, int &x1, int &y0,
            int &y1, int &z0, int &z1)
        V.get_update_extent([int, int, int, int, int, int])
        C++: void GetUpdateExtent(int extent[6])
        V.get_update_extent(int, [int, int, int, int, int, int])
        C++: void GetUpdateExtent(int port, int extent[6])
        These functions return the update extent for output ports that
        use 3d extents. Where port is not specified, it is assumed to be
        0.
        """
        ret = self._wrap_call(self._vtk_obj.GetUpdateExtent, *args)
        return ret

    def set_update_extent(self, *args):
        """
        V.set_update_extent(int, int, int, int)
        C++: void SetUpdateExtent(int port, int piece, int numPieces,
            int ghostLevel)
        V.set_update_extent(int, int, int)
        C++: void SetUpdateExtent(int piece, int numPieces,
            int ghostLevel)
        V.set_update_extent(int, [int, int, int, int, int, int])
        C++: void SetUpdateExtent(int port, int extent[6])
        V.set_update_extent([int, int, int, int, int, int])
        C++: void SetUpdateExtent(int extent[6])
        Set the output update extent in terms of piece and ghost levels.
        """
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtent, *args)
        return ret

    def _get_error_code(self):
        return self._vtk_obj.GetErrorCode()
    error_code = traits.Property(_get_error_code, help=\
        """
        The error code contains a possible error that occurred while
        reading or writing the file.
        """
    )

    def _get_input_algorithm(self):
        return wrap_vtk(self._vtk_obj.GetInputAlgorithm())
    input_algorithm = traits.Property(_get_input_algorithm, help=\
        """
        Returns the algorithm and the output port index of that algorithm
        connected to a port-index pair.
        """
    )

    def get_input_array_information(self, *args):
        """
        V.get_input_array_information(int) -> Information
        C++: Information *GetInputArrayInformation(int idx)
        Get the info object for the specified input array to this
        algorithm
        """
        ret = self._wrap_call(self._vtk_obj.GetInputArrayInformation, *args)
        return wrap_vtk(ret)

    def _get_input_executive(self):
        return wrap_vtk(self._vtk_obj.GetInputExecutive())
    input_executive = traits.Property(_get_input_executive, help=\
        """
        Returns the executive associated with a particular input
        connection.
        """
    )

    def _get_input_information(self):
        return wrap_vtk(self._vtk_obj.GetInputInformation())
    input_information = traits.Property(_get_input_information, help=\
        """
        Return the information object that is associated with a
        particular input connection. This can be used to get meta-data
        coming from the REQUEST_INFORMATION pass and set requests for the
        REQUEST_UPDATE_EXTENT pass. NOTE: Do not use this in any of the
        pipeline passes. Use the information objects passed as arguments
        instead.
        """
    )

    def get_input_port_information(self, *args):
        """
        V.get_input_port_information(int) -> Information
        C++: Information *GetInputPortInformation(int port)
        Get the information object associated with an input port.  There
        is one input port per kind of input to the algorithm.  Each input
        port tells executives what kind of data and downstream requests
        this algorithm can handle for that input.
        """
        ret = self._wrap_call(self._vtk_obj.GetInputPortInformation, *args)
        return wrap_vtk(ret)

    def get_number_of_input_connections(self, *args):
        """
        V.get_number_of_input_connections(int) -> int
        C++: int GetNumberOfInputConnections(int port)
        Get the number of inputs currently connected to a port.
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfInputConnections, *args)
        return ret

    def _get_number_of_input_ports(self):
        return self._vtk_obj.GetNumberOfInputPorts()
    number_of_input_ports = traits.Property(_get_number_of_input_ports, help=\
        """
        Get the number of input ports used by the algorithm.
        """
    )

    def _get_number_of_output_ports(self):
        return self._vtk_obj.GetNumberOfOutputPorts()
    number_of_output_ports = traits.Property(_get_number_of_output_ports, help=\
        """
        Get the number of output ports provided by the algorithm.
        """
    )

    def get_output_data_object(self, *args):
        """
        V.get_output_data_object(int) -> DataObject
        C++: DataObject *GetOutputDataObject(int port)
        Get the data object that will contain the algorithm output for
        the given port.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputDataObject, *args)
        return wrap_vtk(ret)

    def get_output_information(self, *args):
        """
        V.get_output_information(int) -> Information
        C++: Information *GetOutputInformation(int port)
        Return the information object that is associated with a
        particular output port. This can be used to set meta-data coming
        during the REQUEST_INFORMATION. NOTE: Do not use this in any of
        the pipeline passes. Use the information objects passed as
        arguments instead.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputInformation, *args)
        return wrap_vtk(ret)

    def _get_output_port(self):
        if self._vtk_obj.GetNumberOfOutputPorts():
            return wrap_vtk(self._vtk_obj.GetOutputPort())
        else:
            return None
    output_port = traits.Property(_get_output_port, help=\
        """
        Get a proxy object corresponding to the given output port of this
        algorithm.  The proxy object can be passed to another algorithm's
        set_input_connection(), add_input_connection(), and
        remove_input_connection() methods to modify pipeline connectivity.
        """
    )

    def get_output_port_information(self, *args):
        """
        V.get_output_port_information(int) -> Information
        C++: Information *GetOutputPortInformation(int port)
        Get the information object associated with an output port.  There
        is one output port per output from the algorithm.  Each output
        port tells executives what kind of upstream requests this
        algorithm can handle for that output.
        """
        ret = self._wrap_call(self._vtk_obj.GetOutputPortInformation, *args)
        return wrap_vtk(ret)

    def _get_total_number_of_input_connections(self):
        return self._vtk_obj.GetTotalNumberOfInputConnections()
    total_number_of_input_connections = traits.Property(_get_total_number_of_input_connections, help=\
        """
        Get the total number of inputs for this algorithm
        """
    )

    def _get_update_ghost_level(self):
        return self._vtk_obj.GetUpdateGhostLevel()
    update_ghost_level = traits.Property(_get_update_ghost_level, help=\
        """
        These functions return the update extent for output ports that
        use piece extents. Where port is not specified, it is assumed to
        be 0.
        """
    )

    def _get_update_number_of_pieces(self):
        return self._vtk_obj.GetUpdateNumberOfPieces()
    update_number_of_pieces = traits.Property(_get_update_number_of_pieces, help=\
        """
        These functions return the update extent for output ports that
        use piece extents. Where port is not specified, it is assumed to
        be 0.
        """
    )

    def _get_update_piece(self):
        return self._vtk_obj.GetUpdatePiece()
    update_piece = traits.Property(_get_update_piece, help=\
        """
        These functions return the update extent for output ports that
        use piece extents. Where port is not specified, it is assumed to
        be 0.
        """
    )

    def add_input_connection(self, *args):
        """
        V.add_input_connection(int, AlgorithmOutput)
        C++: virtual void AddInputConnection(int port,
            AlgorithmOutput *input)
        V.add_input_connection(AlgorithmOutput)
        C++: virtual void AddInputConnection(AlgorithmOutput *input)
        Add a connection to the given input port index.  See
        set_input_connection() for details on input connections.  This
        method is the complement to remove_input_connection() in that it
        adds only the connection specified without affecting other
        connections.  Typical usage is
        
        * filter_2->_add_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInputConnection, *my_args)
        return ret

    def add_input_data_object(self, *args):
        """
        V.add_input_data_object(int, DataObject)
        C++: virtual void AddInputDataObject(int port,
            DataObject *data)
        V.add_input_data_object(DataObject)
        C++: virtual void AddInputDataObject(DataObject *data)
        Add the data-object as an input to this given port. This will add
        a new input connection on the specified port without affecting
        any existing connections on the same input port.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddInputDataObject, *my_args)
        return ret

    def CAN_HANDLE_PIECE_REQUEST(self):
        """
        V.can__handle__piece__request() -> InformationIntegerKey
        C++: static InformationIntegerKey *CAN_HANDLE_PIECE_REQUEST()
        Key that tells the pipeline that a particular algorithm can or
        cannot handle piece request. If a filter cannot handle piece
        requests and is asked for a piece, the executive will flag an
        error. If a structured data source cannot handle piece requests
        but can produce sub-extents (CAN_PRODUCE_SUB_EXTENT), the
        executive will use an extent translator to split the extent into
        pieces. Otherwise, if a source cannot handle piece requests, the
        executive will ask for the whole data for piece 0 and not execute
        the source for other pieces.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.CAN_HANDLE_PIECE_REQUEST())
        return ret
        

    def CAN_PRODUCE_SUB_EXTENT(self):
        """
        V.can__produce__sub__extent() -> InformationIntegerKey
        C++: static InformationIntegerKey *CAN_PRODUCE_SUB_EXTENT()
        This key tells the executive that a particular output port is
        capable of producing an arbitrary subextent of the whole extent.
        Many image sources and readers fall into this category but some
        such as the legacy structured data readers cannot support this
        feature.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.CAN_PRODUCE_SUB_EXTENT())
        return ret
        

    def convert_total_input_to_port_connection(self, *args):
        """
        V.convert_total_input_to_port_connection(int, int, int)
        C++: void ConvertTotalInputToPortConnection(int ind, int &port,
            int &conn)
        Convenience routine to convert from a linear ordering of input
        connections to a port/connection pair.
        """
        ret = self._wrap_call(self._vtk_obj.ConvertTotalInputToPortConnection, *args)
        return ret

    def has_executive(self):
        """
        V.has_executive() -> int
        C++: int HasExecutive()
        Check whether this algorithm has an assigned executive.  This
        will NOT create a default executive.
        """
        ret = self._vtk_obj.HasExecutive()
        return ret
        

    def INPUT_ARRAYS_TO_PROCESS(self):
        """
        V.input__arrays__to__process() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *INPUT_ARRAYS_TO_PROCESS(
            )
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_ARRAYS_TO_PROCESS())
        return ret
        

    def INPUT_CONNECTION(self):
        """
        V.input__connection() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_CONNECTION()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_CONNECTION())
        return ret
        

    def INPUT_IS_OPTIONAL(self):
        """
        V.input__is__optional() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_IS_OPTIONAL()
        Keys used to specify input port requirements.\ingroup
        information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_IS_OPTIONAL())
        return ret
        

    def INPUT_IS_REPEATABLE(self):
        """
        V.input__is__repeatable() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_IS_REPEATABLE()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_IS_REPEATABLE())
        return ret
        

    def INPUT_PORT(self):
        """
        V.input__port() -> InformationIntegerKey
        C++: static InformationIntegerKey *INPUT_PORT()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_PORT())
        return ret
        

    def INPUT_REQUIRED_DATA_TYPE(self):
        """
        V.input__required__data__type() -> InformationStringVectorKey
        C++: static InformationStringVectorKey *INPUT_REQUIRED_DATA_TYPE(
            )
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_REQUIRED_DATA_TYPE())
        return ret
        

    def INPUT_REQUIRED_FIELDS(self):
        """
        V.input__required__fields() -> InformationInformationVectorKey
        C++: static InformationInformationVectorKey *INPUT_REQUIRED_FIELDS(
            )
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.INPUT_REQUIRED_FIELDS())
        return ret
        

    def modify_request(self, *args):
        """
        V.modify_request(Information, int) -> int
        C++: virtual int ModifyRequest(Information *request, int when)
        This method gives the algorithm a chance to modify the contents
        of a request before or after (specified in the when argument) it
        is forwarded. The default implementation is empty. Returns 1 on
        success, 0 on failure. When can be either
        Executive::BeforeForward or Executive::AfterForward.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ModifyRequest, *my_args)
        return ret

    def process_request(self, *args):
        """
        V.process_request(Information, Collection,
            InformationVector) -> int
        C++: int ProcessRequest(Information *request,
            Collection *inInfo, InformationVector *outInfo)
        Version of process_request() that is wrapped. This converts the
        collection to an array and calls the other version.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ProcessRequest, *my_args)
        return ret

    def propagate_update_extent(self):
        """
        V.propagate_update_extent()
        C++: virtual void PropagateUpdateExtent()
        Propagate meta-data upstream.
        """
        ret = self._vtk_obj.PropagateUpdateExtent()
        return ret
        

    def remove_all_input_connections(self, *args):
        """
        V.remove_all_input_connections(int)
        C++: virtual void RemoveAllInputConnections(int port)
        Removes all input connections.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveAllInputConnections, *args)
        return ret

    def remove_all_inputs(self):
        """
        V.remove_all_inputs()
        C++: void RemoveAllInputs()
        Remove all the input data.
        """
        old_val = self._get_input()
        ret = self._vtk_obj.RemoveAllInputs()
        self.trait_property_changed('input', old_val, self._get_input())
        return ret
        

    def remove_input_connection(self, *args):
        """
        V.remove_input_connection(int, AlgorithmOutput)
        C++: virtual void RemoveInputConnection(int port,
            AlgorithmOutput *input)
        V.remove_input_connection(int, int)
        C++: virtual void RemoveInputConnection(int port, int idx)
        Remove a connection from the given input port index.  See
        set_input_connection() for details on input connection.  This
        method is the complement to add_input_connection() in that it
        removes only the connection specified without affecting other
        connections.  Typical usage is
        
        * filter_2->_remove_input_connection(_0, filter_1->_get_output_port(_0)).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveInputConnection, *my_args)
        return ret

    def set_default_executive_prototype(self, *args):
        """
        V.set_default_executive_prototype(Executive)
        C++: static void SetDefaultExecutivePrototype(Executive *proto)
        If the default_executive_prototype is set, a copy of it is created
        in create_default_executive() using new_instance().
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDefaultExecutivePrototype, *my_args)
        return ret

    def set_input_array_to_process(self, *args):
        """
        V.set_input_array_to_process(int, int, int, int, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, const char *name)
        V.set_input_array_to_process(int, int, int, int, int)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, int fieldAssociation, int fieldAttributeType)
        V.set_input_array_to_process(int, Information)
        C++: virtual void SetInputArrayToProcess(int idx,
            Information *info)
        V.set_input_array_to_process(int, int, int, string, string)
        C++: virtual void SetInputArrayToProcess(int idx, int port,
            int connection, const char *fieldAssociation,
            const char *attributeTypeorName)
        Set the input data arrays that this algorithm will process.
        Specifically the idx array that this algorithm will process
        (starting from 0) is the array on port, connection with the
        specified association and name or attribute type (such as
        SCALARS). The field_association refers to which field in the data
        object the array is stored. See DataObject::FieldAssociations
        for detail.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputArrayToProcess, *my_args)
        return ret

    def set_update_extent_to_whole_extent(self, *args):
        """
        V.set_update_extent_to_whole_extent(int) -> int
        C++: int SetUpdateExtentToWholeExtent(int port)
        V.set_update_extent_to_whole_extent() -> int
        C++: int SetUpdateExtentToWholeExtent()
        If the whole output extent is required, this method can be called
        to set the output update extent to the whole extent. This method
        assumes that the whole extent is known (that update_information
        has been called).
        """
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtentToWholeExtent, *args)
        return ret

    def update(self, *args):
        """
        V.update(int)
        C++: virtual void Update(int port)
        V.update()
        C++: virtual void Update()
        V.update(int, InformationVector) -> int
        C++: virtual int Update(int port, InformationVector *requests)
        V.update(Information) -> int
        C++: virtual int Update(Information *requests)
        Bring this algorithm's outputs up-to-date.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Update, *my_args)
        return ret

    def update_data_object(self):
        """
        V.update_data_object()
        C++: virtual void UpdateDataObject()
        Create output object(s).
        """
        ret = self._vtk_obj.UpdateDataObject()
        return ret
        

    def update_extent(self, *args):
        """
        V.update_extent((int, int, int, int, int, int)) -> int
        C++: virtual int UpdateExtent(const int extents[6])
        Convenience method to update an algorithm after passing requests
        to its first output port. Supports extent request.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateExtent, *args)
        return ret

    def update_extent_is_empty(self, *args):
        """
        V.update_extent_is_empty(Information, DataObject) -> int
        C++: int UpdateExtentIsEmpty(Information *pinfo,
            DataObject *output)
        V.update_extent_is_empty(Information, int) -> int
        C++: int UpdateExtentIsEmpty(Information *pinfo,
            int extentType)
        This detects when the update_extent will generate no data This
        condition is satisfied when the update_extent has zero volume
        (0,-1,...) or the update_number_of_pieces is 0. The source uses this
        call to determine whether to call Execute.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateExtentIsEmpty, *my_args)
        return ret

    def update_information(self):
        """
        V.update_information()
        C++: virtual void UpdateInformation()
        Bring the algorithm's information up-to-date.
        """
        ret = self._vtk_obj.UpdateInformation()
        return ret
        

    def update_piece(self, *args):
        """
        V.update_piece(int, int, int, (int, int, int, int, int, int))
            -> int
        C++: virtual int UpdatePiece(int piece, int numPieces,
            int ghostLevels, const int extents[6]=0)
        Convenience method to update an algorithm after passing requests
        to its first output port. See documentation for Update(int port,
        InformationVector* requests) for details. Supports piece and
        extent (optional) requests.
        """
        ret = self._wrap_call(self._vtk_obj.UpdatePiece, *args)
        return ret

    def update_progress(self, *args):
        """
        V.update_progress(float)
        C++: void UpdateProgress(double amount)
        Update the progress of the process object. If a progress_method
        exists, executes it.  Then set the Progress ivar to amount. The
        parameter amount should range between (0,1).
        """
        ret = self._wrap_call(self._vtk_obj.UpdateProgress, *args)
        return ret

    def update_time_step(self, *args):
        """
        V.update_time_step(float, int, int, int, (int, int, int, int, int,
            int)) -> int
        C++: virtual int UpdateTimeStep(double time, int piece=-1,
            int numPieces=1, int ghostLevels=0, const int extents[6]=0)
        Convenience method to update an algorithm after passing requests
        to its first output port. See documentation for Update(int port,
        InformationVector* requests) for details. Supports time, piece
        (optional) and extent (optional) requests.
        """
        ret = self._wrap_call(self._vtk_obj.UpdateTimeStep, *args)
        return ret

    def update_whole_extent(self):
        """
        V.update_whole_extent()
        C++: virtual void UpdateWholeExtent()
        Bring this algorithm's outputs up-to-date.
        """
        ret = self._vtk_obj.UpdateWholeExtent()
        return ret
        

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
            return super(Algorithm, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Algorithm properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

