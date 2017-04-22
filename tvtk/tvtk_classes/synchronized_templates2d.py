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


class SynchronizedTemplates2D(PolyDataAlgorithm):
    """
    SynchronizedTemplates2D - generate isoline(s) from a structured
    points set
    
    Superclass: PolyDataAlgorithm
    
    SynchronizedTemplates2D is a 2d implementation of the synchronized
    template algorithm. Note that ContourFilter will automatically use
    this class when appropriate.
    
    @warning
    This filter is specialized to 2d images.
    
    @sa
    ContourFilter SynchronizedTemplates3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSynchronizedTemplates2D, obj, update, **traits)
    
    compute_scalars = tvtk_base.true_bool_trait(help=\
        """
        Option to set the point scalars of the output.  The scalars will
        be the iso value of course.  By default this flag is on.
        """
    )

    def _compute_scalars_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeScalars,
                        self.compute_scalars_)

    array_component = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/get which component of the scalar array to contour on;
        defaults to 0.
        """
    )

    def _array_component_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayComponent,
                        self.array_component)

    number_of_contours = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of contours to place into the list. You only
        really need to use this method to reduce list size. The method
        set_value() will automatically increase list size as needed.
        """
    )

    def _number_of_contours_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfContours,
                        self.number_of_contours)

    def get_value(self, *args):
        """
        V.get_value(int) -> float
        C++: double GetValue(int i)
        Get the ith contour value.
        """
        ret = self._wrap_call(self._vtk_obj.GetValue, *args)
        return ret

    def set_value(self, *args):
        """
        V.set_value(int, float)
        C++: void SetValue(int i, double value)
        Set a particular contour value at contour number i. The index i
        ranges between 0<=i<_number_of_contours.
        """
        ret = self._wrap_call(self._vtk_obj.SetValue, *args)
        return ret

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

    def _get_values(self):
        return self._vtk_obj.GetValues()
    values = traits.Property(_get_values, help=\
        """
        Get a pointer to an array of contour values. There will be
        get_number_of_contours() values in the list.
        """
    )

    def generate_values(self, *args):
        """
        V.generate_values(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.generate_values(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        Generate num_contours equally spaced contour values between
        specified range. Contour values will include min/max range
        values.
        """
        ret = self._wrap_call(self._vtk_obj.GenerateValues, *args)
        return ret

    _updateable_traits_ = \
    (('compute_scalars', 'GetComputeScalars'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('array_component', 'GetArrayComponent'),
    ('number_of_contours', 'GetNumberOfContours'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_scalars', 'debug',
    'global_warning_display', 'release_data_flag', 'array_component',
    'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SynchronizedTemplates2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SynchronizedTemplates2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_scalars'], [], ['array_component',
            'number_of_contours']),
            title='Edit SynchronizedTemplates2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SynchronizedTemplates2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

