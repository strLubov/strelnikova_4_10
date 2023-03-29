from pathlib import Path


def path(file_name) -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.joinpath(f'resources/{file_name}')
