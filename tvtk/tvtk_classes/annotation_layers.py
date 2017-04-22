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


class AnnotationLayers(DataObject):
    """
    AnnotationLayers - Stores a ordered collection of annotation sets
    
    Superclass: DataObject
    
    AnnotationLayers stores a vector of annotation layers. Each layer
    may contain any number of Annotation objects. The ordering of the
    layers introduces a prioritization of annotations. Annotations in
    higher layers may obscure annotations in lower layers.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAnnotationLayers, obj, update, **traits)
    
    def _get_current_annotation(self):
        return wrap_vtk(self._vtk_obj.GetCurrentAnnotation())
    def _set_current_annotation(self, arg):
        old_val = self._get_current_annotation()
        self._wrap_call(self._vtk_obj.SetCurrentAnnotation,
                        deref_vtk(arg))
        self.trait_property_changed('current_annotation', old_val, arg)
    current_annotation = traits.Property(_get_current_annotation, _set_current_annotation, help=\
        """
        The current annotation associated with this annotation link.
        """
    )

    def _get_current_selection(self):
        return wrap_vtk(self._vtk_obj.GetCurrentSelection())
    def _set_current_selection(self, arg):
        old_val = self._get_current_selection()
        self._wrap_call(self._vtk_obj.SetCurrentSelection,
                        deref_vtk(arg))
        self.trait_property_changed('current_selection', old_val, arg)
    current_selection = traits.Property(_get_current_selection, _set_current_selection, help=\
        """
        The current selection associated with this annotation link. This
        is simply the selection contained in the current annotation.
        """
    )

    def get_annotation(self, *args):
        """
        V.get_annotation(int) -> Annotation
        C++: Annotation *GetAnnotation(unsigned int idx)
        Retrieve an annotation from a layer.
        """
        ret = self._wrap_call(self._vtk_obj.GetAnnotation, *args)
        return wrap_vtk(ret)

    def _get_number_of_annotations(self):
        return self._vtk_obj.GetNumberOfAnnotations()
    number_of_annotations = traits.Property(_get_number_of_annotations, help=\
        """
        The number of annotations in a specific layer.
        """
    )

    def add_annotation(self, *args):
        """
        V.add_annotation(Annotation)
        C++: void AddAnnotation(Annotation *ann)
        Add an annotation to a layer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddAnnotation, *my_args)
        return ret

    def remove_annotation(self, *args):
        """
        V.remove_annotation(Annotation)
        C++: void RemoveAnnotation(Annotation *ann)
        Remove an annotation from a layer.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveAnnotation, *my_args)
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
            return super(AnnotationLayers, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit AnnotationLayers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], []),
            title='Edit AnnotationLayers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AnnotationLayers properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

