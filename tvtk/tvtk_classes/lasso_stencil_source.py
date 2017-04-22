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

from tvtk.tvtk_classes.image_stencil_source import ImageStencilSource


class LassoStencilSource(ImageStencilSource):
    """
    LassoStencilSource - Create a stencil from a contour
    
    Superclass: ImageStencilSource
    
    LassoStencilSource will create an image stencil from a set of
    points that define a contour.  Its output can be used with
    ImageStecil or other vtk classes that apply a stencil to an image.
    @sa
    ROIStencilSource PolyDataToImageStencil@par Thanks: Thanks to
    David Gobbi for contributing this class to VTK.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkLassoStencilSource, obj, update, **traits)
    
    shape = traits.Trait('polygon',
    tvtk_base.TraitRevPrefixMap({'polygon': 0, 'spline': 1}), help=\
        """
        The shape to use, default is "Polygon".  The spline is a cardinal
        spline.  Bezier splines are not yet supported.
        """
    )

    def _shape_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShape,
                        self.shape_)

    def _get_points(self):
        return wrap_vtk(self._vtk_obj.GetPoints())
    def _set_points(self, arg):
        old_val = self._get_points()
        my_arg = deref_array([arg], [['vtkPoints']])
        self._wrap_call(self._vtk_obj.SetPoints,
                        my_arg[0])
        self.trait_property_changed('points', old_val, arg)
    points = traits.Property(_get_points, _set_points, help=\
        """
        The points that make up the lassoo.  The loop does not have to be
        closed, the last point will automatically be connected to the
        first point by a straight line segment.
        """
    )

    slice_orientation = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        The slice orientation.  The default is 2, which is XY. Other
        values are 0, which is YZ, and 1, which is XZ.
        """
    )

    def _slice_orientation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSliceOrientation,
                        self.slice_orientation)

    def get_slice_points(self, *args):
        """
        V.get_slice_points(int) -> Points
        C++: virtual Points *GetSlicePoints(int i)
        The points for a particular slice.  This will override the points
        that were set by calling set_points() for the slice. To clear the
        setting, call set_slice_points(slice, NULL).
        """
        ret = self._wrap_call(self._vtk_obj.GetSlicePoints, *args)
        return wrap_vtk(ret)

    def set_slice_points(self, *args):
        """
        V.set_slice_points(int, Points)
        C++: virtual void SetSlicePoints(int i, Points *points)
        The points for a particular slice.  This will override the points
        that were set by calling set_points() for the slice. To clear the
        setting, call set_slice_points(slice, NULL).
        """
        my_args = deref_array(args, [('int', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.SetSlicePoints, *my_args)
        return ret

    def remove_all_slice_points(self):
        """
        V.remove_all_slice_points()
        C++: virtual void RemoveAllSlicePoints()
        Remove points from all slices.
        """
        ret = self._vtk_obj.RemoveAllSlicePoints()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('shape',
    'GetShape'), ('slice_orientation', 'GetSliceOrientation'),
    ('output_origin', 'GetOutputOrigin'), ('output_spacing',
    'GetOutputSpacing'), ('output_whole_extent', 'GetOutputWholeExtent'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'shape', 'output_origin', 'output_spacing',
    'output_whole_extent', 'progress_text', 'slice_orientation'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(LassoStencilSource, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit LassoStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['shape'], ['output_origin', 'output_spacing',
            'output_whole_extent', 'slice_orientation']),
            title='Edit LassoStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit LassoStencilSource properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

