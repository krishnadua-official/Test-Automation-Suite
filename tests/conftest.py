import pytest
import json
import os

@pytest.fixture(scope="session")
def router_config():
    """
    Loads router and WiFi configuration from test_config.json.
    Run configTest.py first to generate this file.
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', 'test_config.json')
    if not os.path.exists(config_path):
        pytest.fail(f"Configuration file not found: {config_path}. Run configTest.py to create it.")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

@pytest.fixture(scope="function")
def test_results():
    return {} 
