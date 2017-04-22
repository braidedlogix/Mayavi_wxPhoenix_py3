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

from tvtk.tvtk_classes.point_cloud_filter import PointCloudFilter


class FitImplicitFunction(PointCloudFilter):
    """
    FitImplicitFunction - extract points on the surface of an implicit
    function
    
    Superclass: PointCloudFilter
    
    FitImplicitFunction extract points that are on the surface of an
    implicit function (within some threshold). Implicit functions in VTK
    are any function of the form f(x,y,z)=c, where values c==0 are
    considered the surface of the implicit function. Typical examples of
    implicit functions include planes, spheres, cylinders, cones, etc.
    plus boolean combinations of these functions. In this implementation,
    a threshold is used to create a fuzzy region considered "on" the
    surface. In essence, this is a very poor man's RANSAC algorithm,
    where the user picks a function on which to fit some points. Thus it
    is possible to use this filter to define a proposed model and place
    it into an optimization loop to best fit it to a set of points.
    
    Note that while any PointSet type can be provided as input, the
    output is represented by an explicit representation of points via a
    PolyData. This output polydata will populate its instance of
    Points, but no cells will be defined (i.e., no Vertex or
    PolyVertex are contained in the output). Also, after filter
    execution, the user can request a IdType* map which indicates how
    the input points were mapped to the output. A value of map[i] (where
    i is the ith input point) less than 0 means that the ith input point
    was removed. (See also the superclass documentation for accessing the
    removed points through the filter's second output.)
    
    @warning
    This class has been threaded with SMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    PointCloudFilter ExtractPoints ImplicitFunction
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFitImplicitFunction, obj, update, **traits)
    
    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function defining a surface on which points
        are to be extracted.
        """
    )

    threshold = traits.Trait(0.01, traits.Range(0.0, 9.999999680285692e+37, enter_set=True, auto_set=False), help=\
        """
        Specify a threshold value which defines a fuzzy extraction
        surface. Since in this filter the implicit surface is defined as
        f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) <
        Threshold).
        """
    )

    def _threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThreshold,
                        self.threshold)

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
    (('generate_outliers', 'GetGenerateOutliers'), ('generate_vertices',
    'GetGenerateVertices'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('threshold',
    'GetThreshold'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_outliers', 'generate_vertices',
    'global_warning_display', 'release_data_flag', 'progress_text',
    'threshold'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FitImplicitFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FitImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_outliers', 'generate_vertices'], [], ['threshold']),
            title='Edit FitImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FitImplicitFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

