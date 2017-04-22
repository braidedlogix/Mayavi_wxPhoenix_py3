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

from tvtk.tvtk_classes.hyper_octree_points_grabber import HyperOctreePointsGrabber


class HyperOctreeClipCutPointsGrabber(HyperOctreePointsGrabber):
    """
    HyperOctreeClipCutPointsGrabber - A concrete implementation of
    HyperOctreePointsGrabber used by ClipHyperOctree and
    HyperOctreeCutter.
    
    Superclass: HyperOctreePointsGrabber
    
    @sa
    HyperOctreeClipCut, HyperOctreeClipCutClipCutPointsGrabber,
    ClipHyperOctree, HyperOctreeClipCutCutter
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkHyperOctreeClipCutPointsGrabber, obj, update, **traits)
    
    dimension = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the dimension of the hyperoctree.
        \pre valid_dim: (dim==2 || dim==3)
        \post is_set: get_dimension()==dim
        """
    )

    def _dimension_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimension,
                        self.dimension)

    def _get_polygon(self):
        return wrap_vtk(self._vtk_obj.GetPolygon())
    polygon = traits.Property(_get_polygon, help=\
        """
        Return the polygon.
        """
    )

    def _get_triangulator(self):
        return wrap_vtk(self._vtk_obj.GetTriangulator())
    triangulator = traits.Property(_get_triangulator, help=\
        """
        Return the ordered triangulator.
        """
    )

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('dimension', 'GetDimension'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'dimension'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(HyperOctreeClipCutPointsGrabber, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dimension']),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit HyperOctreeClipCutPointsGrabber properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

