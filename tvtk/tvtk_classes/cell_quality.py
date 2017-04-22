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


class CellQuality(DataSetAlgorithm):
    """
    CellQuality - Calculate functions of quality of the elements
     of a mesh
    
    Superclass: DataSetAlgorithm
    
    CellQuality computes one or more functions of (geometric) quality
    for each cell of a mesh.  The per-cell quality is added to the mesh's
    cell data, in an array named "_cell_quality." Cell types not supported
    by this filter or undefined quality of supported cell types will have
    an entry of -1.
    
    @warning
    Most quadrilateral quality functions are intended for planar
    quadrilaterals only.  The minimal angle is not, strictly speaking, a
    quality function, but it is provided because of its usage by many
    authors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCellQuality, obj, update, **traits)
    
    def get_quality_measure(self):
        """
        V.get_quality_measure() -> int
        C++: int GetQualityMeasure()
        Set/Get the particular estimator used to function the quality of
        all supported geometries. For qualities that are not defined for
        certain geometries, later program logic ensures that
        cell_quality_none static function will be used so that a predefined
        value is returned for the request. There is no default value for
        this call and valid values include all possible qualities
        supported by this class.
        """
        ret = self._vtk_obj.GetQualityMeasure()
        return ret
        

    def set_quality_measure_to_aspect_beta(self):
        """
        V.set_quality_measure_to_aspect_beta()
        C++: void SetQualityMeasureToAspectBeta()"""
        self._vtk_obj.SetQualityMeasureToAspectBeta()

    def set_quality_measure_to_aspect_frobenius(self):
        """
        V.set_quality_measure_to_aspect_frobenius()
        C++: void SetQualityMeasureToAspectFrobenius()"""
        self._vtk_obj.SetQualityMeasureToAspectFrobenius()

    def set_quality_measure_to_aspect_gamma(self):
        """
        V.set_quality_measure_to_aspect_gamma()
        C++: void SetQualityMeasureToAspectGamma()"""
        self._vtk_obj.SetQualityMeasureToAspectGamma()

    def set_quality_measure_to_aspect_ratio(self):
        """
        V.set_quality_measure_to_aspect_ratio()
        C++: void SetQualityMeasureToAspectRatio()"""
        self._vtk_obj.SetQualityMeasureToAspectRatio()

    def set_quality_measure_to_collapse_ratio(self):
        """
        V.set_quality_measure_to_collapse_ratio()
        C++: void SetQualityMeasureToCollapseRatio()"""
        self._vtk_obj.SetQualityMeasureToCollapseRatio()

    def set_quality_measure_to_condition(self):
        """
        V.set_quality_measure_to_condition()
        C++: void SetQualityMeasureToCondition()"""
        self._vtk_obj.SetQualityMeasureToCondition()

    def set_quality_measure_to_diagonal(self):
        """
        V.set_quality_measure_to_diagonal()
        C++: void SetQualityMeasureToDiagonal()"""
        self._vtk_obj.SetQualityMeasureToDiagonal()

    def set_quality_measure_to_dimension(self):
        """
        V.set_quality_measure_to_dimension()
        C++: void SetQualityMeasureToDimension()"""
        self._vtk_obj.SetQualityMeasureToDimension()

    def set_quality_measure_to_distortion(self):
        """
        V.set_quality_measure_to_distortion()
        C++: void SetQualityMeasureToDistortion()"""
        self._vtk_obj.SetQualityMeasureToDistortion()

    def set_quality_measure_to_jacobian(self):
        """
        V.set_quality_measure_to_jacobian()
        C++: void SetQualityMeasureToJacobian()"""
        self._vtk_obj.SetQualityMeasureToJacobian()

    def set_quality_measure_to_max_angle(self):
        """
        V.set_quality_measure_to_max_angle()
        C++: void SetQualityMeasureToMaxAngle()"""
        self._vtk_obj.SetQualityMeasureToMaxAngle()

    def set_quality_measure_to_max_aspect_frobenius(self):
        """
        V.set_quality_measure_to_max_aspect_frobenius()
        C++: void SetQualityMeasureToMaxAspectFrobenius()"""
        self._vtk_obj.SetQualityMeasureToMaxAspectFrobenius()

    def set_quality_measure_to_max_edge_ratio(self):
        """
        V.set_quality_measure_to_max_edge_ratio()
        C++: void SetQualityMeasureToMaxEdgeRatio()"""
        self._vtk_obj.SetQualityMeasureToMaxEdgeRatio()

    def set_quality_measure_to_med_aspect_frobenius(self):
        """
        V.set_quality_measure_to_med_aspect_frobenius()
        C++: void SetQualityMeasureToMedAspectFrobenius()"""
        self._vtk_obj.SetQualityMeasureToMedAspectFrobenius()

    def set_quality_measure_to_min_angle(self):
        """
        V.set_quality_measure_to_min_angle()
        C++: void SetQualityMeasureToMinAngle()"""
        self._vtk_obj.SetQualityMeasureToMinAngle()

    def set_quality_measure_to_oddy(self):
        """
        V.set_quality_measure_to_oddy()
        C++: void SetQualityMeasureToOddy()"""
        self._vtk_obj.SetQualityMeasureToOddy()

    def set_quality_measure_to_radius_ratio(self):
        """
        V.set_quality_measure_to_radius_ratio()
        C++: void SetQualityMeasureToRadiusRatio()"""
        self._vtk_obj.SetQualityMeasureToRadiusRatio()

    def set_quality_measure_to_relative_size_squared(self):
        """
        V.set_quality_measure_to_relative_size_squared()
        C++: void SetQualityMeasureToRelativeSizeSquared()"""
        self._vtk_obj.SetQualityMeasureToRelativeSizeSquared()

    def set_quality_measure_to_scaled_jacobian(self):
        """
        V.set_quality_measure_to_scaled_jacobian()
        C++: void SetQualityMeasureToScaledJacobian()"""
        self._vtk_obj.SetQualityMeasureToScaledJacobian()

    def set_quality_measure_to_shape(self):
        """
        V.set_quality_measure_to_shape()
        C++: void SetQualityMeasureToShape()"""
        self._vtk_obj.SetQualityMeasureToShape()

    def set_quality_measure_to_shape_and_size(self):
        """
        V.set_quality_measure_to_shape_and_size()
        C++: void SetQualityMeasureToShapeAndSize()"""
        self._vtk_obj.SetQualityMeasureToShapeAndSize()

    def set_quality_measure_to_shear(self):
        """
        V.set_quality_measure_to_shear()
        C++: void SetQualityMeasureToShear()"""
        self._vtk_obj.SetQualityMeasureToShear()

    def set_quality_measure_to_shear_and_size(self):
        """
        V.set_quality_measure_to_shear_and_size()
        C++: void SetQualityMeasureToShearAndSize()"""
        self._vtk_obj.SetQualityMeasureToShearAndSize()

    def set_quality_measure_to_skew(self):
        """
        V.set_quality_measure_to_skew()
        C++: void SetQualityMeasureToSkew()"""
        self._vtk_obj.SetQualityMeasureToSkew()

    def set_quality_measure_to_stretch(self):
        """
        V.set_quality_measure_to_stretch()
        C++: void SetQualityMeasureToStretch()"""
        self._vtk_obj.SetQualityMeasureToStretch()

    def set_quality_measure_to_taper(self):
        """
        V.set_quality_measure_to_taper()
        C++: void SetQualityMeasureToTaper()"""
        self._vtk_obj.SetQualityMeasureToTaper()

    def set_quality_measure_to_volume(self):
        """
        V.set_quality_measure_to_volume()
        C++: void SetQualityMeasureToVolume()"""
        self._vtk_obj.SetQualityMeasureToVolume()

    def set_quality_measure_to_warpage(self):
        """
        V.set_quality_measure_to_warpage()
        C++: void SetQualityMeasureToWarpage()"""
        self._vtk_obj.SetQualityMeasureToWarpage()

    undefined_quality = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the return value for undefined quality. Undefined quality
        are qualities that could be addressed by this filter but is not
        well defined for the particular geometry of cell in question,
        e.g. a volume query for a triangle. Undefined quality will always
        be undefined. The default value for undefined_quality is -1.
        """
    )

    def _undefined_quality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUndefinedQuality,
                        self.undefined_quality)

    unsupported_geometry = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the return value for unsupported geometry. Unsupported
        geometry are geometries that are not supported by this filter
        currently, future implementation might include support for them.
        The defalut value for unsupported_geometry is -1.
        """
    )

    def _unsupported_geometry_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUnsupportedGeometry,
                        self.unsupported_geometry)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def pixel_area(self, *args):
        """
        V.pixel_area(Cell) -> float
        C++: double PixelArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PixelArea, *my_args)
        return ret

    def polygon_area(self, *args):
        """
        V.polygon_area(Cell) -> float
        C++: double PolygonArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.PolygonArea, *my_args)
        return ret

    def triangle_strip_area(self, *args):
        """
        V.triangle_strip_area(Cell) -> float
        C++: double TriangleStripArea(Cell *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.TriangleStripArea, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('undefined_quality', 'GetUndefinedQuality'), ('unsupported_geometry',
    'GetUnsupportedGeometry'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'undefined_quality',
    'unsupported_geometry'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CellQuality, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['undefined_quality', 'unsupported_geometry']),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CellQuality properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

