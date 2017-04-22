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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class LabelSizeCalculator(PassInputTypeAlgorithm):
    """
    LabelSizeCalculator - This filter takes an input dataset, an array
    to process (which must be a string array), and a text property.
    
    Superclass: PassInputTypeAlgorithm
    
    It creates a new output array (named "_label_size" by default) with 4
    components per tuple that contain the width, height, horizontal
    offset, and descender height (in that order) of each string in the
    array.
    
    Use the inherited select_input_array_to_process to indicate a string
    array. In no input array is specified, the first of the following
    that is a string array is used: point scalars, cell scalars, field
    scalars.
    
    The second input array to process is an array specifying the type of
    each label. Different label types may have different font properties.
    This array must be a IntArray. Any type that does not map to a
    font property that was set will be set to the type 0's type property.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLabelSizeCalculator, obj, update, **traits)
    
    dpi = traits.Int(72, enter_set=True, auto_set=False, help=\
        """
        Get/Set the DPI at which the labels are to be rendered. Defaults
        to 72.
        @sa Window::GetDPI()
        """
    )

    def _dpi_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDPI,
                        self.dpi)

    def get_font_property(self, *args):
        """
        V.get_font_property(int) -> TextProperty
        C++: virtual TextProperty *GetFontProperty(int type=0)
        Get/Set the font used compute label sizes. This defaults to
        "Arial" at 12 points. If type is provided, it refers to the type
        of the text label provided in the optional label type array. The
        default type is type 0.
        """
        ret = self._wrap_call(self._vtk_obj.GetFontProperty, *args)
        return wrap_vtk(ret)

    def set_font_property(self, *args):
        """
        V.set_font_property(TextProperty, int)
        C++: virtual void SetFontProperty(TextProperty *fontProp,
            int type=0)
        Get/Set the font used compute label sizes. This defaults to
        "Arial" at 12 points. If type is provided, it refers to the type
        of the text label provided in the optional label type array. The
        default type is type 0.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetFontProperty, *my_args)
        return ret

    label_size_array_name = traits.String('LabelSize', enter_set=True, auto_set=False, help=\
        """
        The name of the output array containing text label sizes This
        defaults to "_label_size"
        """
    )

    def _label_size_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelSizeArrayName,
                        self.label_size_array_name)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('dpi',
    'GetDPI'), ('label_size_array_name', 'GetLabelSizeArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dpi', 'label_size_array_name', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LabelSizeCalculator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LabelSizeCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dpi', 'label_size_array_name']),
            title='Edit LabelSizeCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LabelSizeCalculator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

