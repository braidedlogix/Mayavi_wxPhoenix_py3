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

from tvtk.tvtk_classes.demand_driven_pipeline import DemandDrivenPipeline


class StreamingDemandDrivenPipeline(DemandDrivenPipeline):
    """
    StreamingDemandDrivenPipeline - Executive supporting partial
    updates.
    
    Superclass: DemandDrivenPipeline
    
    StreamingDemandDrivenPipeline is an executive that supports
    updating only a portion of the data set in the pipeline.  This is the
    style of pipeline update that is provided by the old-style VTK 4.x
    pipeline.  Instead of always updating an entire data set, this
    executive supports asking for pieces or sub-extents.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkStreamingDemandDrivenPipeline, obj, update, **traits)
    
    def get_request_exact_extent(self, *args):
        """
        V.get_request_exact_extent(int) -> int
        C++: int GetRequestExactExtent(int port)
        This request flag indicates whether the requester can handle more
        data than requested for the given port.  Right now it is used in
        ImageData.  Image filters can return more data than requested.
        The the consumer cannot handle this (i.e. data_set_to_data_set_fitler)
        the image will crop itself.  This functionality used to be in
        image_to_structured_points.
        """
        ret = self._wrap_call(self._vtk_obj.GetRequestExactExtent, *args)
        return ret

    def set_request_exact_extent(self, *args):
        """
        V.set_request_exact_extent(int, int) -> int
        C++: int SetRequestExactExtent(int port, int flag)
        This request flag indicates whether the requester can handle more
        data than requested for the given port.  Right now it is used in
        ImageData.  Image filters can return more data than requested.
        The the consumer cannot handle this (i.e. data_set_to_data_set_fitler)
        the image will crop itself.  This functionality used to be in
        image_to_structured_points.
        """
        ret = self._wrap_call(self._vtk_obj.SetRequestExactExtent, *args)
        return ret

    def get_update_extent(self, *args):
        """
        V.get_update_extent(Information, [int, int, int, int, int, int])
        C++: static void GetUpdateExtent(Information *, int extent[6])
        V.get_update_extent(Information) -> (int, ...)
        C++: static int *GetUpdateExtent(Information *)
        Get/Set the update extent for output ports that use 3d extents.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateExtent, *my_args)
        return ret

    def set_update_extent(self, *args):
        """
        V.set_update_extent(int, [int, int, int, int, int, int]) -> int
        C++: int SetUpdateExtent(int port, int extent[6])
        V.set_update_extent(int, int, int, int, int, int, int) -> int
        C++: int SetUpdateExtent(int port, int x0, int x1, int y0, int y1,
             int z0, int z1)
        V.set_update_extent(Information, [int, int, int, int, int, int])
            -> int
        C++: static int SetUpdateExtent(Information *, int extent[6])
        V.set_update_extent(int, int, int, int) -> int
        C++: int SetUpdateExtent(int port, int piece, int numPieces,
            int ghostLevel)
        V.set_update_extent(Information, int, int, int) -> int
        C++: static int SetUpdateExtent(Information *, int piece,
            int numPieces, int ghostLevel)
        Get/Set the update extent for output ports that use 3d extents.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtent, *my_args)
        return ret

    def get_update_ghost_level(self, *args):
        """
        V.get_update_ghost_level(Information) -> int
        C++: static int GetUpdateGhostLevel(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateGhostLevel, *my_args)
        return ret

    def set_update_ghost_level(self, *args):
        """
        V.set_update_ghost_level(Information, int) -> int
        C++: static int SetUpdateGhostLevel(Information *, int n)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateGhostLevel, *my_args)
        return ret

    def get_update_number_of_pieces(self, *args):
        """
        V.get_update_number_of_pieces(Information) -> int
        C++: static int GetUpdateNumberOfPieces(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdateNumberOfPieces, *my_args)
        return ret

    def set_update_number_of_pieces(self, *args):
        """
        V.set_update_number_of_pieces(Information, int) -> int
        C++: static int SetUpdateNumberOfPieces(Information *, int n)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateNumberOfPieces, *my_args)
        return ret

    def get_update_piece(self, *args):
        """
        V.get_update_piece(Information) -> int
        C++: static int GetUpdatePiece(Information *)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetUpdatePiece, *my_args)
        return ret

    def set_update_piece(self, *args):
        """
        V.set_update_piece(Information, int) -> int
        C++: static int SetUpdatePiece(Information *, int piece)
        Set/Get the update piece, update number of pieces, and update
        number of ghost levels for an output port.  Similar to update
        extent in 3d.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdatePiece, *my_args)
        return ret

    def get_whole_extent(self, *args):
        """
        V.get_whole_extent(Information, [int, int, int, int, int, int])
        C++: static void GetWholeExtent(Information *, int extent[6])
        V.get_whole_extent(Information) -> (int, int, int, int, int, int)
        C++: static int *GetWholeExtent(Information *)
        Set/Get the whole extent of an output port.  The whole extent is
        meta data for structured data sets.  It gets set by the algorithm
        during the update information pass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetWholeExtent, *my_args)
        return ret

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(Information, [int, int, int, int, int, int])
            -> int
        C++: static int SetWholeExtent(Information *, int extent[6])
        Set/Get the whole extent of an output port.  The whole extent is
        meta data for structured data sets.  It gets set by the algorithm
        during the update information pass.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *my_args)
        return ret

    def BOUNDS(self):
        """
        V.bounds() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *BOUNDS()
        key to record the bounds of a dataset.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.BOUNDS())
        return ret
        

    def COMBINED_UPDATE_EXTENT(self):
        """
        V.combined__update__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *COMBINED_UPDATE_EXTENT(
            )
        Key for combining the update extents requested by all consumers,
        so that the final extent that is produced satisfies all
        consumers.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.COMBINED_UPDATE_EXTENT())
        return ret
        

    def CONTINUE_EXECUTING(self):
        """
        V.continue__executing() -> InformationIntegerKey
        C++: static InformationIntegerKey *CONTINUE_EXECUTING()
        Key for an algorithm to store in a request to tell this executive
        to keep executing it.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.CONTINUE_EXECUTING())
        return ret
        

    def EXACT_EXTENT(self):
        """
        V.exact__extent() -> InformationIntegerKey
        C++: static InformationIntegerKey *EXACT_EXTENT()
        Key to specify the request for exact extent in pipeline
        information.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.EXACT_EXTENT())
        return ret
        

    def propagate_time(self, *args):
        """
        V.propagate_time(int) -> int
        C++: int PropagateTime(int outputPort)
        Propagate time through the pipeline. this is a special pass only
        necessary if there is temporal meta data that must be updated
        """
        ret = self._wrap_call(self._vtk_obj.PropagateTime, *args)
        return ret

    def propagate_update_extent(self, *args):
        """
        V.propagate_update_extent(int) -> int
        C++: int PropagateUpdateExtent(int outputPort)
        Propagate the update request from the given output port back
        through the pipeline.  Should be called only when information is
        up to date.
        """
        ret = self._wrap_call(self._vtk_obj.PropagateUpdateExtent, *args)
        return ret

    def REQUEST_TIME_DEPENDENT_INFORMATION(self):
        """
        V.request__time__dependent__information() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_TIME_DEPENDENT_INFORMATION(
            )
        Key defining a request to make sure the meta information is up to
        date.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_TIME_DEPENDENT_INFORMATION())
        return ret
        

    def REQUEST_UPDATE_EXTENT(self):
        """
        V.request__update__extent() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_UPDATE_EXTENT()
        Key defining a request to propagate the update extent
        upstream.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_UPDATE_EXTENT())
        return ret
        

    def REQUEST_UPDATE_TIME(self):
        """
        V.request__update__time() -> InformationRequestKey
        C++: static InformationRequestKey *REQUEST_UPDATE_TIME()
        Key defining a request to propagate the update extent
        upstream.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.REQUEST_UPDATE_TIME())
        return ret
        

    def set_update_extent_to_whole_extent(self, *args):
        """
        V.set_update_extent_to_whole_extent(int) -> int
        C++: int SetUpdateExtentToWholeExtent(int port)
        V.set_update_extent_to_whole_extent(Information) -> int
        C++: static int SetUpdateExtentToWholeExtent(Information *)
        If the whole input extent is required to generate the requested
        output extent, this method can be called to set the input update
        extent to the whole input extent. This method assumes that the
        whole extent is known (that update_information has been called)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateExtentToWholeExtent, *my_args)
        return ret

    def set_update_time_step(self, *args):
        """
        V.set_update_time_step(int, float) -> int
        C++: int SetUpdateTimeStep(int port, double time)
        V.set_update_time_step(Information, float) -> int
        C++: static int SetUpdateTimeStep(Information *, double time)
        Get/Set the update extent for output ports that use Temporal
        Extents
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetUpdateTimeStep, *my_args)
        return ret

    def TIME_DEPENDENT_INFORMATION(self):
        """
        V.time__dependent__information() -> InformationIntegerKey
        C++: static InformationIntegerKey *TIME_DEPENDENT_INFORMATION()
        Whether there are time dependent meta information if there is,
        the pipeline will perform two extra passes to gather the time
        dependent information\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.TIME_DEPENDENT_INFORMATION())
        return ret
        

    def TIME_RANGE(self):
        """
        V.time__range() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *TIME_RANGE()
        Key to store available time range for continuous sources.\ingroup
        information_keys
        """
        ret = wrap_vtk(self._vtk_obj.TIME_RANGE())
        return ret
        

    def TIME_STEPS(self):
        """
        V.time__steps() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *TIME_STEPS()
        Key to store available time steps.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.TIME_STEPS())
        return ret
        

    def UNRESTRICTED_UPDATE_EXTENT(self):
        """
        V.unrestricted__update__extent() -> InformationIntegerKey
        C++: static InformationIntegerKey *UNRESTRICTED_UPDATE_EXTENT()
        This is set if the update extent is not restricted to the whole
        extent, for sources that can generate an extent of any requested
        size.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UNRESTRICTED_UPDATE_EXTENT())
        return ret
        

    def UPDATE_EXTENT(self):
        """
        V.update__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *UPDATE_EXTENT()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_EXTENT())
        return ret
        

    def UPDATE_EXTENT_INITIALIZED(self):
        """
        V.update__extent__initialized() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_EXTENT_INITIALIZED()
        Keys to store an update request in pipeline information.\ingroup
        information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_EXTENT_INITIALIZED())
        return ret
        

    def UPDATE_NUMBER_OF_GHOST_LEVELS(self):
        """
        V.update__number__of__ghost__levels() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_NUMBER_OF_GHOST_LEVELS(
            )
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_NUMBER_OF_GHOST_LEVELS())
        return ret
        

    def UPDATE_NUMBER_OF_PIECES(self):
        """
        V.update__number__of__pieces() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_NUMBER_OF_PIECES()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_NUMBER_OF_PIECES())
        return ret
        

    def UPDATE_PIECE_NUMBER(self):
        """
        V.update__piece__number() -> InformationIntegerKey
        C++: static InformationIntegerKey *UPDATE_PIECE_NUMBER()
        \ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_PIECE_NUMBER())
        return ret
        

    def UPDATE_TIME_STEP(self):
        """
        V.update__time__step() -> InformationDoubleKey
        C++: static InformationDoubleKey *UPDATE_TIME_STEP()
        Update time steps requested by the pipeline.\ingroup
        information_keys
        """
        ret = wrap_vtk(self._vtk_obj.UPDATE_TIME_STEP())
        return ret
        

    def update_time_dependent_information(self, *args):
        """
        V.update_time_dependent_information(int) -> int
        C++: int UpdateTimeDependentInformation(int outputPort)
        Propagate time through the pipeline. this is a special pass only
        necessary if there is temporal meta data that must be updated
        """
        ret = self._wrap_call(self._vtk_obj.UpdateTimeDependentInformation, *args)
        return ret

    def update_whole_extent(self):
        """
        V.update_whole_extent() -> int
        C++: virtual int UpdateWholeExtent()
        Bring the outputs up-to-date.
        """
        ret = self._vtk_obj.UpdateWholeExtent()
        return ret
        

    def WHOLE_EXTENT(self):
        """
        V.whole__extent() -> InformationIntegerVectorKey
        C++: static InformationIntegerVectorKey *WHOLE_EXTENT()
        Key to store the whole extent provided in pipeline
        information.\ingroup information_keys
        """
        ret = wrap_vtk(self._vtk_obj.WHOLE_EXTENT())
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
            return super(StreamingDemandDrivenPipeline, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit StreamingDemandDrivenPipeline properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

