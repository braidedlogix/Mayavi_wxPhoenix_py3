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


class PointLoad(ImageAlgorithm):
    """
    PointLoad - compute stress tensors given point load on
    semi-infinite domain
    
    Superclass: ImageAlgorithm
    
    PointLoad is a source object that computes stress tensors on a
    volume. The tensors are computed from the application of a point load
    on a semi-infinite domain. (The analytical results are adapted from
    Saada - see text.) It also is possible to compute effective stress
    scalars if desired. This object serves as a specialized data
    generator for some of the examples in the text.
    
    @sa
    TensorGlyph, HyperStreamline
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPointLoad, obj, update, **traits)
    
    compute_effective_stress = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off computation of effective stress scalar. These methods
        do nothing. The effective stress is always computed.
        """
    )

    def _compute_effective_stress_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeEffectiveStress,
                        self.compute_effective_stress_)

    load_value = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get value of applied load.
        """
    )

    def _load_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLoadValue,
                        self.load_value)

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    poissons_ratio = traits.Float(0.3, enter_set=True, auto_set=False, help=\
        """
        Set/Get Poisson's ratio.
        """
    )

    def _poissons_ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPoissonsRatio,
                        self.poissons_ratio)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        Specify the dimensions of the volume. A stress tensor will be
        computed for each point in the volume.
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

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
    (('compute_effective_stress', 'GetComputeEffectiveStress'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('load_value',
    'GetLoadValue'), ('model_bounds', 'GetModelBounds'),
    ('poissons_ratio', 'GetPoissonsRatio'), ('sample_dimensions',
    'GetSampleDimensions'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_effective_stress', 'debug',
    'global_warning_display', 'release_data_flag', 'load_value',
    'model_bounds', 'poissons_ratio', 'progress_text',
    'sample_dimensions'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(PointLoad, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_effective_stress'], [], ['load_value', 'model_bounds',
            'poissons_ratio', 'sample_dimensions']),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit PointLoad properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

