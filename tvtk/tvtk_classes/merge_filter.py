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

from tvtk.tvtk_classes.data_set_algorithm import DataSetAlgorithm


class MergeFilter(DataSetAlgorithm):
    """
    MergeFilter - extract separate components of data from different
    datasets
    
    Superclass: DataSetAlgorithm
    
    MergeFilter is a filter that extracts separate components of data
    from different datasets and merges them into a single dataset. The
    output from this filter is of the same type as the input (i.e.,
    DataSet.) It treats both cell and point data set attributes.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergeFilter, obj, update, **traits)
    
    def _get_geometry(self):
        return wrap_vtk(self._vtk_obj.GetGeometry())
    geometry = traits.Property(_get_geometry, help=\
        """
        Specify object from which to extract geometry information. Note
        that this method does not connect the pipeline. The algorithm
        will work on the input data as it is without updating the
        producer of the data. See set_geometry_connection for connecting
        the pipeline.
        """
    )

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def _get_normals(self):
        return wrap_vtk(self._vtk_obj.GetNormals())
    normals = traits.Property(_get_normals, help=\
        """
        Set / get the object from which to extract normal information.
        Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_normals_connection for connecting
        the pipeline.
        """
    )

    def _get_scalars(self):
        return wrap_vtk(self._vtk_obj.GetScalars())
    scalars = traits.Property(_get_scalars, help=\
        """
        Specify object from which to extract scalar information. Note
        that this method does not connect the pipeline. The algorithm
        will work on the input data as it is without updating the
        producer of the data. See set_scalar_connection for connecting the
        pipeline.
        """
    )

    def _get_t_coords(self):
        return wrap_vtk(self._vtk_obj.GetTCoords())
    t_coords = traits.Property(_get_t_coords, help=\
        """
        Set / get the object from which to extract texture coordinates
        information. Note that this method does not connect the pipeline.
        The algorithm will work on the input data as it is without
        updating the producer of the data. See set_t_coords_connection for
        connecting the pipeline.
        """
    )

    def _get_tensors(self):
        return wrap_vtk(self._vtk_obj.GetTensors())
    tensors = traits.Property(_get_tensors, help=\
        """
        Set / get the object from which to extract tensor data. Note that
        this method does not connect the pipeline. The algorithm will
        work on the input data as it is without updating the producer of
        the data. See set_tensors_connection for connecting the pipeline.
        """
    )

    def _get_vectors(self):
        return wrap_vtk(self._vtk_obj.GetVectors())
    vectors = traits.Property(_get_vectors, help=\
        """
        Set / get the object from which to extract vector information.
        Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_vectors_connection for connecting
        the pipeline.
        """
    )

    def add_field(self, *args):
        """
        V.add_field(string, DataSet)
        C++: void AddField(const char *name, DataSet *input)
        Set the object from which to extract a field and the name of the
        field. Note that this does not create pipeline connectivity.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddField, *my_args)
        return ret

    def set_geometry_connection(self, *args):
        """
        V.set_geometry_connection(AlgorithmOutput)
        C++: void SetGeometryConnection(AlgorithmOutput *algOutput)
        Specify object from which to extract geometry information.
        Equivalent to set_input_connection(_0, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGeometryConnection, *my_args)
        return ret

    def set_geometry_input_data(self, *args):
        """
        V.set_geometry_input_data(DataSet)
        C++: void SetGeometryInputData(DataSet *input)
        Specify object from which to extract geometry information. Note
        that this method does not connect the pipeline. The algorithm
        will work on the input data as it is without updating the
        producer of the data. See set_geometry_connection for connecting
        the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetGeometryInputData, *my_args)
        return ret

    def set_normals_connection(self, *args):
        """
        V.set_normals_connection(AlgorithmOutput)
        C++: void SetNormalsConnection(AlgorithmOutput *algOutput)
        Set  the connection from which to extract normal information.
        Equivalent to set_input_connection(_3, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetNormalsConnection, *my_args)
        return ret

    def set_normals_data(self, *args):
        """
        V.set_normals_data(DataSet)
        C++: void SetNormalsData(DataSet *)
        Set / get the object from which to extract normal information.
        Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_normals_connection for connecting
        the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetNormalsData, *my_args)
        return ret

    def set_scalars_connection(self, *args):
        """
        V.set_scalars_connection(AlgorithmOutput)
        C++: void SetScalarsConnection(AlgorithmOutput *algOutput)
        Specify object from which to extract scalar information.
        Equivalent to set_input_connection(_1, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetScalarsConnection, *my_args)
        return ret

    def set_scalars_data(self, *args):
        """
        V.set_scalars_data(DataSet)
        C++: void SetScalarsData(DataSet *)
        Specify object from which to extract scalar information. Note
        that this method does not connect the pipeline. The algorithm
        will work on the input data as it is without updating the
        producer of the data. See set_scalar_connection for connecting the
        pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetScalarsData, *my_args)
        return ret

    def set_t_coords_connection(self, *args):
        """
        V.set_t_coords_connection(AlgorithmOutput)
        C++: void SetTCoordsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract texture coordinates
        information. Equivalent to set_input_connection(_4, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTCoordsConnection, *my_args)
        return ret

    def set_t_coords_data(self, *args):
        """
        V.set_t_coords_data(DataSet)
        C++: void SetTCoordsData(DataSet *)
        Set / get the object from which to extract texture coordinates
        information. Note that this method does not connect the pipeline.
        The algorithm will work on the input data as it is without
        updating the producer of the data. See set_t_coords_connection for
        connecting the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTCoordsData, *my_args)
        return ret

    def set_tensors_connection(self, *args):
        """
        V.set_tensors_connection(AlgorithmOutput)
        C++: void SetTensorsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract tensor data. Equivalent
        to set_input_connection(_5, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTensorsConnection, *my_args)
        return ret

    def set_tensors_data(self, *args):
        """
        V.set_tensors_data(DataSet)
        C++: void SetTensorsData(DataSet *)
        Set / get the object from which to extract tensor data. Note that
        this method does not connect the pipeline. The algorithm will
        work on the input data as it is without updating the producer of
        the data. See set_tensors_connection for connecting the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTensorsData, *my_args)
        return ret

    def set_vectors_connection(self, *args):
        """
        V.set_vectors_connection(AlgorithmOutput)
        C++: void SetVectorsConnection(AlgorithmOutput *algOutput)
        Set the connection from which to extract vector information.
        Equivalent to set_input_connection(_2, alg_output)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVectorsConnection, *my_args)
        return ret

    def set_vectors_data(self, *args):
        """
        V.set_vectors_data(DataSet)
        C++: void SetVectorsData(DataSet *)
        Set / get the object from which to extract vector information.
        Note that this method does not connect the pipeline. The
        algorithm will work on the input data as it is without updating
        the producer of the data. See set_vectors_connection for connecting
        the pipeline.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetVectorsData, *my_args)
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
            return super(MergeFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergeFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

