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


class ProjectedTerrainPath(PolyDataAlgorithm):
    """
    ProjectedTerrainPath - project a polyline onto a terrain
    
    Superclass: PolyDataAlgorithm
    
    ProjectedTerrainPath projects an input polyline onto a terrain.
    (The terrain is defined by a 2d height image and is the second input
    to the filter.) The polyline projection is controlled via several
    modes as follows. 1) Simple mode projects the polyline points onto
    the terrain, taking into account the height offset instance variable.
    2) Non-occluded mode insures that no parts of the polyline are
    occluded by the terrain (e.g. a line passes through a mountain). This
    may require recursive subdivision of the polyline. 3) Hug mode
    insures that the polyine points remain within a constant distance
    from the surface. This may also require recursive subdivision of the
    polyline. Note that both non-occluded mode and hug mode also take
    into account the height offset, so it is possible to create paths
    that hug terrain a certain distance above it. To use this filter,
    define two inputs: 1) a polyline, and 2) an image whose scalar values
    represent a height field. Then specify the mode, and the height
    offset to use.
    
    An description of the algorithm is as follows. The filter begins by
    projecting the polyline points to the image (offset by the specified
    height offset).  If the mode is non-occluded or hug, then the maximum
    error along each line segment is computed and placed into a priority
    queue. Each line segment is then split at the point of maximum error,
    and the two new line segments are evaluated for maximum error. This
    process continues until the line is not occluded by the terrain
    (non-occluded mode) or satisfies the error on variation from the
    surface (hug mode). (Note this process is repeated for each polyline
    in the input. Also, the maximum error is computed in two parts: a
    maximum positive error and maximum negative error. If the polyline is
    above the terrain--i.e., the height offset is positive--in
    non-occluded or hug mode all negative errors are eliminated. If the
    polyline is below the terrain--i.e., the height offset is
    negative--in non-occluded or hug mode all positive errors are
    eliminated.)
    
    @warning
    This algorithm requires the entire input image to be in memory, hence
    it may not work for extremely large images.
    
    @warning
    The input height image is assumed to be positioned in the x-y plane
    so the scalar value is the z-coordinate, height value.
    
    @warning
    A priority queue is used so that the 1) the total number of line
    segments can be controlled, and 2) the algorithm can terminate when
    the errors in the queue are less than the specified error tolerance.
    
    @sa
    GreedyTerrainDecimation
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProjectedTerrainPath, obj, update, **traits)
    
    projection_mode = traits.Trait('simple',
    tvtk_base.TraitRevPrefixMap({'simple': 0, 'hug': 2, 'non_occluded': 1}), help=\
        """
        Determine how to control the projection process. Simple
        projection just projects the original polyline points.
        Non-occluded projection insures that the polyline does not
        intersect the terrain surface. Hug projection is similar to
        non-occulded projection except that produces a path that is
        nearly parallel to the terrain (within the user specified height
        tolerance).
        """
    )

    def _projection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionMode,
                        self.projection_mode_)

    height_offset = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        This is the height above (or below) the terrain that the
        projected path should be. Positive values indicate distances
        above the terrain; negative values indicate distances below the
        terrain.
        """
    )

    def _height_offset_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeightOffset,
                        self.height_offset)

    height_tolerance = traits.Trait(10.0, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        This is the allowable variation in the altitude of the path with
        respect to the variation in the terrain. It only comes into play
        if the hug projection mode is enabled.
        """
    )

    def _height_tolerance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHeightTolerance,
                        self.height_tolerance)

    maximum_number_of_lines = traits.Trait(9223372036854775807, traits.Range(1, 9223372036854775807, enter_set=True, auto_set=False), help=\
        """
        This instance variable can be used to limit the total number of
        line segments created during subdivision. Note that the number of
        input line segments will be the minimum number that cab be
        output.
        """
    )

    def _maximum_number_of_lines_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfLines,
                        self.maximum_number_of_lines)

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

    def _get_source(self):
        return wrap_vtk(self._vtk_obj.GetSource())
    source = traits.Property(_get_source, help=\
        """
        Specify the second input (the terrain) onto which the polyline(s)
        should be projected. Note: This assigns a data object as the
        input terrain. To establish a pipeline connection, use
        set_source_connection() method.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the second input (the terrain) onto which the polyline(s)
        should be projected. Note: ImageData* is required
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(ImageData)
        C++: void SetSourceData(ImageData *source)
        Specify the second input (the terrain) onto which the polyline(s)
        should be projected. Note: This assigns a data object as the
        input terrain. To establish a pipeline connection, use
        set_source_connection() method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('projection_mode', 'GetProjectionMode'), ('height_offset',
    'GetHeightOffset'), ('height_tolerance', 'GetHeightTolerance'),
    ('maximum_number_of_lines', 'GetMaximumNumberOfLines'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'projection_mode', 'height_offset',
    'height_tolerance', 'maximum_number_of_lines', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProjectedTerrainPath, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProjectedTerrainPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['projection_mode'], ['height_offset', 'height_tolerance',
            'maximum_number_of_lines']),
            title='Edit ProjectedTerrainPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProjectedTerrainPath properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

