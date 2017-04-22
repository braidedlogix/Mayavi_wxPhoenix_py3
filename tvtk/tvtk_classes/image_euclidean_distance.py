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

from tvtk.tvtk_classes.image_decompose_filter import ImageDecomposeFilter


class ImageEuclideanDistance(ImageDecomposeFilter):
    """
    ImageEuclideanDistance - computes 3d Euclidean DT
    
    Superclass: ImageDecomposeFilter
    
    ImageEuclideanDistance implements the Euclidean DT using Saito's
    algorithm. The distance map produced contains the square of the
    Euclidean distance values.
    
    The algorithm has a o(n^(D+1)) complexity over nxnx...xn images in D
    dimensions. It is very efficient on relatively small images.
    Cuisenaire's algorithms should be used instead if n >> 500. These are
    not implemented yet.
    
    For the special case of images where the slice-size is a multiple of
    2^N with a large N (typically for 256x256 slices), Saito's algorithm
    encounters a lot of cache conflicts during the 3rd iteration which
    can slow it very significantly. In that case, one should use
    ::_set_algorithm_to_saito_cached() instead for better performance.
    
    References:
    
    T. Saito and J.I. Toriwaki. New algorithms for Euclidean distance
    transformations of an n-dimensional digitised picture with
    applications. Pattern Recognition, 27(11). pp. 1551--1565, 1994.
    
    O. Cuisenaire. Distance Transformation: fast algorithms and
    applications to medical image processing. ph_d Thesis, Universite
    catholique de Louvain, October 1999.
    http://ltswww.epfl.ch/~cuisenai/papers/oc_thesis.pdf
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageEuclideanDistance, obj, update, **traits)
    
    consider_anisotropy = tvtk_base.true_bool_trait(help=\
        """
        Used to define whether Spacing should be used in the computation
        of the distances
        """
    )

    def _consider_anisotropy_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetConsiderAnisotropy,
                        self.consider_anisotropy_)

    initialize = tvtk_base.true_bool_trait(help=\
        """
        Used to set all non-zero voxels to maximum_distance before
        starting the distance transformation. Setting Initialize off
        keeps the current value in the input image as starting point.
        This allows to superimpose several distance maps.
        """
    )

    def _initialize_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInitialize,
                        self.initialize_)

    algorithm = traits.Trait('saito',
    tvtk_base.TraitRevPrefixMap({'saito': 1, 'saito_cached': 0}), help=\
        """
        Selects a Euclidean DT algorithm.
        1. Saito
        2. Saito-cached More algorithms will be added later on.
        """
    )

    def _algorithm_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAlgorithm,
                        self.algorithm_)

    maximum_distance = traits.Float(2147483647.0, enter_set=True, auto_set=False, help=\
        """
        Any distance bigger than this->_maximum_distance will not ne
        computed but set to this->_maximum_distance instead.
        """
    )

    def _maximum_distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumDistance,
                        self.maximum_distance)

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
    (('consider_anisotropy', 'GetConsiderAnisotropy'), ('initialize',
    'GetInitialize'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('algorithm',
    'GetAlgorithm'), ('split_mode', 'GetSplitMode'), ('maximum_distance',
    'GetMaximumDistance'), ('dimensionality', 'GetDimensionality'),
    ('desired_bytes_per_piece', 'GetDesiredBytesPerPiece'), ('enable_smp',
    'GetEnableSMP'), ('global_default_enable_smp',
    'GetGlobalDefaultEnableSMP'), ('minimum_piece_size',
    'GetMinimumPieceSize'), ('number_of_threads', 'GetNumberOfThreads'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'consider_anisotropy', 'debug',
    'global_warning_display', 'initialize', 'release_data_flag',
    'algorithm', 'split_mode', 'desired_bytes_per_piece',
    'dimensionality', 'enable_smp', 'global_default_enable_smp',
    'maximum_distance', 'minimum_piece_size', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageEuclideanDistance, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['consider_anisotropy', 'initialize'], ['algorithm',
            'split_mode'], ['desired_bytes_per_piece', 'dimensionality',
            'enable_smp', 'global_default_enable_smp', 'maximum_distance',
            'minimum_piece_size', 'number_of_threads']),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageEuclideanDistance properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

