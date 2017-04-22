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

from tvtk.tvtk_classes.xml_parser import XMLParser


class BlueObeliskDataParser(XMLParser):
    """
    BlueObeliskDataParser - Fill a BlueObeliskData container with
    data from the BODR XML dataset.
    
    Superclass: XMLParser
    
    The Blue Obelisk Data Repository is a free, open repository of
    chemical information. This class extracts the BODR information into
    vtk arrays, which are stored in a BlueObeliskData object.
    
    \warning The BlueObeliskDataParser class should never need to be
    used directly. For convenient access to the BODR data, use
    PeriodicTable. For access to the raw arrays produced by this
    parser, see the BlueObeliskData class. A static BlueObeliskData
    object is accessible via PeriodicTable::GetBlueObeliskData().
    
    @sa
    PeriodicTable BlueObeliskData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBlueObeliskDataParser, obj, update, **traits)
    
    def set_target(self, *args):
        """
        V.set_target(BlueObeliskData)
        C++: virtual void SetTarget(BlueObeliskData *bodr)
        Set the target BlueObeliskData object that this parser will
        populate
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetTarget, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('encoding', 'GetEncoding'), ('file_name',
    'GetFileName'), ('ignore_character_data', 'GetIgnoreCharacterData'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'encoding', 'file_name',
    'ignore_character_data'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(BlueObeliskDataParser, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BlueObeliskDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['encoding', 'file_name', 'ignore_character_data']),
            title='Edit BlueObeliskDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BlueObeliskDataParser properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

