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


class ImageSeedConnectivity(ImageAlgorithm):
    """
    ImageSeedConnectivity - seed_connectivity with user defined seeds.
    
    Superclass: ImageAlgorithm
    
    ImageSeedConnectivity marks pixels connected to user supplied
    seeds. The input must be unsigned char, and the output is also
    unsigned char.  If a seed supplied by the user does not have pixel
    value "_input_true_value", then the image is scanned +x, +y, +z until a
    pixel is encountered with value "_input_true_value".  This new pixel is
    used as the seed .  Any pixel with out value "_input_true_value" is
    consider off.  The output pixels values are 0 for any off pixel in
    input, "_output_true_value" for any pixels connected to seeds, and
    "_output_unconnected_value" for any on pixels not connected to seeds. 
    The same seeds are used for all images in the image set.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageSeedConnectivity, obj, update, **traits)
    
    dimensionality = traits.Int(3, enter_set=True, auto_set=False, help=\
        """
        Set the number of axes to use in connectivity.
        """
    )

    def _dimensionality_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDimensionality,
                        self.dimensionality)

    input_connect_value = traits.Int(255, enter_set=True, auto_set=False, help=\
        """
        Set/Get what value is considered as connecting pixels.
        """
    )

    def _input_connect_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetInputConnectValue,
                        self.input_connect_value)

    output_connected_value = traits.Int(255, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value to set connected pixels to.
        """
    )

    def _output_connected_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputConnectedValue,
                        self.output_connected_value)

    output_unconnected_value = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value to set unconnected pixels to.
        """
    )

    def _output_unconnected_value_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOutputUnconnectedValue,
                        self.output_unconnected_value)

    def _get_connector(self):
        return wrap_vtk(self._vtk_obj.GetConnector())
    connector = traits.Property(_get_connector, help=\
        """
        Get the ImageCOnnector used by this filter.
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

    def add_seed(self, *args):
        """
        V.add_seed(int, [int, ...])
        C++: void AddSeed(int num, int *index)
        V.add_seed(int, int, int)
        C++: void AddSeed(int i0, int i1, int i2)
        V.add_seed(int, int)
        C++: void AddSeed(int i0, int i1)
        Methods for manipulating the seed pixels.
        """
        ret = self._wrap_call(self._vtk_obj.AddSeed, *args)
        return ret

    def remove_all_seeds(self):
        """
        V.remove_all_seeds()
        C++: void RemoveAllSeeds()
        Methods for manipulating the seed pixels.
        """
        ret = self._vtk_obj.RemoveAllSeeds()
        return ret
        

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('dimensionality', 'GetDimensionality'), ('input_connect_value',
    'GetInputConnectValue'), ('output_connected_value',
    'GetOutputConnectedValue'), ('output_unconnected_value',
    'GetOutputUnconnectedValue'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimensionality', 'input_connect_value',
    'output_connected_value', 'output_unconnected_value',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageSeedConnectivity, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageSeedConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['dimensionality', 'input_connect_value',
            'output_connected_value', 'output_unconnected_value']),
            title='Edit ImageSeedConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageSeedConnectivity properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

