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


class RTAnalyticSource(ImageAlgorithm):
    """
    RTAnalyticSource - Create an image for regression testing
    
    Superclass: ImageAlgorithm
    
    RTAnalyticSource just produces images with pixel values determined
    by a Maximum*Gaussian*XMag*sin(XFreq*x)*sin(YFreq*y)*cos(ZFreq*z)
    Values are float scalars on point data with name "RTData".
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRTAnalyticSource, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    maximum = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Maximum value of the function. Initial value is
        255.0.
        """
    )

    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    standard_deviation = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the standard deviation of the function. Initial value is
        0.5.
        """
    )

    def _standard_deviation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetStandardDeviation,
                        self.standard_deviation)

    subsample_rate = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the sub-sample rate. Initial value is 1.
        """
    )

    def _subsample_rate_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubsampleRate,
                        self.subsample_rate)

    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(-10, 10, -10, 10, -10, 10), cols=3, help=\
        """
        Set/Get the extent of the whole output image. Initial value is
        {-10,10,-10,10,-10,10}
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    x_freq = traits.Float(60.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in x. Initial value is 60.
        """
    )

    def _x_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXFreq,
                        self.x_freq)

    x_mag = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in x. Initial value is 10.
        """
    )

    def _x_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXMag,
                        self.x_mag)

    y_freq = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in y. Initial value is 30.
        """
    )

    def _y_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYFreq,
                        self.y_freq)

    y_mag = traits.Float(18.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in y. Initial value is 18.
        """
    )

    def _y_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYMag,
                        self.y_mag)

    z_freq = traits.Float(40.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the natural frequency in z. Initial value is 40.
        """
    )

    def _z_freq_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZFreq,
                        self.z_freq)

    z_mag = traits.Float(5.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude in z. Initial value is 5.
        """
    )

    def _z_mag_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetZMag,
                        self.z_mag)

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

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('maximum', 'GetMaximum'), ('standard_deviation',
    'GetStandardDeviation'), ('subsample_rate', 'GetSubsampleRate'),
    ('whole_extent', 'GetWholeExtent'), ('x_freq', 'GetXFreq'), ('x_mag',
    'GetXMag'), ('y_freq', 'GetYFreq'), ('y_mag', 'GetYMag'), ('z_freq',
    'GetZFreq'), ('z_mag', 'GetZMag'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'maximum', 'progress_text',
    'standard_deviation', 'subsample_rate', 'whole_extent', 'x_freq',
    'x_mag', 'y_freq', 'y_mag', 'z_freq', 'z_mag'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RTAnalyticSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'maximum', 'standard_deviation',
            'subsample_rate', 'whole_extent', 'x_freq', 'x_mag', 'y_freq',
            'y_mag', 'z_freq', 'z_mag']),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RTAnalyticSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

