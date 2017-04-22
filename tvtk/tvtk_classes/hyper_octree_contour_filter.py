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


class HyperOctreeContourFilter(PolyDataAlgorithm):
    """
    HyperOctreeContourFilter - generate isosurfaces/isolines from
    scalar values
    
    Superclass: PolyDataAlgorithm
    
    ContourFilter is a filter that takes as input any dataset and
    generates on output isosurfaces and/or isolines. The exact form of
    the output depends upon the dimensionality of the input data. Data
    consisting of 3d cells will generate isosurfaces, data consisting of
    2d cells will generate isolines, and data with 1d or 0d cells will
    generate isopoints. Combinations of output type are possible if the
    input dimension is mixed.
    
    To use this filter you must specify one or more contour values. You
    can either use the method set_value() to specify each contour value,
    or use generate_values() to generate a series of evenly spaced
    contours. It is also possible to accelerate the operation of this
    filter (at the cost of extra memory) by using a ScalarTree. A
    scalar tree is used to quickly locate cells that contain a contour
    surface. This is especially effective if multiple contours are being
    extracted. If you want to use a scalar tree, invoke the method
    use_scalar_tree_on().
    
    @warning
    For unstructured data or structured grids, normals and gradients are
    not computed. Use PolyDataNormals to compute the surface normals.
    
    @sa
    MarchingContourFilter KitwareContourFilter MarchingCubes
    SliceCubes DividingCubes MarchingSquares
    ImageMarchingCubes
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeContourFilter, obj, update, **traits)
    
    def _get_locator(self):
        return wrap_vtk(self._vtk_obj.GetLocator())
    def _set_locator(self, arg):
        old_val = self._get_locator()
        self._wrap_call(self._vtk_obj.SetLocator,
                        deref_vtk(arg))
        self.trait_property_changed('locator', old_val, arg)
    locator = traits.Property(_get_locator, _set_locator, help=\
        """
        Set / get a spatial locator for merging points. By default, an
        instance of MergePoints is used.
        """
    )

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
        Methods to set / get contour values.
        
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

    def create_default_locator(self):
        """
        V.create_default_locator()
        C++: void CreateDefaultLocator()
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ret = self._vtk_obj.CreateDefaultLocator()
        return ret
        

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('number_of_contours', 'GetNumberOfContours'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'number_of_contours', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeContourFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['number_of_contours']),
            title='Edit HyperOctreeContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeContourFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

