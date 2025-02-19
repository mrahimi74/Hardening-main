from PredictorCorrector import predictor_corrector as pc
import numpy as np
import pytest

import pytest
import numpy as np

def test_initialization():
    model = ElastoPlastic(E=200e9, H=10e9, Y0=250e6)
    assert model.E == 200e9
    assert model.H == 10e9
    assert model.Y0 == 250e6
    assert model.sigma_n == 0
    assert model.epsilon_p_n == 0
    assert model.alpha_n == 0

def test_elastic_step():
    model = pc.ElastoPlastic(E=200e9, H=10e9, Y0=250e6)
    delta_epsilon = 1e-6  # Small strain increment
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(delta_epsilon)
    assert sigma_new == pytest.approx(model.E * delta_epsilon)
    assert epsilon_p_new == 0  # No plastic deformation

def test_plastic_step():
    model = pc.ElastoPlastic(E=200e9, H=10e9, Y0=250e6)
    delta_epsilon = 5e-3  # Large strain increment
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(delta_epsilon)
    assert sigma_new < model.E * delta_epsilon  # Stress should be lower due to yielding
    assert epsilon_p_new > 0  # Plastic strain should increase

def test_zero_strain():
    model = pc.ElastoPlastic(E=200e9, H=10e9, Y0=250e6)
    sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new = model.update_step_isotropic(0)
    assert sigma_new == 0
    assert epsilon_p_new == 0
