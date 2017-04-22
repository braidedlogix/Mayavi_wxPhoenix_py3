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

from tvtk.tvtk_classes.camera import Camera


class OpenGLCamera(Camera):
    """
    OpenGLCamera - open_gl camera
    
    Superclass: Camera
    
    OpenGLCamera is a concrete implementation of the abstract class
    Camera.  OpenGLCamera interfaces to the open_gl rendering
    library.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLCamera, obj, update, **traits)
    
    _updateable_traits_ = \
    (('parallel_projection', 'GetParallelProjection'),
    ('use_horizontal_view_angle', 'GetUseHorizontalViewAngle'),
    ('use_off_axis_projection', 'GetUseOffAxisProjection'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('clipping_range', 'GetClippingRange'), ('distance', 'GetDistance'),
    ('eye_angle', 'GetEyeAngle'), ('eye_separation', 'GetEyeSeparation'),
    ('focal_disk', 'GetFocalDisk'), ('focal_point', 'GetFocalPoint'),
    ('freeze_focal_point', 'GetFreezeFocalPoint'), ('left_eye',
    'GetLeftEye'), ('parallel_scale', 'GetParallelScale'), ('position',
    'GetPosition'), ('screen_bottom_left', 'GetScreenBottomLeft'),
    ('screen_bottom_right', 'GetScreenBottomRight'), ('screen_top_right',
    'GetScreenTopRight'), ('thickness', 'GetThickness'), ('use_scissor',
    'GetUseScissor'), ('view_angle', 'GetViewAngle'), ('view_shear',
    'GetViewShear'), ('view_up', 'GetViewUp'), ('window_center',
    'GetWindowCenter'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'parallel_projection',
    'use_horizontal_view_angle', 'use_off_axis_projection',
    'clipping_range', 'distance', 'eye_angle', 'eye_separation',
    'focal_disk', 'focal_point', 'freeze_focal_point', 'left_eye',
    'parallel_scale', 'position', 'screen_bottom_left',
    'screen_bottom_right', 'screen_top_right', 'thickness', 'use_scissor',
    'view_angle', 'view_shear', 'view_up', 'window_center'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLCamera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['parallel_projection', 'use_horizontal_view_angle',
            'use_off_axis_projection'], [], ['clipping_range', 'distance',
            'eye_angle', 'eye_separation', 'focal_disk', 'focal_point',
            'freeze_focal_point', 'left_eye', 'parallel_scale', 'position',
            'screen_bottom_left', 'screen_bottom_right', 'screen_top_right',
            'thickness', 'use_scissor', 'view_angle', 'view_shear', 'view_up',
            'window_center']),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLCamera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

