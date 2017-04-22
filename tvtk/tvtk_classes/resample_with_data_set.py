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

from tvtk.tvtk_classes.pass_input_type_algorithm import PassInputTypeAlgorithm


class ResampleWithDataSet(PassInputTypeAlgorithm):
    """
    ResampleWithDataSet - no description provided.
    
    Superclass: PassInputTypeAlgorithm
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkResampleWithDataSet, obj, update, **traits)
    
    pass_cell_arrays = tvtk_base.false_bool_trait(help=\
        """
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
    )

    def _pass_cell_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassCellArrays,
                        self.pass_cell_arrays_)

    pass_field_arrays = tvtk_base.true_bool_trait(help=\
        """
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
    )

    def _pass_field_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassFieldArrays,
                        self.pass_field_arrays_)

    pass_point_arrays = tvtk_base.false_bool_trait(help=\
        """
        Shallow copy the input point data arrays to the output Off by
        default.
        """
    )

    def _pass_point_arrays_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPassPointArrays,
                        self.pass_point_arrays_)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        Get the input data object. This method is not recommended for
        use, but lots of old style filters use it.
        """
    )

    def set_source_connection(self, *args):
        """
        V.set_source_connection(AlgorithmOutput)
        C++: void SetSourceConnection(AlgorithmOutput *algOutput)
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceConnection, *my_args)
        return ret

    def set_source_data(self, *args):
        """
        V.set_source_data(DataObject)
        C++: void SetSourceData(DataObject *source)
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetSourceData, *my_args)
        return ret

    _updateable_traits_ = \
    (('pass_cell_arrays', 'GetPassCellArrays'), ('pass_field_arrays',
    'GetPassFieldArrays'), ('pass_point_arrays', 'GetPassPointArrays'),
    ('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('progress',
    'GetProgress'), ('progress_text', 'GetProgressText'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'pass_cell_arrays', 'pass_field_arrays', 'pass_point_arrays',
    'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ResampleWithDataSet, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ResampleWithDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['pass_cell_arrays', 'pass_field_arrays', 'pass_point_arrays'],
            [], []),
            title='Edit ResampleWithDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ResampleWithDataSet properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

