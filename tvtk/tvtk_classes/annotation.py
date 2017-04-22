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

from tvtk.tvtk_classes.data_object import DataObject


class Annotation(DataObject):
    """
    Annotation - Stores a collection of annotation artifacts.
    
    Superclass: DataObject
    
    Annotation is a collection of annotation properties along with an
    associated selection indicating the portion of data the annotation
    refers to.
    
    @par Thanks: Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories contributed code to this class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAnnotation, obj, update, **traits)
    
    def _get_selection(self):
        return wrap_vtk(self._vtk_obj.GetSelection())
    def _set_selection(self, arg):
        old_val = self._get_selection()
        self._wrap_call(self._vtk_obj.SetSelection,
                        deref_vtk(arg))
        self.trait_property_changed('selection', old_val, arg)
    selection = traits.Property(_get_selection, _set_selection, help=\
        """
        The selection to which this set of annotations will apply.
        """
    )

    def COLOR(self):
        """
        V.color() -> InformationDoubleVectorKey
        C++: static InformationDoubleVectorKey *COLOR()
        The color for this annotation. This is stored as an RGB triple
        with values between 0 and 1.
        """
        ret = wrap_vtk(self._vtk_obj.COLOR())
        return ret
        

    def DATA(self):
        """
        V.data() -> InformationDataObjectKey
        C++: static InformationDataObjectKey *DATA()
        Associate a DataObject with this annotation
        """
        ret = wrap_vtk(self._vtk_obj.DATA())
        return ret
        

    def ENABLE(self):
        """
        V.enable() -> InformationIntegerKey
        C++: static InformationIntegerKey *ENABLE()
        Whether or not this annotation is enabled. A value of 1 means
        enabled, 0 disabled.
        """
        ret = wrap_vtk(self._vtk_obj.ENABLE())
        return ret
        

    def HIDE(self):
        """
        V.hide() -> InformationIntegerKey
        C++: static InformationIntegerKey *HIDE()
        Whether or not this annotation is visible.
        """
        ret = wrap_vtk(self._vtk_obj.HIDE())
        return ret
        

    def ICON_INDEX(self):
        """
        V.icon__index() -> InformationIntegerKey
        C++: static InformationIntegerKey *ICON_INDEX()
        An icon index for this annotation.
        """
        ret = wrap_vtk(self._vtk_obj.ICON_INDEX())
        return ret
        

    def LABEL(self):
        """
        V.label() -> InformationStringKey
        C++: static InformationStringKey *LABEL()
        The label for this annotation.
        """
        ret = wrap_vtk(self._vtk_obj.LABEL())
        return ret
        

    def OPACITY(self):
        """
        V.opacity() -> InformationDoubleKey
        C++: static InformationDoubleKey *OPACITY()
        The color for this annotation. This is stored as a value between
        0 and 1.
        """
        ret = wrap_vtk(self._vtk_obj.OPACITY())
        return ret
        

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Annotation, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Annotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit Annotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Annotation properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

