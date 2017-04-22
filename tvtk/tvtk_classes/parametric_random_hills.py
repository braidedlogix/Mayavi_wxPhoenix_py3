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

from tvtk.tvtk_classes.parametric_function import ParametricFunction


class ParametricRandomHills(ParametricFunction):
    """
    ParametricRandomHills - Generate a surface covered with randomly
    placed hills.
    
    Superclass: ParametricFunction
    
    ParametricRandomHills generates a surface covered with randomly
    placed hills. Hills will vary in shape and height since the presence
    of nearby hills will contribute to the shape and height of a given
    hill. An option is provided for placing hills on a regular grid on
    the surface. In this case the hills will all have the same shape and
    height.
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/publications in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    @par Thanks: Andrew Maclean andrew.amaclean@gmail.com for creating
    and contributing the class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricRandomHills, obj, update, **traits)
    
    allow_random_generation = tvtk_base.true_bool_trait(help=\
        """
        Set/Get the random generation flag. A value of 0 will disable the
        generation of random hills on the surface allowing a reproducible
        number of identically shaped hills to be generated. If zero, then
        the number of hills used will be the nearest perfect square less
        than or equal to the number of hills. For example, selecting 30
        hills will result in a 5 X 5 array of hills being generated. Thus
        a square array of hills will be generated.
        
        * Any other value means that the hills will be placed randomly on
        the
        * surface.
        * Default is 1.
        """
    )

    def _allow_random_generation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAllowRandomGeneration,
                        self.allow_random_generation_)

    amplitude_scale_factor = traits.Float(0.3333333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the amplitude. Default is 1/3.
        """
    )

    def _amplitude_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAmplitudeScaleFactor,
                        self.amplitude_scale_factor)

    hill_amplitude = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill amplitude (height). Default is 2.
        """
    )

    def _hill_amplitude_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillAmplitude,
                        self.hill_amplitude)

    hill_x_variance = traits.Float(2.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill variance in the x-direction. Default is 2.5.
        """
    )

    def _hill_x_variance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillXVariance,
                        self.hill_x_variance)

    hill_y_variance = traits.Float(2.5, enter_set=True, auto_set=False, help=\
        """
        Set/Get the hill variance in the y-direction. Default is 2.5.
        """
    )

    def _hill_y_variance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHillYVariance,
                        self.hill_y_variance)

    number_of_hills = traits.Int(30, enter_set=True, auto_set=False, help=\
        """
        Set/Get the number of hills. Default is 30.
        """
    )

    def _number_of_hills_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfHills,
                        self.number_of_hills)

    random_seed = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set/Get the Seed for the random number generator, a value of 1
        will initialize the random number generator, a negative value
        will initialize it with the system time. Default is 1.
        """
    )

    def _random_seed_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRandomSeed,
                        self.random_seed)

    x_variance_scale_factor = traits.Float(0.3333333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the variance in the x-direction.
        Default is 1/3.
        """
    )

    def _x_variance_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetXVarianceScaleFactor,
                        self.x_variance_scale_factor)

    y_variance_scale_factor = traits.Float(0.3333333333333333, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling factor for the variance in the y-direction.
        Default is 1/3.
        """
    )

    def _y_variance_scale_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetYVarianceScaleFactor,
                        self.y_variance_scale_factor)

    def _get_allow_random_generation_max_value(self):
        return self._vtk_obj.GetAllowRandomGenerationMaxValue()
    allow_random_generation_max_value = traits.Property(_get_allow_random_generation_max_value, help=\
        """
        Set/Get the random generation flag. A value of 0 will disable the
        generation of random hills on the surface allowing a reproducible
        number of identically shaped hills to be generated. If zero, then
        the number of hills used will be the nearest perfect square less
        than or equal to the number of hills. For example, selecting 30
        hills will result in a 5 X 5 array of hills being generated. Thus
        a square array of hills will be generated.
        
        * Any other value means that the hills will be placed randomly on
        the
        * surface.
        * Default is 1.
        """
    )

    def _get_allow_random_generation_min_value(self):
        return self._vtk_obj.GetAllowRandomGenerationMinValue()
    allow_random_generation_min_value = traits.Property(_get_allow_random_generation_min_value, help=\
        """
        Set/Get the random generation flag. A value of 0 will disable the
        generation of random hills on the surface allowing a reproducible
        number of identically shaped hills to be generated. If zero, then
        the number of hills used will be the nearest perfect square less
        than or equal to the number of hills. For example, selecting 30
        hills will result in a 5 X 5 array of hills being generated. Thus
        a square array of hills will be generated.
        
        * Any other value means that the hills will be placed randomly on
        the
        * surface.
        * Default is 1.
        """
    )

    _updateable_traits_ = \
    (('allow_random_generation', 'GetAllowRandomGeneration'),
    ('clockwise_ordering', 'GetClockwiseOrdering'),
    ('derivatives_available', 'GetDerivativesAvailable'), ('join_u',
    'GetJoinU'), ('join_v', 'GetJoinV'), ('join_w', 'GetJoinW'),
    ('twist_u', 'GetTwistU'), ('twist_v', 'GetTwistV'), ('twist_w',
    'GetTwistW'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('amplitude_scale_factor',
    'GetAmplitudeScaleFactor'), ('hill_amplitude', 'GetHillAmplitude'),
    ('hill_x_variance', 'GetHillXVariance'), ('hill_y_variance',
    'GetHillYVariance'), ('number_of_hills', 'GetNumberOfHills'),
    ('random_seed', 'GetRandomSeed'), ('x_variance_scale_factor',
    'GetXVarianceScaleFactor'), ('y_variance_scale_factor',
    'GetYVarianceScaleFactor'), ('maximum_u', 'GetMaximumU'),
    ('maximum_v', 'GetMaximumV'), ('maximum_w', 'GetMaximumW'),
    ('minimum_u', 'GetMinimumU'), ('minimum_v', 'GetMinimumV'),
    ('minimum_w', 'GetMinimumW'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['allow_random_generation', 'clockwise_ordering', 'debug',
    'derivatives_available', 'global_warning_display', 'join_u', 'join_v',
    'join_w', 'twist_u', 'twist_v', 'twist_w', 'amplitude_scale_factor',
    'hill_amplitude', 'hill_x_variance', 'hill_y_variance', 'maximum_u',
    'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w',
    'number_of_hills', 'random_seed', 'x_variance_scale_factor',
    'y_variance_scale_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricRandomHills, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['allow_random_generation', 'clockwise_ordering',
            'derivatives_available', 'join_u', 'join_v', 'join_w', 'twist_u',
            'twist_v', 'twist_w'], [], ['amplitude_scale_factor',
            'hill_amplitude', 'hill_x_variance', 'hill_y_variance', 'maximum_u',
            'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v', 'minimum_w',
            'number_of_hills', 'random_seed', 'x_variance_scale_factor',
            'y_variance_scale_factor']),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricRandomHills properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

