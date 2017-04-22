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

from tvtk.tvtk_classes.image_algorithm import ImageAlgorithm


class ImageCanvasSource2D(ImageAlgorithm):
    """
    ImageCanvasSource2D - Paints on a canvas
    
    Superclass: ImageAlgorithm
    
    ImageCanvasSource2D is a source that starts as a blank image. you
    may add to the image with two-dimensional drawing routines. It can
    paint multi-spectral images.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageCanvasSource2D, obj, update, **traits)
    
    scalar_type = traits.Trait('double',
    tvtk_base.TraitRevPrefixMap({'double': 11, 'char': 2, 'float': 10, 'int': 6, 'long': 8, 'short': 4, 'unsigned_char': 3, 'unsigned_int': 7, 'unsigned_long': 9, 'unsigned_short': 5}), help=\
        """
        Set/Get the data scalar type (i.e VTK_DOUBLE). Note that these
        methods are setting and getting the pipeline scalar type. i.e.
        they are setting the type that the image data will be once it has
        executed. Until the REQUEST_DATA pass the actual scalars may be
        of some other type. This is for backwards compatibility
        """
    )

    def _scalar_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarType,
                        self.scalar_type_)

    default_z = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        The drawing operations can only draw into one 2d XY plane at a
        time. If the canvas is a 3d volume, then this z value is used as
        the default for 2d operations. The default is 0.
        """
    )

    def _default_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDefaultZ,
                        self.default_z)

    draw_color = traits.Array(enter_set=True, auto_set=False, shape=(4,), dtype=float, value=(0.0, 0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _draw_color_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDrawColor,
                        self.draw_color)

    number_of_scalar_components = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the number of scalar components
        """
    )

    def _number_of_scalar_components_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfScalarComponents,
                        self.number_of_scalar_components)

    ratio = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(1.0, 1.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _ratio_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRatio,
                        self.ratio)

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        Get a data object for one of the input port connections.  The use
        of this method is strongly discouraged, but some filters that
        were written a long time ago still use this method.
        """
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def draw_circle(self, *args):
        """
        V.draw_circle(int, int, float)
        C++: void DrawCircle(int c0, int c1, double radius)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.DrawCircle, *args)
        return ret

    def draw_image(self, *args):
        """
        V.draw_image(int, int, ImageData)
        C++: void DrawImage(int x0, int y0, ImageData *i)
        V.draw_image(int, int, ImageData, int, int, int, int)
        C++: void DrawImage(int x0, int y0, ImageData *, int sx,
            int sy, int width, int height)
        Draw subimage of the input image in the canvas at position x0 and
        y0. The subimage is defined with sx, sy, width, and height.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DrawImage, *my_args)
        return ret

    def draw_point(self, *args):
        """
        V.draw_point(int, int)
        C++: void DrawPoint(int p0, int p1)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.DrawPoint, *args)
        return ret

    def draw_segment(self, *args):
        """
        V.draw_segment(int, int, int, int)
        C++: void DrawSegment(int x0, int y0, int x1, int y1)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.DrawSegment, *args)
        return ret

    def draw_segment3d(self, *args):
        """
        V.draw_segment3d([float, ...], [float, ...])
        C++: void DrawSegment3D(double *p0, double *p1)
        V.draw_segment3d(float, float, float, float, float, float)
        C++: void DrawSegment3D(double x1, double y1, double z1,
            double x2, double y2, double z2)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.DrawSegment3D, *args)
        return ret

    def fill_box(self, *args):
        """
        V.fill_box(int, int, int, int)
        C++: void FillBox(int min0, int max0, int min1, int max1)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.FillBox, *args)
        return ret

    def fill_pixel(self, *args):
        """
        V.fill_pixel(int, int)
        C++: void FillPixel(int x, int y)
        Fill a colored area with another color. (like connectivity) All
        pixels connected (and with the same value) to pixel (x, y) get
        replaced by the current "_draw_color".
        """
        ret = self._wrap_call(self._vtk_obj.FillPixel, *args)
        return ret

    def fill_triangle(self, *args):
        """
        V.fill_triangle(int, int, int, int, int, int)
        C++: void FillTriangle(int x0, int y0, int x1, int y1, int x2,
            int y2)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.FillTriangle, *args)
        return ret

    def fill_tube(self, *args):
        """
        V.fill_tube(int, int, int, int, float)
        C++: void FillTube(int x0, int y0, int x1, int y1, double radius)
        Set the pixels inside the box (min0, max0, min1, max1) to the
        current draw_color
        """
        ret = self._wrap_call(self._vtk_obj.FillTube, *args)
        return ret

    def initialize_canvas_volume(self, *args):
        """
        V.initialize_canvas_volume(ImageData)
        C++: void InitializeCanvasVolume(ImageData *volume)
        Initialize the canvas with a given volume
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.InitializeCanvasVolume, *my_args)
        return ret

    def set_extent(self, *args):
        """
        V.set_extent([int, ...])
        C++: void SetExtent(int *extent)
        V.set_extent(int, int, int, int, int, int)
        C++: void SetExtent(int x1, int x2, int y1, int y2, int z1,
            int z2)
        These methods set the whole_extent of the output It sets the size
        of the canvas. Extent is a min max 3d box.  Minimums and maximums
        are inclusive.
        """
        ret = self._wrap_call(self._vtk_obj.SetExtent, *args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('scalar_type',
    'GetScalarType'), ('default_z', 'GetDefaultZ'), ('draw_color',
    'GetDrawColor'), ('number_of_scalar_components',
    'GetNumberOfScalarComponents'), ('ratio', 'GetRatio'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'scalar_type', 'default_z', 'draw_color',
    'number_of_scalar_components', 'progress_text', 'ratio'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageCanvasSource2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageCanvasSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['scalar_type'], ['default_z', 'draw_color',
            'number_of_scalar_components', 'ratio']),
            title='Edit ImageCanvasSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageCanvasSource2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

