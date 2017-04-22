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


class Points(Object):
    """
    Points - represent and manipulate 3d points
    
    Superclass: Object
    
    Points represents 3d points. The data model for Points is an
    array of vx-vy-vz triplets accessible by (point or cell) id.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPoints, obj, update, **traits)
    
    data_type = traits.Trait('float',
    tvtk_base.TraitRevPrefixMap({'float': 10, 'bit': 1, 'char': 2, 'double': 11, 'int': 6, 'long': 8, 'short': 4, 'unsigned_char': 3, 'unsigned_int': 7, 'unsigned_long': 9, 'unsigned_short': 5}), help=\
        """
        Specify the underlying data type of the object.
        """
    )

    def _data_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDataType,
                        self.data_type_)

    def _get_data(self):
        return wrap_vtk(self._vtk_obj.GetData())
    def _set_data(self, arg):
        old_val = self._get_data()
        my_arg = deref_array([arg], [['vtkDataArray']])
        self._wrap_call(self._vtk_obj.SetData,
                        my_arg[0])
        self.trait_property_changed('data', old_val, arg)
    data = traits.Property(_get_data, _set_data, help=\
        """
        
        """
    )

    number_of_points = traits.Int(0, enter_set=True, auto_set=False, help=\
        """
        Specify the number of points for this object to hold. Does an
        allocation as well as setting the max_id ivar. Used in conjunction
        with set_point() method for fast insertion.
        """
    )

    def _number_of_points_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetNumberOfPoints,
                        self.number_of_points)

    def get_point(self, *args):
        """
        V.get_point(int) -> (float, float, float)
        C++: double *GetPoint(IdType id)
        V.get_point(int, [float, float, float])
        C++: void GetPoint(IdType id, double x[3])
        Return a pointer to a double point x[3] for a specific id.
        WARNING: Just don't use this error-prone method, the returned
        pointer and its values are only valid as long as another method
        invocation is not performed. Prefer get_point() with the return
        value in argument.
        """
        ret = self._wrap_call(self._vtk_obj.GetPoint, *args)
        return ret

    def set_point(self, *args):
        """
        V.set_point(int, (float, float, float))
        C++: void SetPoint(IdType id, const double x[3])
        V.set_point(int, float, float, float)
        C++: void SetPoint(IdType id, double x, double y, double z)"""
        ret = self._wrap_call(self._vtk_obj.SetPoint, *args)
        return ret

    def _get_actual_memory_size(self):
        return self._vtk_obj.GetActualMemorySize()
    actual_memory_size = traits.Property(_get_actual_memory_size, help=\
        """
        Return the memory in kibibytes (1024 bytes) consumed by this
        attribute data. Used to support streaming and reading/writing
        data. The value returned is guaranteed to be greater than or
        equal to the memory required to actually represent the data
        represented by this object. The information returned is valid
        only after the pipeline has been updated.
        """
    )

    def _get_bounds(self):
        return self._vtk_obj.GetBounds()
    bounds = traits.Property(_get_bounds, help=\
        """
        Return the bounds of the points.
        """
    )

    def get_points(self, *args):
        """
        V.get_points(IdList, Points)
        C++: void GetPoints(IdList *ptId, Points *fp)
        Given a list of pt ids, return an array of points.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.GetPoints, *my_args)
        return ret

    def get_void_pointer(self, *args):
        """
        V.get_void_pointer(int) -> void
        C++: void *GetVoidPointer(const int id)
        Return a void pointer. For image pipeline interface and other
        special pointer manipulation.
        """
        ret = self._wrap_call(self._vtk_obj.GetVoidPointer, *args)
        return ret

    def allocate(self, *args):
        """
        V.allocate(int, int) -> int
        C++: virtual int Allocate(const IdType sz,
            const IdType ext=1000)
        Allocate initial memory size. ext is no longer used.
        """
        ret = self._wrap_call(self._vtk_obj.Allocate, *args)
        return ret

    def compute_bounds(self):
        """
        V.compute_bounds()
        C++: virtual void ComputeBounds()
        Determine (xmin,xmax, ymin,ymax, zmin,zmax) bounds of points.
        """
        ret = self._vtk_obj.ComputeBounds()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(Points)
        C++: virtual void DeepCopy(Points *ad)
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def initialize(self):
        """
        V.initialize()
        C++: virtual void Initialize()
        Return object to instantiated state.
        """
        ret = self._vtk_obj.Initialize()
        return ret
        

    def insert_next_point(self, *args):
        """
        V.insert_next_point((float, float, float)) -> int
        C++: IdType InsertNextPoint(const double x[3])
        V.insert_next_point(float, float, float) -> int
        C++: IdType InsertNextPoint(double x, double y, double z)"""
        ret = self._wrap_call(self._vtk_obj.InsertNextPoint, *args)
        return ret

    def insert_point(self, *args):
        """
        V.insert_point(int, (float, float, float))
        C++: void InsertPoint(IdType id, const double x[3])
        V.insert_point(int, float, float, float)
        C++: void InsertPoint(IdType id, double x, double y, double z)
        Insert point into object. Range checking performed and memory
        allocated as necessary.
        """
        ret = self._wrap_call(self._vtk_obj.InsertPoint, *args)
        return ret

    def insert_points(self, *args):
        """
        V.insert_points(IdList, IdList, Points)
        C++: void InsertPoints(IdList *dstIds, IdList *srcIds,
            Points *source)
        V.insert_points(int, int, int, Points)
        C++: void InsertPoints(IdType dstStart, IdType n,
            IdType srcStart, Points *source)
        Copy the points indexed in src_ids from the source array to the
        tuple locations indexed by dst_ids in this array. Note that memory
        allocation is performed as necessary to hold the data.
        """
        my_args = deref_array(args, [('vtkIdList', 'vtkIdList', 'vtkPoints'), ('int', 'int', 'int', 'vtkPoints')])
        ret = self._wrap_call(self._vtk_obj.InsertPoints, *my_args)
        return ret

    def reset(self):
        """
        V.reset()
        C++: virtual void Reset()
        Make object look empty but do not delete memory.
        """
        ret = self._vtk_obj.Reset()
        return ret
        

    def resize(self, *args):
        """
        V.resize(int) -> int
        C++: int Resize(IdType numPoints)
        Resize the internal array while conserving the data.  Returns 1
        if resizing succeeded and 0 otherwise.
        """
        ret = self._wrap_call(self._vtk_obj.Resize, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Points)
        C++: virtual void ShallowCopy(Points *ad)
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        my_args = deref_array(args, [['vtkPoints']])
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def squeeze(self):
        """
        V.squeeze()
        C++: virtual void Squeeze()
        Reclaim any extra memory.
        """
        ret = self._vtk_obj.Squeeze()
        return ret
        

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('data_type', 'GetDataType'),
    ('number_of_points', 'GetNumberOfPoints'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'data_type', 'number_of_points'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Points, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Points properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], ['data_type'], ['number_of_points']),
            title='Edit Points properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Points properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
    def __len__(self):
        return self._vtk_obj.GetNumberOfPoints()
    
    def __iter__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfPoints()
        for i in range(n):
            yield obj.GetPoint(i)
    
    def _check_key(self, key, n):
        ##############################################
        # Allow int and long keys. Fixes GH Issue 173.
        ##############################################
        if not isinstance(key, (int, long)):
            raise TypeError("Only int and long are valid keys.")
        if key < 0:
            key =  n + key
        if key < 0 or key >= n:
            raise IndexError("Index %s out of range."%key)
        return key
    
    def __getitem__(self, key):
        obj = self._vtk_obj
        n = obj.GetNumberOfPoints()
        key = self._check_key(key, n)
        return obj.GetPoint(key)
    
    def __setitem__(self, key, val):
        obj = self._vtk_obj
        n = obj.GetNumberOfPoints()
        key = self._check_key(key, n)
        obj.SetPoint(key, val)
    
    def __repr__(self):
        obj = self._vtk_obj
        n = obj.GetNumberOfPoints()
        if n <= 10:
            return repr([x for x in self])
        else:
            meth = obj.GetPoint
            return '[%s, ..., %s], length = %s'%(meth(0),
                                                 meth(n-1), n)
    
    def append(self, val):
        self._vtk_obj.InsertNextPoint(val)
        self.update_traits()
    
    def extend(self, arr):
        obj = self._vtk_obj
        for i in arr:
            obj.InsertNextPoint(i)
        self.update_traits()
    
    def from_array(self, arr):
        '''Set the value of the data array using the passed
        Numeric array or Python list.  This is implemented
        efficiently.
        '''
        array_handler.array2vtkPoints(arr, self._vtk_obj)
        self.update_traits()
    
    def to_array(self):
        '''Return the object as a Numeric array.'''
        return array_handler.vtk2array(self._vtk_obj.GetData())
    

