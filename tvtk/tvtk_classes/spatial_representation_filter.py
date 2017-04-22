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

from tvtk.tvtk_classes.multi_block_data_set_algorithm import MultiBlockDataSetAlgorithm


class SpatialRepresentationFilter(MultiBlockDataSetAlgorithm):
    """
    SpatialRepresentationFilter - generate polygonal model of spatial
    search object (i.e., a Locator)
    
    Superclass: MultiBlockDataSetAlgorithm
    
    SpatialRepresentationFilter generates an polygonal representation
    of a spatial search (vtk_locator) object. The representation varies
    depending upon the nature of the spatial search object. For example,
    the representation for OBBTree is a collection of oriented
    bounding boxes. This input to this filter is a dataset of any type,
    and the output is polygonal data. You must also specify the spatial
    search object to use.
    
    Generally spatial search objects are used for collision detection and
    other geometric operations, but in this filter one or more levels of
    spatial searchers can be generated to form a geometric approximation
    to the input data. This is a form of data simplification, generally
    used to accelerate the rendering process. Or, this filter can be used
    as a debugging/ visualization aid for spatial search objects.
    
    This filter can generate one or more  PolyData blocks
    corresponding to different levels in the spatial search tree. The
    block ids range from 0 (root level) to maximum_level. Note that the
    block for level "id" is not computed unless a add_level(id) method is
    issued. Thus, if you desire three levels of output (say 2,4,7), you
    would have to invoke add_level(_2), add_level(_4), and add_level(_7). If
    generate_leaves is set to true (off by default), all leaf nodes of the
    locator (which may be at different levels) are computed and stored in
    block with id maximum_level + 1.
    
    @sa
    Locator PointLocator CellLocator OBBTree
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkSpatialRepresentationFilter, obj, update, **traits)
    
    generate_leaves = tvtk_base.false_bool_trait(help=\
        """
        Turn on/off the generation of leaf nodes. Off by default.
        """
    )

    def _generate_leaves_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGenerateLeaves,
                        self.generate_leaves_)

    def _get_spatial_representation(self):
        return wrap_vtk(self._vtk_obj.GetSpatialRepresentation())
    def _set_spatial_representation(self, arg):
        old_val = self._get_spatial_representation()
        self._wrap_call(self._vtk_obj.SetSpatialRepresentation,
                        deref_vtk(arg))
        self.trait_property_changed('spatial_representation', old_val, arg)
    spatial_representation = traits.Property(_get_spatial_representation, _set_spatial_representation, help=\
        """
        Set/Get the locator that will be used to generate the
        representation.
        """
    )

    def _get_maximum_level(self):
        return self._vtk_obj.GetMaximumLevel()
    maximum_level = traits.Property(_get_maximum_level, help=\
        """
        Get the maximum level that is available. Populated during
        request_data().
        """
    )

    def add_level(self, *args):
        """
        V.add_level(int)
        C++: void AddLevel(int level)
        Add a level to be computed.
        """
        ret = self._wrap_call(self._vtk_obj.AddLevel, *args)
        return ret

    def reset_levels(self):
        """
        V.reset_levels()
        C++: void ResetLevels()
        Remove all levels.
        """
        ret = self._vtk_obj.ResetLevels()
        return ret
        

    _updateable_traits_ = \
    (('generate_leaves', 'GetGenerateLeaves'), ('abort_execute',
    'GetAbortExecute'), ('release_data_flag', 'GetReleaseDataFlag'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress', 'GetProgress'),
    ('progress_text', 'GetProgressText'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'generate_leaves',
    'global_warning_display', 'release_data_flag', 'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(SpatialRepresentationFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['generate_leaves'], [], []),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit SpatialRepresentationFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

