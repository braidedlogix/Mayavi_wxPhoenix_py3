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

from tvtk.tvtk_classes.abstract_volume_mapper import AbstractVolumeMapper


class UnstructuredGridVolumeMapper(AbstractVolumeMapper):
    """
    UnstructuredGridVolumeMapper - Abstract class for a unstructured
    grid volume mapper
    
    Superclass: AbstractVolumeMapper
    
    UnstructuredGridVolumeMapper is the abstract definition of a
    volume mapper for unstructured data (vtk_unstructured_grid).  Several 
    basic types of volume mappers are supported as subclasses
    
    @sa
    UnstructuredGridVolumeRayCastMapper
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridVolumeMapper, obj, update, **traits)
    
    blend_mode = traits.Trait('composite',
    tvtk_base.TraitRevPrefixMap({'composite': 0, 'maximum_intensity': 1}), help=\
        """
        
        """
    )

    def _blend_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBlendMode,
                        self.blend_mode_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Set/Get the input data
        """
    )

    def set_input_data(self, *args):
        """
        V.set_input_data(UnstructuredGridBase)
        C++: virtual void SetInputData(UnstructuredGridBase *)
        V.set_input_data(DataSet)
        C++: virtual void SetInputData(DataSet *)
        Set/Get the input data
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetInputData, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('blend_mode',
    'GetBlendMode'), ('scalar_mode', 'GetScalarMode'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'blend_mode', 'scalar_mode', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridVolumeMapper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['blend_mode', 'scalar_mode'], []),
            title='Edit UnstructuredGridVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridVolumeMapper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

