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

from tvtk.tvtk_classes.point_set_algorithm import PointSetAlgorithm


class WarpLens(PointSetAlgorithm):
    """
    WarpLens - deform geometry by applying lens distortion
    
    Superclass: PointSetAlgorithm
    
    WarpLens is a filter that modifies point coordinates by moving in
    accord with a lens distortion model.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkWarpLens, obj, update, **traits)
    
    center = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        Specify the center of radial distortion in pixels. This is
        obsoleted by newer instance variables.
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    format_height = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the imager format width / height in mm
        """
    )

    def _format_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFormatHeight,
                        self.format_height)

    format_width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Specify the imager format width / height in mm
        """
    )

    def _format_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFormatWidth,
                        self.format_width)

    image_height = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the image width / height in pixels
        """
    )

    def _image_height_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageHeight,
                        self.image_height)

    image_width = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Specify the image width / height in pixels
        """
    )

    def _image_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetImageWidth,
                        self.image_width)

    k1 = traits.Float(-1e-06, enter_set=True, auto_set=False, help=\
        """
        Specify the symmetric radial distortion parameters for the lens
        """
    )

    def _k1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetK1,
                        self.k1)

    k2 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the symmetric radial distortion parameters for the lens
        """
    )

    def _k2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetK2,
                        self.k2)

    kappa = traits.Float(-1e-06, enter_set=True, auto_set=False, help=\
        """
        Specify second order symmetric radial lens distortion parameter.
        This is obsoleted by newer instance variables.
        """
    )

    def _kappa_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKappa,
                        self.kappa)

    p1 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the decentering distortion parameters for the lens
        """
    )

    def _p1_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetP1,
                        self.p1)

    p2 = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Specify the decentering distortion parameters for the lens
        """
    )

    def _p2_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetP2,
                        self.p2)

    principal_point = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        
        """
    )

    def _principal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPrincipalPoint,
                        self.principal_point)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    def fill_input_port_information(self, *args):
        """
        V.fill_input_port_information(int, Information) -> int
        C++: int FillInputPortInformation(int port, Information *info)
            override;"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.FillInputPortInformation, *my_args)
        return ret

    _updateable_traits_ = \
    (('abort_execute', 'GetAbortExecute'), ('release_data_flag',
    'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('format_height', 'GetFormatHeight'), ('format_width',
    'GetFormatWidth'), ('image_height', 'GetImageHeight'), ('image_width',
    'GetImageWidth'), ('k1', 'GetK1'), ('k2', 'GetK2'), ('kappa',
    'GetKappa'), ('p1', 'GetP1'), ('p2', 'GetP2'), ('principal_point',
    'GetPrincipalPoint'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'center', 'format_height', 'format_width',
    'image_height', 'image_width', 'k1', 'k2', 'kappa', 'p1', 'p2',
    'principal_point', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(WarpLens, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['center', 'format_height', 'format_width',
            'image_height', 'image_width', 'k1', 'k2', 'kappa', 'p1', 'p2',
            'principal_point']),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit WarpLens properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

