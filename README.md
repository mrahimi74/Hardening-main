# Hardening

# PredictorCorrector

PredictorCorrector is a numerical analysis tool implementing a predictor-corrector method for solving ordinary differential equations (ODEs).

## 📂 Project Structure
- **`predictor_corrector.py`**: Contains the Predictor-Corrector method implementation.  
- **`test_predictor_corrector.py`**: Unit tests for the predictor-corrector algorithm using `pytest`.  
- **`tutorial.ipynb`**: A Jupyter notebook demonstrating how to use the algorithm with examples.  
- **`pyproject.toml`**: Project dependencies and build configurations.  

## 🚀 Installation
Ensure you have Python 3.9 or above. You can install the required dependencies using:
```bash
pip install -r requirements.txt
```
Or, using the `pyproject.toml`:
```bash
pip install .
```

## 📖 Usage
To use the predictor-corrector algorithm, see the `tutorial.ipynb` notebook or run:
```bash
python predictor_corrector.py
```

## 🧪 Testing
Run tests using `pytest`:
```bash
pytest --cov=PredictorCorrector
```

## 🛠 Dependencies
- `matplotlib==3.10.0`
- `numpy==1.26.4`
- `pytest==7.1.2`
- `pytest-cov==3.0.0`
- `scipy==1.12.0`

## 💻 Contributing
Pull requests are welcome. For major changes, please open an issue to discuss what you would like to change.

## 📜 License
This project is licensed under the MIT License.
