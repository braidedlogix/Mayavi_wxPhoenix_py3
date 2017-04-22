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

class OpenGLGL2PSHelperImpl(object):
    """
    OpenGLGL2PSHelperImpl - OpenGLGL2PSHelper override
    implementation.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkOpenGLGL2PSHelperImpl, obj, update, **traits)
    
    def _get_class_name(self):
        return self._vtk_obj.GetClassName()
    class_name = traits.Property(_get_class_name, help=\
        """
        
        """
    )

    def draw3d_path(self, *args):
        """
        V.draw3d_path(Path, Matrix4x4, [float, float, float], [int,
            int, int, int], Renderer, string)
        C++: virtual void Draw3DPath(Path *path,
            Matrix4x4 *actorMatrix, double rasterPos[3],
            unsigned char actorColor[4], Renderer *ren,
            const char *label=NULL)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Draw3DPath, *my_args)
        return ret

    def draw_image(self, *args):
        """
        V.draw_image(ImageData, [float, float, float])
        C++: virtual void DrawImage(ImageData *image, double pos[3])"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawImage, *my_args)
        return ret

    def draw_path(self, *args):
        """
        V.draw_path(Path, [float, float, float], [float, float], [int,
            int, int, int], [float, float], float, float, string)
        C++: virtual void DrawPath(Path *path, double rasterPos[3],
            double windowPos[2], unsigned char rgba[4],
            double scale[2]=NULL, double rotateAngle=0.0,
            float strokeWidth=-1, const char *label=NULL)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawPath, *my_args)
        return ret

    def draw_string(self, *args):
        """
        V.draw_string(string, TextProperty, [float, float, float],
            float, Renderer)
        C++: virtual void DrawString(const std::string &str,
            TextProperty *tprop, double pos[3], double backgroundDepth,
             Renderer *ren)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawString, *my_args)
        return ret

    def is_a(self, *args):
        """
        V.is_a(string) -> int
        C++: int IsA(const char *name)"""
        ret = self._wrap_call(self._vtk_obj.IsA, *args)
        return ret

    def new_instance(self):
        """
        V.new_instance() -> OpenGLGL2PSHelperImpl
        C++: OpenGLGL2PSHelperImpl *NewInstance()"""
        ret = wrap_vtk(self._vtk_obj.NewInstance())
        return ret
        

    def process_transform_feedback(self, *args):
        """
        V.process_transform_feedback(TransformFeedback, Renderer,
            Actor)
        C++: virtual void ProcessTransformFeedback(
            TransformFeedback *tfc, Renderer *ren, Actor *act)
        V.process_transform_feedback(TransformFeedback, Renderer,
            [int, int, int, int])
        C++: virtual void ProcessTransformFeedback(
            TransformFeedback *tfc, Renderer *ren,
            unsigned char col[4])
        V.process_transform_feedback(TransformFeedback, Renderer,
            [float, float, float, float])
        C++: virtual void ProcessTransformFeedback(
            TransformFeedback *tfc, Renderer *ren, float col[4])"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ProcessTransformFeedback, *my_args)
        return ret

    def safe_down_cast(self, *args):
        """
        V.safe_down_cast(Object) -> OpenGLGL2PSHelperImpl
        C++: OpenGLGL2PSHelperImpl *SafeDownCast(Object* o)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SafeDownCast, *my_args)
        return wrap_vtk(ret)

    _updateable_traits_ = \
    ()
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    ([])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(OpenGLGL2PSHelperImpl, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit OpenGLGL2PSHelperImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit OpenGLGL2PSHelperImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit OpenGLGL2PSHelperImpl properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

