from chip_viewer import Chip, export_to_html
import os

json_path = "/config/Desktop/marsd/tpu_v7_architecture.json"
chip = Chip.from_json_file(json_path)
export_to_html(chip, "/config/Desktop/marsd/tpu_v7_viewer.html")
print("Viewer generated at /config/Desktop/marsd/tpu_v7_viewer.html")
