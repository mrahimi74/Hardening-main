from PredictorCorrector import predictor_corrector as pc
import numpy as np
import pytest

def test_predictor_corrector_iso():
    E = 1000
    H = 111.1
    Y0 = 10
    material = pc.ElastoPlastic(E, H, Y0)
    assert np.isclose(material.update_step_isotropic(0.0075)[0], 7.5)

def test_predictor_corrector_kin():
    E = 1000
    H = 111.1
    Y0 = 10
    material = pc.ElastoPlastic(E, H, Y0)
    assert np.isclose(material.update_step_kinematic(0.0075)[2], -2.5)