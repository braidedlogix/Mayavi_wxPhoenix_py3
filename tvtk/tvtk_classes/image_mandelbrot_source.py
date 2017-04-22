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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageMandelbrotSource(ImageAlgorithm):
    """
    ImageMandelbrotSource - Mandelbrot image.
    
    Superclass: ImageAlgorithm
    
    ImageMandelbrotSource creates an unsigned char image of the
    Mandelbrot set.  The values in the image are the number of iterations
    it takes for the magnitude of the value to get over 2.  The equation
    repeated is z = z^2 + C (z and C are complex).  Initial value of z is
    zero, and the real value of C is mapped onto the x axis, and the
    imaginary value of C is mapped onto the Y Axis.  I was thinking of
    extending this source to generate Julia Sets (initial value of Z
    varies).  This would be 4 possible parameters to vary, but there are
    no more 4d images :( The third dimension (z axis) is the imaginary
    value of the initial value.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageMandelbrotSource, obj, update, **traits)
    
    constant_size = tvtk_base.true_bool_trait(help=\
        """
        This flag determines whether the Size or spacing of a data set
        remain constant (when extent is changed). By default, size
        remains constant.
        """
    )

    def _constant_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConstantSize,
                        self.constant_size_)

    maximum_number_of_iterations = traits.Trait(100, traits.Range(1, 5000, enter_set=True, auto_set=False), help=\
        """
        The maximum number of cycles run to see if the value goes over 2
        """
    )

    def _maximum_number_of_iterations_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfIterations,
                        self.maximum_number_of_iterations)

    origin_cx = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(-1.75, -1.25, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_cx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginCX,
                        self.origin_cx)

    projection_axes = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 1, 2), cols=3, help=\
        """
        Set the projection from  the 4d space (4 parameters / 2 imaginary
        numbers) to the axes of the 3d Volume. 0=C_Real, 1=C_Imaginary,
        2=X_Real, 4=X_Imaginary
        """
    )

    def _projection_axes_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetProjectionAxes,
                        self.projection_axes)

    sample_cx = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.01, 0.01, 0.01, 0.01), cols=3, help=\
        """
        
        """
    )

    def _sample_cx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleCX,
                        self.sample_cx)

    size_cx = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(2.5, 2.5, 2.0, 1.5), cols=3, help=\
        """
        Just a different way of setting the sample. This sets the size of
        the 4d volume. sample_cx is computed from size and extent. Size is
        ignored when a dimension i 0 (collapsed).
        """
    )

    def _size_cx_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSizeCX,
                        self.size_cx)

    subsample_rate = traits.Trait(1, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set/Get a subsample rate.
        """
    )

    def _subsample_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubsampleRate,
                        self.subsample_rate)

    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, 250, 0, 250, 0, 0), cols=3, help=\
        """
        Set/Get the extent of the whole output Volume.
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def copy_origin_and_sample(self, *args):
        """
        V.copy_origin_and_sample(ImageMandelbrotSource)
        C++: void CopyOriginAndSample(ImageMandelbrotSource *source)
        Convienence for Viewer.  Copy the origin_cx and the spacing_cx.
        What about other parameters ???
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CopyOriginAndSample, *my_args)
        return ret

    def pan(self, *args):
        """
        V.pan(float, float, float)
        C++: void Pan(double x, double y, double z)
        Convienence for Viewer.  Pan 3d volume relative to spacing. Zoom
        constant factor.
        """
        ret = self._wrap_call(self._vtk_obj.Pan, *args)
        return ret

    def zoom(self, *args):
        """
        V.zoom(float)
        C++: void Zoom(double factor)
        Convienence for Viewer.  Pan 3d volume relative to spacing. Zoom
        constant factor.
        """
        ret = self._wrap_call(self._vtk_obj.Zoom, *args)
        return ret

    _updateable_traits_ = \
    (('constant_size', 'GetConstantSize'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('maximum_number_of_iterations',
    'GetMaximumNumberOfIterations'), ('origin_cx', 'GetOriginCX'),
    ('projection_axes', 'GetProjectionAxes'), ('sample_cx',
    'GetSampleCX'), ('size_cx', 'GetSizeCX'), ('subsample_rate',
    'GetSubsampleRate'), ('whole_extent', 'GetWholeExtent'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'constant_size', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum_number_of_iterations', 'origin_cx',
    'progress_text', 'projection_axes', 'sample_cx', 'size_cx',
    'subsample_rate', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageMandelbrotSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageMandelbrotSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['constant_size'], [], ['maximum_number_of_iterations',
            'origin_cx', 'projection_axes', 'sample_cx', 'size_cx',
            'subsample_rate', 'whole_extent']),
            title='Edit ImageMandelbrotSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageMandelbrotSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

