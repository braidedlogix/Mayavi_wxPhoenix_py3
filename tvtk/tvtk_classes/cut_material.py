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

from tvtk.tvtk_classes.poly_data_algorithm import PolyDataAlgorithm


class CutMaterial(PolyDataAlgorithm):
    """
    CutMaterial - Automatically computes the cut plane for a material
    array pair.
    
    Superclass: PolyDataAlgorithm
    
    CutMaterial computes a cut plane based on an up vector, center of
    the bounding box and the location of the maximum variable value.
     These computed values are available so that they can be used to set
    the camera for the best view of the plane.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCutMaterial, obj, update, **traits)
    
    array_name = traits.Trait(None, None, traits.String(enter_set=True, auto_set=False), help=\
        """
        For now, we just use the cell values. The array name to cut.
        """
    )

    def _array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetArrayName,
                        self.array_name)

    material = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Material to probe.
        """
    )

    def _material_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterial,
                        self.material)

    material_array_name = traits.String('material', enter_set=True, auto_set=False, help=\
        """
        Cell array that contains the material values.
        """
    )

    def _material_array_name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetMaterialArrayName,
                        self.material_array_name)

    up_vector = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        
        """
    )

    def _up_vector_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUpVector,
                        self.up_vector)

    def _get_center_point(self):
        return self._vtk_obj.GetCenterPoint()
    center_point = traits.Property(_get_center_point, help=\
        """
        
        """
    )

    def _get_input(self):
        try:
            return wrap_vtk(self._vtk_obj.GetInput(0))
        except TypeError:
            return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input,
                            help="The first input of this object, i.e. the result of `get_input(0)`.")
    
    def get_input(self, *args):
        """
        V.get_input() -> DataObject
        C++: DataObject *GetInput()
        V.get_input(int) -> DataObject
        C++: DataObject *GetInput(int port)"""
        ret = self._wrap_call(self._vtk_obj.GetInput, *args)
        return wrap_vtk(ret)

    def _get_maximum_point(self):
        return self._vtk_obj.GetMaximumPoint()
    maximum_point = traits.Property(_get_maximum_point, help=\
        """
        
        """
    )

    def _get_normal(self):
        return self._vtk_obj.GetNormal()
    normal = traits.Property(_get_normal, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('array_name',
    'GetArrayName'), ('material', 'GetMaterial'), ('material_array_name',
    'GetMaterialArrayName'), ('up_vector', 'GetUpVector'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'array_name', 'material', 'material_array_name',
    'progress_text', 'up_vector'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(CutMaterial, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit CutMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['array_name', 'material', 'material_array_name',
            'up_vector']),
            title='Edit CutMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit CutMaterial properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

