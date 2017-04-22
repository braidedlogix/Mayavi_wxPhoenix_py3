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

from tvtk.tvtk_classes.synchronized_templates3d import SynchronizedTemplates3D


class SynchronizedTemplatesCutter3D(SynchronizedTemplates3D):
    """
    SynchronizedTemplatesCutter3D - generate cut surface from
    structured points
    
    Superclass: SynchronizedTemplates3D
    
    SynchronizedTemplatesCutter3D is an implementation of the
    synchronized template algorithm. Note that CutFilter will
    automatically use this class when appropriate.
    
    @sa
    ContourFilter SynchronizedTemplates3D
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSynchronizedTemplatesCutter3D, obj, update, **traits)
    
    def _get_cut_function(self):
        return wrap_vtk(self._vtk_obj.GetCutFunction())
    def _set_cut_function(self, arg):
        old_val = self._get_cut_function()
        self._wrap_call(self._vtk_obj.SetCutFunction,
                        deref_vtk(arg))
        self.trait_property_changed('cut_function', old_val, arg)
    cut_function = traits.Property(_get_cut_function, _set_cut_function, help=\
        """
        Specify the implicit function to perform the cutting.
        """
    )

    output_points_precision = traits.Trait(2, traits.Range(0, 2, enter_set=True, auto_set=False), help=\
        """
        Set/get the desired precision for the output types. See the
        documentation for the Algorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
    )

    def _output_points_precision_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputPointsPrecision,
                        self.output_points_precision)

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

    _updateable_traits_ = \
    (('compute_gradients', 'GetComputeGradients'), ('compute_normals',
    'GetComputeNormals'), ('compute_scalars', 'GetComputeScalars'),
    ('generate_triangles', 'GetGenerateTriangles'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('output_points_precision',
    'GetOutputPointsPrecision'), ('array_component', 'GetArrayComponent'),
    ('input_memory_limit', 'GetInputMemoryLimit'), ('number_of_contours',
    'GetNumberOfContours'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'compute_gradients', 'compute_normals',
    'compute_scalars', 'debug', 'generate_triangles',
    'global_warning_display', 'release_data_flag', 'array_component',
    'input_memory_limit', 'number_of_contours', 'output_points_precision',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SynchronizedTemplatesCutter3D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['compute_gradients', 'compute_normals', 'compute_scalars',
            'generate_triangles'], [], ['array_component', 'input_memory_limit',
            'number_of_contours', 'output_points_precision']),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SynchronizedTemplatesCutter3D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

