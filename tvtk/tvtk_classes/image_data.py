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

from tvtk.tvtk_classes.data_set import DataSet


class ImageData(DataSet):
    """
    ImageData - topologically and geometrically regular array of data
    
    Superclass: DataSet
    
    ImageData is a data object that is a concrete implementation of
    DataSet. ImageData represents a geometric structure that is a
    topological and geometrical regular array of points. Examples include
    volumes (voxel data) and pixmaps.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageData, obj, update, **traits)
    
    def get_axis_update_extent(self, *args):
        """
        V.get_axis_update_extent(int, int, int, (int, ...))
        C++: virtual void GetAxisUpdateExtent(int axis, int &min,
            int &max, const int *updateExtent)
        Set / Get the extent on just one axis
        """
        ret = self._wrap_call(self._vtk_obj.GetAxisUpdateExtent, *args)
        return ret

    def set_axis_update_extent(self, *args):
        """
        V.set_axis_update_extent(int, int, int, (int, ...), [int, ...])
        C++: virtual void SetAxisUpdateExtent(int axis, int min, int max,
            const int *updateExtent, int *axisUpdateExtent)
        Set / Get the extent on just one axis
        """
        ret = self._wrap_call(self._vtk_obj.SetAxisUpdateExtent, *args)
        return ret

    dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        Same as set_extent(_0, i-1, 0, j-1, 0, k-1)
        """
    )

    def _dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensions,
                        self.dimensions)

    extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        Set/Get the extent. On each axis, the extent is defined by the
        index of the first point and the index of the last point.  The
        extent should be set before the "Scalars" are set or allocated. 
        The Extent is stored in the order (X, Y, Z). The dataset extent
        does not have to start at (0,0,0). (0,0,0) is just the extent of
        the origin. The first point (the one with Id=0) is at extent
        (Extent[0],Extent[2],Extent[4]). As for any dataset, a data array
        on point data starts at Id=0.
        """
    )

    def _extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtent,
                        self.extent)

    number_of_scalar_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of scalar components for points. As with the
        set_scalar_type method this is setting pipeline info.
        """
    )

    def _number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfScalarComponents,
                        self.number_of_scalar_components)

    origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacing,
                        self.spacing)

    def get_array_increments(self, *args):
        """
        V.get_array_increments(DataArray, [int, int, int])
        C++: void GetArrayIncrements(DataArray *array,
            IdType increments[3])
        Since various arrays have different number of components, the
        will have different increments.
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayIncrements, *my_args)
        return ret

    def get_array_pointer(self, *args):
        """
        V.get_array_pointer(DataArray, [int, int, int]) -> void
        C++: void *GetArrayPointer(DataArray *array,
            int coordinates[3])
        These are convenience methods for getting a pointer from any
        filed array.  It is a start at expanding image filters to process
        any array (not just scalars).
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayPointer, *my_args)
        return ret

    def get_array_pointer_for_extent(self, *args):
        """
        V.get_array_pointer_for_extent(DataArray, [int, int, int, int, int,
             int]) -> void
        C++: void *GetArrayPointerForExtent(DataArray *array,
            int extent[6])
        These are convenience methods for getting a pointer from any
        filed array.  It is a start at expanding image filters to process
        any array (not just scalars).
        """
        my_args = deref_array(args, [('vtkDataArray', ['int', 'int', 'int', 'int', 'int', 'int'])])
        ret = self._wrap_call(self._vtk_obj.GetArrayPointerForExtent, *my_args)
        return ret

    def get_continuous_increments(self, *args):
        """
        V.get_continuous_increments([int, int, int, int, int, int], int,
            int, int)
        C++: virtual void GetContinuousIncrements(int extent[6],
            IdType &incX, IdType &incY, IdType &incZ)
        V.get_continuous_increments(DataArray, [int, int, int, int, int,
            int], int, int, int)
        C++: virtual void GetContinuousIncrements(DataArray *scalars,
            int extent[6], IdType &incX, IdType &incY,
            IdType &incZ)
        Different ways to get the increments for moving around the data.
        inc_x is always returned with 0.  inc_y is returned with the
        increment needed to move from the end of one X scanline of data
        to the start of the next line.  inc_z is filled in with the
        increment needed to move from the end of one image to the start
        of the next.  The proper way to use these values is to for a loop
        over Z, Y, X, C, incrementing the pointer by 1 after each
        component.  When the end of the component is reached, the pointer
        is set to the beginning of the next pixel, thus inc_x is properly
        set to 0. The first form of get_continuous_increments uses the
        active scalar field while the second form allows the scalar array
        to be passed in.
        """
        my_args = deref_array(args, [(['int', 'int', 'int', 'int', 'int', 'int'], 'int', 'int', 'int'), ('vtkDataArray', ['int', 'int', 'int', 'int', 'int', 'int'], 'int', 'int', 'int')])
        ret = self._wrap_call(self._vtk_obj.GetContinuousIncrements, *my_args)
        return ret

    def _get_data_dimension(self):
        return self._vtk_obj.GetDataDimension()
    data_dimension = traits.Property(_get_data_dimension, help=\
        """
        Return the dimensionality of the data.
        """
    )

    def _get_increments(self):
        return self._vtk_obj.GetIncrements()
    increments = traits.Property(_get_increments, help=\
        """
        Different ways to get the increments for moving around the data.
        get_increments() calls compute_increments() to ensure the
        increments are up to date.  The first three methods compute the
        increments based on the active scalar field while the next three,
        the scalar field is passed in.
        """
    )

    def get_point_gradient(self, *args):
        """
        V.get_point_gradient(int, int, int, DataArray, [float, float,
            float])
        C++: virtual void GetPointGradient(int i, int j, int k,
            DataArray *s, double g[3])
        Given structured coordinates (i,j,k) for a point in a structured
        point dataset, compute the gradient vector from the scalar data
        at that point. The scalars s are the scalars from which the
        gradient is to be computed. This method will treat structured
        point datasets of any dimension.
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'vtkDataArray', ['float', 'float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.GetPointGradient, *my_args)
        return ret

    def get_scalar_component_as_double(self, *args):
        """
        V.get_scalar_component_as_double(int, int, int, int) -> float
        C++: virtual double GetScalarComponentAsDouble(int x, int y,
            int z, int component)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentAsDouble, *args)
        return ret

    def get_scalar_component_as_float(self, *args):
        """
        V.get_scalar_component_as_float(int, int, int, int) -> float
        C++: virtual float GetScalarComponentAsFloat(int x, int y, int z,
            int component)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarComponentAsFloat, *args)
        return ret

    def _get_scalar_pointer(self):
        return self._vtk_obj.GetScalarPointer()
    scalar_pointer = traits.Property(_get_scalar_pointer, help=\
        """
        Access the native pointer for the scalar data
        """
    )

    def get_scalar_pointer_for_extent(self, *args):
        """
        V.get_scalar_pointer_for_extent([int, int, int, int, int, int])
            -> void
        C++: virtual void *GetScalarPointerForExtent(int extent[6])
        Access the native pointer for the scalar data
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarPointerForExtent, *args)
        return ret

    def _get_scalar_size(self):
        return self._vtk_obj.GetScalarSize()
    scalar_size = traits.Property(_get_scalar_size, help=\
        """
        Get the size of the scalar type in bytes.
        """
    )

    def _get_scalar_type_as_string(self):
        return self._vtk_obj.GetScalarTypeAsString()
    scalar_type_as_string = traits.Property(_get_scalar_type_as_string, help=\
        """
        
        """
    )

    def _get_scalar_type_max(self):
        return self._vtk_obj.GetScalarTypeMax()
    scalar_type_max = traits.Property(_get_scalar_type_max, help=\
        """
        These returns the minimum and maximum values the scalar_type can
        hold without overflowing.
        """
    )

    def _get_scalar_type_min(self):
        return self._vtk_obj.GetScalarTypeMin()
    scalar_type_min = traits.Property(_get_scalar_type_min, help=\
        """
        These returns the minimum and maximum values the scalar_type can
        hold without overflowing.
        """
    )

    def get_voxel_gradient(self, *args):
        """
        V.get_voxel_gradient(int, int, int, DataArray, DataArray)
        C++: virtual void GetVoxelGradient(int i, int j, int k,
            DataArray *s, DataArray *g)
        Given structured coordinates (i,j,k) for a voxel cell, compute
        the eight gradient values for the voxel corners. The order in
        which the gradient vectors are arranged corresponds to the
        ordering of the voxel points. Gradient vector is computed by
        central differences (except on edges of volume where forward
        difference is used). The scalars s are the scalars from which the
        gradient is to be computed. This method will treat only 3d
        structured point datasets (i.e., volumes).
        """
        my_args = deref_array(args, [('int', 'int', 'int', 'vtkDataArray', 'vtkDataArray')])
        ret = self._wrap_call(self._vtk_obj.GetVoxelGradient, *my_args)
        return ret

    def allocate_scalars(self, *args):
        """
        V.allocate_scalars(int, int)
        C++: virtual void AllocateScalars(int dataType, int numComponents)
        V.allocate_scalars(Information)
        C++: virtual void AllocateScalars(Information *pipeline_info)
        Allocate the point scalars for this dataset. The data type
        determines the type of the array (VTK_FLOAT, VTK_INT etc.) where
        as num_components determines its number of components.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AllocateScalars, *my_args)
        return ret

    def compute_cell_id(self, *args):
        """
        V.compute_cell_id([int, int, int]) -> int
        C++: virtual IdType ComputeCellId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        cell id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeCellId, *args)
        return ret

    def compute_internal_extent(self, *args):
        """
        V.compute_internal_extent([int, ...], [int, ...], [int, ...])
        C++: void ComputeInternalExtent(int *intExt, int *tgtExt,
            int *bnds)
        Given how many pixel are required on a side for bounrary
        conditions (in bnds), the target extent to traverse, compute the
        internal extent (the extent for this image_data that does not
        suffer from any boundary conditions) and place it in int_ext
        """
        ret = self._wrap_call(self._vtk_obj.ComputeInternalExtent, *args)
        return ret

    def compute_point_id(self, *args):
        """
        V.compute_point_id([int, int, int]) -> int
        C++: virtual IdType ComputePointId(int ijk[3])
        Given a location in structured coordinates (i-j-k), return the
        point id.
        """
        ret = self._wrap_call(self._vtk_obj.ComputePointId, *args)
        return ret

    def compute_structured_coordinates(self, *args):
        """
        V.compute_structured_coordinates((float, float, float), [int, int,
            int], [float, float, float]) -> int
        C++: virtual int ComputeStructuredCoordinates(const double x[3],
            int ijk[3], double pcoords[3])
        V.compute_structured_coordinates((float, float, float), [int, int,
            int], [float, float, float], (int, ...), (float, ...), (float,
             ...), (float, ...)) -> int
        C++: static int ComputeStructuredCoordinates(const double x[3],
            int ijk[3], double pcoords[3], const int *extent,
            const double *spacing, const double *origin,
            const double *bounds)
        Convenience function computes the structured coordinates for a
        point x[3]. The voxel is specified by the array ijk[3], and the
        parametric coordinates in the cell are specified with pcoords[3].
        The function returns a 0 if the point x is outside of the volume,
        and a 1 if inside the volume.
        """
        ret = self._wrap_call(self._vtk_obj.ComputeStructuredCoordinates, *args)
        return ret

    def copy_and_cast_from(self, *args):
        """
        V.copy_and_cast_from(ImageData, [int, int, int, int, int, int])
        C++: virtual void CopyAndCastFrom(ImageData *inData,
            int extent[6])
        V.copy_and_cast_from(ImageData, int, int, int, int, int, int)
        C++: virtual void CopyAndCastFrom(ImageData *inData, int x0,
            int x1, int y0, int y1, int z0, int z1)
        This method is passed a input and output region, and executes the
        filter algorithm to fill the output from the input. It just
        executes a switch statement to call the correct function for the
        regions data types.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyAndCastFrom, *my_args)
        return ret

    def has_number_of_scalar_components(self, *args):
        """
        V.has_number_of_scalar_components(Information) -> bool
        C++: static bool HasNumberOfScalarComponents(
            Information *meta_data)
        Set/Get the number of scalar components for points. As with the
        set_scalar_type method this is setting pipeline info.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasNumberOfScalarComponents, *my_args)
        return ret

    def has_scalar_type(self, *args):
        """
        V.has_scalar_type(Information) -> bool
        C++: static bool HasScalarType(Information *meta_data)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.HasScalarType, *my_args)
        return ret

    def set_scalar_component_from_double(self, *args):
        """
        V.set_scalar_component_from_double(int, int, int, int, float)
        C++: virtual void SetScalarComponentFromDouble(int x, int y,
            int z, int component, double v)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarComponentFromDouble, *args)
        return ret

    def set_scalar_component_from_float(self, *args):
        """
        V.set_scalar_component_from_float(int, int, int, int, float)
        C++: virtual void SetScalarComponentFromFloat(int x, int y, int z,
             int component, float v)
        For access to data from tcl
        """
        ret = self._wrap_call(self._vtk_obj.SetScalarComponentFromFloat, *args)
        return ret

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('dimensions', 'GetDimensions'), ('extent', 'GetExtent'),
    ('number_of_scalar_components', 'GetNumberOfScalarComponents'),
    ('origin', 'GetOrigin'), ('spacing', 'GetSpacing'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'dimensions', 'extent', 'number_of_scalar_components', 'origin',
    'spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['dimensions', 'extent',
            'number_of_scalar_components', 'origin', 'spacing']),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

