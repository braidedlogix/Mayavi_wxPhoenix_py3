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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class SurfaceReconstructionFilter(ImageAlgorithm):
    """
    SurfaceReconstructionFilter - reconstructs a surface from
    unorganized points
    
    Superclass: ImageAlgorithm
    
    SurfaceReconstructionFilter takes a list of points assumed to lie
    on the surface of a solid 3d object. A signed measure of the distance
    to the surface is computed and sampled on a regular grid. The grid
    can then be contoured at zero to extract the surface. The default
    values for neighborhood size and sample spacing should give
    reasonable results for most uses but can be set if desired. This
    procedure is based on the ph_d work of Hugues Hoppe:
    http://www.research.microsoft.com/~hoppe
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSurfaceReconstructionFilter, obj, update, **traits)
    
    neighborhood_size = traits.Int(20, enter_set=True, auto_set=False, help=\
        """
        Specify the number of neighbors each point has, used for
        estimating the local surface orientation.  The default value of
        20 should be OK for most applications, higher values can be
        specified if the spread of points is uneven. Values as low as 10
        may yield adequate results for some surfaces. Higher values cause
        the algorithm to take longer. Higher values will cause errors on
        sharp boundaries.
        """
    )

    def _neighborhood_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNeighborhoodSize,
                        self.neighborhood_size)

    sample_spacing = traits.Float(-1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the spacing of the 3d sampling grid. If not set, a
        reasonable guess will be made.
        """
    )

    def _sample_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleSpacing,
                        self.sample_spacing)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('neighborhood_size', 'GetNeighborhoodSize'), ('sample_spacing',
    'GetSampleSpacing'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'neighborhood_size', 'progress_text',
    'sample_spacing'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SurfaceReconstructionFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SurfaceReconstructionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['neighborhood_size', 'sample_spacing']),
            title='Edit SurfaceReconstructionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SurfaceReconstructionFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

