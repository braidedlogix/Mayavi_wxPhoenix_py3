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


class ParametricFigure8Klein(ParametricFunction):
    """
    ParametricFigure8Klein - Generate a figure-8 Klein bottle.
    
    Superclass: ParametricFunction
    
    ParametricFigure8Klein generates a figure-8 Klein bottle.  A Klein
    bottle is a closed surface with no interior and only one surface.  It
    is unrealisable in 3 dimensions without intersecting surfaces.  It
    can be realised in 4 dimensions by considering the map $F:R^2
    \rightarrow R^4 $  given by:
    
    - $f(u,v) =
      ((r*cos(v)+a)*cos(u),(r*cos(v)+a)*sin(u),r*sin(v)*cos(u/2),r*sin(v)*
      sin(u/2)) $
    
    This representation of the immersion in $R^3 $ is formed by taking
    two Mobius strips and joining them along their boundaries, this is
    the so called "Figure-8 Klein Bottle"
    
    For further information about this surface, please consult the
    technical description "Parametric surfaces" in
    http://www.vtk.org/publications in the "VTK Technical Documents"
    section in the VTk.org web pages.
    
    @par Thanks: Andrew Maclean andrew.amaclean@gmail.com for creating
    and contributing the class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricFigure8Klein, obj, update, **traits)
    
    radius = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the radius of the bottle. Default is 1.
        """
    )

    def _radius_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadius,
                        self.radius)

    _updateable_traits_ = \
    (('clockwise_ordering', 'GetClockwiseOrdering'),
    ('derivatives_available', 'GetDerivativesAvailable'), ('join_u',
    'GetJoinU'), ('join_v', 'GetJoinV'), ('join_w', 'GetJoinW'),
    ('twist_u', 'GetTwistU'), ('twist_v', 'GetTwistV'), ('twist_w',
    'GetTwistW'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('radius', 'GetRadius'), ('maximum_u',
    'GetMaximumU'), ('maximum_v', 'GetMaximumV'), ('maximum_w',
    'GetMaximumW'), ('minimum_u', 'GetMinimumU'), ('minimum_v',
    'GetMinimumV'), ('minimum_w', 'GetMinimumW'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['clockwise_ordering', 'debug', 'derivatives_available',
    'global_warning_display', 'join_u', 'join_v', 'join_w', 'twist_u',
    'twist_v', 'twist_w', 'maximum_u', 'maximum_v', 'maximum_w',
    'minimum_u', 'minimum_v', 'minimum_w', 'radius'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricFigure8Klein, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricFigure8Klein properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clockwise_ordering', 'derivatives_available', 'join_u',
            'join_v', 'join_w', 'twist_u', 'twist_v', 'twist_w'], [],
            ['maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
            'minimum_w', 'radius']),
            title='Edit ParametricFigure8Klein properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricFigure8Klein properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

