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

from tvtk.tvtk_classes.object import Object


class TDxInteractorStyleSettings(Object):
    """
    TDxInteractorStyleSettings - 3d_connexion device settings
    
    Superclass: Object
    
    TDxInteractorStyleSettings defines settings for 3d_connexion device
    such as sensitivity, axis filters
    
    @sa
    InteractorStyle RenderWindowInteractor TDxInteractorStyle
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkTDxInteractorStyleSettings, obj, update, **traits)
    
    angle_sensitivity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Sensitivity of the rotation angle. This can be any value:
        positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no rotation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster
        """
    )

    def _angle_sensitivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAngleSensitivity,
                        self.angle_sensitivity)

    translation_x_sensitivity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Sensitivity of the translation along the X-axis. This can be any
        value: positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no translation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster Initial value is 1.0
        """
    )

    def _translation_x_sensitivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationXSensitivity,
                        self.translation_x_sensitivity)

    translation_y_sensitivity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Sensitivity of the translation along the Y-axis. See comment of
        set_translation_x_sensitivity().
        """
    )

    def _translation_y_sensitivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationYSensitivity,
                        self.translation_y_sensitivity)

    translation_z_sensitivity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Sensitivity of the translation along the Z-axis. See comment of
        set_translation_x_sensitivity().
        """
    )

    def _translation_z_sensitivity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetTranslationZSensitivity,
                        self.translation_z_sensitivity)

    use_rotation_x = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Use or mask the rotation component around the X-axis. Initial
        value is true.
        """
    )

    def _use_rotation_x_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRotationX,
                        self.use_rotation_x)

    use_rotation_y = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Use or mask the rotation component around the Y-axis. Initial
        value is true.
        """
    )

    def _use_rotation_y_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRotationY,
                        self.use_rotation_y)

    use_rotation_z = traits.Bool(True, enter_set=True, auto_set=False, help=\
        """
        Use or mask the rotation component around the Z-axis. Initial
        value is true.
        """
    )

    def _use_rotation_z_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseRotationZ,
                        self.use_rotation_z)

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('angle_sensitivity',
    'GetAngleSensitivity'), ('translation_x_sensitivity',
    'GetTranslationXSensitivity'), ('translation_y_sensitivity',
    'GetTranslationYSensitivity'), ('translation_z_sensitivity',
    'GetTranslationZSensitivity'), ('use_rotation_x', 'GetUseRotationX'),
    ('use_rotation_y', 'GetUseRotationY'), ('use_rotation_z',
    'GetUseRotationZ'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'angle_sensitivity',
    'translation_x_sensitivity', 'translation_y_sensitivity',
    'translation_z_sensitivity', 'use_rotation_x', 'use_rotation_y',
    'use_rotation_z'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(TDxInteractorStyleSettings, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit TDxInteractorStyleSettings properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['angle_sensitivity', 'translation_x_sensitivity',
            'translation_y_sensitivity', 'translation_z_sensitivity',
            'use_rotation_x', 'use_rotation_y', 'use_rotation_z']),
            title='Edit TDxInteractorStyleSettings properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit TDxInteractorStyleSettings properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

