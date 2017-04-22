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

from tvtk.tvtk_classes.open_gl_buffer_object import OpenGLBufferObject


class OpenGLVertexBufferObject(OpenGLBufferObject):
    """
    OpenGLVertexBufferObject - no description provided.
    
    Superclass: OpenGLBufferObject
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLVertexBufferObject, obj, update, **traits)
    
    coord_scale = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        Get the shift and scale vectors computed by create_vbo; or set the
        values create_vbo and append_vbo will use. Note that the "Set"
        methods **must** be called before the first time that create_vbo
        or append_vbo is invoked and should never be called afterwards.
        
        The coord_shift_and_scale_method describes how the shift and scale
        vectors are obtained (or that they should never be used). The
        get_coord_shift_and_scale_enabled() method returns true if a shift and
        scale are currently being applied (or false if not).
        
        The "Get" methods are used by the mapper to modify the world and
        camera transformation matrices to match the scaling applied to
        coordinates in the VBO. create_vbo only applies a shift and scale
        when the midpoint of the point bounding-box is distant from the
        origin by a factor of 10,000 or more relative to the size of the
        box along any axis.
        
        For example, if the x coordinates of the points range from
        200,000 to 200,001 then the factor is 200,000.5 / (200,001 -
        200,000) = 2x10^5, which is larger than 10,000 -- so the
        coordinates will be shifted and scaled.
        
        This is important as many open_gl drivers use reduced precision to
        hold point coordinates.
        
        These methods are used by the mapper to determine the additional
        transform (if any) to apply to the rendering transform.
        """
    )

    def _coord_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordScale,
                        self.coord_scale)

    coord_shift = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Get the shift and scale vectors computed by create_vbo; or set the
        values create_vbo and append_vbo will use. Note that the "Set"
        methods **must** be called before the first time that create_vbo
        or append_vbo is invoked and should never be called afterwards.
        
        The coord_shift_and_scale_method describes how the shift and scale
        vectors are obtained (or that they should never be used). The
        get_coord_shift_and_scale_enabled() method returns true if a shift and
        scale are currently being applied (or false if not).
        
        The "Get" methods are used by the mapper to modify the world and
        camera transformation matrices to match the scaling applied to
        coordinates in the VBO. create_vbo only applies a shift and scale
        when the midpoint of the point bounding-box is distant from the
        origin by a factor of 10,000 or more relative to the size of the
        box along any axis.
        
        For example, if the x coordinates of the points range from
        200,000 to 200,001 then the factor is 200,000.5 / (200,001 -
        200,000) = 2x10^5, which is larger than 10,000 -- so the
        coordinates will be shifted and scaled.
        
        This is important as many open_gl drivers use reduced precision to
        hold point coordinates.
        
        These methods are used by the mapper to determine the additional
        transform (if any) to apply to the rendering transform.
        """
    )

    def _coord_shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCoordShift,
                        self.coord_shift)

    def _get_coord_shift_and_scale_enabled(self):
        return self._vtk_obj.GetCoordShiftAndScaleEnabled()
    coord_shift_and_scale_enabled = traits.Property(_get_coord_shift_and_scale_enabled, help=\
        """
        Get the shift and scale vectors computed by create_vbo; or set the
        values create_vbo and append_vbo will use. Note that the "Set"
        methods **must** be called before the first time that create_vbo
        or append_vbo is invoked and should never be called afterwards.
        
        The coord_shift_and_scale_method describes how the shift and scale
        vectors are obtained (or that they should never be used). The
        get_coord_shift_and_scale_enabled() method returns true if a shift and
        scale are currently being applied (or false if not).
        
        The "Get" methods are used by the mapper to modify the world and
        camera transformation matrices to match the scaling applied to
        coordinates in the VBO. create_vbo only applies a shift and scale
        when the midpoint of the point bounding-box is distant from the
        origin by a factor of 10,000 or more relative to the size of the
        box along any axis.
        
        For example, if the x coordinates of the points range from
        200,000 to 200,001 then the factor is 200,000.5 / (200,001 -
        200,000) = 2x10^5, which is larger than 10,000 -- so the
        coordinates will be shifted and scaled.
        
        This is important as many open_gl drivers use reduced precision to
        hold point coordinates.
        
        These methods are used by the mapper to determine the additional
        transform (if any) to apply to the rendering transform.
        """
    )

    def append_vbo(self, *args):
        """
        V.append_vbo(Points, int, DataArray, DataArray, [int,
            ...], int)
        C++: void AppendVBO(Points *points, unsigned int numPoints,
            DataArray *normals, DataArray *tcoords,
            unsigned char *colors, int colorComponents)"""
        my_args = deref_array(args, [('vtkPoints', 'int', 'vtkDataArray', 'vtkDataArray', ['int', Ellipsis], 'int')])
        ret = self._wrap_call(self._vtk_obj.AppendVBO, *my_args)
        return ret

    def create_vbo(self, *args):
        """
        V.create_vbo(Points, int, DataArray, DataArray, [int,
            ...], int)
        C++: void CreateVBO(Points *points, unsigned int numPoints,
            DataArray *normals, DataArray *tcoords,
            unsigned char *colors, int colorComponents)"""
        my_args = deref_array(args, [('vtkPoints', 'int', 'vtkDataArray', 'vtkDataArray', ['int', Ellipsis], 'int')])
        ret = self._wrap_call(self._vtk_obj.CreateVBO, *my_args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('coord_scale', 'GetCoordScale'),
    ('coord_shift', 'GetCoordShift'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'coord_scale', 'coord_shift'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLVertexBufferObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLVertexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['coord_scale', 'coord_shift']),
            title='Edit OpenGLVertexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLVertexBufferObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

