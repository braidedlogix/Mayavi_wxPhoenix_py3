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

from tvtk.tvtk_classes.object import Object


class AxisExtended(Object):
    """
    AxisExtended - octree-based spatial search object to quickly
    locate cells
    
    Superclass: Object
    
    This implements the optimization based tick position calculating
    algorithm in the paper "An Extension of Wilkinson's Algorithm for
    Positioning Tick Labels on Axes" by Junstin Talbot, Sharon Lin and
    Pat Hanrahan
    
    @sa
    Axis
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAxisExtended, obj, update, **traits)
    
    desired_font_size = traits.Int(10, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _desired_font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDesiredFontSize,
                        self.desired_font_size)

    font_size = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get methods for variables
        """
    )

    def _font_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFontSize,
                        self.font_size)

    is_axis_vertical = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _is_axis_vertical_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIsAxisVertical,
                        self.is_axis_vertical)

    label_format = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _label_format_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelFormat,
                        self.label_format)

    orientation = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrientation,
                        self.orientation)

    precision = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrecision,
                        self.precision)

    def coverage(self, *args):
        """
        V.coverage(float, float, float, float) -> float
        C++: static double Coverage(double dmin, double dmax, double lmin,
             double lmax)
        This method makes the data range approximately same as the
        labeling range more preferable
        """
        ret = self._wrap_call(self._vtk_obj.Coverage, *args)
        return ret

    def coverage_max(self, *args):
        """
        V.coverage_max(float, float, float) -> float
        C++: static double CoverageMax(double dmin, double dmax,
            double span)
        This gives the maximum possible value of coverage given the step
        size
        """
        ret = self._wrap_call(self._vtk_obj.CoverageMax, *args)
        return ret

    def density(self, *args):
        """
        V.density(int, float, float, float, float, float) -> float
        C++: static double Density(int k, double m, double dmin,
            double dmax, double lmin, double lmax)
        This method return a value to make the density of the labels
        close to the user given value
        """
        ret = self._wrap_call(self._vtk_obj.Density, *args)
        return ret

    def density_max(self, *args):
        """
        V.density_max(int, float) -> float
        C++: static double DensityMax(int k, double m)
        Derives the maximum values for density given k (number of ticks)
        and m (user given)
        """
        ret = self._wrap_call(self._vtk_obj.DensityMax, *args)
        return ret

    def format_legibility_score(self, *args):
        """
        V.format_legibility_score(float, int) -> float
        C++: static double FormatLegibilityScore(double n, int format)
        This methods return the legibility score of different formats
        """
        ret = self._wrap_call(self._vtk_obj.FormatLegibilityScore, *args)
        return ret

    def format_string_length(self, *args):
        """
        V.format_string_length(int, float, int) -> int
        C++: static int FormatStringLength(int format, double n,
            int precision)
        This method returns the string length of different format
        notations.
        """
        ret = self._wrap_call(self._vtk_obj.FormatStringLength, *args)
        return ret

    def generate_extended_tick_labels(self, *args):
        """
        V.generate_extended_tick_labels(float, float, float, float)
            -> Vector3d
        C++: Vector3d GenerateExtendedTickLabels(double dmin,
            double dmax, double m, double scaling)
        This method implements the algorithm given in the paper The
        method return the minimum tick position, maximum tick position
        and the tick spacing
        """
        ret = self._wrap_call(self._vtk_obj.GenerateExtendedTickLabels, *args)
        return wrap_vtk(ret)

    def simplicity(self, *args):
        """
        V.simplicity(int, int, int, float, float, float) -> float
        C++: static double Simplicity(int qIndex, int qLength, int j,
            double lmin, double lmax, double lstep)
        This method return a value to make step sizes corresponding to
        low q and j values more preferable
        """
        ret = self._wrap_call(self._vtk_obj.Simplicity, *args)
        return ret

    def simplicity_max(self, *args):
        """
        V.simplicity_max(int, int, int) -> float
        C++: static double SimplicityMax(int qIndex, int qLength, int j)
        This method returns the maximum possible value of simplicity
        value given q and j
        """
        ret = self._wrap_call(self._vtk_obj.SimplicityMax, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('desired_font_size',
    'GetDesiredFontSize'), ('font_size', 'GetFontSize'),
    ('is_axis_vertical', 'GetIsAxisVertical'), ('label_format',
    'GetLabelFormat'), ('orientation', 'GetOrientation'), ('precision',
    'GetPrecision'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'desired_font_size', 'font_size',
    'is_axis_vertical', 'label_format', 'orientation', 'precision'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AxisExtended, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AxisExtended properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['desired_font_size', 'font_size', 'is_axis_vertical',
            'label_format', 'orientation', 'precision']),
            title='Edit AxisExtended properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AxisExtended properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

