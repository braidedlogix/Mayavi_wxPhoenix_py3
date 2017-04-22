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

from tvtk.tvtk_classes.point_locator import PointLocator


class MergePoints(PointLocator):
    """
    MergePoints - merge exactly coincident points
    
    Superclass: PointLocator
    
    MergePoints is a locator object to quickly locate points in 3d.
    The primary difference between MergePoints and its superclass
    PointLocator is that MergePoints merges precisely coincident
    points and is therefore much faster.
    @sa
    CleanPolyData
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMergePoints, obj, update, **traits)
    
    _updateable_traits_ = \
    (('automatic', 'GetAutomatic'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('divisions',
    'GetDivisions'), ('number_of_points_per_bucket',
    'GetNumberOfPointsPerBucket'), ('max_level', 'GetMaxLevel'),
    ('tolerance', 'GetTolerance'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['automatic', 'debug', 'global_warning_display', 'divisions',
    'max_level', 'number_of_points_per_bucket', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MergePoints, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit MergePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['automatic'], [], ['divisions', 'max_level',
            'number_of_points_per_bucket', 'tolerance']),
            title='Edit MergePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MergePoints properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

