# Flight Price Prediction Model

This project is a machine learning model that predicts flight prices based on various input parameters.

## Features

- Predicts flight costs using advanced machine learning algorithms
- User-friendly web interface built with **FastAPI**
- Responsive design that works on desktop and mobile devices
- Interactive forms with real-time validation
- Fast and efficient dependency management with **uv**

## Deployment

The model is live and can be accessed here: [Flight Price Prediction](https://flight-cost-predict.onrender.com)

## Running Locally

### Prerequisites

- [uv](https://github.com/astral-sh/uv) installed.

### Steps

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Aditi4275/Flight-Cost-Predict.git
   cd Flight-Cost-Predict
   ```

2. **Sync dependencies**:
   ```bash
   uv sync
   ```

3. **Run the application**:
   ```bash
   uv run uvicorn app:app --reload
   ```

4. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.
