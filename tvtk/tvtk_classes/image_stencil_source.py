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

from tvtk.tvtk_classes.image_stencil_algorithm import ImageStencilAlgorithm


class ImageStencilSource(ImageStencilAlgorithm):
    """
    ImageStencilSource - generate an image stencil
    
    Superclass: ImageStencilAlgorithm
    
    ImageStencilSource is a superclass for filters that generate image
    stencils.  Given a clipping object such as a ImplicitFunction, it
    will set up a list of clipping extents for each x-row through the
    image data.  The extents for each x-row can be retrieved via the
    get_next_extent() method after the extent lists have been built with
    the build_extents() method.  For large images, using clipping extents
    is much more memory efficient (and slightly more time-efficient) than
    building a mask.  This class can be subclassed to allow clipping with
    objects other than ImplicitFunction.
    @sa
    ImplicitFunction ImageStencil PolyDataToImageStencil
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageStencilSource, obj, update, **traits)
    
    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    def _set_information_input(self, arg):
        old_val = self._get_information_input()
        self._wrap_call(self._vtk_obj.SetInformationInput,
                        deref_vtk(arg))
        self.trait_property_changed('information_input', old_val, arg)
    information_input = traits.Property(_get_information_input, _set_information_input, help=\
        """
        Set a ImageData that has the Spacing, Origin, and whole_extent
        that will be used for the stencil.  This input should be set to
        the image that you wish to apply the stencil to.  If you use this
        method, then any values set with the set_output_spacing,
        set_output_origin, and set_output_whole_extent methods will be
        ignored.
        """
    )

    output_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    output_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    output_whole_extent = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=int, value=(0, -1, 0, -1, 0, -1), cols=3, help=\
        """
        
        """
    )

    def _output_whole_extent_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputWholeExtent,
                        self.output_whole_extent)

    def report_references(self, *args):
        """
        V.report_references(GarbageCollector)
        
        Report object referenced by instances of this class.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReportReferences, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('output_origin', 'GetOutputOrigin'), ('output_spacing',
    'GetOutputSpacing'), ('output_whole_extent', 'GetOutputWholeExtent'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageStencilSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['output_origin', 'output_spacing',
            'output_whole_extent']),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

