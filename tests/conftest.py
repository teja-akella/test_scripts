# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--credentials",
        action="store",
        default=None,
        help="Path to the credentials YAML file"
    )
