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


class ImageClip(ImageAlgorithm):
    """
    ImageClip - Reduces the image extent of the input.
    
    Superclass: ImageAlgorithm
    
    ImageClip  will make an image smaller.  The output must have an
    image extent which is the subset of the input.  The filter has two
    modes of operation: 1: By default, the data is not copied in this
    filter. Only the whole extent is modified. 2: If clip_data_on is set,
    then you will get no more that the clipped extent.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageClip, obj, update, **traits)
    
    clip_data = tvtk_base.false_bool_trait(help=\
        """
        By default, clip_data is off, and only the whole_extent is
        modified. the data's extent may actually be larger.  When this
        flag is on, the data extent will be no more than the
        output_whole_extent.
        """
    )

    def _clip_data_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClipData,
                        self.clip_data_)

    output_whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(-2147483647, 2147483647, -2147483647, 2147483647, -2147483647, 2147483647), cols=3, help=\
        """
        The whole extent of the output has to be set explicitly.
        """
    )

    def _output_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputWholeExtent,
                        self.output_whole_extent)

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

    def reset_output_whole_extent(self):
        """
        V.reset_output_whole_extent()
        C++: void ResetOutputWholeExtent()"""
        ret = self._vtk_obj.ResetOutputWholeExtent()
        return ret
        

    _updateable_traits_ = \
    (('clip_data', 'GetClipData'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_whole_extent', 'GetOutputWholeExtent'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clip_data', 'debug', 'global_warning_display',
    'release_data_flag', 'output_whole_extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageClip, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['clip_data'], [], ['output_whole_extent']),
            title='Edit ImageClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageClip properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

