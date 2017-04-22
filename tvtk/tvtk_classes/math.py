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


class Math(Object):
    """
    Math - performs common math operations
    
    Superclass: Object
    
    Math provides methods to perform common math operations. These
    include providing constants such as Pi; conversion from degrees to
    radians; vector operations such as dot and cross products and vector
    norm; matrix determinant for 2x2 and 3x3 matrices; univariate
    polynomial solvers; and for random number generation (for backward
    compatibility only).
    @sa
    MinimalStandardRandomSequence, BoxMuellerRandomSequence,
    Quaternion
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMath, obj, update, **traits)
    
    def get_adjusted_scalar_range(self, *args):
        """
        V.get_adjusted_scalar_range(DataArray, int, [float, float]) -> int
        C++: static int GetAdjustedScalarRange(DataArray *array,
            int comp, double range[2])
        Get a DataArray's scalar range for a given component. If the
        DataArray's data type is unsigned char (VTK_UNSIGNED_CHAR) the
        range is adjusted to the whole data type range [0, 255.0]. Same
        goes for unsigned short (VTK_UNSIGNED_SHORT) but the upper bound
        is also adjusted down to 4095.0 if was between ]255, 4095.0].
        Return 1 on success, 0 otherwise.
        """
        my_args = deref_array(args, [('vtkDataArray', 'int', ['float', 'float'])])
        ret = self._wrap_call(self._vtk_obj.GetAdjustedScalarRange, *my_args)
        return ret

    def get_scalar_type_fitting_range(self, *args):
        """
        V.get_scalar_type_fitting_range(float, float, float, float) -> int
        C++: static int GetScalarTypeFittingRange(double range_min,
            double range_max, double scale=1.0, double shift=0.0)
        Return the scalar type that is most likely to have enough
        precision to store a given range of data once it has been scaled
        and shifted (i.e. [range_min * scale + shift, range_max * scale +
        shift]. If any one of the parameters is not an integer number
        (decimal part != 0), the search will default to float types only
        (float or double) Return -1 on error or no scalar type found.
        """
        ret = self._wrap_call(self._vtk_obj.GetScalarTypeFittingRange, *args)
        return ret

    def _get_seed(self):
        return self._vtk_obj.GetSeed()
    seed = traits.Property(_get_seed, help=\
        """
        Return the current seed used by the random number generator.
        
        * DON'T USE Random(), random_seed(), get_seed(), Gaussian()
        * THIS IS STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR
          REGRESSION TESTS)
        * THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY.
        * Instead, for a sequence of random numbers with a uniform
          distribution
        * create a MinimalStandardRandomSequence object.
        * For a sequence of random numbers with a gaussian/normal
          distribution
        * create a BoxMuellerRandomSequence object.
        """
    )

    def add(self, *args):
        """
        V.add((float, float, float), (float, float, float), [float, float,
             float])
        C++: static void Add(const double a[3], const double b[3],
            double c[3])
        Addition of two 3-vectors (double version). Result is stored in
        c.
        """
        ret = self._wrap_call(self._vtk_obj.Add, *args)
        return ret

    def angle_between_vectors(self, *args):
        """
        V.angle_between_vectors((float, float, float), (float, float, float)
            ) -> float
        C++: static double AngleBetweenVectors(const double v1[3],
            const double v2[3])
        Compute angle in radians between two vectors.
        """
        ret = self._wrap_call(self._vtk_obj.AngleBetweenVectors, *args)
        return ret

    def are_bounds_initialized(self, *args):
        """
        V.are_bounds_initialized([float, float, float, float, float, float])
             -> int
        C++: static TypeBool AreBoundsInitialized(double bounds[6])
        Are the bounds initialized?
        """
        ret = self._wrap_call(self._vtk_obj.AreBoundsInitialized, *args)
        return ret

    def begin_combination(self, *args):
        """
        V.begin_combination(int, int) -> (int, ...)
        C++: static int *BeginCombination(int m, int n)
        Start iterating over "m choose n" objects. This function returns
        an array of n integers, each from 0 to m-1. These integers
        represent the n items chosen from the set [0,m[.
        
        * You are responsible for calling Math::FreeCombination() once
        the iterator is no longer needed.
        
        * Warning: this gets large very quickly, especially when n nears
          m/2!
        * (Hint: think of Pascal's triangle.)
        """
        ret = self._wrap_call(self._vtk_obj.BeginCombination, *args)
        return ret

    def binomial(self, *args):
        """
        V.binomial(int, int) -> int
        C++: static TypeInt64 Binomial(int m, int n)
        The number of combinations of n objects from a pool of m objects
        (m>n). This is commonly known as "m choose n" and sometimes
        denoted $_m_c_n $ or $\left(\begin{array}{c}m \
        n\end{array}\right) $.
        """
        ret = self._wrap_call(self._vtk_obj.Binomial, *args)
        return ret

    def bounds_is_within_other_bounds(self, *args):
        """
        V.bounds_is_within_other_bounds([float, float, float, float, float,
            float], [float, float, float, float, float, float], [float,
            float, float]) -> int
        C++: static TypeBool BoundsIsWithinOtherBounds(
            double bounds1[6], double bounds2[6], double delta[3])
        Return true if first 3d bounds is within the second 3d bounds
        Bounds is x-min, x-max, y-min, y-max, z-min, z-max Delta is the
        error margin along each axis (usually a small number)
        """
        ret = self._wrap_call(self._vtk_obj.BoundsIsWithinOtherBounds, *args)
        return ret

    def ceil(self, *args):
        """
        V.ceil(float) -> int
        C++: static int Ceil(double x)
        Rounds a double to the nearest integer not less than itself. This
        is faster than ceil() but provides undefined output on overflow.
        """
        ret = self._wrap_call(self._vtk_obj.Ceil, *args)
        return ret

    def ceil_log2(self, *args):
        """
        V.ceil_log2(int) -> int
        C++: static int CeilLog2(TypeUInt64 x)
        Gives the exponent of the lowest power of two not less than x. Or
        in mathspeak, return the smallest "i" for which 2^i >= x. If x is
        zero, then the return value will be zero.
        """
        ret = self._wrap_call(self._vtk_obj.CeilLog2, *args)
        return ret

    def clamp_and_normalize_value(self, *args):
        """
        V.clamp_and_normalize_value(float, (float, float)) -> float
        C++: static double ClampAndNormalizeValue(double value,
            const double range[2])
        Clamp a value against a range and then normalized it between 0
        and 1. If range[0]==range[1], the result is 0.
        \pre valid_range: range[0]<=range[1]
        \post valid_result: result>=0.0 && result<=1.0
        """
        ret = self._wrap_call(self._vtk_obj.ClampAndNormalizeValue, *args)
        return ret

    def clamp_value(self, *args):
        """
        V.clamp_value([float, ...], (float, float))
        C++: static void ClampValue(double *value, const double range[2])
        V.clamp_value(float, (float, float), [float, ...])
        C++: static void ClampValue(double value, const double range[2],
            double *clamped_value)
        Clamp some values against a range The method without
        'clamped_values' will perform in-place clamping.
        """
        ret = self._wrap_call(self._vtk_obj.ClampValue, *args)
        return ret

    def clamp_values(self, *args):
        """
        V.clamp_values([float, ...], int, (float, float))
        C++: static void ClampValues(double *values, int nb_values,
            const double range[2])
        V.clamp_values((float, ...), int, (float, float), [float, ...])
        C++: static void ClampValues(const double *values, int nb_values,
            const double range[2], double *clamped_values)
        Clamp some values against a range The method without
        'clamped_values' will perform in-place clamping.
        """
        ret = self._wrap_call(self._vtk_obj.ClampValues, *args)
        return ret

    def cross(self, *args):
        """
        V.cross((float, float, float), (float, float, float), [float,
            float, float])
        C++: static void Cross(const double a[3], const double b[3],
            double c[3])
        Cross product of two 3-vectors. Result (a x b) is stored in c.
        (double-precision version)
        """
        ret = self._wrap_call(self._vtk_obj.Cross, *args)
        return ret

    def degrees_from_radians(self, *args):
        """
        V.degrees_from_radians(float) -> float
        C++: static double DegreesFromRadians(double radians)
        Convert radians into degrees
        """
        ret = self._wrap_call(self._vtk_obj.DegreesFromRadians, *args)
        return ret

    def determinant2x2(self, *args):
        """
        V.determinant2x2(float, float, float, float) -> float
        C++: static double Determinant2x2(double a, double b, double c,
            double d)
        V.determinant2x2((float, float), (float, float)) -> float
        C++: static double Determinant2x2(const double c1[2],
            const double c2[2])
        Calculate the determinant of a 2x2 matrix: | a b | | c d |
        """
        ret = self._wrap_call(self._vtk_obj.Determinant2x2, *args)
        return ret

    def determinant3x3(self, *args):
        """
        V.determinant3x3([[float, float, float], [float, float, float],
            [float, float, float]]) -> float
        C++: static double Determinant3x3(double A[3][3])
        V.determinant3x3((float, float, float), (float, float, float), (
            float, float, float)) -> float
        C++: static double Determinant3x3(const double c1[3],
            const double c2[3], const double c3[3])
        V.determinant3x3(float, float, float, float, float, float, float,
            float, float) -> float
        C++: static double Determinant3x3(double a1, double a2, double a3,
             double b1, double b2, double b3, double c1, double c2,
            double c3)
        Return the determinant of a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.Determinant3x3, *args)
        return ret

    def diagonalize3x3(self, *args):
        """
        V.diagonalize3x3(((float, float, float), (float, float, float), (
            float, float, float)), [float, float, float], [[float, float,
            float], [float, float, float], [float, float, float]])
        C++: static void Diagonalize3x3(const double A[3][3], double w[3],
             double V[3][3])
        Diagonalize a symmetric 3x3 matrix and return the eigenvalues in
        w and the eigenvectors in the columns of V.  The matrix V will
        have a positive determinant, and the three eigenvectors will be
        aligned as closely as possible with the x, y, and z axes.
        """
        ret = self._wrap_call(self._vtk_obj.Diagonalize3x3, *args)
        return ret

    def distance2_between_points(self, *args):
        """
        V.distance2_between_points((float, float, float), (float, float,
            float)) -> float
        C++: static double Distance2BetweenPoints(const double p1[3],
            const double p2[3])
        Compute distance squared between two points p1 and p2 (double
        precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Distance2BetweenPoints, *args)
        return ret

    def dot(self, *args):
        """
        V.dot((float, float, float), (float, float, float)) -> float
        C++: static double Dot(const double a[3], const double b[3])
        Dot product of two 3-vectors (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Dot, *args)
        return ret

    def dot2d(self, *args):
        """
        V.dot2d((float, float), (float, float)) -> float
        C++: static double Dot2D(const double x[2], const double y[2])
        Dot product of two 2-vectors. (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Dot2D, *args)
        return ret

    def extent_is_within_other_extent(self, *args):
        """
        V.extent_is_within_other_extent([int, int, int, int, int, int], [int,
            int, int, int, int, int]) -> int
        C++: static TypeBool ExtentIsWithinOtherExtent(int extent1[6],
            int extent2[6])
        Return true if first 3d extent is within second 3d extent Extent
        is x-min, x-max, y-min, y-max, z-min, z-max
        """
        ret = self._wrap_call(self._vtk_obj.ExtentIsWithinOtherExtent, *args)
        return ret

    def factorial(self, *args):
        """
        V.factorial(int) -> int
        C++: static TypeInt64 Factorial(int N)
        Compute N factorial, N! = N*(N-1) * (N-2)...*3*2*1. 0! is taken
        to be 1.
        """
        ret = self._wrap_call(self._vtk_obj.Factorial, *args)
        return ret

    def floor(self, *args):
        """
        V.floor(float) -> int
        C++: static int Floor(double x)
        Rounds a double to the nearest integer not greater than itself.
        This is faster than floor() but provides undefined output on
        overflow.
        """
        ret = self._wrap_call(self._vtk_obj.Floor, *args)
        return ret

    def free_combination(self, *args):
        """
        V.free_combination([int, ...])
        C++: static void FreeCombination(int *combination)
        Free the "iterator" array created by Math::BeginCombination.
        """
        ret = self._wrap_call(self._vtk_obj.FreeCombination, *args)
        return ret

    def gaussian(self, *args):
        """
        V.gaussian() -> float
        C++: static double Gaussian()
        V.gaussian(float, float) -> float
        C++: static double Gaussian(double mean, double std)
        Generate pseudo-random numbers distributed according to the
        standard normal distribution.
        
        * DON'T USE Random(), random_seed(), get_seed(), Gaussian()
        * THIS IS STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR
          REGRESSION TESTS)
        * THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY.
        * Instead, for a sequence of random numbers with a uniform
          distribution
        * create a MinimalStandardRandomSequence object.
        * For a sequence of random numbers with a gaussian/normal
          distribution
        * create a BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.Gaussian, *args)
        return ret

    def gaussian_amplitude(self, *args):
        """
        V.gaussian_amplitude(float, float) -> float
        C++: static double GaussianAmplitude(const double variance,
            const double distanceFromMean)
        V.gaussian_amplitude(float, float, float) -> float
        C++: static double GaussianAmplitude(const double mean,
            const double variance, const double position)
        Compute the amplitude of a Gaussian function with mean=0 and
        specified variance. That is, 1./(sqrt(2 Pi * variance)) *
        exp(-distance_from_mean^_2/(_2.*variance)).
        """
        ret = self._wrap_call(self._vtk_obj.GaussianAmplitude, *args)
        return ret

    def gaussian_weight(self, *args):
        """
        V.gaussian_weight(float, float) -> float
        C++: static double GaussianWeight(const double variance,
            const double distanceFromMean)
        V.gaussian_weight(float, float, float) -> float
        C++: static double GaussianWeight(const double mean,
            const double variance, const double position)
        Compute the amplitude of an unnormalized Gaussian function with
        mean=0 and specified variance. That is,
        exp(-distance_from_mean^_2/(_2.*variance)). When distance_from_mean =
        0, this function returns 1.
        """
        ret = self._wrap_call(self._vtk_obj.GaussianWeight, *args)
        return ret

    def hsv_to_rgb(self, *args):
        """
        V.hsv_to_rgb((float, float, float)) -> (float, float, float)
        C++: static double *HSVToRGB(const double hsv[3])
        V.hsv_to_rgb(float, float, float) -> (float, float, float)
        C++: static double *HSVToRGB(double h, double s, double v)
        V.hsv_to_rgb((float, float, float), [float, float, float])
        C++: static void HSVToRGB(const double hsv[3], double rgb[3])
        V.hsv_to_rgb(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void HSVToRGB(double h, double s, double v, double *r,
             double *g, double *b)
        Convert color in HSV format (Hue, Saturation, Value) to RGB
        format (Red, Green, Blue). The input color is not modified. The
        input 'hsv' must be float values in the range [0,1]. The elements
        of each component of the output 'rgb' are in the range [0, 1].
        """
        ret = self._wrap_call(self._vtk_obj.HSVToRGB, *args)
        return ret

    def identity3x3(self, *args):
        """
        V.identity3x3([[float, float, float], [float, float, float],
            [float, float, float]])
        C++: static void Identity3x3(double A[3][3])
        Set A to the identity matrix.
        """
        ret = self._wrap_call(self._vtk_obj.Identity3x3, *args)
        return ret

    def inf(self):
        """
        V.inf() -> float
        C++: static double Inf()
        Special IEEE-754 number used to represent positive infinity.
        """
        ret = self._vtk_obj.Inf()
        return ret
        

    def invert3x3(self, *args):
        """
        V.invert3x3(((float, float, float), (float, float, float), (float,
             float, float)), [[float, float, float], [float, float,
            float], [float, float, float]])
        C++: static void Invert3x3(const double A[3][3], double AI[3][3])
        Invert a 3x3 matrix. The input matrix is A. The output is stored
        in AI.
        """
        ret = self._wrap_call(self._vtk_obj.Invert3x3, *args)
        return ret

    def is_finite(self, *args):
        """
        V.is_finite(float) -> bool
        C++: static bool IsFinite(double x)
        Test if a number has finite value i.e. it is normal, subnormal or
        zero, but not infinite or Nan.
        """
        ret = self._wrap_call(self._vtk_obj.IsFinite, *args)
        return ret

    def is_inf(self, *args):
        """
        V.is_inf(float) -> int
        C++: static TypeBool IsInf(double x)
        Test if a number is equal to the special floating point value
        infinity.
        """
        ret = self._wrap_call(self._vtk_obj.IsInf, *args)
        return ret

    def is_nan(self, *args):
        """
        V.is_nan(float) -> int
        C++: static TypeBool IsNan(double x)
        Test if a number is equal to the special floating point value
        Not-A-Number (Nan).
        """
        ret = self._wrap_call(self._vtk_obj.IsNan, *args)
        return ret

    def is_power_of_two(self, *args):
        """
        V.is_power_of_two(int) -> bool
        C++: static bool IsPowerOfTwo(TypeUInt64 x)
        Returns true if integer is a power of two.
        """
        ret = self._wrap_call(self._vtk_obj.IsPowerOfTwo, *args)
        return ret

    def lu_factor3x3(self, *args):
        """
        V.lu_factor3x3([[float, float, float], [float, float, float],
            [float, float, float]], [int, int, int])
        C++: static void LUFactor3x3(double A[3][3], int index[3])
        LU Factorization of a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.LUFactor3x3, *args)
        return ret

    def lu_solve3x3(self, *args):
        """
        V.lu_solve3x3(((float, float, float), (float, float, float), (
            float, float, float)), (int, int, int), [float, float, float])
        C++: static void LUSolve3x3(const double A[3][3],
            const int index[3], double x[3])
        LU back substitution for a 3x3 matrix.
        """
        ret = self._wrap_call(self._vtk_obj.LUSolve3x3, *args)
        return ret

    def lab_to_rgb(self, *args):
        """
        V.lab_to_rgb((float, float, float), [float, float, float])
        C++: static void LabToRGB(const double lab[3], double rgb[3])
        V.lab_to_rgb(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void LabToRGB(double L, double a, double b,
            double *red, double *green, double *blue)
        V.lab_to_rgb((float, float, float)) -> (float, float, float)
        C++: static double *LabToRGB(const double lab[3])
        Convert color from the CIE-L*ab system to RGB.
        """
        ret = self._wrap_call(self._vtk_obj.LabToRGB, *args)
        return ret

    def lab_to_xyz(self, *args):
        """
        V.lab_to_xyz((float, float, float), [float, float, float])
        C++: static void LabToXYZ(const double lab[3], double xyz[3])
        V.lab_to_xyz(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void LabToXYZ(double L, double a, double b, double *x,
             double *y, double *z)
        V.lab_to_xyz((float, float, float)) -> (float, float, float)
        C++: static double *LabToXYZ(const double lab[3])
        Convert color from the CIE-L*ab system to CIE XYZ.
        """
        ret = self._wrap_call(self._vtk_obj.LabToXYZ, *args)
        return ret

    def linear_solve3x3(self, *args):
        """
        V.linear_solve3x3(((float, float, float), (float, float, float), (
            float, float, float)), (float, float, float), [float, float,
            float])
        C++: static void LinearSolve3x3(const double A[3][3],
            const double x[3], double y[3])
        Solve Ay = x for y and place the result in y.  The matrix A is
        destroyed in the process.
        """
        ret = self._wrap_call(self._vtk_obj.LinearSolve3x3, *args)
        return ret

    def matrix3x3_to_quaternion(self, *args):
        """
        V.matrix3x3_to_quaternion(((float, float, float), (float, float,
            float), (float, float, float)), [float, float, float, float])
        C++: static void Matrix3x3ToQuaternion(const double A[3][3],
            double quat[4])
        Convert a 3x3 matrix into a quaternion.  This will provide the
        best possible answer even if the matrix is not a pure rotation
        matrix. The quaternion is in the form [w, x, y, z]. The method
        used is that of B.K.P. Horn.
        @sa quaternion_to_matrix3x3() multiply_quaternion()
        @sa Quaternion
        """
        ret = self._wrap_call(self._vtk_obj.Matrix3x3ToQuaternion, *args)
        return ret

    def multiply3x3(self, *args):
        """
        V.multiply3x3(((float, float, float), (float, float, float), (
            float, float, float)), (float, float, float), [float, float,
            float])
        C++: static void Multiply3x3(const double A[3][3],
            const double in[3], double out[3])
        V.multiply3x3(((float, float, float), (float, float, float), (
            float, float, float)), ((float, float, float), (float, float,
            float), (float, float, float)), [[float, float, float],
            [float, float, float], [float, float, float]])
        C++: static void Multiply3x3(const double A[3][3],
            const double B[3][3], double C[3][3])
        Multiply a vector by a 3x3 matrix.  The result is placed in out.
        """
        ret = self._wrap_call(self._vtk_obj.Multiply3x3, *args)
        return ret

    def multiply_quaternion(self, *args):
        """
        V.multiply_quaternion((float, float, float, float), (float, float,
            float, float), [float, float, float, float])
        C++: static void MultiplyQuaternion(const double q1[4],
            const double q2[4], double q[4])
        Multiply two quaternions. This is used to concatenate rotations.
        Quaternions are in the form [w, x, y, z].
        @sa matrix3x3_to_quaternion() quaternion_to_matrix3x3()
        @sa Quaternion
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyQuaternion, *args)
        return ret

    def multiply_scalar(self, *args):
        """
        V.multiply_scalar([float, float, float], float)
        C++: static void MultiplyScalar(double a[3], double s)
        Multiplies a 3-vector by a scalar (double version). This modifies
        the input 3-vector.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyScalar, *args)
        return ret

    def multiply_scalar2d(self, *args):
        """
        V.multiply_scalar2d([float, float], float)
        C++: static void MultiplyScalar2D(double a[2], double s)
        Multiplies a 2-vector by a scalar (double version). This modifies
        the input 2-vector.
        """
        ret = self._wrap_call(self._vtk_obj.MultiplyScalar2D, *args)
        return ret

    def nan(self):
        """
        V.nan() -> float
        C++: static double Nan()
        Special IEEE-754 number used to represent Not-A-Number (Nan).
        """
        ret = self._vtk_obj.Nan()
        return ret
        

    def nearest_power_of_two(self, *args):
        """
        V.nearest_power_of_two(int) -> int
        C++: static int NearestPowerOfTwo(int x)
        Compute the nearest power of two that is not less than x. The
        return value is 1 if x is less than or equal to zero, and is
        VTK_INT_MIN if result is too large to fit in an int.
        """
        ret = self._wrap_call(self._vtk_obj.NearestPowerOfTwo, *args)
        return ret

    def neg_inf(self):
        """
        V.neg_inf() -> float
        C++: static double NegInf()
        Special IEEE-754 number used to represent negative infinity.
        """
        ret = self._vtk_obj.NegInf()
        return ret
        

    def next_combination(self, *args):
        """
        V.next_combination(int, int, [int, ...]) -> int
        C++: static int NextCombination(int m, int n, int *combination)
        Given m, n, and a valid combination of n integers in the range
        [0,m[, this function alters the integers into the next
        combination in a sequence of all combinations of n items from a
        pool of m.
        
        * If the combination is the last item in the sequence on input,
        * then combination is unaltered and 0 is returned.
        * Otherwise, 1 is returned and combination is updated.
        """
        ret = self._wrap_call(self._vtk_obj.NextCombination, *args)
        return ret

    def norm(self, *args):
        """
        V.norm((float, ...), int) -> float
        C++: static double Norm(const double *x, int n)
        V.norm((float, float, float)) -> float
        C++: static double Norm(const double v[3])
        Compute the norm of n-vector. x is the vector, n is its length.
        """
        ret = self._wrap_call(self._vtk_obj.Norm, *args)
        return ret

    def norm2d(self, *args):
        """
        V.norm2d((float, float)) -> float
        C++: static double Norm2D(const double x[2])
        Compute the norm of a 2-vector. (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Norm2D, *args)
        return ret

    def normalize(self, *args):
        """
        V.normalize([float, float, float]) -> float
        C++: static double Normalize(double v[3])
        Normalize (in place) a 3-vector. Returns norm of vector
        (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Normalize, *args)
        return ret

    def normalize2d(self, *args):
        """
        V.normalize2d([float, float]) -> float
        C++: static double Normalize2D(double v[2])
        Normalize (in place) a 2-vector. Returns norm of vector.
        (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Normalize2D, *args)
        return ret

    def orthogonalize3x3(self, *args):
        """
        V.orthogonalize3x3(((float, float, float), (float, float, float),
            (float, float, float)), [[float, float, float], [float, float,
             float], [float, float, float]])
        C++: static void Orthogonalize3x3(const double A[3][3],
            double B[3][3])
        Orthogonalize a 3x3 matrix and put the result in B.  If matrix A
        has a negative determinant, then B will be a rotation plus a flip
        i.e. it will have a determinant of -1.
        """
        ret = self._wrap_call(self._vtk_obj.Orthogonalize3x3, *args)
        return ret

    def outer(self, *args):
        """
        V.outer((float, float, float), (float, float, float), [[float,
            float, float], [float, float, float], [float, float, float]])
        C++: static void Outer(const double a[3], const double b[3],
            double C[3][3])
        Outer product of two 3-vectors (double-precision version).
        """
        ret = self._wrap_call(self._vtk_obj.Outer, *args)
        return ret

    def outer2d(self, *args):
        """
        V.outer2d((float, float), (float, float), [[float, float], [float,
             float]])
        C++: static void Outer2D(const double x[2], const double y[2],
            double A[2][2])
        Outer product of two 2-vectors (float version).
        """
        ret = self._wrap_call(self._vtk_obj.Outer2D, *args)
        return ret

    def perpendiculars(self, *args):
        """
        V.perpendiculars((float, float, float), [float, float, float],
            [float, float, float], float)
        C++: static void Perpendiculars(const double v1[3], double v2[3],
            double v3[3], double theta)
        Given a unit vector v1, find two unit vectors v2 and v3 such that
        v1 cross v2 = v3 (i.e. the vectors are perpendicular to each
        other). There is an infinite number of such vectors, specify an
        angle theta to choose one set.  If you want only one
        perpendicular vector, specify NULL for v3.
        """
        ret = self._wrap_call(self._vtk_obj.Perpendiculars, *args)
        return ret

    def pi(self):
        """
        V.pi() -> float
        C++: static double Pi()
        A mathematical constant. This version is atan(1.0) * 4.0
        """
        ret = self._vtk_obj.Pi()
        return ret
        

    def point_is_within_bounds(self, *args):
        """
        V.point_is_within_bounds([float, float, float], [float, float, float,
             float, float, float], [float, float, float]) -> int
        C++: static TypeBool PointIsWithinBounds(double point[3],
            double bounds[6], double delta[3])
        Return true if point is within the given 3d bounds Bounds is
        x-min, x-max, y-min, y-max, z-min, z-max Delta is the error
        margin along each axis (usually a small number)
        """
        ret = self._wrap_call(self._vtk_obj.PointIsWithinBounds, *args)
        return ret

    def project_vector(self, *args):
        """
        V.project_vector((float, float, float), (float, float, float),
            [float, float, float]) -> bool
        C++: static bool ProjectVector(const double a[3],
            const double b[3], double projection[3])
        Compute the projection of vector a on vector b and return it in
        projection[3]. If b is a zero vector, the function returns false
        and 'projection' is invalid. Otherwise, it returns true.
        """
        ret = self._wrap_call(self._vtk_obj.ProjectVector, *args)
        return ret

    def project_vector2d(self, *args):
        """
        V.project_vector2d((float, float), (float, float), [float, float])
            -> bool
        C++: static bool ProjectVector2D(const double a[2],
            const double b[2], double projection[2])
        Compute the projection of 2d vector a on 2d vector b and returns
        the result in projection[2]. If b is a zero vector, the function
        returns false and 'projection' is invalid. Otherwise, it returns
        true.
        """
        ret = self._wrap_call(self._vtk_obj.ProjectVector2D, *args)
        return ret

    def quaternion_to_matrix3x3(self, *args):
        """
        V.quaternion_to_matrix3x3((float, float, float, float), [[float,
            float, float], [float, float, float], [float, float, float]])
        C++: static void QuaternionToMatrix3x3(const double quat[4],
            double A[3][3])
        Convert a quaternion to a 3x3 rotation matrix.  The quaternion
        does not have to be normalized beforehand. The quaternion must be
        in the form [w, x, y, z].
        @sa matrix3x3_to_quaternion() multiply_quaternion()
        @sa Quaternion
        """
        ret = self._wrap_call(self._vtk_obj.QuaternionToMatrix3x3, *args)
        return ret

    def rgb_to_hsv(self, *args):
        """
        V.rgb_to_hsv((float, float, float)) -> (float, float, float)
        C++: static double *RGBToHSV(const double rgb[3])
        V.rgb_to_hsv(float, float, float) -> (float, float, float)
        C++: static double *RGBToHSV(double r, double g, double b)
        V.rgb_to_hsv((float, float, float), [float, float, float])
        C++: static void RGBToHSV(const double rgb[3], double hsv[3])
        V.rgb_to_hsv(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void RGBToHSV(double r, double g, double b, double *h,
             double *s, double *v)
        Convert color in RGB format (Red, Green, Blue) to HSV format
        (Hue, Saturation, Value). The input color is not modified. The
        input RGB must be float values in the range [0,1]. The output
        ranges are hue [0, 1], saturation [0, 1], and value [0, 1].
        """
        ret = self._wrap_call(self._vtk_obj.RGBToHSV, *args)
        return ret

    def rgb_to_lab(self, *args):
        """
        V.rgb_to_lab((float, float, float), [float, float, float])
        C++: static void RGBToLab(const double rgb[3], double lab[3])
        V.rgb_to_lab(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void RGBToLab(double red, double green, double blue,
            double *L, double *a, double *b)
        V.rgb_to_lab((float, float, float)) -> (float, float, float)
        C++: static double *RGBToLab(const double rgb[3])
        Convert color from the RGB system to CIE-L*ab. The input RGB must
        be values in the range [0,1]. The output ranges of 'L' is [0,
        100]. The output range of 'a' and 'b' are approximately [-110,
        110].
        """
        ret = self._wrap_call(self._vtk_obj.RGBToLab, *args)
        return ret

    def rgb_to_xyz(self, *args):
        """
        V.rgb_to_xyz((float, float, float), [float, float, float])
        C++: static void RGBToXYZ(const double rgb[3], double xyz[3])
        V.rgb_to_xyz(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void RGBToXYZ(double r, double g, double b, double *x,
             double *y, double *z)
        V.rgb_to_xyz((float, float, float)) -> (float, float, float)
        C++: static double *RGBToXYZ(const double rgb[3])
        Convert color from the RGB system to CIE XYZ.
        """
        ret = self._wrap_call(self._vtk_obj.RGBToXYZ, *args)
        return ret

    def radians_from_degrees(self, *args):
        """
        V.radians_from_degrees(float) -> float
        C++: static double RadiansFromDegrees(double degrees)
        Convert degrees into radians
        """
        ret = self._wrap_call(self._vtk_obj.RadiansFromDegrees, *args)
        return ret

    def random(self, *args):
        """
        V.random() -> float
        C++: static double Random()
        V.random(float, float) -> float
        C++: static double Random(double min, double max)
        Generate pseudo-random numbers distributed according to the
        uniform distribution between 0.0 and 1.0. This is used to provide
        portability across different systems.
        
        * DON'T USE Random(), random_seed(), get_seed(), Gaussian()
        * THIS IS STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR
          REGRESSION TESTS)
        * THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY.
        * Instead, for a sequence of random numbers with a uniform
          distribution
        * create a MinimalStandardRandomSequence object.
        * For a sequence of random numbers with a gaussian/normal
          distribution
        * create a BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.Random, *args)
        return ret

    def random_seed(self, *args):
        """
        V.random_seed(int)
        C++: static void RandomSeed(int s)
        Initialize seed value. NOTE: Random() has the bad property that
        the first random number returned after random_seed() is called is
        proportional to the seed value! To help solve this, call
        random_seed() a few times inside seed. This doesn't ruin the
        repeatability of Random().
        
        * DON'T USE Random(), random_seed(), get_seed(), Gaussian()
        * THIS IS STATIC SO THIS IS PRONE TO ERRORS (SPECIALLY FOR
          REGRESSION TESTS)
        * THIS IS HERE FOR BACKWARD COMPATIBILITY ONLY.
        * Instead, for a sequence of random numbers with a uniform
          distribution
        * create a MinimalStandardRandomSequence object.
        * For a sequence of random numbers with a gaussian/normal
          distribution
        * create a BoxMuellerRandomSequence object.
        """
        ret = self._wrap_call(self._vtk_obj.RandomSeed, *args)
        return ret

    def round(self, *args):
        """
        V.round(float) -> int
        C++: static int Round(double f)"""
        ret = self._wrap_call(self._vtk_obj.Round, *args)
        return ret

    def singular_value_decomposition3x3(self, *args):
        """
        V.singular_value_decomposition3x3(((float, float, float), (float,
            float, float), (float, float, float)), [[float, float, float],
             [float, float, float], [float, float, float]], [float, float,
             float], [[float, float, float], [float, float, float],
            [float, float, float]])
        C++: static void SingularValueDecomposition3x3(
            const double A[3][3], double U[3][3], double w[3],
            double VT[3][3])
        Perform singular value decomposition on a 3x3 matrix.  This is
        not done using a conventional SVD algorithm, instead it is done
        using Orthogonalize3x3 and Diagonalize3x3.  Both output matrices
        U and VT will have positive determinants, and the w values will
        be arranged such that the three rows of VT are aligned as closely
        as possible with the x, y, and z axes respectively.  If the
        determinant of A is negative, then the three w values will be
        negative.
        """
        ret = self._wrap_call(self._vtk_obj.SingularValueDecomposition3x3, *args)
        return ret

    def solve3_point_circle(self, *args):
        """
        V.solve3_point_circle((float, float, float), (float, float, float),
            (float, float, float), [float, float, float]) -> float
        C++: static double Solve3PointCircle(const double p1[3],
            const double p2[3], const double p3[3], double center[3])
        In Euclidean space, there is a unique circle passing through any
        given three non-collinear points P1, P2, and P3. Using Cartesian
        coordinates to represent these points as spatial vectors, it is
        possible to use the dot product and cross product to calculate
        the radius and center of the circle. See:
        http://en.wikipedia.org/wiki/Circumscribed_circle and more
        specifically the section Barycentric coordinates from cross- and
        dot-products
        """
        ret = self._wrap_call(self._vtk_obj.Solve3PointCircle, *args)
        return ret

    def subtract(self, *args):
        """
        V.subtract((float, float, float), (float, float, float), [float,
            float, float])
        C++: static void Subtract(const double a[3], const double b[3],
            double c[3])
        Subtraction of two 3-vectors (double version). Result is stored
        in c according to c = a - b.
        """
        ret = self._wrap_call(self._vtk_obj.Subtract, *args)
        return ret

    def transpose3x3(self, *args):
        """
        V.transpose3x3(((float, float, float), (float, float, float), (
            float, float, float)), [[float, float, float], [float, float,
            float], [float, float, float]])
        C++: static void Transpose3x3(const double A[3][3],
            double AT[3][3])
        Transpose a 3x3 matrix. The input matrix is A. The output is
        stored in AT.
        """
        ret = self._wrap_call(self._vtk_obj.Transpose3x3, *args)
        return ret

    def uninitialize_bounds(self, *args):
        """
        V.uninitialize_bounds([float, float, float, float, float, float])
        C++: static void UninitializeBounds(double bounds[6])
        Set the bounds to an uninitialized state
        """
        ret = self._wrap_call(self._vtk_obj.UninitializeBounds, *args)
        return ret

    def xyz_to_lab(self, *args):
        """
        V.xyz_to_lab((float, float, float), [float, float, float])
        C++: static void XYZToLab(const double xyz[3], double lab[3])
        V.xyz_to_lab(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void XYZToLab(double x, double y, double z, double *L,
             double *a, double *b)
        V.xyz_to_lab((float, float, float)) -> (float, float, float)
        C++: static double *XYZToLab(const double xyz[3])
        Convert Color from the CIE XYZ system to CIE-L*ab.
        """
        ret = self._wrap_call(self._vtk_obj.XYZToLab, *args)
        return ret

    def xyz_to_rgb(self, *args):
        """
        V.xyz_to_rgb((float, float, float), [float, float, float])
        C++: static void XYZToRGB(const double xyz[3], double rgb[3])
        V.xyz_to_rgb(float, float, float, [float, ...], [float, ...],
            [float, ...])
        C++: static void XYZToRGB(double x, double y, double z, double *r,
             double *g, double *b)
        V.xyz_to_rgb((float, float, float)) -> (float, float, float)
        C++: static double *XYZToRGB(const double xyz[3])
        Convert color from the CIE XYZ system to RGB.
        """
        ret = self._wrap_call(self._vtk_obj.XYZToRGB, *args)
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
            return super(Math, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            View((Item("handler._full_traits_list",show_label=False)),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            View(([], [], []),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            View((HGroup(spring, "handler.view_type", show_border=True), 
            Item("handler.info.object", editor = InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Math properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

