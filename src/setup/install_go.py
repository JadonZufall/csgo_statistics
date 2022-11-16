# Tools for insuring that golang is properly installed and or installing golang if not properly installed.
import subprocess

# TODO: Write functions for golang setup and installation.


def ensure_go_install() -> bool:
    """ Ensures that golang is installed.

    :returns:
    """
    result = subprocess.run(["go", "version"], stdout=False)
    return True if result.returncode == 0 else False

