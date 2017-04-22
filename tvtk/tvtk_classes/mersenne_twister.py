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

from tvtk.tvtk_classes.random_sequence import RandomSequence


class MersenneTwister(RandomSequence):
    """
    MersenneTwister - Generator for Mersenne Twister pseudorandom
    numbers
    
    Superclass: RandomSequence
    
    MersenneTwister is an implementation of the Mersenne Twister
    pseudorandom number generator. The VTK class is simply a wrapper
    around an implementation written by M. Matsumoto, T. Nishimura and M.
    Saito, whose source code can be found at
    http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/DC/dc.html.
    
    This implementation of the Mersenne Twister facilitates the
    generation and query from multiple independent pseudorandom
    sequences. Independent sequences are identified by a unique
    MersenneTwister::SequenceId, which is either generated upon
    request or passed into the initialization method. This id is factored
    into the initialization of the Mersenne Twister's initial state, so
    two sequences with the same seed and different sequence ids will
    produce different results. Once a sequence is initialized with an
    associated sequence id, this id is used to obtain values from the
    sequence.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMersenneTwister, obj, update, **traits)
    
    def initialize_new_sequence(self, *args):
        """
        V.initialize_new_sequence(int, int) -> int
        C++: SequenceId InitializeNewSequence(TypeUInt32 seed,
            int p=521)
        Initialize a new Mersenne Twister sequence, given a) a and b) a
        Mersenne exponent (p s.t. 2^p-1 is a Mersenne prime). If
        
        is not a usable Mersenne exponent, its value is used to pick one
        from a list. The return value is the id for the generated
        sequence, which is used as a key to access values of the
        sequence.
        """
        ret = self._wrap_call(self._vtk_obj.InitializeNewSequence, *args)
        return ret

    def initialize_sequence(self, *args):
        """
        V.initialize_sequence(int, int, int)
        C++: void InitializeSequence(SequenceId id, TypeUInt32 seed,
            int p=521)
        Initialize a sequence as in initialize_new_sequence(), but
        additionally pass an id to associate with the new sequence. If a
        sequence is already associated with this id, a warning is given
        and the sequence is reset using the given parameters.
        """
        ret = self._wrap_call(self._vtk_obj.InitializeSequence, *args)
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
            return super(MersenneTwister, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MersenneTwister properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit MersenneTwister properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MersenneTwister properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

