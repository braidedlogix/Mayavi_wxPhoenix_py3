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

from tvtk.tvtk_classes.molecule_to_poly_data_filter import MoleculeToPolyDataFilter


class MoleculeToAtomBallFilter(MoleculeToPolyDataFilter):
    """
    MoleculeToAtomBallFilter - Generate polydata with spheres
    representing atoms
    
    Superclass: MoleculeToPolyDataFilter
    
    This filter is used to generate one sphere for each atom in the input
    Molecule. Each sphere is centered at the atom center and can be
    scaled using either covalent or van der Waals radii. The point
    scalars of the output PolyData contains the atomic number of the
    appropriate atom for color mapping.
    
    ote Consider using the faster, simpler MoleculeMapper class,
    rather than generating polydata manually via these filters.
    
    @sa
    MoleculeMapper MoleculeToBondStickFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMoleculeToAtomBallFilter, obj, update, **traits)
    
    radius_scale = traits.Float(0.8, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _radius_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadiusScale,
                        self.radius_scale)

    radius_source = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _radius_source_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRadiusSource,
                        self.radius_source)

    resolution = traits.Int(50, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetResolution,
                        self.resolution)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('radius_scale', 'GetRadiusScale'), ('radius_source',
    'GetRadiusSource'), ('resolution', 'GetResolution'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'radius_scale', 'radius_source',
    'resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MoleculeToAtomBallFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MoleculeToAtomBallFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['radius_scale', 'radius_source', 'resolution']),
            title='Edit MoleculeToAtomBallFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MoleculeToAtomBallFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

