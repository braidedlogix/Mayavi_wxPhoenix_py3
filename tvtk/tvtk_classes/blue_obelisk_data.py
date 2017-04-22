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


class BlueObeliskData(Object):
    """
    BlueObeliskData - Contains chemical data from the Blue
    
    Superclass: Object
    
    Obelisk Data Repository
    
    The Blue Obelisk Data Repository is a free, open repository of
    chemical information. This class is a container for this information.
    
    ote This class contains only the raw arrays parsed from the BODR. For
    more convenient access to this data, use the PeriodicTable class.
    
    ote If you must use this class directly, consider using the static
    BlueObeliskData object accessible through
    PeriodicTable::GetBlueObeliskData(). This object is automatically
    populated on the first instantiation of PeriodicTable.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkBlueObeliskData, obj, update, **traits)
    
    def _get_boiling_points(self):
        return wrap_vtk(self._vtk_obj.GetBoilingPoints())
    boiling_points = traits.Property(_get_boiling_points, help=\
        """
        
        """
    )

    def _get_covalent_radii(self):
        return wrap_vtk(self._vtk_obj.GetCovalentRadii())
    covalent_radii = traits.Property(_get_covalent_radii, help=\
        """
        
        """
    )

    def _get_default_colors(self):
        return wrap_vtk(self._vtk_obj.GetDefaultColors())
    default_colors = traits.Property(_get_default_colors, help=\
        """
        
        """
    )

    def _get_electron_affinities(self):
        return wrap_vtk(self._vtk_obj.GetElectronAffinities())
    electron_affinities = traits.Property(_get_electron_affinities, help=\
        """
        
        """
    )

    def _get_electronic_configurations(self):
        return wrap_vtk(self._vtk_obj.GetElectronicConfigurations())
    electronic_configurations = traits.Property(_get_electronic_configurations, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_exact_masses(self):
        return wrap_vtk(self._vtk_obj.GetExactMasses())
    exact_masses = traits.Property(_get_exact_masses, help=\
        """
        
        """
    )

    def _get_families(self):
        return wrap_vtk(self._vtk_obj.GetFamilies())
    families = traits.Property(_get_families, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_groups(self):
        return wrap_vtk(self._vtk_obj.GetGroups())
    groups = traits.Property(_get_groups, help=\
        """
        
        """
    )

    def _get_ionization_energies(self):
        return wrap_vtk(self._vtk_obj.GetIonizationEnergies())
    ionization_energies = traits.Property(_get_ionization_energies, help=\
        """
        
        """
    )

    def _get_lower_names(self):
        return wrap_vtk(self._vtk_obj.GetLowerNames())
    lower_names = traits.Property(_get_lower_names, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_lower_symbols(self):
        return wrap_vtk(self._vtk_obj.GetLowerSymbols())
    lower_symbols = traits.Property(_get_lower_symbols, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_masses(self):
        return wrap_vtk(self._vtk_obj.GetMasses())
    masses = traits.Property(_get_masses, help=\
        """
        
        """
    )

    def _get_melting_points(self):
        return wrap_vtk(self._vtk_obj.GetMeltingPoints())
    melting_points = traits.Property(_get_melting_points, help=\
        """
        
        """
    )

    def _get_names(self):
        return wrap_vtk(self._vtk_obj.GetNames())
    names = traits.Property(_get_names, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_number_of_elements(self):
        return self._vtk_obj.GetNumberOfElements()
    number_of_elements = traits.Property(_get_number_of_elements, help=\
        """
        Return the number of elements for which this BlueObeliskData
        instance contains information.
        """
    )

    def _get_pauling_electronegativities(self):
        return wrap_vtk(self._vtk_obj.GetPaulingElectronegativities())
    pauling_electronegativities = traits.Property(_get_pauling_electronegativities, help=\
        """
        
        """
    )

    def _get_periodic_table_blocks(self):
        return wrap_vtk(self._vtk_obj.GetPeriodicTableBlocks())
    periodic_table_blocks = traits.Property(_get_periodic_table_blocks, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_periods(self):
        return wrap_vtk(self._vtk_obj.GetPeriods())
    periods = traits.Property(_get_periods, help=\
        """
        
        """
    )

    def _get_symbols(self):
        return wrap_vtk(self._vtk_obj.GetSymbols())
    symbols = traits.Property(_get_symbols, help=\
        """
        Access the raw arrays stored in this BlueObeliskData.
        """
    )

    def _get_vdw_radii(self):
        return wrap_vtk(self._vtk_obj.GetVDWRadii())
    vdw_radii = traits.Property(_get_vdw_radii, help=\
        """
        
        """
    )

    def initialize(self):
        """
        V.initialize()
        C++: void Initialize()
        Fill this object using an internal BlueObeliskDataParser
        instance. Check that the SimpleMutexLock get_write_mutex() is
        locked before calling this method on a static instance in a
        multithreaded environment.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def is_initialized(self):
        """
        V.is_initialized() -> bool
        C++: bool IsInitialized()
        Check if this object has been initialized yet.
        """
        ret = self._vtk_obj.IsInitialized()
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
            return super(BlueObeliskData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit BlueObeliskData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit BlueObeliskData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit BlueObeliskData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

