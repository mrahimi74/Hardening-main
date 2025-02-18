from PredictorCorrector import predictor_corrector as pc
import numpy as np
import pytest

def test_predictor_corrector():
    E = 1000
    H = 111.1
    Y0 = 10
    material = pc.ElastoPlastic(E, H, Y0)
    assert np.isclose(material.update_step_isotropic(0.0075)[0], 7.5)