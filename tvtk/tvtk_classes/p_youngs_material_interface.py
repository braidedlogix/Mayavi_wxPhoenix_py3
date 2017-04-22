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

from tvtk.tvtk_classes.youngs_material_interface import YoungsMaterialInterface


class PYoungsMaterialInterface(YoungsMaterialInterface):
    """
    PYoungsMaterialInterface - parallel reconstruction of material
    interfaces
    
    Superclass: YoungsMaterialInterface
    
    This is a subclass of YoungsMaterialInterface, implementing the
    reconstruction of material interfaces, for parallel data sets
    
    @par Thanks: This file is part of the generalized Youngs material
    interface reconstruction algorithm contributed by
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Implementation by Thierry Carrard and Philippe Pebay
    
    @sa
    YoungsMaterialInterface
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPYoungsMaterialInterface, obj, update, **traits)
    
    def _get_controller(self):
        return wrap_vtk(self._vtk_obj.GetController())
    def _set_controller(self, arg):
        old_val = self._get_controller()
        self._wrap_call(self._vtk_obj.SetController,
                        deref_vtk(arg))
        self.trait_property_changed('controller', old_val, arg)
    controller = traits.Property(_get_controller, _set_controller, help=\
        """
        Get/Set the multiprocess controller. If no controller is set,
        single process is assumed.
        """
    )

    def aggregate(self, *args):
        """
        V.aggregate(int, [int, ...])
        C++: virtual void Aggregate(int, int *)
        Parallel implementation of the material aggregation.
        """
        ret = self._wrap_call(self._vtk_obj.Aggregate, *args)
        return ret

    _updateable_traits_ = \
    (('axis_symetric', 'GetAxisSymetric'), ('fill_material',
    'GetFillMaterial'), ('inverse_normal', 'GetInverseNormal'),
    ('onion_peel', 'GetOnionPeel'), ('reverse_material_order',
    'GetReverseMaterialOrder'), ('use_all_blocks', 'GetUseAllBlocks'),
    ('use_fraction_as_distance', 'GetUseFractionAsDistance'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_materials', 'GetNumberOfMaterials'),
    ('volume_fraction_range', 'GetVolumeFractionRange'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'axis_symetric', 'debug', 'fill_material',
    'global_warning_display', 'inverse_normal', 'onion_peel',
    'release_data_flag', 'reverse_material_order', 'use_all_blocks',
    'use_fraction_as_distance', 'number_of_materials', 'progress_text',
    'volume_fraction_range'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PYoungsMaterialInterface, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PYoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['axis_symetric', 'fill_material', 'inverse_normal',
            'onion_peel', 'reverse_material_order', 'use_all_blocks',
            'use_fraction_as_distance'], [], ['number_of_materials',
            'volume_fraction_range']),
            title='Edit PYoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PYoungsMaterialInterface properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

