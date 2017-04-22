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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ImageDataGeometryFilter(PolyDataAlgorithm):
    """
    ImageDataGeometryFilter - extract geometry for structured points
    
    Superclass: PolyDataAlgorithm
    
    ImageDataGeometryFilter is a filter that extracts geometry from a
    structured points dataset. By specifying appropriate i-j-k indices
    (via the "Extent" instance variable), it is possible to extract a
    point, a line, a plane (i.e., image), or a "volume" from dataset.
    (Since the output is of type polydata, the volume is actually a (n x
    m x o) region of points.)
    
    The extent specification is zero-offset. That is, the first k-plane
    in a 50x50x50 volume is given by (0,49, 0,49, 0,0).
    @warning
    If you don't know the dimensions of the input dataset, you can use a
    large number to specify extent (the number will be clamped
    appropriately). For example, if the dataset dimensions are 50x50x50,
    and you want a the fifth k-plane, you can use the extents (0,100,
    0,100, 4,4). The 100 will automatically be clamped to 49.
    
    @sa
    GeometryFilter StructuredGridSource
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDataGeometryFilter, obj, update, **traits)
    
    output_triangles = tvtk_base.false_bool_trait(help=\
        """
        Set output_triangles to true if you wish to generate triangles
        instead of quads when extracting cells from 2d imagedata
        Currently this functionality is only implemented for 2d imagedata
        """
    )

    def _output_triangles_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputTriangles,
                        self.output_triangles_)

    threshold_cells = tvtk_base.false_bool_trait(help=\
        """
        Set threshold_cells to true if you wish to skip any voxel/pixels
        which have scalar values less than the specified threshold.
        Currently this functionality is only implemented for 2d imagedata
        """
    )

    def _threshold_cells_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThresholdCells,
                        self.threshold_cells_)

    threshold_value = tvtk_base.false_bool_trait(help=\
        """
        Set threshold_value to the scalar value by which to threshold
        cells when extracting geometry when threshold_cells is true. Cells
        with scalar values greater than the threshold will be output.
        """
    )

    def _threshold_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThresholdValue,
                        self.threshold_value_)

    def _get_extent(self):
        return self._vtk_obj.GetExtent()
    extent = traits.Property(_get_extent, help=\
        """
        Set / get the extent (imin,imax, jmin,jmax, kmin,kmax) indices.
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def set_extent(self, *args):
        """
        V.set_extent([int, int, int, int, int, int])
        C++: void SetExtent(int extent[6])
        V.set_extent(int, int, int, int, int, int)
        C++: void SetExtent(int iMin, int iMax, int jMin, int jMax,
            int kMin, int kMax)
        Set / get the extent (imin,imax, jmin,jmax, kmin,kmax) indices.
        """
        ret = self._wrap_call(self._vtk_obj.SetExtent, *args)
        return ret

    _updateable_traits_ = \
    (('output_triangles', 'GetOutputTriangles'), ('threshold_cells',
    'GetThresholdCells'), ('threshold_value', 'GetThresholdValue'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'output_triangles', 'release_data_flag', 'threshold_cells',
    'threshold_value', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDataGeometryFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['output_triangles', 'threshold_cells', 'threshold_value'], [],
            []),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDataGeometryFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

