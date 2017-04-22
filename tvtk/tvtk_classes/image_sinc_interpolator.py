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

from tvtk.tvtk_classes.abstract_image_interpolator import AbstractImageInterpolator


class ImageSincInterpolator(AbstractImageInterpolator):
    """
    ImageSincInterpolator - perform sinc interpolation on images
    
    Superclass: AbstractImageInterpolator
    
    ImageSincInterpolator provides various windowed sinc interpolation
    methods for image data.  The default is a five-lobed Lanczos
    interpolant, with a kernel size of 6.  The interpolator can also
    bandlimit the image, which can be used for antialiasing.  The
    interpolation kernels are evaluated via a lookup table for
    efficiency.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    @sa
    ImageReslice
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSincInterpolator, obj, update, **traits)
    
    antialiasing = tvtk_base.false_bool_trait(help=\
        """
        Turn on antialiasing.  If antialiasing is on, then the
        blur_factors will be computed automatically from the output
        sampling rate such that that the image will be bandlimited to the
        Nyquist frequency.  This is only applicable when the interpolator
        is being used by a resampling filter like ImageReslice.  Such
        a filter will indicate the output sampling by calling the
        interpolator's compute_support_size() method, which will compute
        the blur factors at the same time that it computes the support
        size.
        """
    )

    def _antialiasing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAntialiasing,
                        self.antialiasing_)

    renormalization = tvtk_base.true_bool_trait(help=\
        """
        Turn off renormalization.  Most of the sinc windows provide
        kernels for which the weights do not sum to one, and for which
        the sum depends on the offset.  This results in small ripple
        artifacts in the output. By default, the ImageSincInterpolator
        will renormalize these kernels. This method allows the
        renormalization to be turned off.
        """
    )

    def _renormalization_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenormalization,
                        self.renormalization_)

    use_window_parameter = tvtk_base.false_bool_trait(help=\
        """
        Turn this on in order to use set_window_parameter.  If it is off,
        then the default parameter will be used for the window.
        """
    )

    def _use_window_parameter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseWindowParameter,
                        self.use_window_parameter_)

    window_function = traits.Trait('lanczos',
    tvtk_base.TraitRevPrefixMap({'lanczos': 0, 'blackman': 5, 'blackman_harris3': 6, 'blackman_harris4': 7, 'blackman_nuttall3': 9, 'blackman_nuttall4': 10, 'cosine': 2, 'hamming': 4, 'hann': 3, 'kaiser': 1, 'nuttall': 8}), help=\
        """
        The window function to use.  The default is Lanczos, which is
        very popular and performs well with a kernel width of 6.  The
        Cosine window is included for historical reasons.  All other
        windows are described in AH Nuttall, "Some windows with very good
        sidelobe behavior," IEEE Transactions on Acoustics, Speech, and
        Signal Processing 29:84-91, 1981.
        """
    )

    def _window_function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowFunction,
                        self.window_function_)

    blur_factors = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        Blur the image by widening the windowed sinc kernel by the
        specified factors for the x, y, and z directions.  This reduces
        the bandwidth by these same factors.  If you turn Antialiasing
        on, then the blur factors will be computed automatically from the
        output sampling rate. Blurring increases the computation time
        because the kernel size increases by the blur factor.
        """
    )

    def _blur_factors_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlurFactors,
                        self.blur_factors)

    window_half_width = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the window half-width, this must be an integer between 1 and
        16, with a default value of 3.  The kernel size will be twice
        this value if no blur factors are applied. The total number of
        sinc lobes will be one less than twice the half-width, so if the
        half-width is 3 then the kernel size will be 6 and there will be
        5 sinc lobes.
        """
    )

    def _window_half_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowHalfWidth,
                        self.window_half_width)

    window_parameter = traits.Float(0.5, enter_set=True, auto_set=False, help=\
        """
        Set the alpha parameter for the Kaiser window function. This
        parameter will be ignored unless use_window_parameter is On. If
        use_window_parameter is Off, then alpha is set to be the same as n
        where n is the window half-width.  Using an alpha less than n
        increases the sharpness and ringing, while using an alpha greater
        than n increases the blurring.
        """
    )

    def _window_parameter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowParameter,
                        self.window_parameter)

    _updateable_traits_ = \
    (('antialiasing', 'GetAntialiasing'), ('renormalization',
    'GetRenormalization'), ('use_window_parameter',
    'GetUseWindowParameter'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('window_function', 'GetWindowFunction'), ('border_mode',
    'GetBorderMode'), ('blur_factors', 'GetBlurFactors'),
    ('window_half_width', 'GetWindowHalfWidth'), ('window_parameter',
    'GetWindowParameter'), ('component_count', 'GetComponentCount'),
    ('component_offset', 'GetComponentOffset'), ('out_value',
    'GetOutValue'), ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['antialiasing', 'debug', 'global_warning_display',
    'renormalization', 'use_window_parameter', 'border_mode',
    'window_function', 'blur_factors', 'component_count',
    'component_offset', 'out_value', 'tolerance', 'window_half_width',
    'window_parameter'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSincInterpolator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSincInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['antialiasing', 'renormalization', 'use_window_parameter'],
            ['border_mode', 'window_function'], ['blur_factors',
            'component_count', 'component_offset', 'out_value', 'tolerance',
            'window_half_width', 'window_parameter']),
            title='Edit ImageSincInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSincInterpolator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

