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


class ParametricPluckerConoid(ParametricFunction):
    """
    ParametricPluckerConoid - Generate Plucker's conoid surface.
    
    Superclass: ParametricFunction
    
    ParametricPluckerConoid generates Plucker's conoid surface
    parametrically. Plucker's conoid is a ruled surface, named after
    Julius Plucker. It is possible to set the number of folds in this
    class via the parameter 'N'.
    
    For more information, see the Wikipedia page on <a
    href="https://en.wikipedia.org/wiki/Plücker%27s_conoid">Plucker's
    Conoid.
    @warning
    I haven't done any special checking on the number of folds parameter,
    N.@par Thanks: Tim Meehan
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkParametricPluckerConoid, obj, update, **traits)
    
    n = traits.Int(2, enter_set=True, auto_set=False, help=\
        """
        This is the number of folds in the conoid.
        """
    )

    def _n_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetN,
                        self.n)

    _updateable_traits_ = \
    (('clockwise_ordering', 'GetClockwiseOrdering'),
    ('derivatives_available', 'GetDerivativesAvailable'), ('join_u',
    'GetJoinU'), ('join_v', 'GetJoinV'), ('join_w', 'GetJoinW'),
    ('twist_u', 'GetTwistU'), ('twist_v', 'GetTwistV'), ('twist_w',
    'GetTwistW'), ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('n', 'GetN'), ('maximum_u',
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
    'minimum_u', 'minimum_v', 'minimum_w', 'n'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ParametricPluckerConoid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ParametricPluckerConoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clockwise_ordering', 'derivatives_available', 'join_u',
            'join_v', 'join_w', 'twist_u', 'twist_v', 'twist_w'], [],
            ['maximum_u', 'maximum_v', 'maximum_w', 'minimum_u', 'minimum_v',
            'minimum_w', 'n']),
            title='Edit ParametricPluckerConoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ParametricPluckerConoid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

