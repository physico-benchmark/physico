import matplotlib.pyplot as plt
import numpy as np

__all__ = ["grid_to_image", "grid_pairs_to_image"]

COLORS = [
    "#000000",  # 0 black
    "#0074D9",  # 1 blue
    "#FF4136",  # 2 red
    "#2ECC40",  # 3 green
    "#FFDC00",  # 4 yellow
    "#AAAAAA",  # 5 grey
    "#F012BE",  # 6 fuschia
    "#FF851B",  # 7 orange
    "#7FDBFF",  # 8 teal
    "#870C25",  # 9 brown
]


def grid_to_image(grid, ax=None, image_path=None, dpi=100):
    if ax is None:
        fig, ax = plt.subplots()
    cmap = plt.cm.colors.ListedColormap(COLORS)
    image = ax.imshow(grid, cmap=cmap)
    image.set_clim(-0.5, len(COLORS) - 0.5)
    ax.set_xticks(np.arange(len(grid[0])) - 0.5)
    ax.set_yticks(np.arange(len(grid)) - 0.5)
    ax.grid(True, color="white", linestyle="-")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis="both", length=0)
    plt.tight_layout()
    if image_path:
        plt.savefig(image_path, dpi=dpi, bbox_inches="tight")


def grid_pairs_to_image(input_grids, output_grids, image_path=None, dpi=100):
    assert len(input_grids) == len(output_grids)
    fig, axes = plt.subplots(len(input_grids), 2)
    for _, (input_grid, output_grid) in enumerate(zip(input_grids, output_grids)):
        grid_to_image(output_grid, axes[_, 1])
        grid_to_image(input_grid, axes[_, 0])
        plt.tight_layout()
    if image_path:
        plt.savefig(image_path, dpi=dpi, bbox_inches="tight")
    else:
        plt.show()
