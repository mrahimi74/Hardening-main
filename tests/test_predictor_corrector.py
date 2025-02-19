from PredictorCorrector import predictor_corrector as pc
import numpy as np
import pytest

def test_predictor_corrector():
    E = 1000
    H = 111.1
    Y0 = 10
    material = pc.ElastoPlastic(E, H, Y0)
    assert np.isclose(material.update_step_isotropic(0.0075)[0], 7.5)
    assert np.isclose(material.update_step_kinematic(0.0075)[2], 5)

def test_no_strain_increment():
    model = pc.ElastoPlastic(E=200, H=10, Y0=5)
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(0)
    assert sigma_trial == 0
    assert phi_trial == 0
    assert Y_n == 0
    assert sigma_new == 0
    assert epsilon_p_new == 0

def sfsgfsg():
    model = pc.ElastoPlastic(1000, 111.1, 10)
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(0.0225)
    assert phi_trial > 0
    assert sigma_trial > sigma_new
    assert np.isclose(epsilon_p_new, .011250112501125013)