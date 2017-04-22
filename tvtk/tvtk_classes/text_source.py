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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class TextSource(PolyDataAlgorithm):
    """
    TextSource - create polygonal text
    
    Superclass: PolyDataAlgorithm
    
    TextSource converts a text string into polygons.  This way you can
    insert text into your renderings. It uses the 9x15 font from X
    Windows. You can specify if you want the background to be drawn or
    not. The characters are formed by scan converting the raster font
    into quadrilaterals. Colors are assigned to the letters using scalar
    data. To set the color of the characters with the source's actor
    property, set backing_off on the text source and scalar_visibility_off
    on the associated PolyDataMapper. Then, the color can be set using
    the associated actor's property.
    
    VectorText generates higher quality polygonal representations of
    characters.
    
    @sa
    VectorText
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextSource, obj, update, **traits)
    
    backing = tvtk_base.true_bool_trait(help=\
        """
        Controls whether or not a background is drawn with the text.
        """
    )

    def _backing_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBacking,
                        self.backing_)

    background_color = tvtk_base.vtk_color_trait((0.0, 0.0, 0.0), help=\
        """
        
        """
    )

    def _background_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBackgroundColor,
                        self.background_color, False)

    foreground_color = tvtk_base.vtk_color_trait((1.0, 1.0, 1.0), help=\
        """
        
        """
    )

    def _foreground_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetForegroundColor,
                        self.foreground_color, False)

    output_points_precision = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get the desired precision for the output points.
        Algorithm::SINGLE_PRECISION - Output single-precision floating
        point. Algorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

    text = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        Set/Get the text to be drawn.
        """
    )

    def _text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetText,
                        self.text)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    (('backing', 'GetBacking'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('background_color', 'GetBackgroundColor'), ('foreground_color',
    'GetForegroundColor'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('text', 'GetText'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'backing', 'debug', 'global_warning_display',
    'release_data_flag', 'background_color', 'foreground_color',
    'output_points_precision', 'progress_text', 'text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['backing'], [], ['background_color', 'foreground_color',
            'output_points_precision', 'text']),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

