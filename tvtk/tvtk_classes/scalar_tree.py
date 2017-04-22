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


class ScalarTree(Object):
    """
    ScalarTree - organize data according to scalar values (used to
    accelerate contouring operations)
    
    Superclass: Object
    
    ScalarTree is an abstract class that defines the API to concrete
    scalar tree subclasses. A scalar tree is a data structure that
    organizes data according to its scalar value. This allows rapid
    access to data for those algorithms that access the data based on
    scalar value. For example, isocontouring operates on cells based on
    the scalar (isocontour) value.
    
    To use subclasses of this class, you must specify a dataset to
    operate on, and then specify a scalar value in the init_traversal()
    method. Then calls to get_next_cell() return cells whose scalar data
    contains the scalar value specified. (This describes serial
    traversal.)
    
    Methods supporting parallel traversal (such as threading) are also
    supported. Basically thread-safe batches of cells (which are a
    portion of the whole dataset) are available for processing using a
    parallel For() operation. First request the number of batches, and
    then for each batch, retrieve the array of cell ids in that batch.
    These batches contain cell ids that are likely to contain the
    isosurface.
    
    @sa
    SimpleScalarTree SpanSpace
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkScalarTree, obj, update, **traits)
    
    def _get_data_set(self):
        return wrap_vtk(self._vtk_obj.GetDataSet())
    def _set_data_set(self, arg):
        old_val = self._get_data_set()
        self._wrap_call(self._vtk_obj.SetDataSet,
                        deref_vtk(arg))
        self.trait_property_changed('data_set', old_val, arg)
    data_set = traits.Property(_get_data_set, _set_data_set, help=\
        """
        Build the tree from the points/cells and scalars defining this
        dataset.
        """
    )

    def _get_scalars(self):
        return wrap_vtk(self._vtk_obj.GetScalars())
    def _set_scalars(self, arg):
        old_val = self._get_scalars()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetScalars,
                        my_arg[0])
        self.trait_property_changed('scalars', old_val, arg)
    scalars = traits.Property(_get_scalars, _set_scalars, help=\
        """
        Build the tree from the points/cells and scalars defining the
        dataset and scalars provided. Typically the scalars come from the
        DataSet specified, but sometimes a separate DataArray is
        provided to specify the scalars. If the scalar array is
        explicitly set, then it takes precedence over the scalars held in
        the DataSet.
        """
    )

    def get_cell_batch(self, *args):
        """
        V.get_cell_batch(int, int) -> (int, ...)
        C++: virtual const IdType *GetCellBatch(IdType batchNum,
            IdType &numCells)
        Return the array of cell ids in the specified batch. The method
        also returns the number of cell ids in the array. Make sure to
        call init_traversal() beforehand.
        """
        ret = self._wrap_call(self._vtk_obj.GetCellBatch, *args)
        return ret

    def _get_number_of_cell_batches(self):
        return self._vtk_obj.GetNumberOfCellBatches()
    number_of_cell_batches = traits.Property(_get_number_of_cell_batches, help=\
        """
        Get the number of cell batches available for processing. Note
        that this methods should be called after init_traversal(). This is
        because the number of batches available is typically a function
        of the isocontour value. Note that the cells found in
        [_0...(_number_of_cell_batches-_1)] will contain all the cells
        potentially containing the isocontour.
        """
    )

    def _get_scalar_value(self):
        return self._vtk_obj.GetScalarValue()
    scalar_value = traits.Property(_get_scalar_value, help=\
        """
        Return the current scalar value over which tree traversal is
        proceeding. This is the scalar value provided in init_traversal().
        """
    )

    def build_tree(self):
        """
        V.build_tree()
        C++: virtual void BuildTree()
        Construct the scalar tree from the dataset provided. Checks build
        times and modified time from input and reconstructs the tree if
        necessary.
        """
        ret = self._vtk_obj.BuildTree()
        return ret
        

    def init_traversal(self, *args):
        """
        V.init_traversal(float)
        C++: virtual void InitTraversal(double scalarValue)
        Begin to traverse the cells based on a scalar value. Returned
        cells will have scalar values that span the scalar value
        specified. Note that changing the scalar_value does not cause the
        scalar tree to be modified, and hence it does not rebuild.
        """
        ret = self._wrap_call(self._vtk_obj.InitTraversal, *args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Initialize locator. Frees memory and resets object as
        appropriate.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ScalarTree, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ScalarTree properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

