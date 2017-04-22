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


class ImageNoiseSource(ImageAlgorithm):
    """
    ImageNoiseSource - Create an image filled with noise.
    
    Superclass: ImageAlgorithm
    
    ImageNoiseSource just produces images filled with noise.  The only
    option now is uniform noise specified by a min and a max.  There is
    one major problem with this source. Every time it executes, it will
    output different pixel values.  This has important implications when
    a stream requests overlapping regions.  The same pixels will have
    different values on different updates.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageNoiseSource, obj, update, **traits)
    
    maximum = traits.Float(10.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum and maximum values for the generated noise.
        """
    )

    def _maximum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximum,
                        self.maximum)

    minimum = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the minimum and maximum values for the generated noise.
        """
    )

    def _minimum_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinimum,
                        self.minimum)

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

    def set_whole_extent(self, *args):
        """
        V.set_whole_extent(int, int, int, int, int, int)
        C++: void SetWholeExtent(int xMinx, int xMax, int yMin, int yMax,
            int zMin, int zMax)
        V.set_whole_extent((int, int, int, int, int, int))
        C++: void SetWholeExtent(const int ext[6])
        Set how large of an image to generate.
        """
        ret = self._wrap_call(self._vtk_obj.SetWholeExtent, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('maximum',
    'GetMaximum'), ('minimum', 'GetMinimum'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'maximum', 'minimum', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageNoiseSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['maximum', 'minimum']),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageNoiseSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

