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

from tvtk.tvtk_classes.information_integer_key import InformationIntegerKey


class InformationIntegerRequestKey(InformationIntegerKey):
    """
    InformationIntegerRequestKey - key that can used to request
    integer values from the pipeline InformationIntegerRequestKey is a
    InformationIntegerKey that can used to request integer values from
    upstream.
    
    Superclass: InformationIntegerKey
    
    A good example of this is UPDATE_NUMBER_OF_PIECES where downstream
    can request that upstream provides data partitioned into a certain
    number of pieces. There are several components that make this work.
    First, the key will copy itself upstream during
    REQUEST_UPDATE_EXTENT. Second, after a successfull execution, it will
    stor its value into a data object's information using a specific key
    defined by its data member data_key. Third, before execution, it will
    check if the requested value matched the value in the data object's
    information. If not, it will ask the pipeline to execute.
    
    The best way to use this class is to subclass it to set the data_key
    data member. This is usually done in the subclass' constructor.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkInformationIntegerRequestKey, obj, update, **traits)
    
    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'),)
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(InformationIntegerRequestKey, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit InformationIntegerRequestKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit InformationIntegerRequestKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit InformationIntegerRequestKey properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

