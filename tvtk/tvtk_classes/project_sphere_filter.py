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


class ProjectSphereFilter(PointSetAlgorithm):
    """
    ProjectSphereFilter - A filter to 'unroll' a sphere.
    
    Superclass: PointSetAlgorithm
    
    The unroll longitude is -180.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkProjectSphereFilter, obj, update, **traits)
    
    keep_pole_points = tvtk_base.false_bool_trait(help=\
        """
        Specify whether or not to keep the cells using a point at a pole.
        The default is false.
        """
    )

    def _keep_pole_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetKeepPolePoints,
                        self.keep_pole_points_)

    translate_z = tvtk_base.false_bool_trait(help=\
        """
        Specify whether (true) or not to translate the points in the
        projected transformation such that the input point with the
        smallest radius is at 0. The default is false.
        """
    )

    def _translate_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslateZ,
                        self.translate_z_)

    center = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        
        """
    )

    def _center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCenter,
                        self.center)

    def _get_input(self):
        return wrap_vtk(self._vtk_obj.GetInput())
    input = traits.Property(_get_input, help=\
        """
        
        """
    )

    _updateable_traits_ = \
    (('keep_pole_points', 'GetKeepPolePoints'), ('translate_z',
    'GetTranslateZ'), ('abort_execute', 'GetAbortExecute'),
    ('release_data_flag', 'GetReleaseDataFlag'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('center',
    'GetCenter'), ('progress', 'GetProgress'), ('progress_text',
    'GetProgressText'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'keep_pole_points', 'release_data_flag', 'translate_z', 'center',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ProjectSphereFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ProjectSphereFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['keep_pole_points', 'translate_z'], [], ['center']),
            title='Edit ProjectSphereFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ProjectSphereFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

