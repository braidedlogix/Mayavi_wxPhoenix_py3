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

from tvtk.tvtk_classes.render_view_base import RenderViewBase


class RenderView(RenderViewBase):
    """
    RenderView - A view containing a renderer.
    
    Superclass: RenderViewBase
    
    RenderView is a view which contains a Renderer.  You may add
    Actors directly to the renderer, or add certain
    DataRepresentation subclasses to the renderer.  The render view
    supports drag selection with the mouse to select cells.
    
    This class is also the parent class for any more specialized view
    which uses a renderer.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkRenderView, obj, update, **traits)
    
    display_hover_text = tvtk_base.false_bool_trait(help=\
        """
        Whether the view should display hover text.
        """
    )

    def _display_hover_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayHoverText,
                        self.display_hover_text_)

    render_on_mouse_move = tvtk_base.false_bool_trait(help=\
        """
        Whether to render on every mouse move.
        """
    )

    def _render_on_mouse_move_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetRenderOnMouseMove,
                        self.render_on_mouse_move_)

    def get_interaction_mode(self):
        """
        V.get_interaction_mode() -> int
        C++: int GetInteractionMode()"""
        ret = self._vtk_obj.GetInteractionMode()
        return ret
        

    def set_interaction_mode_to_2d(self):
        """
        V.set_interaction_mode_to2d()
        C++: virtual void SetInteractionModeTo2D()
        Set the interaction mode for the view. Choices are:
        RenderView::INTERACTION_MODE_2D - 2d interactor
        RenderView::INTERACTION_MODE_3D - 3d interactor
        """
        self._vtk_obj.SetInteractionModeTo2D()

    def set_interaction_mode_to_3d(self):
        """
        V.set_interaction_mode_to3d()
        C++: virtual void SetInteractionModeTo3D()"""
        self._vtk_obj.SetInteractionModeTo3D()

    label_placement_mode = traits.Trait('no_overlap',
    tvtk_base.TraitRevPrefixMap({'no_overlap': 0, 'all': 1}), help=\
        """
        Label placement mode. NO_OVERLAP uses LabelPlacementMapper,
        which has a faster startup time and works with 2d or 3d labels.
        ALL displays all labels (Warning: This may cause incredibly slow
        render times on datasets with more than a few hundred labels).
        """
    )

    def _label_placement_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelPlacementMode,
                        self.label_placement_mode_)

    label_render_mode = traits.Trait('qt',
    tvtk_base.TraitRevPrefixMap({'qt': 0, 'freetype': 0}), help=\
        """
        Label render mode. FREETYPE uses the freetype label rendering. QT
        uses more advanced Qt-based label rendering.
        """
    )

    def _label_render_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLabelRenderMode,
                        self.label_render_mode_)

    selection_mode = traits.Trait('surface',
    tvtk_base.TraitRevPrefixMap({'surface': 0, 'frustum': 1}), help=\
        """
        Sets the selection mode for the render view. SURFACE selection
        uses HardwareSelector to perform a selection of visible cells.
        FRUSTUM selection just creates a view frustum selection, which
        will select everything in the frustum.
        """
    )

    def _selection_mode_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetSelectionMode,
                        self.selection_mode_)

    display_size = traits.Trait((traits.Undefined, traits.Undefined), traits.Array(shape=(2,), dtype=int, value=(0, 0), cols=2), enter_set=True, auto_set=False, help=\
        """
        
        """
    )

    def _display_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplaySize,
                        self.display_size)

    icon_size = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=int, value=(16, 16), cols=2, help=\
        """
        
        """
    )

    def _icon_size_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIconSize,
                        self.icon_size)

    def _get_icon_texture(self):
        return wrap_vtk(self._vtk_obj.GetIconTexture())
    def _set_icon_texture(self, arg):
        old_val = self._get_icon_texture()
        self._wrap_call(self._vtk_obj.SetIconTexture,
                        deref_vtk(arg))
        self.trait_property_changed('icon_texture', old_val, arg)
    icon_texture = traits.Property(_get_icon_texture, _set_icon_texture, help=\
        """
        Set the icon sheet to use for rendering icons.
        """
    )

    def _get_interactor(self):
        return wrap_vtk(self._vtk_obj.GetInteractor())
    def _set_interactor(self, arg):
        old_val = self._get_interactor()
        self._wrap_call(self._vtk_obj.SetInteractor,
                        deref_vtk(arg))
        self.trait_property_changed('interactor', old_val, arg)
    interactor = traits.Property(_get_interactor, _set_interactor, help=\
        """
        The render window interactor. Note that this requires special
        handling in order to do correctly - see the notes in the detailed
        description of RenderViewBase.
        """
    )

    def _get_interactor_style(self):
        return wrap_vtk(self._vtk_obj.GetInteractorStyle())
    def _set_interactor_style(self, arg):
        old_val = self._get_interactor_style()
        self._wrap_call(self._vtk_obj.SetInteractorStyle,
                        deref_vtk(arg))
        self.trait_property_changed('interactor_style', old_val, arg)
    interactor_style = traits.Property(_get_interactor_style, _set_interactor_style, help=\
        """
        Get the interactor style associated with the render view.
        """
    )

    def _get_render_window(self):
        return wrap_vtk(self._vtk_obj.GetRenderWindow())
    def _set_render_window(self, arg):
        old_val = self._get_render_window()
        self._wrap_call(self._vtk_obj.SetRenderWindow,
                        deref_vtk(arg))
        self.trait_property_changed('render_window', old_val, arg)
    render_window = traits.Property(_get_render_window, _set_render_window, help=\
        """
        Get a handle to the render window.
        """
    )

    def _get_transform(self):
        return wrap_vtk(self._vtk_obj.GetTransform())
    def _set_transform(self, arg):
        old_val = self._get_transform()
        self._wrap_call(self._vtk_obj.SetTransform,
                        deref_vtk(arg))
        self.trait_property_changed('transform', old_val, arg)
    transform = traits.Property(_get_transform, _set_transform, help=\
        """
        Set the view's transform. All RenderedRepresentations added to
        this view should use this transform.
        """
    )

    def add_labels(self, *args):
        """
        V.add_labels(AlgorithmOutput)
        C++: virtual void AddLabels(AlgorithmOutput *conn)
        Add labels from an input connection with an associated text
        property. The output must be a LabelHierarchy (normally the
        output of PointSetToLabelHierarchy).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.AddLabels, *my_args)
        return ret

    def remove_labels(self, *args):
        """
        V.remove_labels(AlgorithmOutput)
        C++: virtual void RemoveLabels(AlgorithmOutput *conn)
        Remove labels from an input connection.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.RemoveLabels, *my_args)
        return ret

    _updateable_traits_ = \
    (('display_hover_text', 'GetDisplayHoverText'),
    ('render_on_mouse_move', 'GetRenderOnMouseMove'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('label_placement_mode', 'GetLabelPlacementMode'),
    ('label_render_mode', 'GetLabelRenderMode'), ('selection_mode',
    'GetSelectionMode'), ('icon_size', 'GetIconSize'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'display_hover_text', 'global_warning_display',
    'render_on_mouse_move', 'label_placement_mode', 'label_render_mode',
    'selection_mode', 'icon_size'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(RenderView, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['display_hover_text', 'render_on_mouse_move'],
            ['label_placement_mode', 'label_render_mode', 'selection_mode'],
            ['icon_size']),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit RenderView properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

