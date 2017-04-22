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


class ImageSinusoidSource(ImageAlgorithm):
    """
    ImageSinusoidSource - Create an image with sinusoidal pixel values.
    
    Superclass: ImageAlgorithm
    
    ImageSinusoidSource just produces images with pixel values
    determined by a sinusoid.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSinusoidSource, obj, update, **traits)
    
    amplitude = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the magnitude of the sinusoid.
        """
    )

    def _amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmplitude,
                        self.amplitude)

    direction = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the direction vector which determines the sinusoidal
        orientation. The magnitude is ignored.
        """
    )

    def _direction_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDirection,
                        self.direction)

    period = traits.Float(20.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the period of the sinusoid in pixels.
        """
    )

    def _period_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPeriod,
                        self.period)

    phase = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the phase: 0->_2_pi.  0 => Cosine, pi/2 => Sine.
        """
    )

    def _phase_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPhase,
                        self.phase)

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

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(int, int, int, int, int, int)
        C++: void SetWholeExtent(int xMinx, int xMax, int yMin, int yMax,
            int zMin, int zMax)
        Set/Get the extent of the whole output image.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('amplitude',
    'GetAmplitude'), ('direction', 'GetDirection'), ('period',
    'GetPeriod'), ('phase', 'GetPhase'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'amplitude', 'direction', 'period', 'phase',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSinusoidSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['amplitude', 'direction', 'period', 'phase']),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSinusoidSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

