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


class SampleFunction(ImageAlgorithm):
    """
    SampleFunction - sample an implicit function over a structured
    point set
    
    Superclass: ImageAlgorithm
    
    SampleFunction is a source object that evaluates an implicit
    function and normals at each point in a StructuredPoints. The user
    can specify the sample dimensions and location in space to perform
    the sampling. To create closed surfaces (in conjunction with the
    ContourFilter), capping can be turned on to set a particular value
    on the boundaries of the sample space.
    
    @sa
    ImplicitModeller
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSampleFunction, obj, update, **traits)
    
    capping = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off capping. If capping is on, then the outer boundaries
        of the structured point set are set to cap value. This can be
        used to insure surfaces are closed.
        """
    )

    def _capping_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapping,
                        self.capping_)

    compute_normals = tvtk_base.true_bool_trait(help=\
        """
        Turn on/off the computation of normals (normals are float
        values).
        """
    )

    def _compute_normals_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetComputeNormals,
                        self.compute_normals_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set what type of scalar data this source should generate.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        Set what type of scalar data this source should generate.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_char(self):
        """
        V.set_output_scalar_type_to_char()
        C++: void SetOutputScalarTypeToChar()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToChar()

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set what type of scalar data this source should generate.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    cap_value = traits.Float(1e+299, enter_set=True, auto_set=False, help=\
        """
        Set the cap value.
        """
    )

    def _cap_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCapValue,
                        self.cap_value)

    def _get_implicit_function(self):
        return wrap_vtk(self._vtk_obj.GetImplicitFunction())
    def _set_implicit_function(self, arg):
        old_val = self._get_implicit_function()
        self._wrap_call(self._vtk_obj.SetImplicitFunction,
                        deref_vtk(arg))
        self.trait_property_changed('implicit_function', old_val, arg)
    implicit_function = traits.Property(_get_implicit_function, _set_implicit_function, help=\
        """
        Specify the implicit function to use to generate data.
        """
    )

    model_bounds = traits.Array(enter_set=True, auto_set=False, shape=(6,), dtype=float, value=(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0), cols=3, help=\
        """
        Specify the region in space over which the sampling occurs. The
        bounds is specified as (x_min,x_max, y_min,y_max, z_min,z_max).
        """
    )

    def _model_bounds_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetModelBounds,
                        self.model_bounds)

    normal_array_name = traits.String('normals', enter_set=True, auto_set=False, help=\
        """
        Set/get the normal array name for this data set. Initial value is
        "normals".
        """
    )

    def _normal_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNormalArrayName,
                        self.normal_array_name)

    sample_dimensions = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=int, value=(50, 50, 50), cols=3, help=\
        """
        Specify the dimensions of the data on which to sample.
        """
    )

    def _sample_dimensions_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSampleDimensions,
                        self.sample_dimensions)

    scalar_array_name = traits.String('scalars', enter_set=True, auto_set=False, help=\
        """
        Set/get the scalar array name for this data set. Initial value is
        "scalars".
        """
    )

    def _scalar_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScalarArrayName,
                        self.scalar_array_name)

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

    _updateable_traits_ = \
    (('capping', 'GetCapping'), ('compute_normals', 'GetComputeNormals'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('cap_value',
    'GetCapValue'), ('model_bounds', 'GetModelBounds'),
    ('normal_array_name', 'GetNormalArrayName'), ('sample_dimensions',
    'GetSampleDimensions'), ('scalar_array_name', 'GetScalarArrayName'),
    ('progress', 'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'capping', 'compute_normals', 'debug',
    'global_warning_display', 'release_data_flag', 'cap_value',
    'model_bounds', 'normal_array_name', 'progress_text',
    'sample_dimensions', 'scalar_array_name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SampleFunction, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['capping', 'compute_normals'], [], ['cap_value',
            'model_bounds', 'normal_array_name', 'sample_dimensions',
            'scalar_array_name']),
            title='Edit SampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SampleFunction properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

