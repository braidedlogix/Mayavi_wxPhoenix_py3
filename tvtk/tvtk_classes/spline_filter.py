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


class SplineFilter(PolyDataAlgorithm):
    """
    SplineFilter - generate uniformly subdivided polylines from a set
    of input polyline using a Spline
    
    Superclass: PolyDataAlgorithm
    
    SplineFilter is a filter that generates an output polylines from
    an input set of polylines. The polylines are uniformly subdivided and
    produced with the help of a Spline class that the user can specify
    (by default a CardinalSpline is used). The number of subdivisions
    of the line can be controlled in several ways. The user can either
    specify the number of subdivisions or a length of each subdivision
    can be provided (and the class will figure out how many subdivisions
    is required over the whole polyline). The maximum number of
    subdivisions can also be set.
    
    The output of this filter is a polyline per input polyline (or line).
    New points and texture coordinates are created. Point data is
    interpolated and cell data passed on. Any polylines with less than
    two points, or who have coincident points, are ignored.
    
    @sa
    RibbonFilter TubeFilter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSplineFilter, obj, update, **traits)
    
    generate_t_coords = traits.Trait('normalized_length',
    tvtk_base.TraitRevPrefixMap({'normalized_length': 1, 'off': 0, 'use_length': 2, 'use_scalars': 3}), help=\
        """
        Control whether and how texture coordinates are produced. This is
        useful for striping the output polyline. The texture coordinates
        can be generated in three ways: a normalized (0,1) generation;
        based on the length (divided by the texture length); and by using
        the input scalar values.
        """
    )

    def _generate_t_coords_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateTCoords,
                        self.generate_t_coords_)

    subdivide = traits.Trait('specified',
    tvtk_base.TraitRevPrefixMap({'specified': 0, 'length': 1}), help=\
        """
        Specify how the number of subdivisions is determined.
        """
    )

    def _subdivide_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSubdivide,
                        self.subdivide_)

    length = traits.Trait(0.1, traits.Range(1e-07, 1e+299, enter_set=True, auto_set=False), help=\
        """
        Control the number of subdivisions that are created for the
        polyline based on an absolute length. The length of the spline is
        divided by this length to determine the number of subdivisions.
        """
    )

    def _length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLength,
                        self.length)

    maximum_number_of_subdivisions = traits.Trait(2147483647, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the maximum number of subdivisions that are created for each
        polyline.
        """
    )

    def _maximum_number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaximumNumberOfSubdivisions,
                        self.maximum_number_of_subdivisions)

    number_of_subdivisions = traits.Trait(100, traits.Range(1, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Set the number of subdivisions that are created for the polyline.
        This method only has effect if Subdivisions is set to
        set_subdivisions_to_specify().
        """
    )

    def _number_of_subdivisions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfSubdivisions,
                        self.number_of_subdivisions)

    def _get_spline(self):
        return wrap_vtk(self._vtk_obj.GetSpline())
    def _set_spline(self, arg):
        old_val = self._get_spline()
        self._wrap_call(self._vtk_obj.SetSpline,
                        deref_vtk(arg))
        self.trait_property_changed('spline', old_val, arg)
    spline = traits.Property(_get_spline, _set_spline, help=\
        """
        Specify an instance of Spline to use to perform the
        interpolation.
        """
    )

    texture_length = traits.Trait(1.0, traits.Range(1e-06, 2147483647.0, enter_set=True, auto_set=False), help=\
        """
        Control the conversion of units during the texture coordinates
        calculation. The texture_length indicates what length (whether
        calculated from scalars or length) is mapped to the [0,1) texture
        space.
        """
    )

    def _texture_length_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTextureLength,
                        self.texture_length)

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
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('generate_t_coords', 'GetGenerateTCoords'), ('subdivide',
    'GetSubdivide'), ('length', 'GetLength'),
    ('maximum_number_of_subdivisions', 'GetMaximumNumberOfSubdivisions'),
    ('number_of_subdivisions', 'GetNumberOfSubdivisions'),
    ('texture_length', 'GetTextureLength'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'generate_t_coords', 'subdivide', 'length',
    'maximum_number_of_subdivisions', 'number_of_subdivisions',
    'progress_text', 'texture_length'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SplineFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SplineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['generate_t_coords', 'subdivide'], ['length',
            'maximum_number_of_subdivisions', 'number_of_subdivisions',
            'texture_length']),
            title='Edit SplineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SplineFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

