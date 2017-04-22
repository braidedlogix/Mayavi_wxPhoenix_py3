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

from tvtk.tvtk_classes.abstract_electronic_data import AbstractElectronicData


class ProgrammableElectronicData(AbstractElectronicData):
    """
    ProgrammableElectronicData - Provides access to and storage of
    user-generated ImageData that describes electrons.
    
    Superclass: AbstractElectronicData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProgrammableElectronicData, obj, update, **traits)
    
    def _get_electron_density(self):
        return wrap_vtk(self._vtk_obj.GetElectronDensity())
    def _set_electron_density(self, arg):
        old_val = self._get_electron_density()
        self._wrap_call(self._vtk_obj.SetElectronDensity,
                        deref_vtk(arg))
        self.trait_property_changed('electron_density', old_val, arg)
    electron_density = traits.Property(_get_electron_density, _set_electron_density, help=\
        """
        Get/Set the ImageData for the molecule's electron density.
        """
    )

    def get_mo(self, *args):
        """
        V.get_mo(int) -> ImageData
        C++: virtual ImageData *GetMO(IdType orbitalNumber)
        Get/Set the ImageData for the requested molecular orbital.
        """
        ret = self._wrap_call(self._vtk_obj.GetMO, *args)
        return wrap_vtk(ret)

    def set_mo(self, *args):
        """
        V.set_mo(int, ImageData)
        C++: void SetMO(IdType orbitalNumber, ImageData *data)
        Get/Set the ImageData for the requested molecular orbital.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetMO, *my_args)
        return ret

    number_of_electrons = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of electrons in the molecule. Needed for
        HOMO/LUMO convenience functions
        """
    )

    def _number_of_electrons_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfElectrons,
                        self.number_of_electrons)

    number_of_m_os = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Get/Set the number of molecular orbitals. Setting this will
        resize this internal array of MOs.
        """
    )

    def _number_of_m_os_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfMOs,
                        self.number_of_m_os)

    padding = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the padding around the molecule to which the cube
        extends. This is used to determine the dataset bounds.
        """
    )

    def _padding_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPadding,
                        self.padding)

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_electrons', 'GetNumberOfElectrons'), ('number_of_m_os',
    'GetNumberOfMOs'), ('padding', 'GetPadding'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'number_of_electrons', 'number_of_m_os', 'padding'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProgrammableElectronicData, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProgrammableElectronicData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['number_of_electrons',
            'number_of_m_os', 'padding']),
            title='Edit ProgrammableElectronicData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProgrammableElectronicData properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

