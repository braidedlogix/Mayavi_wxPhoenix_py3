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

from tvtk.tvtk_classes.data_object_algorithm import DataObjectAlgorithm


class ImageDataToUniformGrid(DataObjectAlgorithm):
    """
    ImageDataToUniformGrid - convert ImageData to UniformGrid
    
    Superclass: DataObjectAlgorithm
    
    Convert a ImageData to UniformGrid and set blanking based on
    specified by named arrays. By default, values of 0 in the named array
    will result in the point or cell being blanked. Set Reverse to 1 to
    indicate that values of 0 will result in the point or cell to not be
    blanked.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageDataToUniformGrid, obj, update, **traits)
    
    reverse = tvtk_base.false_bool_trait(help=\
        """
        By default, values of 0 (i.e. Reverse = 0) in the array will
        result in that point or cell to be blanked. Set Reverse to 1 to
        make points or cells to not be blanked for array values of 0.
        """
    )

    def _reverse_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReverse,
                        self.reverse_)

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

    def _get_reverse_max_value(self):
        return self._vtk_obj.GetReverseMaxValue()
    reverse_max_value = traits.Property(_get_reverse_max_value, help=\
        """
        By default, values of 0 (i.e. Reverse = 0) in the array will
        result in that point or cell to be blanked. Set Reverse to 1 to
        make points or cells to not be blanked for array values of 0.
        """
    )

    def _get_reverse_min_value(self):
        return self._vtk_obj.GetReverseMinValue()
    reverse_min_value = traits.Property(_get_reverse_min_value, help=\
        """
        By default, values of 0 (i.e. Reverse = 0) in the array will
        result in that point or cell to be blanked. Set Reverse to 1 to
        make points or cells to not be blanked for array values of 0.
        """
    )

    _updateable_traits_ = \
    (('reverse', 'GetReverse'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'reverse', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageDataToUniformGrid, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageDataToUniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['reverse'], [], []),
            title='Edit ImageDataToUniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageDataToUniformGrid properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

