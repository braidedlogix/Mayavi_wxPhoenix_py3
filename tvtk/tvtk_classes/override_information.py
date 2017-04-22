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

from tvtk.tvtk_classes.object import Object


class OverrideInformation(Object):
    """
    OverrideInformation - Factory object override information
    
    Superclass: Object
    
    OverrideInformation is used to represent the information about a
    class which is overriden in a ObjectFactory.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOverrideInformation, obj, update, **traits)
    
    class_override_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the class override name
        """
    )

    def _class_override_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClassOverrideName,
                        self.class_override_name)

    class_override_with_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the class override with name
        """
    )

    def _class_override_with_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClassOverrideWithName,
                        self.class_override_with_name)

    description = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set the description
        """
    )

    def _description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDescription,
                        self.description)

    def _get_object_factory(self):
        return wrap_vtk(self._vtk_obj.GetObjectFactory())
    object_factory = traits.Property(_get_object_factory, help=\
        """
        Return the specific object factory that this override occurs in.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('class_override_name',
    'GetClassOverrideName'), ('class_override_with_name',
    'GetClassOverrideWithName'), ('description', 'GetDescription'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'class_override_name',
    'class_override_with_name', 'description'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OverrideInformation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OverrideInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['class_override_name', 'class_override_with_name',
            'description']),
            title='Edit OverrideInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OverrideInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

