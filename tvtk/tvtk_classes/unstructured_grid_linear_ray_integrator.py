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

from tvtk.tvtk_classes.unstructured_grid_volume_ray_integrator import UnstructuredGridVolumeRayIntegrator


class UnstructuredGridLinearRayIntegrator(UnstructuredGridVolumeRayIntegrator):
    """
    UnstructuredGridLinearRayIntegrator - performs piecewise linear
    ray integration.
    
    Superclass: UnstructuredGridVolumeRayIntegrator
    
    UnstructuredGridLinearRayIntegrator performs piecewise linear ray
    integration.  Considering that transfer functions in VTK are
    piecewise linear, this class should give the "correct" integration
    under most circumstances.  However, the computations performed are
    fairly hefty and should, for the most part, only be used as a
    benchmark for other, faster methods.
    
    @sa
    UnstructuredGridPartialPreIntegration
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridLinearRayIntegrator, obj, update, **traits)
    
    def integrate_ray(self, *args):
        """
        V.integrate_ray(float, float, float, float, float, [float, float,
            float, float])
        C++: static void IntegrateRay(double length,
            double intensity_front, double attenuation_front,
            double intensity_back, double attenuation_back,
            float color[4])
        V.integrate_ray(float, (float, float, float), float, (float, float,
             float), float, [float, float, float, float])
        C++: static void IntegrateRay(double length,
            const double color_front[3], double attenuation_front,
            const double color_back[3], double attenuation_back,
            float color[4])
        Integrates a single ray segment.  color is blended with the
        result (with color in front).  The result is written back into
        color.
        """
        ret = self._wrap_call(self._vtk_obj.IntegrateRay, *args)
        return ret

    def psi(self, *args):
        """
        V.psi(float, float, float) -> float
        C++: static float Psi(float length, float attenuation_front,
            float attenuation_back)
        Computes Psi (as defined by Moreland and Angel, "A Fast High
        Accuracy Volume Renderer for Unstructured Data").
        """
        ret = self._wrap_call(self._vtk_obj.Psi, *args)
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
            return super(UnstructuredGridLinearRayIntegrator, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridLinearRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit UnstructuredGridLinearRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridLinearRayIntegrator properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

