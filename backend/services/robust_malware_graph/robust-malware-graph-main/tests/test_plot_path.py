import pytest

pytest.importorskip("matplotlib")
import matplotlib.pyplot as plt
from src.cli.preprocessing import ensure_dir


def test_save_plot_when_dir_absent(tmp_path):
    plot_path = tmp_path / "plots" / "img.png"
    # ensure the directory is created before saving
    ensure_dir(plot_path.parent)
    plt.figure()
    plt.plot([0, 1], [0, 1])
    plt.savefig(plot_path)
    plt.close()
    assert plot_path.exists()

