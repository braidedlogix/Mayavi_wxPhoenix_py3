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


class TextureObject(Object):
    """
    TextureObject - abstracts an open_gl texture object.
    
    Superclass: Object
    
    TextureObject represents an open_gl texture object. It provides API
    to create textures using data already loaded into pixel buffer
    objects. It can also be used to create textures without uploading any
    data.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTextureObject, obj, update, **traits)
    
    auto_parameters = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Send all the texture object parameters to the hardware if not
        done yet. Parameters are automatically sent as a side affect of
        Bind. Disable this by setting auto_parameters 0.
        \pre is_bound: is_bound()
        """
    )

    def _auto_parameters_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAutoParameters,
                        self.auto_parameters)

    base_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Level of detail of the first texture image. A texture object is a
        list of texture images. It is a non-negative integer value.
        Initial value is 0, as in open_gl spec.
        """
    )

    def _base_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBaseLevel,
                        self.base_level)

    border_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _border_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderColor,
                        self.border_color)

    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. This does not increase the reference count
        of the context to avoid reference loops.
        
        * {
        * this->_texture_object = TextureObject::New();
        * }_set_context() may raise an error is the open_gl context does not
        support the
        * required open_gl extensions.
        """
    )

    def get_data_type(self, *args):
        """
        V.get_data_type(int) -> int
        C++: int GetDataType(int vtk_scalar_type)
        Get the data type for the texture as GLenum type.
        """
        ret = self._wrap_call(self._vtk_obj.GetDataType, *args)
        return ret

    def set_data_type(self, *args):
        """
        V.set_data_type(int)
        C++: void SetDataType(unsigned int glType)
        Get the data type for the texture as GLenum type.
        """
        ret = self._wrap_call(self._vtk_obj.SetDataType, *args)
        return ret

    depth_texture_compare = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Tells if the output of a texture unit with a depth texture uses
        comparison or not. Comparison happens between D_t the depth
        texture value in the range [0,1] and with R the interpolated
        third texture coordinate clamped to range [0,1]. The result of
        the comparison is noted `r'. If this flag is false, r=D_t.
        Initial value is false, as in open_gl spec. Ignored if the texture
        object is not a depth texture.
        """
    )

    def _depth_texture_compare_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthTextureCompare,
                        self.depth_texture_compare)

    depth_texture_compare_function = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        In case depth_texture_compare is true, specify the comparison
        function in use. The result of the comparison is noted `r'. Valid
        values are:
        - Value
        - Lequal: r=R<=Dt ? 1.0 : 0.0
        - Gequal: r=R>=Dt ? 1.0 : 0.0
        - Less: r=R<D_t ? 1.0 : 0.0
        - Greater: r=R>Dt ? 1.0 : 0.0
        - Equal: r=R==Dt ? 1.0 : 0.0
        - not_equal: r=R!=Dt ? 1.0 : 0.0
        - always_true: r=1.0
        - Never: r=0.0 If the magnification of minification factor are
          not nearest, percentage closer filtering (PCF) is used: R is
          compared to several D_t and r is the average of the comparisons
        (it is NOT the average of D_t compared once to R). Initial value
          is Lequal, as in open_gl spec. Ignored if the texture object is
          not a depth texture.
        """
    )

    def _depth_texture_compare_function_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDepthTextureCompareFunction,
                        self.depth_texture_compare_function)

    def get_format(self, *args):
        """
        V.get_format(int, int, bool) -> int
        C++: unsigned int GetFormat(int vtktype, int numComps,
            bool shaderSupportsTextureInt)
        Get/Set format (_open_gl internal format) that should be used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.GetFormat, *args)
        return ret

    def set_format(self, *args):
        """
        V.set_format(int)
        C++: void SetFormat(unsigned int glFormat)
        Get/Set format (_open_gl internal format) that should be used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.SetFormat, *args)
        return ret

    generate_mipmap = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Tells the hardware to generate mipmap textures from the first
        texture image at base_level. Initial value is false, as in open_gl
        spec.
        """
    )

    def _generate_mipmap_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateMipmap,
                        self.generate_mipmap)

    def get_internal_format(self, *args):
        """
        V.get_internal_format(int, int, bool) -> int
        C++: unsigned int GetInternalFormat(int vtktype, int numComps,
            bool shaderSupportsTextureInt)
        Get/Set internal format (_open_gl internal format) that should be
        used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.GetInternalFormat, *args)
        return ret

    def set_internal_format(self, *args):
        """
        V.set_internal_format(int)
        C++: void SetInternalFormat(unsigned int glInternalFormat)
        Get/Set internal format (_open_gl internal format) that should be
        used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.SetInternalFormat, *args)
        return ret

    linear_magnification = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Tells if the magnification mode is linear (true) or nearest
        (false). Initial value is false (initial value in open_gl spec is
        true).
        """
    )

    def _linear_magnification_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLinearMagnification,
                        self.linear_magnification)

    magnification_filter = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Magnification filter mode. Valid values are:
        - Nearest
        - Linear Initial value is Nearest
        """
    )

    def _magnification_filter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMagnificationFilter,
                        self.magnification_filter)

    max_lod = traits.Float(1000.0, enter_set=True, auto_set=False, help=\
        """
        Upper-clamp the computed LOD against this value. Any float value
        is valid. Initial value is 1000.0f, as in open_gl spec.
        """
    )

    def _max_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLOD,
                        self.max_lod)

    max_level = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Level of detail of the first texture image. A texture object is a
        list of texture images. It is a non-negative integer value.
        Initial value is 1000, as in open_gl spec.
        """
    )

    def _max_level_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaxLevel,
                        self.max_level)

    min_lod = traits.Float(-1000.0, enter_set=True, auto_set=False, help=\
        """
        Lower-clamp the computed LOD against this value. Any float value
        is valid. Initial value is -1000.0f, as in open_gl spec.
        """
    )

    def _min_lod_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinLOD,
                        self.min_lod)

    minification_filter = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Minification filter mode. Valid values are:
        - Nearest
        - Linear
        - nearest_mipmap_nearest
        - nearest_mipmap_linear
        - linear_mipmap_nearest
        - linear_mipmap_linear Initial value is Nearest (note initial value
        in open_gl spec is nearest_mip_map_linear but this is error-prone
          because it makes the texture object incomplete. ).
        """
    )

    def _minification_filter_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMinificationFilter,
                        self.minification_filter)

    require_depth_buffer_float = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Optional, require support for floating point depth buffer
        formats. If supported extensions will be loaded, however loading
        will fail if the extension is required but not available.
        """
    )

    def _require_depth_buffer_float_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequireDepthBufferFloat,
                        self.require_depth_buffer_float)

    require_texture_float = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Optional, require support for floating point texture formats. If
        supported extensions will be loaded, however loading will fail if
        the extension is required but not available.
        """
    )

    def _require_texture_float_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequireTextureFloat,
                        self.require_texture_float)

    require_texture_integer = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Optional, require support for integer texture formats. If
        supported extensions will be loaded, however loading will fail if
        the extension is required but not available.
        """
    )

    def _require_texture_integer_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRequireTextureInteger,
                        self.require_texture_integer)

    wrap_r = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "r" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )

    def _wrap_r_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapR,
                        self.wrap_r)

    wrap_s = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "s" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )

    def _wrap_s_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapS,
                        self.wrap_s)

    wrap_t = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Wrap mode for the first texture coordinate "t" Valid values are:
        - Clamp
        - clamp_to_edge
        - Repeat
        - clamp_to_border
        - mirrored_repeat Initial value is Repeat (as in open_gl spec)
        """
    )

    def _wrap_t_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWrapT,
                        self.wrap_t)

    def _get_components(self):
        return self._vtk_obj.GetComponents()
    components = traits.Property(_get_components, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def get_default_data_type(self, *args):
        """
        V.get_default_data_type(int) -> int
        C++: int GetDefaultDataType(int vtk_scalar_type)
        Get the data type for the texture as GLenum type.
        """
        ret = self._wrap_call(self._vtk_obj.GetDefaultDataType, *args)
        return ret

    def get_default_format(self, *args):
        """
        V.get_default_format(int, int, bool) -> int
        C++: unsigned int GetDefaultFormat(int vtktype, int numComps,
            bool shaderSupportsTextureInt)
        Get/Set format (_open_gl internal format) that should be used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.GetDefaultFormat, *args)
        return ret

    def get_default_internal_format(self, *args):
        """
        V.get_default_internal_format(int, int, bool) -> int
        C++: unsigned int GetDefaultInternalFormat(int vtktype,
            int numComps, bool shaderSupportsTextureInt)
        Get/Set internal format (_open_gl internal format) that should be
        used.
        (https://www.opengl.org/sdk/docs/man_2/xhtml/gl_tex_image2d.xml)
        """
        ret = self._wrap_call(self._vtk_obj.GetDefaultInternalFormat, *args)
        return ret

    def _get_depth(self):
        return self._vtk_obj.GetDepth()
    depth = traits.Property(_get_depth, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def _get_handle(self):
        return self._vtk_obj.GetHandle()
    handle = traits.Property(_get_handle, help=\
        """
        Returns the open_gl handle.
        """
    )

    def _get_height(self):
        return self._vtk_obj.GetHeight()
    height = traits.Property(_get_height, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def get_magnification_filter_mode(self, *args):
        """
        V.get_magnification_filter_mode(int) -> int
        C++: unsigned int GetMagnificationFilterMode(int vtktype)"""
        ret = self._wrap_call(self._vtk_obj.GetMagnificationFilterMode, *args)
        return ret

    def get_maximum_texture_size(self, *args):
        """
        V.get_maximum_texture_size(OpenGLRenderWindow) -> int
        C++: static int GetMaximumTextureSize(
            OpenGLRenderWindow *context)
        Query and return maximum texture size (dimension) supported by
        the open_gl driver for a particular context. It should be noted
        that this size does not consider the internal format of the
        texture and therefore there is no guarentee that a texture of
        this size will be allocated by the driver. Also, the method does
        not make the context current so if the passed context is not
        valid or current, a value of -1 will be returned.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetMaximumTextureSize, *my_args)
        return ret

    def get_minification_filter_mode(self, *args):
        """
        V.get_minification_filter_mode(int) -> int
        C++: unsigned int GetMinificationFilterMode(int vtktype)"""
        ret = self._wrap_call(self._vtk_obj.GetMinificationFilterMode, *args)
        return ret

    def _get_number_of_dimensions(self):
        return self._vtk_obj.GetNumberOfDimensions()
    number_of_dimensions = traits.Property(_get_number_of_dimensions, help=\
        """
        
        """
    )

    def get_shift_and_scale(self, *args):
        """
        V.get_shift_and_scale(float, float)
        C++: void GetShiftAndScale(float &shift, float &scale)
        Get the shift and scale required in the shader to return the
        texture values to their original range. Thsi is useful when for
        example you have unsigned char data and it is being accessed
        using the floating point texture calls. In that case open_gl maps
        the uchar range to a different floating point range under the
        hood. Applying the shift and scale will return the data to its
        original values in the shader. The texture's internal format must
        be set before calling these routines. Creating the texture does
        set it.
        """
        ret = self._wrap_call(self._vtk_obj.GetShiftAndScale, *args)
        return ret

    def _get_supports_depth_buffer_float(self):
        return self._vtk_obj.GetSupportsDepthBufferFloat()
    supports_depth_buffer_float = traits.Property(_get_supports_depth_buffer_float, help=\
        """
        Optional, require support for floating point depth buffer
        formats. If supported extensions will be loaded, however loading
        will fail if the extension is required but not available.
        """
    )

    def _get_supports_texture_float(self):
        return self._vtk_obj.GetSupportsTextureFloat()
    supports_texture_float = traits.Property(_get_supports_texture_float, help=\
        """
        Optional, require support for floating point texture formats. If
        supported extensions will be loaded, however loading will fail if
        the extension is required but not available.
        """
    )

    def _get_supports_texture_integer(self):
        return self._vtk_obj.GetSupportsTextureInteger()
    supports_texture_integer = traits.Property(_get_supports_texture_integer, help=\
        """
        Optional, require support for integer texture formats. If
        supported extensions will be loaded, however loading will fail if
        the extension is required but not available.
        """
    )

    def _get_target(self):
        return self._vtk_obj.GetTarget()
    target = traits.Property(_get_target, help=\
        """
        Returns open_gl texture target to which the texture is/can be
        bound.
        """
    )

    def _get_texture_unit(self):
        return self._vtk_obj.GetTextureUnit()
    texture_unit = traits.Property(_get_texture_unit, help=\
        """
        Return the texture unit used for this texture
        """
    )

    def _get_tuples(self):
        return self._vtk_obj.GetTuples()
    tuples = traits.Property(_get_tuples, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def _get_vtk_data_type(self):
        return self._vtk_obj.GetVTKDataType()
    vtk_data_type = traits.Property(_get_vtk_data_type, help=\
        """
        Get the data type for the texture as a vtk type int i.e. VTK_INT
        etc.
        """
    )

    def _get_width(self):
        return self._vtk_obj.GetWidth()
    width = traits.Property(_get_width, help=\
        """
        Get the texture dimensions. These are the properties of the
        open_gl texture this instance represents.
        """
    )

    def get_wrap_r_mode(self, *args):
        """
        V.get_wrap_r_mode(int) -> int
        C++: unsigned int GetWrapRMode(int vtktype)"""
        ret = self._wrap_call(self._vtk_obj.GetWrapRMode, *args)
        return ret

    def get_wrap_s_mode(self, *args):
        """
        V.get_wrap_s_mode(int) -> int
        C++: unsigned int GetWrapSMode(int vtktype)"""
        ret = self._wrap_call(self._vtk_obj.GetWrapSMode, *args)
        return ret

    def get_wrap_t_mode(self, *args):
        """
        V.get_wrap_t_mode(int) -> int
        C++: unsigned int GetWrapTMode(int vtktype)"""
        ret = self._wrap_call(self._vtk_obj.GetWrapTMode, *args)
        return ret

    def activate(self):
        """
        V.activate()
        C++: void Activate()
        Activate and Bind the texture
        """
        ret = self._vtk_obj.Activate()
        return ret
        

    def allocate1d(self, *args):
        """
        V.allocate1d(int, int, int) -> bool
        C++: bool Allocate1D(unsigned int width, int numComps,
            int Type)
        Create a 1d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate1D, *args)
        return ret

    def allocate2d(self, *args):
        """
        V.allocate2d(int, int, int, int) -> bool
        C++: bool Allocate2D(unsigned int width, unsigned int height,
            int numComps, int Type)
        Create a 2d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate2D, *args)
        return ret

    def allocate3d(self, *args):
        """
        V.allocate3d(int, int, int, int, int) -> bool
        C++: bool Allocate3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, int Type)
        Create a 3d color texture but does not initialize its values.
        Internal format is deduced from num_comps and Type.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate3D, *args)
        return ret

    def allocate_depth(self, *args):
        """
        V.allocate_depth(int, int, int) -> bool
        C++: bool AllocateDepth(unsigned int width, unsigned int height,
            int internalFormat)
        Create a 2d depth texture but does not initialize its values.
        """
        ret = self._wrap_call(self._vtk_obj.AllocateDepth, *args)
        return ret

    def bind(self):
        """
        V.bind()
        C++: void Bind()
        Bind un_bind The texture must have been created using Create(). A
        side affect is that tex paramteres are sent. render_window must be
        set before calling this.
        """
        ret = self._vtk_obj.Bind()
        return ret
        

    def copy_from_frame_buffer(self, *args):
        """
        V.copy_from_frame_buffer(int, int, int, int, int, int)
        C++: void CopyFromFrameBuffer(int srcXmin, int srcYmin,
            int dstXmin, int dstYmin, int width, int height)
        Copy a sub-part of a logical buffer of the framebuffer (color or
        depth) to the texture object. src is the framebuffer, dst is the
        texture. (src_xmin,src_ymin) is the location of the lower left
        corner of the rectangle in the framebuffer. (dst_xmin,dst_ymin) is
        the location of the lower left corner of the rectangle in the
        texture. width and height specifies the size of the rectangle in
        pixels. If the logical buffer is a color buffer, it has to be
        selected first with gl_read_buffer().
        \pre is_2d: get_number_of_dimensions()==_2
        """
        ret = self._wrap_call(self._vtk_obj.CopyFromFrameBuffer, *args)
        return ret

    def copy_to_frame_buffer(self, *args):
        """
        V.copy_to_frame_buffer(ShaderProgram, OpenGLVertexArrayObject)
        C++: void CopyToFrameBuffer(ShaderProgram *program,
            OpenGLVertexArrayObject *vao)
        V.copy_to_frame_buffer(int, int, int, int, int, int, int, int, int,
            int, ShaderProgram, OpenGLVertexArrayObject)
        C++: void CopyToFrameBuffer(int srcXmin, int srcYmin, int srcXmax,
             int srcYmax, int dstXmin, int dstYmin, int dstXmax,
            int dstYmax, int dstSizeX, int dstSizeY,
            ShaderProgram *program, OpenGLVertexArrayObject *vao)
        V.copy_to_frame_buffer(int, int, int, int, int, int, int, int,
            ShaderProgram, OpenGLVertexArrayObject)
        C++: void CopyToFrameBuffer(int srcXmin, int srcYmin, int srcXmax,
             int srcYmax, int dstXmin, int dstYmin, int dstSizeX,
            int dstSizeY, ShaderProgram *program,
            OpenGLVertexArrayObject *vao)
        V.copy_to_frame_buffer([float, ...], [float, ...], ShaderProgram,
            OpenGLVertexArrayObject)
        C++: void CopyToFrameBuffer(float *tcoords, float *verts,
            ShaderProgram *program, OpenGLVertexArrayObject *vao)
        Copy the texture (src) in the current framebuffer.  A variety of
        signatures based on what you want to do Copy the entire texture
        to the entire current viewport
        """
        my_args = deref_array(args, [('vtkShaderProgram', 'vtkOpenGLVertexArrayObject'), ('int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'vtkShaderProgram', 'vtkOpenGLVertexArrayObject'), ('int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'vtkShaderProgram', 'vtkOpenGLVertexArrayObject'), ('tuple', 'tuple', 'vtkShaderProgram', 'vtkOpenGLVertexArrayObject')])
        ret = self._wrap_call(self._vtk_obj.CopyToFrameBuffer, *my_args)
        return ret

    def create1d(self, *args):
        """
        V.create1d(int, PixelBufferObject, bool) -> bool
        C++: bool Create1D(int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        Create a 1d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4]. shader_supports_texture_int is true if the shader has an
        alternate implementation supporting sampler with integer values.
        Even if the card supports texture int, it does not mean that the
        implementor of the shader made a version that supports texture
        int.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create1D, *my_args)
        return ret

    def create1d_from_raw(self, *args):
        """
        V.create1d_from_raw(int, int, int, void) -> bool
        C++: bool Create1DFromRaw(unsigned int width, int numComps,
            int dataType, void *data)
        Create 1d texture from client memory
        """
        ret = self._wrap_call(self._vtk_obj.Create1DFromRaw, *args)
        return ret

    def create2d(self, *args):
        """
        V.create2d(int, int, int, PixelBufferObject, bool) -> bool
        C++: bool Create2D(unsigned int width, unsigned int height,
            int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        V.create2d(int, int, int, int, bool) -> bool
        C++: bool Create2D(unsigned int width, unsigned int height,
            int numComps, int vtktype, bool shaderSupportsTextureInt)
        Create a 2d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4].
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create2D, *my_args)
        return ret

    def create2d_from_raw(self, *args):
        """
        V.create2d_from_raw(int, int, int, int, void) -> bool
        C++: bool Create2DFromRaw(unsigned int width, unsigned int height,
             int numComps, int dataType, void *data)
        Create a 2d texture from client memory num_comps must be in [1-4].
        """
        ret = self._wrap_call(self._vtk_obj.Create2DFromRaw, *args)
        return ret

    def create3d(self, *args):
        """
        V.create3d(int, int, int, int, PixelBufferObject, bool) -> bool
        C++: bool Create3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, PixelBufferObject *pbo,
            bool shaderSupportsTextureInt)
        V.create3d(int, int, int, int, int, bool) -> bool
        C++: bool Create3D(unsigned int width, unsigned int height,
            unsigned int depth, int numComps, int vtktype,
            bool shaderSupportsTextureInt)
        Create a 3d texture using the PBO. Eventually we may start
        supporting creating a texture from subset of data in the PBO, but
        for simplicity we'll begin with entire PBO data. num_comps must be
        in [1-4].
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Create3D, *my_args)
        return ret

    def create3d_from_raw(self, *args):
        """
        V.create3d_from_raw(int, int, int, int, int, void) -> bool
        C++: bool Create3DFromRaw(unsigned int width, unsigned int height,
             unsigned int depth, int numComps, int dataType, void *data)
        Create a 3d texture from client memory num_comps must be in [1-4].
        """
        ret = self._wrap_call(self._vtk_obj.Create3DFromRaw, *args)
        return ret

    def create_alpha_from_raw(self, *args):
        """
        V.create_alpha_from_raw(int, int, int, void) -> bool
        C++: bool CreateAlphaFromRaw(unsigned int width,
            int internalFormat, int rawType, void *raw)
        Create a 1d alpha texture using a raw pointer. This is a blocking
        call. If you can, use PBO instead.
        """
        ret = self._wrap_call(self._vtk_obj.CreateAlphaFromRaw, *args)
        return ret

    def create_depth(self, *args):
        """
        V.create_depth(int, int, int, PixelBufferObject) -> bool
        C++: bool CreateDepth(unsigned int width, unsigned int height,
            int internalFormat, PixelBufferObject *pbo)
        Create a 2d depth texture using a PBO.
        \pre: valid_internal_format: internal_format>=_0 &&
            internal_format<_number_of_depth_formats
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateDepth, *my_args)
        return ret

    def create_depth_from_raw(self, *args):
        """
        V.create_depth_from_raw(int, int, int, int, void) -> bool
        C++: bool CreateDepthFromRaw(unsigned int width,
            unsigned int height, int internalFormat, int rawType,
            void *raw)
        Create a 2d depth texture using a raw pointer. This is a blocking
        call. If you can, use PBO instead.
        """
        ret = self._wrap_call(self._vtk_obj.CreateDepthFromRaw, *args)
        return ret

    def create_texture_buffer(self, *args):
        """
        V.create_texture_buffer(int, int, int, OpenGLBufferObject)
            -> bool
        C++: bool CreateTextureBuffer(unsigned int numValues,
            int numComps, int dataType, OpenGLBufferObject *bo)
        Create a texture buffer basically a 1d texture that can be very
        large for passing data into the fragment shader
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.CreateTextureBuffer, *my_args)
        return ret

    def deactivate(self):
        """
        V.deactivate()
        C++: void Deactivate()
        Deactivate and un_bind the texture
        """
        ret = self._vtk_obj.Deactivate()
        return ret
        

    def download(self):
        """
        V.download() -> PixelBufferObject
        C++: PixelBufferObject *Download()
        This is used to download raw data from the texture into a pixel
        bufer. The pixel buffer API can then be used to download the
        pixel buffer data to CPU arrays. The caller takes on the
        responsibility of deleting the returns PixelBufferObject once
        it done with it.
        """
        ret = wrap_vtk(self._vtk_obj.Download())
        return ret
        

    def is_bound(self):
        """
        V.is_bound() -> bool
        C++: bool IsBound()
        Tells if the texture object is bound to the active texture image
        unit. (a texture object can be bound to multiple texture image
        unit).
        """
        ret = self._vtk_obj.IsBound()
        return ret
        

    def is_supported(self, *args):
        """
        V.is_supported(OpenGLRenderWindow, bool, bool, bool) -> bool
        C++: static bool IsSupported(OpenGLRenderWindow *renWin,
            bool requireTexFloat, bool requireDepthFloat,
            bool requireTexInt)
        V.is_supported(OpenGLRenderWindow) -> bool
        C++: static bool IsSupported(OpenGLRenderWindow *renWin)
        Returns if the context supports the required extensions. If flags
        for optional extenisons are set then the test fails when support
        for them is not found.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def release_graphics_resources(self, *args):
        """
        V.release_graphics_resources(Window)
        C++: void ReleaseGraphicsResources(Window *win)
        Deactivate and un_bind the texture
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ReleaseGraphicsResources, *my_args)
        return ret

    def reset_format_and_type(self):
        """
        V.reset_format_and_type()
        C++: void ResetFormatAndType()
        Reset format, internal format, and type of the texture.
        
        * This method is useful when a texture is reused in a
        * context same as the previous render call. In such
        * cases, texture destruction does not happen and therefore
        * previous set values are used.
        """
        ret = self._vtk_obj.ResetFormatAndType()
        return ret
        

    def send_parameters(self):
        """
        V.send_parameters()
        C++: void SendParameters()
        Send all the texture object parameters to the hardware if not
        done yet. Parameters are automatically sent as a side affect of
        Bind. Disable this by setting auto_parameters 0.
        \pre is_bound: is_bound()
        """
        ret = self._vtk_obj.SendParameters()
        return ret
        

    def un_bind(self):
        """
        V.un_bind()
        C++: void UnBind()
        Bind un_bind The texture must have been created using Create(). A
        side affect is that tex paramteres are sent. render_window must be
        set before calling this.
        """
        ret = self._vtk_obj.UnBind()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('auto_parameters', 'GetAutoParameters'),
    ('base_level', 'GetBaseLevel'), ('border_color', 'GetBorderColor'),
    ('depth_texture_compare', 'GetDepthTextureCompare'),
    ('depth_texture_compare_function', 'GetDepthTextureCompareFunction'),
    ('generate_mipmap', 'GetGenerateMipmap'), ('linear_magnification',
    'GetLinearMagnification'), ('magnification_filter',
    'GetMagnificationFilter'), ('max_lod', 'GetMaxLOD'), ('max_level',
    'GetMaxLevel'), ('min_lod', 'GetMinLOD'), ('minification_filter',
    'GetMinificationFilter'), ('require_depth_buffer_float',
    'GetRequireDepthBufferFloat'), ('require_texture_float',
    'GetRequireTextureFloat'), ('require_texture_integer',
    'GetRequireTextureInteger'), ('wrap_r', 'GetWrapR'), ('wrap_s',
    'GetWrapS'), ('wrap_t', 'GetWrapT'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'auto_parameters', 'base_level',
    'border_color', 'depth_texture_compare',
    'depth_texture_compare_function', 'generate_mipmap',
    'linear_magnification', 'magnification_filter', 'max_level',
    'max_lod', 'min_lod', 'minification_filter',
    'require_depth_buffer_float', 'require_texture_float',
    'require_texture_integer', 'wrap_r', 'wrap_s', 'wrap_t'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TextureObject, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['auto_parameters', 'base_level', 'border_color',
            'depth_texture_compare', 'depth_texture_compare_function',
            'generate_mipmap', 'linear_magnification', 'magnification_filter',
            'max_level', 'max_lod', 'min_lod', 'minification_filter',
            'require_depth_buffer_float', 'require_texture_float',
            'require_texture_integer', 'wrap_r', 'wrap_s', 'wrap_t']),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TextureObject properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

