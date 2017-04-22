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

from tvtk.tvtk_classes.composite_data_set import CompositeDataSet


class UniformGridAMR(CompositeDataSet):
    """
    UniformGridAMR - no description provided.
    
    Superclass: CompositeDataSet
    
    UniformGridAMR is a concrete implementation of
    CompositeDataSet. The dataset type is restricted to
    UniformGrid.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUniformGridAMR, obj, update, **traits)
    
    def get_data_set(self, *args):
        """
        V.get_data_set(CompositeDataIterator) -> DataObject
        C++: DataObject *GetDataSet(CompositeDataIterator *iter)
            override;
        V.get_data_set(int, int) -> UniformGrid
        C++: UniformGrid *GetDataSet(unsigned int level,
            unsigned int idx)
        Return the data set pointed to by iter
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetDataSet, *my_args)
        return wrap_vtk(ret)

    def set_data_set(self, *args):
        """
        V.set_data_set(CompositeDataIterator, DataObject)
        C++: void SetDataSet(CompositeDataIterator *iter,
            DataObject *dataObj) override;
        V.set_data_set(int, int, UniformGrid)
        C++: virtual void SetDataSet(unsigned int level, unsigned int idx,
             UniformGrid *grid)
        Unhiding superclass method.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetDataSet, *my_args)
        return ret

    grid_description = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the data description of this uniform grid instance, e.g.
        VTK_XYZ_GRID
        """
    )

    def _grid_description_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetGridDescription,
                        self.grid_description)

    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Retrieve the bounds of the AMR domain
        """
    )

    def get_composite_index(self, *args):
        """
        V.get_composite_index(int, int) -> int
        C++: int GetCompositeIndex(const unsigned int level,
            const unsigned int index)
        Retrieves the composite index  associated with the data at the
        given (level,index) pair.
        """
        ret = self._wrap_call(self._vtk_obj.GetCompositeIndex, *args)
        return ret

    def get_level_and_index(self, *args):
        """
        V.get_level_and_index(int, int, int)
        C++: void GetLevelAndIndex(const unsigned int compositeIdx,
            unsigned int &level, unsigned int &idx)
        Givenes the composite Idx (as set by set_composite_idx) this method
        returns the corresponding level and dataset index within the
        level.
        """
        ret = self._wrap_call(self._vtk_obj.GetLevelAndIndex, *args)
        return ret

    def get_max(self, *args):
        """
        V.get_max([float, float, float])
        C++: void GetMax(double max[3])
        Retrieve the bounds of the AMR domain
        """
        ret = self._wrap_call(self._vtk_obj.GetMax, *args)
        return ret

    def get_min(self, *args):
        """
        V.get_min([float, float, float])
        C++: void GetMin(double min[3])
        Retrieve the bounds of the AMR domain
        """
        ret = self._wrap_call(self._vtk_obj.GetMin, *args)
        return ret

    def get_number_of_data_sets(self, *args):
        """
        V.get_number_of_data_sets(int) -> int
        C++: unsigned int GetNumberOfDataSets(const unsigned int level)
        Returns the number of datasets at the given level, including null
        blocks
        """
        ret = self._wrap_call(self._vtk_obj.GetNumberOfDataSets, *args)
        return ret

    def _get_number_of_levels(self):
        return self._vtk_obj.GetNumberOfLevels()
    number_of_levels = traits.Property(_get_number_of_levels, help=\
        """
        Return the number of levels
        """
    )

    def _get_total_number_of_blocks(self):
        return self._vtk_obj.GetTotalNumberOfBlocks()
    total_number_of_blocks = traits.Property(_get_total_number_of_blocks, help=\
        """
        Return the total number of blocks, including NULL blocks
        """
    )

    _updateable_traits_ = \
    (('global_release_data_flag', 'GetGlobalReleaseDataFlag'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('grid_description', 'GetGridDescription'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_release_data_flag', 'global_warning_display',
    'grid_description'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UniformGridAMR, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UniformGridAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['global_release_data_flag'], [], ['grid_description']),
            title='Edit UniformGridAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UniformGridAMR properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

