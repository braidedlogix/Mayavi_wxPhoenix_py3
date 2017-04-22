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


class ImageIslandRemoval2D(ImageAlgorithm):
    """
    ImageIslandRemoval2D - Removes small clusters in masks.
    
    Superclass: ImageAlgorithm
    
    ImageIslandRemoval2D computes the area of separate islands in a
    mask image.  It removes any island that has less than area_threshold
    pixels.  Output has the same scalar_type as input.  It generates the
    whole 2d output image for any output request.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageIslandRemoval2D, obj, update, **traits)
    
    square_neighborhood = tvtk_base.false_bool_trait(help=\
        """
        Set/Get whether to use 4 or 8 neighbors
        """
    )

    def _square_neighborhood_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSquareNeighborhood,
                        self.square_neighborhood_)

    area_threshold = traits.Int(4, enter_set=True, auto_set=False, help=\
        """
        Set/Get the cutoff area for removal
        """
    )

    def _area_threshold_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAreaThreshold,
                        self.area_threshold)

    island_value = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value to remove.
        """
    )

    def _island_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIslandValue,
                        self.island_value)

    replace_value = traits.Float(255.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value to put in the place of removed pixels.
        """
    )

    def _replace_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetReplaceValue,
                        self.replace_value)

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
    (('square_neighborhood', 'GetSquareNeighborhood'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('area_threshold', 'GetAreaThreshold'),
    ('island_value', 'GetIslandValue'), ('replace_value',
    'GetReplaceValue'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'square_neighborhood', 'area_threshold',
    'island_value', 'progress_text', 'replace_value'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageIslandRemoval2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageIslandRemoval2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['square_neighborhood'], [], ['area_threshold', 'island_value',
            'replace_value']),
            title='Edit ImageIslandRemoval2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageIslandRemoval2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

