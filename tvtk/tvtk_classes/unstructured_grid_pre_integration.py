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

from tvtk.tvtk_classes.unstructured_grid_volume_ray_integrator import UnstructuredGridVolumeRayIntegrator


class UnstructuredGridPreIntegration(UnstructuredGridVolumeRayIntegrator):
    """
    UnstructuredGridPreIntegration - performs ray integration with
    pre-integration tables.
    
    Superclass: UnstructuredGridVolumeRayIntegrator
    
    UnstructuredGridPreIntegration performs ray integration by looking
    into a precomputed table.  The result should be equivalent to that
    computed by UnstructuredGridLinearRayIntegrator and
    UnstructuredGridPartialPreIntegration, but faster than either one.
    The pre-integration algorithm was first introduced by Roettger,
    Kraus, and Ertl in "Hardware-Accelerated Volume And Isosurface
    Rendering Based On Cell-Projection."
    
    Due to table size limitations, a table can only be indexed by
    independent scalars.  Thus, dependent scalars are not supported.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkUnstructuredGridPreIntegration, obj, update, **traits)
    
    incremental_pre_integration = tvtk_base.true_bool_trait(help=\
        """
        Get/set whether to use incremental pre-integration (by default
        it's on).  Incremental pre-integration is much faster but can
        introduce error due to numerical imprecision.  Under most
        circumstances, the error is not noticeable.
        """
    )

    def _incremental_pre_integration_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIncrementalPreIntegration,
                        self.incremental_pre_integration_)

    integration_table_length_resolution = traits.Int(256, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the integration table built.
        """
    )

    def _integration_table_length_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationTableLengthResolution,
                        self.integration_table_length_resolution)

    integration_table_scalar_resolution = traits.Int(128, enter_set=True, auto_set=False, help=\
        """
        Set/Get the size of the integration table built.
        """
    )

    def _integration_table_scalar_resolution_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetIntegrationTableScalarResolution,
                        self.integration_table_scalar_resolution)

    def _get_integrator(self):
        return wrap_vtk(self._vtk_obj.GetIntegrator())
    def _set_integrator(self, arg):
        old_val = self._get_integrator()
        self._wrap_call(self._vtk_obj.SetIntegrator,
                        deref_vtk(arg))
        self.trait_property_changed('integrator', old_val, arg)
    integrator = traits.Property(_get_integrator, _set_integrator, help=\
        """
        The class used to fill the pre integration table.  By default, a
        UnstructuredGridPartialPreIntegration is built.
        """
    )

    def get_indexed_table_entry(self, *args):
        """
        V.get_indexed_table_entry(int, int, int, int) -> (float, ...)
        C++: float *GetIndexedTableEntry(int scalar_front_index,
            int scalar_back_index, int length_index, int component=0)
        Like get_table_entry, except the inputs are scaled indices into the
        table rather than than the actual scalar and length values.  Use
        get_table_entry unless you are really sure you know what you are
        doing.
        """
        ret = self._wrap_call(self._vtk_obj.GetIndexedTableEntry, *args)
        return ret

    def _get_integration_table_length_scale(self):
        return self._vtk_obj.GetIntegrationTableLengthScale()
    integration_table_length_scale = traits.Property(_get_integration_table_length_scale, help=\
        """
        Get how an integration table is indexed.
        """
    )

    def get_integration_table_scalar_scale(self, *args):
        """
        V.get_integration_table_scalar_scale(int) -> float
        C++: virtual double GetIntegrationTableScalarScale(
            int component=0)
        Get how an integration table is indexed.
        """
        ret = self._wrap_call(self._vtk_obj.GetIntegrationTableScalarScale, *args)
        return ret

    def get_integration_table_scalar_shift(self, *args):
        """
        V.get_integration_table_scalar_shift(int) -> float
        C++: virtual double GetIntegrationTableScalarShift(
            int component=0)
        Get how an integration table is indexed.
        """
        ret = self._wrap_call(self._vtk_obj.GetIntegrationTableScalarShift, *args)
        return ret

    def get_pre_integration_table(self, *args):
        """
        V.get_pre_integration_table(int) -> (float, ...)
        C++: virtual float *GetPreIntegrationTable(int component=0)
        Get the partial pre-integration table for the given scalar
        component. The tables are built when Initialize is called.  A
        segment of length d with a front scalar of sf and a back scalar
        of sb is referenced in the resulting table as 4 * ((l *
        integration_table_length_scale) * \c
        integration_table_scalar_resolution *
        integration_table_scalar_resolution + (sb *
        integration_table_scalar_scale + \c integration_table_scalar_shift) *
        integration_table_scalar_resolution + (sf *
        integration_table_scalar_scale + \c integration_table_scalar_shift)).
        """
        ret = self._wrap_call(self._vtk_obj.GetPreIntegrationTable, *args)
        return ret

    def get_table_entry(self, *args):
        """
        V.get_table_entry(float, float, float, int) -> (float, ...)
        C++: float *GetTableEntry(double scalar_front, double scalar_back,
             double lenth, int component=0)
        Get an entry (RGBA) in one of the pre-integration tables.  The
        tables are built when Intialize is called.
        """
        ret = self._wrap_call(self._vtk_obj.GetTableEntry, *args)
        return ret

    _updateable_traits_ = \
    (('incremental_pre_integration', 'GetIncrementalPreIntegration'),
    ('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('integration_table_length_resolution',
    'GetIntegrationTableLengthResolution'),
    ('integration_table_scalar_resolution',
    'GetIntegrationTableScalarResolution'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'incremental_pre_integration',
    'integration_table_length_resolution',
    'integration_table_scalar_resolution'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(UnstructuredGridPreIntegration, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit UnstructuredGridPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['incremental_pre_integration'], [],
            ['integration_table_length_resolution',
            'integration_table_scalar_resolution']),
            title='Edit UnstructuredGridPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit UnstructuredGridPreIntegration properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

