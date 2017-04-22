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


class GeoProjection(Object):
    """
    GeoProjection - Represent a projection from a sphere to a plane
    
    Superclass: Object
    
    This class uses the PROJ.4 library to represent geographic coordinate
    projections.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkGeoProjection, obj, update, **traits)
    
    central_meridian = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/get the longitude which corresponds to the central meridian
        of the projection. This defaults to 0, the Greenwich Meridian.
        """
    )

    def _central_meridian_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCentralMeridian,
                        self.central_meridian)

    name = traits.String('latlong', enter_set=True, auto_set=False, help=\
        """
        Set/get the short name describing the projection you wish to use.
        This defaults to "rpoly" for no reason other than I like it. To
        get a list of valid values, use the get_number_of_projections() and
        get_projection_name(int) static methods.
        """
    )

    def _name_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetName,
                        self.name)

    def _get_description(self):
        return self._vtk_obj.GetDescription()
    description = traits.Property(_get_description, help=\
        """
        Get the description of a projection. This will return NULL if the
        projection name is invalid.
        """
    )

    def _get_index(self):
        return self._vtk_obj.GetIndex()
    index = traits.Property(_get_index, help=\
        """
        Return the index of the current projection's type in the list of
        all projection types. On error, this will return -1. On success,
        it returns a number in [_0,_get_number_of_projections()[.
        """
    )

    def _get_number_of_optional_parameters(self):
        return self._vtk_obj.GetNumberOfOptionalParameters()
    number_of_optional_parameters = traits.Property(_get_number_of_optional_parameters, help=\
        """
        Return the number of optional parameters
        """
    )

    def _get_number_of_projections(self):
        return self._vtk_obj.GetNumberOfProjections()
    number_of_projections = traits.Property(_get_number_of_projections, help=\
        """
        Returns the number of projections that this class offers.
        """
    )

    def get_optional_parameter_key(self, *args):
        """
        V.get_optional_parameter_key(int) -> string
        C++: const char *GetOptionalParameterKey(int index)
        Return the number of optional parameters
        """
        ret = self._wrap_call(self._vtk_obj.GetOptionalParameterKey, *args)
        return ret

    def get_optional_parameter_value(self, *args):
        """
        V.get_optional_parameter_value(int) -> string
        C++: const char *GetOptionalParameterValue(int index)
        Return the number of optional parameters
        """
        ret = self._wrap_call(self._vtk_obj.GetOptionalParameterValue, *args)
        return ret

    def get_projection_description(self, *args):
        """
        V.get_projection_description(int) -> string
        C++: static const char *GetProjectionDescription(int projection)
        Returns a description of one of the projections supported by this
        class.
        @param projection the index of a projection, must be in
            [_0,_get_number_of_projections()[.
        """
        ret = self._wrap_call(self._vtk_obj.GetProjectionDescription, *args)
        return ret

    def get_projection_name(self, *args):
        """
        V.get_projection_name(int) -> string
        C++: static const char *GetProjectionName(int projection)
        Returns the name of one of the projections supported by this
        class. You can pass these strings to set_name(char*).
        @param projection the index of a projection, must be in
            [_0,_get_number_of_projections()[.
        """
        ret = self._wrap_call(self._vtk_obj.GetProjectionName, *args)
        return ret

    def clear_optional_parameters(self):
        """
        V.clear_optional_parameters()
        C++: void ClearOptionalParameters()
        Clear all optional parameters
        """
        ret = self._vtk_obj.ClearOptionalParameters()
        return ret
        

    def remove_optional_parameter(self, *args):
        """
        V.remove_optional_parameter(string)
        C++: void RemoveOptionalParameter(const char *)
        Remove an optional parameter to the projection that will be
        computed
        """
        ret = self._wrap_call(self._vtk_obj.RemoveOptionalParameter, *args)
        return ret

    def set_optional_parameter(self, *args):
        """
        V.set_optional_parameter(string, string)
        C++: void SetOptionalParameter(const char *key, const char *value)
        Add an optional parameter to the projection that will be computed
        or replace it if already present.
        """
        ret = self._wrap_call(self._vtk_obj.SetOptionalParameter, *args)
        return ret

    _updateable_traits_ = \
    (('debug', 'GetDebug'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('central_meridian',
    'GetCentralMeridian'), ('name', 'GetName'), ('reference_count',
    'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'central_meridian', 'name'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(GeoProjection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], ['central_meridian', 'name']),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit GeoProjection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

