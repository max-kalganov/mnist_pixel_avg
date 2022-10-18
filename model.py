from typing import Dict, Set, List, Union

import numpy as np


class MnistSolver:
    pixel_groups_to_color: Dict[str, int] = {}
    activated_pixel_groups: List[Set] = []
    num_of_pixels: int = 0
    num_of_colors = 16**6

    def __init__(self, num_of_pixels):
        self.num_of_pixels = num_of_pixels

    def get_node_color(self, value: Union[str, int]) -> int:
        assert self.num_of_pixels != 0, f"num of pixels is undefined"
        if value in self.pixel_groups_to_color:
            value_color = self.pixel_groups_to_color[value]
        else:
            value_color = int(value / self.num_of_pixels * self.num_of_colors)
        return value_color

    def process_image(self, image: np.ndarray):
        flat_image = image.flatten()
        active_pixels = np.where(flat_image > 0)[0].tolist()
        current_group = set(active_pixels)
        used_pixels = set()
        for pixels_group in self.activated_pixel_groups:
            if pixels_group <= current_group:
                used_pixels = used_pixels.union(pixels_group)
                current_group.add(','.join(map(str, pixels_group)))

        current_group_color = int(np.mean([self.get_node_color(val) for val in current_group]))
        current_group_id = ','.join(map(str, current_group))
        self.pixel_groups_to_color[current_group_id] = current_group_color
        self.activated_pixel_groups.append(current_group)

        return current_group_color
