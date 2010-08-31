import numpy as np
from numpy.testing import *

from scipy.interpolate.griddatand import griddata


class TestGriddata(object):

    def test_alternative_call(self):
        x = np.array([(0,0), (-0.5,-0.5), (-0.5,0.5), (0.5, 0.5), (0.25, 0.3)],
                     dtype=np.double)
        y = (np.arange(x.shape[0], dtype=np.double)[:,None]
             + np.array([0,1])[None,:])

        for method in ('nearest', 'linear', 'cubic'):
            yi = griddata((x[:,0], x[:,1]), y, (x[:,0], x[:,1]), method=method)
            assert_almost_equal(y, yi, err_msg=method)

    def test_multivalue_2d(self):
        x = np.array([(0,0), (-0.5,-0.5), (-0.5,0.5), (0.5, 0.5), (0.25, 0.3)],
                     dtype=np.double)
        y = (np.arange(x.shape[0], dtype=np.double)[:,None]
             + np.array([0,1])[None,:])

        for method in ('nearest', 'linear', 'cubic'):
            yi = griddata(x, y, x, method=method)
            assert_almost_equal(y, yi, err_msg=method)

    def test_multipoint_2d(self):
        x = np.array([(0,0), (-0.5,-0.5), (-0.5,0.5), (0.5, 0.5), (0.25, 0.3)],
                     dtype=np.double)
        y = np.arange(x.shape[0], dtype=np.double)

        xi = x[:,None,:] + np.array([0,0,0])[None,:,None]

        for method in ('nearest', 'linear', 'cubic'):
            yi = griddata(x, y, xi, method=method)

            assert_equal(yi.shape, (5, 3), err_msg=method)
            assert_almost_equal(yi, np.tile(y[:,None], (1, 3)), err_msg=method)

    def test_complex_2d(self):
        x = np.array([(0,0), (-0.5,-0.5), (-0.5,0.5), (0.5, 0.5), (0.25, 0.3)],
                     dtype=np.double)
        y = np.arange(x.shape[0], dtype=np.double)
        y = y - 2j*y[::-1]

        xi = x[:,None,:] + np.array([0,0,0])[None,:,None]

        for method in ('nearest', 'linear', 'cubic'):
            yi = griddata(x, y, xi, method=method)

            assert_equal(yi.shape, (5, 3), err_msg=method)
            assert_almost_equal(yi, np.tile(y[:,None], (1, 3)), err_msg=method)

if __name__ == "__main__":
    run_module_suite()
