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

from tvtk.tvtk_classes.frame_buffer_object_base import FrameBufferObjectBase


class FrameBufferObject2(FrameBufferObjectBase):
    """
    FrameBufferObject2 - Interface to open_gl framebuffer object.
    
    Superclass: FrameBufferObjectBase
    
    A light and efficient interface to an open_gl Frame Buffer Object. Use
    is very simillalry to directly calling open_gl, but as Object it
    may safely stored, shared, or passed around. It supports FBO Blit and
    transfer to Pixel Buffer Object.
    
    Typical use case:{.cpp}
    FrameBufferObject2 *fbo = this->Internals->FBO;
    fbo->_save_current_bindings();
    fbo->Bind(vtkgl::FRAMEBUFFER_EXT);
    fbo->_add_depth_attachment(vtkgl::_draw__framebuffer__ext, depth_buffer);
    fbo->_add_color_attachment(vtkgl::_draw__framebuffer__ext, 0u, color_tex1);
    fbo->_add_color_attachment(vtkgl::_draw__framebuffer__ext, 1u, color_tex2);
    fbo->_add_color_attachment(vtkgl::_draw__framebuffer__ext, 2u, color_tex3);
    fbo->_activate_draw_buffers(_3);
    CheckFrameBufferStatusMacro(vtkgl::FRAMEBUFFER_EXT);
    
    ...
    
    fbo->_un_bind(vtkgl::_framebuffer__ext);
    
    @sa
    Renderbuffer, PixelBufferObject
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkFrameBufferObject2, obj, update, **traits)
    
    def _get_context(self):
        return wrap_vtk(self._vtk_obj.GetContext())
    def _set_context(self, arg):
        old_val = self._get_context()
        self._wrap_call(self._vtk_obj.SetContext,
                        deref_vtk(arg))
        self.trait_property_changed('context', old_val, arg)
    context = traits.Property(_get_context, _set_context, help=\
        """
        Get/Set the context. Context must be a OpenGLRenderWindow.
        This does not increase the reference count of the context to
        avoid reference loops. set_context() may raise an error is the
        open_gl context does not support the required open_gl extensions.
        """
    )

    def activate_draw_buffer(self, *args):
        """
        V.activate_draw_buffer(int)
        C++: void ActivateDrawBuffer(unsigned int id)
        Select a single specific draw or read buffer (zero based)
        """
        ret = self._wrap_call(self._vtk_obj.ActivateDrawBuffer, *args)
        return ret

    def activate_draw_buffers(self, *args):
        """
        V.activate_draw_buffers(int)
        C++: void ActivateDrawBuffers(unsigned int n)
        V.activate_draw_buffers([int, ...], int)
        C++: void ActivateDrawBuffers(unsigned int *ids, int n)
        Select n consecutive write attachments. Low level api.
        """
        ret = self._wrap_call(self._vtk_obj.ActivateDrawBuffers, *args)
        return ret

    def activate_read_buffer(self, *args):
        """
        V.activate_read_buffer(int)
        C++: void ActivateReadBuffer(unsigned int id)
        Select a single specific draw or read buffer (zero based)
        """
        ret = self._wrap_call(self._vtk_obj.ActivateReadBuffer, *args)
        return ret

    def add_color_attachment(self, *args):
        """
        V.add_color_attachment(int, int, TextureObject)
        C++: void AddColorAttachment(unsigned int mode,
            unsigned int attId, TextureObject *tex)
        V.add_color_attachment(int, int, Renderbuffer)
        C++: void AddColorAttachment(unsigned int mode,
            unsigned int attId, Renderbuffer *tex)
        Directly assign/remove a texture to color attachments.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddColorAttachment, *my_args)
        return ret

    def add_depth_attachment(self, *args):
        """
        V.add_depth_attachment(int, TextureObject)
        C++: void AddDepthAttachment(unsigned int mode,
            TextureObject *tex)
        V.add_depth_attachment(int, Renderbuffer)
        C++: void AddDepthAttachment(unsigned int mode,
            Renderbuffer *tex)
        Directly assign/remove a texture/renderbuffer to depth
        attachments.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddDepthAttachment, *my_args)
        return ret

    def add_ren_color_attachment(self, *args):
        """
        V.add_ren_color_attachment(int, int, int)
        C++: void AddRenColorAttachment(unsigned int mode,
            unsigned int attId, unsigned int handle)"""
        ret = self._wrap_call(self._vtk_obj.AddRenColorAttachment, *args)
        return ret

    def add_ren_depth_attachment(self, *args):
        """
        V.add_ren_depth_attachment(int, int)
        C++: void AddRenDepthAttachment(unsigned int mode,
            unsigned int handle)
        Directly assign/remove a renderbuffer to depth attachments.
        """
        ret = self._wrap_call(self._vtk_obj.AddRenDepthAttachment, *args)
        return ret

    def add_tex_color_attachment(self, *args):
        """
        V.add_tex_color_attachment(int, int, int)
        C++: void AddTexColorAttachment(unsigned int mode,
            unsigned int attId, unsigned int handle)"""
        ret = self._wrap_call(self._vtk_obj.AddTexColorAttachment, *args)
        return ret

    def add_tex_depth_attachment(self, *args):
        """
        V.add_tex_depth_attachment(int, int)
        C++: void AddTexDepthAttachment(unsigned int mode,
            unsigned int handle)
        Directly assign/remove a texture/renderbuffer to depth
        attachments.
        """
        ret = self._wrap_call(self._vtk_obj.AddTexDepthAttachment, *args)
        return ret

    def bind(self, *args):
        """
        V.bind(int)
        C++: void Bind(unsigned int mode)
        Bind FBO to FRAMEBUFFER,  DRAW_FRAMEBUFFER or READ_FRAMEBUFFER
        The current binding is not saved, nor restored. (see
        gl_bind_framebuffer) This method can be used to prepare for FBO
        Blit or buffer ping-pong. Low level api.
        """
        ret = self._wrap_call(self._vtk_obj.Bind, *args)
        return ret

    def blit(self, *args):
        """
        V.blit([int, int, int, int], [int, int, int, int], int, int)
            -> int
        C++: static int Blit(int srcExt[4], int destExt[4],
            unsigned int bits, unsigned int mapping)
        Copy from the currently bound READ FBO to the currently bound
        DRAW FBO. The method is static so that one doesn't need to
        ccreate an instance when transfering between attachments in the
        default FBO.
        """
        ret = self._wrap_call(self._vtk_obj.Blit, *args)
        return ret

    def check_frame_buffer_status(self, *args):
        """
        V.check_frame_buffer_status(int) -> int
        C++: int CheckFrameBufferStatus(unsigned int mode)
        Validate the current FBO configuration (attachments, formats,
        etc) prints detected errors to ErrorMacro. Low level api.
        """
        ret = self._wrap_call(self._vtk_obj.CheckFrameBufferStatus, *args)
        return ret

    def deactivate_draw_buffers(self):
        """
        V.deactivate_draw_buffers()
        C++: void DeactivateDrawBuffers()
        Select n consecutive write attachments. Low level api.
        """
        ret = self._vtk_obj.DeactivateDrawBuffers()
        return ret
        

    def deactivate_read_buffer(self):
        """
        V.deactivate_read_buffer()
        C++: void DeactivateReadBuffer()
        Select a single specific draw or read buffer (zero based)
        """
        ret = self._vtk_obj.DeactivateReadBuffer()
        return ret
        

    def download(self, *args):
        """
        V.download([int, int, int, int], int, int, int, int)
            -> PixelBufferObject
        C++: PixelBufferObject *Download(int extent[4], int Type,
            int nComps, int oglType, int oglFormat)
        V.download([int, int, int, int], int, int, int, int,
            PixelBufferObject)
        C++: static void Download(int extent[4], int Type, int nComps,
            int oglType, int oglFormat, PixelBufferObject *pbo)
        Download data from the read buffer of the current FBO. These are
        low level meothds. In the static variant a PBO must be passed in
        since we don't have access to a context. The static method is
        provided so that one may download from the default FBO.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Download, *my_args)
        return wrap_vtk(ret)

    def download_color1(self, *args):
        """
        V.download_color1([int, int, int, int], int, int)
            -> PixelBufferObject
        C++: PixelBufferObject *DownloadColor1(int extent[4],
            int Type, int channel)
        Download data from the read color attachment of the currently
        bound FBO into the retruned PBO. The PBO must be free'd when you
        are finished with it. The number of components in the PBO is the
        same as in the name of the specific  download fucntion. When
        downloading a single color channel, the channel must be
        identified by index, 1->red, 2->green, 3-> blue.
        """
        ret = self._wrap_call(self._vtk_obj.DownloadColor1, *args)
        return wrap_vtk(ret)

    def download_color3(self, *args):
        """
        V.download_color3([int, int, int, int], int)
            -> PixelBufferObject
        C++: PixelBufferObject *DownloadColor3(int extent[4],
            int Type)"""
        ret = self._wrap_call(self._vtk_obj.DownloadColor3, *args)
        return wrap_vtk(ret)

    def download_color4(self, *args):
        """
        V.download_color4([int, int, int, int], int)
            -> PixelBufferObject
        C++: PixelBufferObject *DownloadColor4(int extent[4],
            int Type)"""
        ret = self._wrap_call(self._vtk_obj.DownloadColor4, *args)
        return wrap_vtk(ret)

    def download_depth(self, *args):
        """
        V.download_depth([int, int, int, int], int) -> PixelBufferObject
        C++: PixelBufferObject *DownloadDepth(int extent[4],
            int Type)
        Download data from the depth attachment of the currently bound
        FBO. The returned PBO must be Delete'd by the caller. The
        retruned PBO has one component.
        """
        ret = self._wrap_call(self._vtk_obj.DownloadDepth, *args)
        return wrap_vtk(ret)

    def initialize_viewport(self, *args):
        """
        V.initialize_viewport(int, int)
        C++: static void InitializeViewport(int width, int height)
        Set up ortho viewport with scissor, lighting, blend, and depth
        disabled. The method affects the current bound FBO. The method is
        static so that it may be used on the default FBO without an
        instance. Low level api.
        """
        ret = self._wrap_call(self._vtk_obj.InitializeViewport, *args)
        return ret

    def is_supported(self, *args):
        """
        V.is_supported(RenderWindow) -> bool
        C++: static bool IsSupported(RenderWindow *renWin)
        Returns if the context supports the required extensions.
        Extension will be loaded when the conetxt is set.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.IsSupported, *my_args)
        return ret

    def remove_ren_color_attachment(self, *args):
        """
        V.remove_ren_color_attachment(int, int)
        C++: void RemoveRenColorAttachment(unsigned int mode,
            unsigned int attId)"""
        ret = self._wrap_call(self._vtk_obj.RemoveRenColorAttachment, *args)
        return ret

    def remove_ren_color_attachments(self, *args):
        """
        V.remove_ren_color_attachments(int, int)
        C++: void RemoveRenColorAttachments(unsigned int mode,
            unsigned int num)"""
        ret = self._wrap_call(self._vtk_obj.RemoveRenColorAttachments, *args)
        return ret

    def remove_ren_depth_attachment(self, *args):
        """
        V.remove_ren_depth_attachment(int)
        C++: void RemoveRenDepthAttachment(unsigned int mode)
        Directly assign/remove a renderbuffer to depth attachments.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveRenDepthAttachment, *args)
        return ret

    def remove_tex_color_attachment(self, *args):
        """
        V.remove_tex_color_attachment(int, int)
        C++: void RemoveTexColorAttachment(unsigned int mode,
            unsigned int attId)"""
        ret = self._wrap_call(self._vtk_obj.RemoveTexColorAttachment, *args)
        return ret

    def remove_tex_color_attachments(self, *args):
        """
        V.remove_tex_color_attachments(int, int)
        C++: void RemoveTexColorAttachments(unsigned int mode,
            unsigned int num)"""
        ret = self._wrap_call(self._vtk_obj.RemoveTexColorAttachments, *args)
        return ret

    def remove_tex_depth_attachment(self, *args):
        """
        V.remove_tex_depth_attachment(int)
        C++: void RemoveTexDepthAttachment(unsigned int mode)
        Directly assign/remove a texture/renderbuffer to depth
        attachments.
        """
        ret = self._wrap_call(self._vtk_obj.RemoveTexDepthAttachment, *args)
        return ret

    def restore_previous_buffers(self, *args):
        """
        V.restore_previous_buffers(int)
        C++: void RestorePreviousBuffers(unsigned int mode)
        Store the current draw and read buffers. When restored only the
        buffers matching mode are modified. DRAW_FRAMEBUFFER ->
        gl_draw_buffer READ_FRAMEBUFFER -> gl_read_buffer FRAMEBUFFER -> both
        """
        ret = self._wrap_call(self._vtk_obj.RestorePreviousBuffers, *args)
        return ret

    def save_current_bindings(self):
        """
        V.save_current_bindings()
        C++: void SaveCurrentBindings()
        Store the current framebuffer bindings. If this method is called
        then un_bind will restore the saved value accoring to its mode
        (DRAW_FRAMEBUFFER,READ_FRAMEBUFFER,FRAMEBUFFER) Restoration
        occurs in un_bind. Low level api
        """
        ret = self._vtk_obj.SaveCurrentBindings()
        return ret
        

    def save_current_buffers(self):
        """
        V.save_current_buffers()
        C++: void SaveCurrentBuffers()
        Store the current draw and read buffers. When restored only the
        buffers matching mode are modified. DRAW_FRAMEBUFFER ->
        gl_draw_buffer READ_FRAMEBUFFER -> gl_read_buffer FRAMEBUFFER -> both
        """
        ret = self._vtk_obj.SaveCurrentBuffers()
        return ret
        

    def un_bind(self, *args):
        """
        V.un_bind(int)
        C++: void UnBind(unsigned int mode)
        Bind saved FBO (see save_current_bindings) for DRAW or READ (see
        gl_bind_framebuffer) If no bindings were saved bind to default FBO.
        Low level api.
        """
        ret = self._wrap_call(self._vtk_obj.UnBind, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(FrameBufferObject2, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit FrameBufferObject2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit FrameBufferObject2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit FrameBufferObject2 properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

