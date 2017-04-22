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

from tvtk.tvtk_classes.algorithm import Algorithm


class TrivialProducer(Algorithm):
    """
    TrivialProducer - Producer for stand-alone data objects.
    
    Superclass: Algorithm
    
    TrivialProducer allows stand-alone data objects to be connected as
    inputs in a pipeline.  All data objects that are connected to a
    pipeline involving Algorithm must have a producer.  This trivial
    producer allows data objects that are hand-constructed in a program
    without another vtk producer to be connected.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTrivialProducer, obj, update, **traits)
    
    whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        
        """
    )

    def _whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWholeExtent,
                        self.whole_extent)

    def fill_output_data_information(self, *args):
        """
        V.fill_output_data_information(DataObject, Information)
        C++: static void FillOutputDataInformation(DataObject *output,
            Information *outInfo)
        This method can be used to copy meta-data from an existing data
        object to an information object. For example, whole extent, image
        data spacing, origin etc.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillOutputDataInformation, *my_args)
        return ret

    def set_output(self, *args):
        """
        V.set_output(DataObject)
        C++: virtual void SetOutput(DataObject *output)
        Set the data object that is "produced" by this producer.  It is
        never really modified.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetOutput, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('whole_extent', 'GetWholeExtent'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'progress_text', 'whole_extent'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TrivialProducer, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TrivialProducer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['whole_extent']),
            title='Edit TrivialProducer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TrivialProducer properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

