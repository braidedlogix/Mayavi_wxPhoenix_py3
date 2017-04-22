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

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageBSplineCoefficients(ThreadedImageAlgorithm):
    """
    ImageBSplineCoefficients - convert image to b-spline knots
    
    Superclass: ThreadedImageAlgorithm
    
    ImageBSplineCoefficients prepares an image for b-spline
    interpolation by converting the image values into b-spline knot
    coefficients.  It is a necessary pre-filtering step before applying
    b-spline interpolation with ImageReslice.
    
    This class is based on code provided by Philippe Thevenaz of EPFL,
    Lausanne, Switzerland.  Please acknowledge his contribution by citing
    the following paper: [1] P. Thevenaz, T. Blu, M. Unser, "Interpolation
    Revisited,"
        IEEE Transactions on Medical Imaging 19(7):739-758, 2000.
    
    The clamped boundary condition (which is the default) is taken from
    code presented in the following paper: [2] D. Ruijters, P. Thevenaz,
        "GPU Prefilter for Accurate Cubic B-spline Interpolation,"
        The Computer Journal, doi: 10.1093/comjnl/bxq086, 2010.
    
    @par Thanks: This class was written by David Gobbi at the Seaman
    Family MR Research Centre, Foothills Medical Centre, Calgary,
    Alberta. DG Gobbi and YP Starreveld, "Uniform B-Splines for the VTK Imaging
    Pipeline," VTK Journal, 2011, http://hdl.handle.net/10380/3252
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageBSplineCoefficients, obj, update, **traits)
    
    bypass = tvtk_base.false_bool_trait(help=\
        """
        Bypass the filter, do not do any processing.  If this is on, then
        the output data will reference the input data directly, and the
        output type will be the same as the input type.  This is useful a
        downstream filter sometimes uses b-spline interpolation and
        sometimes uses other forms of interpolation.
        """
    )

    def _bypass_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBypass,
                        self.bypass_)

    border_mode = traits.Trait('clamp',
    tvtk_base.TraitRevPrefixMap({'clamp': 0, 'mirror': 2, 'repeat': 1}), help=\
        """
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
    )

    def _border_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBorderMode,
                        self.border_mode_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int)
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    spline_degree = traits.Trait(3, traits.Range(0, 9, enter_set=True, auto_set=False), help=\
        """
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.
        """
    )

    def _spline_degree_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSplineDegree,
                        self.spline_degree)

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

    def check_bounds(self, *args):
        """
        V.check_bounds((float, float, float)) -> int
        C++: int CheckBounds(const double point[3])
        Check a point against the image bounds.  Return 0 if out of
        bounds, and 1 if inside bounds.  Calling Evaluate on a point
        outside the bounds will not generate an error, but the value
        returned will depend on the border_mode.
        """
        ret = self._wrap_call(self._vtk_obj.CheckBounds, *args)
        return ret

    def evaluate(self, *args):
        """
        V.evaluate((float, float, float), [float, ...])
        C++: void Evaluate(const double point[3], double *value)
        V.evaluate(float, float, float) -> float
        C++: double Evaluate(double x, double y, double z)
        V.evaluate((float, float, float)) -> float
        C++: double Evaluate(const double point[3])
        Interpolate a value from the image.  You must call Update()
        before calling this method for the first time.  The first
        signature can return multiple components, while the second
        signature is for use on single-component images.
        """
        ret = self._wrap_call(self._vtk_obj.Evaluate, *args)
        return ret

    _updateable_traits_ = \
    (('bypass', 'GetBypass'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('border_mode',
    'GetBorderMode'), ('split_mode', 'GetSplitMode'), ('spline_degree',
    'GetSplineDegree'), ('desired_bytes_per_piece',
    'GetDesiredBytesPerPiece'), ('enable_smp', 'GetEnableSMP'),
    ('global_default_enable_smp', 'GetGlobalDefaultEnableSMP'),
    ('minimum_piece_size', 'GetMinimumPieceSize'), ('number_of_threads',
    'GetNumberOfThreads'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'bypass', 'debug', 'global_warning_display',
    'release_data_flag', 'border_mode', 'split_mode',
    'desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
    'minimum_piece_size', 'number_of_threads', 'progress_text',
    'spline_degree'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageBSplineCoefficients, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageBSplineCoefficients properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['bypass'], ['border_mode', 'split_mode'],
            ['desired_bytes_per_piece', 'enable_smp', 'global_default_enable_smp',
            'minimum_piece_size', 'number_of_threads', 'spline_degree']),
            title='Edit ImageBSplineCoefficients properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageBSplineCoefficients properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

