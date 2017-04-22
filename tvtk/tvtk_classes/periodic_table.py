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


class PeriodicTable(Object):
    """
    PeriodicTable - Access to information about the elements.
    
    Superclass: Object
    
    Sourced from the Blue Obelisk Data Repository
    
    @sa
    BlueObeliskData BlueObeliskDataParser
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPeriodicTable, obj, update, **traits)
    
    def get_atomic_number(self, *args):
        """
        V.get_atomic_number(string) -> int
        C++: unsigned short GetAtomicNumber(const StdString &str)
        Given a case-insensitive string that contains the symbol or name
        of an element, return the corresponding atomic number.
        """
        ret = self._wrap_call(self._vtk_obj.GetAtomicNumber, *args)
        return ret

    def _get_blue_obelisk_data(self):
        return wrap_vtk(self._vtk_obj.GetBlueObeliskData())
    blue_obelisk_data = traits.Property(_get_blue_obelisk_data, help=\
        """
        Access the static BlueObeliskData object for raw access to
        BODR data.
        """
    )

    def get_covalent_radius(self, *args):
        """
        V.get_covalent_radius(int) -> float
        C++: float GetCovalentRadius(const unsigned short atomicNum)
        Given an atomic number, return the covalent radius of the atom
        """
        ret = self._wrap_call(self._vtk_obj.GetCovalentRadius, *args)
        return ret

    def get_default_lut(self, *args):
        """
        V.get_default_lut(LookupTable)
        C++: void GetDefaultLUT(LookupTable *)
        Fill the given LookupTable to map atomic numbers to the
        familiar RGB tuples provided by the Blue Obelisk Data Repository
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDefaultLUT, *my_args)
        return ret

    def get_default_rgb_tuple(self, *args):
        """
        V.get_default_rgb_tuple(int, [float, float, float])
        C++: void GetDefaultRGBTuple(unsigned short atomicNum,
            float rgb[3])
        V.get_default_rgb_tuple(int) -> Color3f
        C++: Color3f GetDefaultRGBTuple(unsigned short atomicNum)
        Given an atomic number, return the familiar RGB tuple provided by
        the Blue Obelisk Data Repository
        """
        ret = self._wrap_call(self._vtk_obj.GetDefaultRGBTuple, *args)
        return wrap_vtk(ret)

    def get_element_name(self, *args):
        """
        V.get_element_name(int) -> string
        C++: const char *GetElementName(const unsigned short atomicNum)
        Given an atomic number, returns the name of the element
        """
        ret = self._wrap_call(self._vtk_obj.GetElementName, *args)
        return ret

    def _get_number_of_elements(self):
        return self._vtk_obj.GetNumberOfElements()
    number_of_elements = traits.Property(_get_number_of_elements, help=\
        """
        Returns the number of elements in the periodic table.
        """
    )

    def get_symbol(self, *args):
        """
        V.get_symbol(int) -> string
        C++: const char *GetSymbol(const unsigned short atomicNum)
        Given an atomic number, returns the symbol associated with the
        element
        """
        ret = self._wrap_call(self._vtk_obj.GetSymbol, *args)
        return ret

    def get_vdw_radius(self, *args):
        """
        V.get_vdw_radius(int) -> float
        C++: float GetVDWRadius(const unsigned short atomicNum)
        Given an atomic number, returns the van der Waals radius of the
        atom
        """
        ret = self._wrap_call(self._vtk_obj.GetVDWRadius, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PeriodicTable, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PeriodicTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit PeriodicTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PeriodicTable properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

