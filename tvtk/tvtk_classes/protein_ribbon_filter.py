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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class ProteinRibbonFilter(PolyDataAlgorithm):
    """
    ProteinRibbonFilter - generates protein ribbons
    
    Superclass: PolyDataAlgorithm
    
    ProteinRibbonFilter is a polydata algorithm that generates protein
    ribbons.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProteinRibbonFilter, obj, update, **traits)
    
    coil_width = traits.Float(0.30000001192092896, enter_set=True, auto_set=False, help=\
        """
        Width of the ribbon coil. Default is 0.3.
        """
    )

    def _coil_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoilWidth,
                        self.coil_width)

    draw_small_molecules_as_spheres = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        If enabled, small molecules (HETATMs) are drawn as spheres.
        Default is true.
        """
    )

    def _draw_small_molecules_as_spheres_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawSmallMoleculesAsSpheres,
                        self.draw_small_molecules_as_spheres)

    helix_width = traits.Float(1.2999999523162842, enter_set=True, auto_set=False, help=\
        """
        Width of the helix part of the ribbon. Default is 1.3.
        """
    )

    def _helix_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetHelixWidth,
                        self.helix_width)

    sphere_resolution = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Resolution of the spheres for small molecules. Default is 20.
        """
    )

    def _sphere_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSphereResolution,
                        self.sphere_resolution)

    subdivide_factor = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Smoothing factor of the ribbon. Default is 20.
        """
    )

    def _subdivide_factor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubdivideFactor,
                        self.subdivide_factor)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('coil_width',
    'GetCoilWidth'), ('draw_small_molecules_as_spheres',
    'GetDrawSmallMoleculesAsSpheres'), ('helix_width', 'GetHelixWidth'),
    ('sphere_resolution', 'GetSphereResolution'), ('subdivide_factor',
    'GetSubdivideFactor'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'coil_width', 'draw_small_molecules_as_spheres',
    'helix_width', 'progress_text', 'sphere_resolution',
    'subdivide_factor'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProteinRibbonFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProteinRibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['coil_width', 'draw_small_molecules_as_spheres',
            'helix_width', 'sphere_resolution', 'subdivide_factor']),
            title='Edit ProteinRibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProteinRibbonFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

