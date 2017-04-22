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


class Camera(Object):
    """
    Camera - a virtual camera for 3d rendering
    
    Superclass: Object
    
    Camera is a virtual camera for 3d rendering. It provides methods
    to position and orient the view point and focal point. Convenience
    methods for moving about the focal point also are provided. More
    complex methods allow the manipulation of the computer graphics model
    including view up vector, clipping planes, and camera perspective.
    @sa
    PerspectiveTransform
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkCamera, obj, update, **traits)
    
    parallel_projection = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the value of the parallel_projection instance variable.
        This determines if the camera should do a perspective or parallel
        projection.
        """
    )

    def _parallel_projection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParallelProjection,
                        self.parallel_projection_)

    use_horizontal_view_angle = tvtk_base.false_bool_trait(help=\
        """
        Set/Get the value of the use_horizontal_view_angle instance
        variable. If set, the camera's view angle represents a horizontal
        view angle, rather than the default vertical view angle. This is
        useful if the application uses a display device which whose specs
        indicate a particular horizontal view angle, or if the
        application varies the window height but wants to keep the
        perspective transform unchanges.
        """
    )

    def _use_horizontal_view_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseHorizontalViewAngle,
                        self.use_horizontal_view_angle_)

    use_off_axis_projection = tvtk_base.false_bool_trait(help=\
        """
        Set/Get use offaxis frustum. off_axis frustum is used for off-axis
        frustum calculations specificly for stereo rendering. For
        reference see "High Resolution Virtual Reality", in Proc.
        SIGGRAPH '92, Computer Graphics, pages 195-202, 1992.
        """
    )

    def _use_off_axis_projection_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseOffAxisProjection,
                        self.use_off_axis_projection_)

    clipping_range = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.01, 1000.01), cols=2, help=\
        """
        Set/Get the location of the near and far clipping planes along
        the direction of projection.  Both of these values must be
        positive. How the clipping planes are set can have a large impact
        on how well z-buffering works.  In particular the front clipping
        plane can make a very big difference. Setting it to 0.01 when it
        really could be 1.0 can have a big impact on your z-buffer
        resolution farther away.  The default clipping range is
        (0.1,1000). Clipping distance is measured in world coordinate
        unless a scale factor exists in camera's model_transform_matrix.
        """
    )

    def _clipping_range_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClippingRange,
                        self.clipping_range)

    distance = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Move the focal point so that it is the specified distance from
        the camera position.  This distance must be positive.
        """
    )

    def _distance_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDistance,
                        self.distance)

    eye_angle = traits.Float(2.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the separation between eyes (in degrees). This is used
        when generating stereo images.
        """
    )

    def _eye_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEyeAngle,
                        self.eye_angle)

    def get_eye_position(self, *args):
        """
        V.get_eye_position([float, float, float])
        C++: void GetEyePosition(double eyePosition[3])
        Set/Get the eye position (center point between two eyes). This is
        a convenience function that sets the translation component of
        eye_transform_matrix. This will be used only for offaxis frustum
        calculation.
        """
        ret = self._wrap_call(self._vtk_obj.GetEyePosition, *args)
        return ret

    def set_eye_position(self, *args):
        """
        V.set_eye_position([float, float, float])
        C++: void SetEyePosition(double eyePosition[3])
        Set/Get the eye position (center point between two eyes). This is
        a convenience function that sets the translation component of
        eye_transform_matrix. This will be used only for offaxis frustum
        calculation.
        """
        ret = self._wrap_call(self._vtk_obj.SetEyePosition, *args)
        return ret

    eye_separation = traits.Float(0.06, enter_set=True, auto_set=False, help=\
        """
        Set/Get distance between the eyes. This will be used only for
        offaxis frustum calculation. Default is 0.06.
        """
    )

    def _eye_separation_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetEyeSeparation,
                        self.eye_separation)

    def _get_eye_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetEyeTransformMatrix())
    def _set_eye_transform_matrix(self, arg):
        old_val = self._get_eye_transform_matrix()
        self._wrap_call(self._vtk_obj.SetEyeTransformMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('eye_transform_matrix', old_val, arg)
    eye_transform_matrix = traits.Property(_get_eye_transform_matrix, _set_eye_transform_matrix, help=\
        """
        Set/Get eye transformation matrix. This is the transformation
        matrix for the point between eyes. This will be used only for
        offaxis frustum calculation. Default is identity.
        """
    )

    focal_disk = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the size of the cameras lens in world coordinates. This is
        only used when the renderer is doing focal depth rendering. When
        that is being done the size of the focal disk will effect how
        significant the depth effects will be.
        """
    )

    def _focal_disk_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalDisk,
                        self.focal_disk)

    focal_point = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 0.0), cols=3, help=\
        """
        Set/Get the focal of the camera in world coordinates. The default
        focal point is the origin.
        """
    )

    def _focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFocalPoint,
                        self.focal_point)

    freeze_focal_point = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Set/Get the value of the freeze_dolly instance variable. This
        determines if the camera should move the focal point with the
        camera position. HACK!!!
        """
    )

    def _freeze_focal_point_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetFreezeFocalPoint,
                        self.freeze_focal_point)

    left_eye = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the Left Eye setting
        """
    )

    def _left_eye_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLeftEye,
                        self.left_eye)

    def _get_model_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetModelTransformMatrix())
    def _set_model_transform_matrix(self, arg):
        old_val = self._get_model_transform_matrix()
        self._wrap_call(self._vtk_obj.SetModelTransformMatrix,
                        deref_vtk(arg))
        self.trait_property_changed('model_transform_matrix', old_val, arg)
    model_transform_matrix = traits.Property(_get_model_transform_matrix, _set_model_transform_matrix, help=\
        """
        Set/Get model transformation matrix. This matrix could be used
        for model related transformations such as scale, shear, roations
        and translations.
        """
    )

    parallel_scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scaling used for a parallel projection, i.e. the
        height of the viewport in world-coordinate distances. The default
        is 1. Note that the "scale" parameter works as an "inverse scale"
        --- larger numbers produce smaller images. This method has no
        effect in perspective projection mode.
        """
    )

    def _parallel_scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetParallelScale,
                        self.parallel_scale)

    position = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        Set/Get the position of the camera in world coordinates. The
        default position is (0,0,1).
        """
    )

    def _position_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetPosition,
                        self.position)

    def get_scissor_rect(self, *args):
        """
        V.get_scissor_rect(Recti)
        C++: void GetScissorRect(Recti &scissorRect)
        Set/Get the Rect value of the scissor
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetScissorRect, *my_args)
        return ret

    def set_scissor_rect(self, *args):
        """
        V.set_scissor_rect(Recti)
        C++: void SetScissorRect(Recti scissorRect)
        Set/Get the Rect value of the scissor
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.SetScissorRect, *my_args)
        return ret

    screen_bottom_left = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(-0.5, -0.5, -0.5), cols=3, help=\
        """
        
        """
    )

    def _screen_bottom_left_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenBottomLeft,
                        self.screen_bottom_left)

    screen_bottom_right = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, -0.5, -0.5), cols=3, help=\
        """
        
        """
    )

    def _screen_bottom_right_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenBottomRight,
                        self.screen_bottom_right)

    screen_top_right = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.5, 0.5, -0.5), cols=3, help=\
        """
        
        """
    )

    def _screen_top_right_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScreenTopRight,
                        self.screen_top_right)

    thickness = traits.Float(1000.0, enter_set=True, auto_set=False, help=\
        """
        Set the distance between clipping planes.  This method adjusts
        the far clipping plane to be set a distance 'thickness' beyond
        the near clipping plane.
        """
    )

    def _thickness_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetThickness,
                        self.thickness)

    use_scissor = traits.Bool(False, enter_set=True, auto_set=False, help=\
        """
        Enable/Disable the scissor
        """
    )

    def _use_scissor_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetUseScissor,
                        self.use_scissor)

    def _get_user_transform(self):
        return wrap_vtk(self._vtk_obj.GetUserTransform())
    def _set_user_transform(self, arg):
        old_val = self._get_user_transform()
        self._wrap_call(self._vtk_obj.SetUserTransform,
                        deref_vtk(arg))
        self.trait_property_changed('user_transform', old_val, arg)
    user_transform = traits.Property(_get_user_transform, _set_user_transform, help=\
        """
        In addition to the instance variables such as position and
        orientation, you can add an additional transformation for your
        own use. This transformation is concatenated to the camera's
        projection_transform
        """
    )

    def _get_user_view_transform(self):
        return wrap_vtk(self._vtk_obj.GetUserViewTransform())
    def _set_user_view_transform(self, arg):
        old_val = self._get_user_view_transform()
        self._wrap_call(self._vtk_obj.SetUserViewTransform,
                        deref_vtk(arg))
        self.trait_property_changed('user_view_transform', old_val, arg)
    user_view_transform = traits.Property(_get_user_view_transform, _set_user_view_transform, help=\
        """
        In addition to the instance variables such as position and
        orientation, you can add an additional transformation for your
        own use.  This transformation is concatenated to the camera's
        view_transform
        """
    )

    view_angle = traits.Float(30.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the camera view angle, which is the angular height of the
        camera view measured in degrees.  The default angle is 30
        degrees. This method has no effect in parallel projection mode.
        The formula for setting the angle up for perfect perspective
        viewing is: angle = 2*atan((h/2)/d) where h is the height of the
        render_window (measured by holding a ruler up to your screen) and
        d is the distance from your eyes to the screen.
        """
    )

    def _view_angle_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewAngle,
                        self.view_angle)

    view_shear = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 0.0, 1.0), cols=3, help=\
        """
        Set/get the shear transform of the viewing frustum.  Parameters
        are dx/dz, dy/dz, and center.  center is a factor that describes
        where to shear around. The distance dshear from the camera where
        no shear occurs is given by (dshear = center * focal_distance).
        """
    )

    def _view_shear_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewShear,
                        self.view_shear)

    view_up = traits.Array(enter_set=True, auto_set=False, shape=(3,), dtype=float, value=(0.0, 1.0, 0.0), cols=3, help=\
        """
        Set/Get the view up direction for the camera.  The default is
        (0,1,0).
        """
    )

    def _view_up_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetViewUp,
                        self.view_up)

    window_center = traits.Array(enter_set=True, auto_set=False, shape=(2,), dtype=float, value=(0.0, 0.0), cols=2, help=\
        """
        Set/Get the center of the window in viewport coordinates. The
        viewport coordinate range is ([-1,+1],[-1,+1]).  This method is
        for if you have one window which consists of several viewports,
        or if you have several screens which you want to act together as
        one large screen.
        """
    )

    def _window_center_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWindowCenter,
                        self.window_center)

    def _get_camera_light_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetCameraLightTransformMatrix())
    camera_light_transform_matrix = traits.Property(_get_camera_light_transform_matrix, help=\
        """
        Returns a transformation matrix for a coordinate frame attached
        to the camera, where the camera is located at (0, 0, 1) looking
        at the focal point at (0, 0, 0), with up being (0, 1, 0).
        """
    )

    def get_composite_projection_transform_matrix(self, *args):
        """
        V.get_composite_projection_transform_matrix(float, float, float)
            -> Matrix4x4
        C++: virtual Matrix4x4 *GetCompositeProjectionTransformMatrix(
            double aspect, double nearz, double farz)
        Return the concatenation of the view_transform and the
        projection_transform. This transform will convert world
        coordinates to viewport coordinates. The 'aspect' is the
        width/height for the viewport, and the nearz and farz are the
        Z-buffer values that map to the near and far clipping planes. The
        viewport coordinates of a point located inside the frustum are in
        the range ([-1,+1],[-1,+1],[nearz,farz]).
        """
        ret = self._wrap_call(self._vtk_obj.GetCompositeProjectionTransformMatrix, *args)
        return wrap_vtk(ret)

    def _get_direction_of_projection(self):
        return self._vtk_obj.GetDirectionOfProjection()
    direction_of_projection = traits.Property(_get_direction_of_projection, help=\
        """
        
        """
    )

    def get_eye_plane_normal(self, *args):
        """
        V.get_eye_plane_normal([float, float, float])
        C++: void GetEyePlaneNormal(double normal[3])
        Get normal vector from eye to screen rotated by
        eye_transform_matrix. This will be used only for offaxis frustum
        calculation.
        """
        ret = self._wrap_call(self._vtk_obj.GetEyePlaneNormal, *args)
        return ret

    def get_frustum_planes(self, *args):
        """
        V.get_frustum_planes(float, [float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float, float])
        C++: virtual void GetFrustumPlanes(double aspect,
            double planes[24])
        Get the plane equations that bound the view frustum. The plane
        normals point inward. The planes array contains six plane
        equations of the form (Ax+By+Cz+D=0), the first four values are
        (A,B,C,D) which repeats for each of the planes. The planes are
        given in the following order: -x,+x,-y,+y,-z,+z. Warning: it
        means left,right,bottom,top,far,near (NOT near,far) The aspect of
        the viewport is needed to correctly compute the planes
        """
        ret = self._wrap_call(self._vtk_obj.GetFrustumPlanes, *args)
        return ret

    def _get_model_view_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetModelViewTransformMatrix())
    model_view_transform_matrix = traits.Property(_get_model_view_transform_matrix, help=\
        """
        Return the model view matrix of model view transform.
        """
    )

    def _get_model_view_transform_object(self):
        return wrap_vtk(self._vtk_obj.GetModelViewTransformObject())
    model_view_transform_object = traits.Property(_get_model_view_transform_object, help=\
        """
        Return the model view transform.
        """
    )

    def _get_orientation(self):
        return self._vtk_obj.GetOrientation()
    orientation = traits.Property(_get_orientation, help=\
        """
        Get the orientation of the camera.
        """
    )

    def _get_orientation_wxyz(self):
        return self._vtk_obj.GetOrientationWXYZ()
    orientation_wxyz = traits.Property(_get_orientation_wxyz, help=\
        """
        Get the orientation of the camera.
        """
    )

    def get_projection_transform_matrix(self, *args):
        """
        V.get_projection_transform_matrix(float, float, float)
            -> Matrix4x4
        C++: virtual Matrix4x4 *GetProjectionTransformMatrix(
            double aspect, double nearz, double farz)
        V.get_projection_transform_matrix(Renderer) -> Matrix4x4
        C++: virtual Matrix4x4 *GetProjectionTransformMatrix(
            Renderer *ren)
        Return the projection transform matrix, which converts from
        camera coordinates to viewport coordinates.  The 'aspect' is the
        width/height for the viewport, and the nearz and farz are the
        Z-buffer values that map to the near and far clipping planes. The
        viewport coordinates of a point located inside the frustum are in
        the range ([-1,+1],[-1,+1],[nearz,farz]).
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.GetProjectionTransformMatrix, *my_args)
        return wrap_vtk(ret)

    def get_projection_transform_object(self, *args):
        """
        V.get_projection_transform_object(float, float, float)
            -> PerspectiveTransform
        C++: virtual PerspectiveTransform *GetProjectionTransformObject(
            double aspect, double nearz, double farz)
        Return the projection transform matrix, which converts from
        camera coordinates to viewport coordinates. The 'aspect' is the
        width/height for the viewport, and the nearz and farz are the
        Z-buffer values that map to the near and far clipping planes. The
        viewport coordinates of a point located inside the frustum are in
        the range ([-1,+1],[-1,+1],[nearz,farz]).
        """
        ret = self._wrap_call(self._vtk_obj.GetProjectionTransformObject, *args)
        return wrap_vtk(ret)

    def _get_view_plane_normal(self):
        return self._vtk_obj.GetViewPlaneNormal()
    view_plane_normal = traits.Property(_get_view_plane_normal, help=\
        """
        
        """
    )

    def _get_view_transform_matrix(self):
        return wrap_vtk(self._vtk_obj.GetViewTransformMatrix())
    view_transform_matrix = traits.Property(_get_view_transform_matrix, help=\
        """
        For backward compatibility. Use get_model_view_transform_matrix()
        now. Return the matrix of the view transform. The view_transform
        depends on only three ivars:  the Position, the focal_point, and
        the view_up vector.  All the other methods are there simply for
        the sake of the users' convenience.
        """
    )

    def _get_view_transform_object(self):
        return wrap_vtk(self._vtk_obj.GetViewTransformObject())
    view_transform_object = traits.Property(_get_view_transform_object, help=\
        """
        For backward compatibility. Use get_model_view_transform_object()
        now. Return the view transform. If the camera's
        model_transform_matrix is identity then the view_transform depends
        on only three ivars: the Position, the focal_point, and the view_up
        vector. All the other methods are there simply for the sake of
        the users' convenience.
        """
    )

    def _get_viewing_rays_m_time(self):
        return self._vtk_obj.GetViewingRaysMTime()
    viewing_rays_m_time = traits.Property(_get_viewing_rays_m_time, help=\
        """
        Return the MTime that concerns recomputing the view rays of the
        camera.
        """
    )

    def apply_transform(self, *args):
        """
        V.apply_transform(Transform)
        C++: void ApplyTransform(Transform *t)
        Apply a transform to the camera.  The camera position,
        focal-point, and view-up are re-calculated using the transform's
        matrix to multiply the old points by the new transform.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ApplyTransform, *my_args)
        return ret

    def azimuth(self, *args):
        """
        V.azimuth(float)
        C++: void Azimuth(double angle)
        Rotate the camera about the view up vector centered at the focal
        point. Note that the view up vector is whatever was set via
        set_view_up, and is not necessarily perpendicular to the direction
        of projection.  The result is a horizontal rotation of the
        camera.
        """
        ret = self._wrap_call(self._vtk_obj.Azimuth, *args)
        return ret

    def compute_view_plane_normal(self):
        """
        V.compute_view_plane_normal()
        C++: void ComputeViewPlaneNormal()
        This method is called automatically whenever necessary, it should
        never be used outside of Camera.cxx.
        """
        ret = self._vtk_obj.ComputeViewPlaneNormal()
        return ret
        

    def deep_copy(self, *args):
        """
        V.deep_copy(Camera)
        C++: void DeepCopy(Camera *source)
        Copy the properties of `source' into `this'. Copy the contents of
        the matrices.
        \pre source_exists!=0
        \pre not_this: source!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def dolly(self, *args):
        """
        V.dolly(float)
        C++: void Dolly(double value)
        Divide the camera's distance from the focal point by the given
        dolly value.  Use a value greater than one to dolly-in toward the
        focal point, and use a value less than one to dolly-out away from
        the focal point.
        """
        ret = self._wrap_call(self._vtk_obj.Dolly, *args)
        return ret

    def elevation(self, *args):
        """
        V.elevation(float)
        C++: void Elevation(double angle)
        Rotate the camera about the cross product of the negative of the
        direction of projection and the view up vector, using the focal
        point as the center of rotation.  The result is a vertical
        rotation of the scene.
        """
        ret = self._wrap_call(self._vtk_obj.Elevation, *args)
        return ret

    def orthogonalize_view_up(self):
        """
        V.orthogonalize_view_up()
        C++: void OrthogonalizeViewUp()
        Recompute the view_up vector to force it to be perpendicular to
        camera->focalpoint vector.  Unless you are going to use Yaw or
        Azimuth on the camera, there is no need to do this.
        """
        ret = self._vtk_obj.OrthogonalizeViewUp()
        return ret
        

    def pitch(self, *args):
        """
        V.pitch(float)
        C++: void Pitch(double angle)
        Rotate the focal point about the cross product of the view up
        vector and the direction of projection, using the camera's
        position as the center of rotation.  The result is a vertical
        rotation of the camera.
        """
        ret = self._wrap_call(self._vtk_obj.Pitch, *args)
        return ret

    def render(self, *args):
        """
        V.render(Renderer)
        C++: virtual void Render(Renderer *)
        This method causes the camera to set up whatever is required for
        viewing the scene. This is actually handled by an subclass of
        Camera, which is created through New()
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Render, *my_args)
        return ret

    def roll(self, *args):
        """
        V.roll(float)
        C++: void Roll(double angle)
        Rotate the camera about the direction of projection.  This will
        spin the camera about its axis.
        """
        ret = self._wrap_call(self._vtk_obj.Roll, *args)
        return ret

    def set_oblique_angles(self, *args):
        """
        V.set_oblique_angles(float, float)
        C++: void SetObliqueAngles(double alpha, double beta)
        Get/Set the oblique viewing angles.  The first angle, alpha, is
        the angle (measured from the horizontal) that rays along the
        direction of projection will follow once projected onto the 2d
        screen. The second angle, beta, is the angle between the view
        plane and the direction of projection.  This creates a shear
        transform x' = x + dz*cos(alpha)/tan(beta), y' =
        dz*sin(alpha)/tan(beta) where dz is the distance of the point
        from the focal plane. The angles are (45,90) by default.  Oblique
        projections commonly use (30,63.435).
        """
        ret = self._wrap_call(self._vtk_obj.SetObliqueAngles, *args)
        return ret

    def shallow_copy(self, *args):
        """
        V.shallow_copy(Camera)
        C++: void ShallowCopy(Camera *source)
        Copy the properties of `source' into `this'. Copy pointers of
        matrices.
        \pre source_exists!=0
        \pre not_this: source!=this
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ShallowCopy, *my_args)
        return ret

    def update_viewport(self, *args):
        """
        V.update_viewport(Renderer)
        C++: virtual void UpdateViewport(Renderer *ren)
        Update the viewport
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.UpdateViewport, *my_args)
        return ret

    def viewing_rays_modified(self):
        """
        V.viewing_rays_modified()
        C++: void ViewingRaysModified()
        Mark that something has changed which requires the view rays to
        be recomputed.
        """
        ret = self._vtk_obj.ViewingRaysModified()
        return ret
        

    def yaw(self, *args):
        """
        V.yaw(float)
        C++: void Yaw(double angle)
        Rotate the focal point about the view up vector, using the
        camera's position as the center of rotation. Note that the view
        up vector is whatever was set via set_view_up, and is not
        necessarily perpendicular to the direction of projection.  The
        result is a horizontal rotation of the scene.
        """
        ret = self._wrap_call(self._vtk_obj.Yaw, *args)
        return ret

    def zoom(self, *args):
        """
        V.zoom(float)
        C++: void Zoom(double factor)
        In perspective mode, decrease the view angle by the specified
        factor. In parallel mode, decrease the parallel scale by the
        specified factor. A value greater than 1 is a zoom-in, a value
        less than 1 is a zoom-out.
        """
        ret = self._wrap_call(self._vtk_obj.Zoom, *args)
        return ret

    def get_roll(self):
        """
        V.get_roll() -> float
        C++: double GetRoll()
        Set the roll angle of the camera about the direction of
        projection.
        """
        ret = self._vtk_obj.GetRoll()
        return ret
        

    def set_roll(self, *args):
        """
        V.set_roll(float)
        C++: void SetRoll(double angle)
        Set the roll angle of the camera about the direction of
        projection.
        """
        ret = self._wrap_call(self._vtk_obj.SetRoll, *args)
        return ret

    _updateable_traits_ = \
    (('parallel_projection', 'GetParallelProjection'),
    ('use_horizontal_view_angle', 'GetUseHorizontalViewAngle'),
    ('use_off_axis_projection', 'GetUseOffAxisProjection'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('clipping_range', 'GetClippingRange'), ('distance', 'GetDistance'),
    ('eye_angle', 'GetEyeAngle'), ('eye_separation', 'GetEyeSeparation'),
    ('focal_disk', 'GetFocalDisk'), ('focal_point', 'GetFocalPoint'),
    ('freeze_focal_point', 'GetFreezeFocalPoint'), ('left_eye',
    'GetLeftEye'), ('parallel_scale', 'GetParallelScale'), ('position',
    'GetPosition'), ('screen_bottom_left', 'GetScreenBottomLeft'),
    ('screen_bottom_right', 'GetScreenBottomRight'), ('screen_top_right',
    'GetScreenTopRight'), ('thickness', 'GetThickness'), ('use_scissor',
    'GetUseScissor'), ('view_angle', 'GetViewAngle'), ('view_shear',
    'GetViewShear'), ('view_up', 'GetViewUp'), ('window_center',
    'GetWindowCenter'), ('reference_count', 'GetReferenceCount'))
    
    _allow_update_failure_ = \
    ()
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'parallel_projection',
    'use_horizontal_view_angle', 'use_off_axis_projection',
    'clipping_range', 'distance', 'eye_angle', 'eye_separation',
    'focal_disk', 'focal_point', 'freeze_focal_point', 'left_eye',
    'parallel_scale', 'position', 'screen_bottom_left',
    'screen_bottom_right', 'screen_top_right', 'thickness', 'use_scissor',
    'view_angle', 'view_shear', 'view_up', 'window_center'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Camera, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Camera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View((['parallel_projection', 'use_horizontal_view_angle',
            'use_off_axis_projection'], [], ['clipping_range', 'distance',
            'eye_angle', 'eye_separation', 'focal_disk', 'focal_point',
            'freeze_focal_point', 'left_eye', 'parallel_scale', 'position',
            'screen_bottom_left', 'screen_bottom_right', 'screen_top_right',
            'thickness', 'use_scissor', 'view_angle', 'view_shear', 'view_up',
            'window_center']),
            title='Edit Camera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Camera properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

