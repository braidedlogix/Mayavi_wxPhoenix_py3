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


class ImageChangeInformation(ImageAlgorithm):
    """
    ImageChangeInformation - modify spacing, origin and extent.
    
    Superclass: ImageAlgorithm
    
    ImageChangeInformation  modify the spacing, origin, or extent of
    the data without changing the data itself.  The data is not resampled
    by this filter, only the information accompanying the data is
    modified.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageChangeInformation, obj, update, **traits)
    
    center_image = tvtk_base.false_bool_trait(help=\
        """
        Set the Origin of the output so that image coordinate (0,0,0)
        lies at the Center of the data set.  This will override
        set_output_origin.  This is often a useful operation to apply
        before using ImageReslice to apply a transformation to an
        image.
        """
    )

    def _center_image_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenterImage,
                        self.center_image_)

    extent_translation = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(0, 0, 0), cols=3, help=\
        """
        
        """
    )

    def _extent_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetExtentTranslation,
                        self.extent_translation)

    origin_scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _origin_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginScale,
                        self.origin_scale)

    origin_translation = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _origin_translation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOriginTranslation,
                        self.origin_translation)

    output_extent_start = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(2147483647, 2147483647, 2147483647), cols=3, help=\
        """
        
        """
    )

    def _output_extent_start_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputExtentStart,
                        self.output_extent_start)

    output_origin = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1e+299, 1e+299, 1e+299), cols=3, help=\
        """
        
        """
    )

    def _output_origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputOrigin,
                        self.output_origin)

    output_spacing = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1e+299, 1e+299, 1e+299), cols=3, help=\
        """
        
        """
    )

    def _output_spacing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputSpacing,
                        self.output_spacing)

    spacing_scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _spacing_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSpacingScale,
                        self.spacing_scale)

    def _get_information_input(self):
        return wrap_vtk(self._vtk_obj.GetInformationInput())
    information_input = traits.Property(_get_information_input, help=\
        """
        Copy the information from another data set.  By default, the
        information is copied from the input.
        """
    )

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

    def set_information_input_data(self, *args):
        """
        V.set_information_input_data(ImageData)
        C++: virtual void SetInformationInputData(ImageData *)
        Copy the information from another data set.  By default, the
        information is copied from the input.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInformationInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('center_image', 'GetCenterImage'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('extent_translation',
    'GetExtentTranslation'), ('origin_scale', 'GetOriginScale'),
    ('origin_translation', 'GetOriginTranslation'),
    ('output_extent_start', 'GetOutputExtentStart'), ('output_origin',
    'GetOutputOrigin'), ('output_spacing', 'GetOutputSpacing'),
    ('spacing_scale', 'GetSpacingScale'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'center_image', 'debug', 'global_warning_display',
    'release_data_flag', 'extent_translation', 'origin_scale',
    'origin_translation', 'output_extent_start', 'output_origin',
    'output_spacing', 'progress_text', 'spacing_scale'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageChangeInformation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['center_image'], [], ['extent_translation', 'origin_scale',
            'origin_translation', 'output_extent_start', 'output_origin',
            'output_spacing', 'spacing_scale']),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageChangeInformation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

