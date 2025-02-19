import numpy as np

class ElastoPlastic:
    def __init__(self, E, H, Y0):
        
        self.E = E             # Elastic modulus
        self.H = H             # Hardening modulus
        self.Y0 = Y0           # Initial yield stress
        self.sigma_n = 0       # Previous step stress
        self.epsilon_p_n = 0   # Previous step plastic strain
        self.alpha_n = 0       # Previous step backstress

    def update_step_isotropic(self, delta_epsilon):
        
        # Step 1: Compute current yield stress
        Y_n = self.Y0 + self.H * self.epsilon_p_n
        Y_new = 0

        # Step 2: Elastic Predictor Step
        delta_sigma_trial = self.E * delta_epsilon
        sigma_trial = self.sigma_n + delta_sigma_trial

        # Step 3: Check yield condition
        phi_trial = abs(sigma_trial) - Y_n

        if phi_trial <= 0:
            # Elastic step: accept trial values
            sigma_new = sigma_trial
            epsilon_p_new = self.epsilon_p_n
        else:
            # Plastic step: return mapping
            delta_epsilon_p = phi_trial / (self.E + self.H)
            sigma_new = sigma_trial - self.E * delta_epsilon_p * (1 if sigma_trial > 0 else -1)
            epsilon_p_new = self.epsilon_p_n + delta_epsilon_p
            

        # Update state variables
        self.sigma_n = sigma_new
        self.epsilon_p_n = epsilon_p_new
        Y_new = self.Y0 + self.H * self.epsilon_p_n
        if delta_epsilon == 0:
            Y_n = 0 
            phi_trial = 0
        else:
            Y_n = Y_new
        

        # Return results for this step
        return sigma_trial, phi_trial, Y_n, sigma_new, epsilon_p_new

    def update_step_kinematic(self, delta_epsilon):
        
        # Step 1: Elastic Predictor (Trial State)
        sigma_trial = self.sigma_n + self.E * delta_epsilon
        alpha_trial = self.alpha_n
        eta_trial = sigma_trial - alpha_trial
        phi_trial = np.abs(eta_trial) - self.Y0

        if phi_trial <= 0:
            # Elastic region: no plastic correction
            sigma_new = sigma_trial
            alpha_new = alpha_trial
            epsilon_p_new = self.epsilon_p_n
        else:
            # Plastic region: return mapping
            delta_epsilon_p = phi_trial / (self.E + self.H)
            sigma_new = sigma_trial - self.E * delta_epsilon_p * (1 if eta_trial > 0 else -1)
            alpha_new = alpha_trial + self.H * delta_epsilon_p * (1 if eta_trial > 0 else -1)
            epsilon_p_new = self.epsilon_p_n + delta_epsilon_p

        # Update state variables
        self.sigma_n = sigma_new
        self.alpha_n = alpha_new
        self.epsilon_p_n = epsilon_p_new

        if delta_epsilon == 0:
            phi_trial = 0

        # Return results for this step
        return alpha_trial, eta_trial, phi_trial, sigma_new, epsilon_p_new, alpha_new
    