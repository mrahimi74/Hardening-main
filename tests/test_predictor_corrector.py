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

def test_plastic_return_mapping_positive_sigma():
    model = pc.ElastoPlastic(E=200, H=10, Y0=5)
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(0.05)
    assert sigma_new < sigma_trial  # Should reduce due to plasticity
    assert epsilon_p_new > 0

def test_plastic_return_mapping_negative_sigma():
    model = pc.ElastoPlastic(E=200, H=10, Y0=5)
    model.sigma_n = -10  # Start with a negative stress state
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(0.05)
    assert sigma_new > sigma_trial  # Should increase due to plasticity
    assert epsilon_p_new > 0
