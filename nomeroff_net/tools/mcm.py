import os
from pathlib import Path
from modelhub_client import ModelHub
CONFIGS_DIR = Path("/app/src/data/configs/")
model_config_urls = [
    # numberplate classification
    f"{os.path.join(CONFIGS_DIR, 'all/model_efficientnet_v2_s-400x100-7.json')}",
    f"{os.path.join(CONFIGS_DIR, 'ua-custom/model_efficientnet_v2_s-400x100-4.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-am/model-4.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-am/model-shufflenet_v2_x2_0-3.json')}",
    # ocr
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-by/model-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-by/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu/model-5.json')}",

    f"{os.path.join(CONFIGS_DIR, 'eu-universal/model-efficientnet_b2-5.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_1995/model-7.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_1995/model-efficientnet_b2-7.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_1995/model-shufflenet_v2_x2_0-3.json')}",

    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_from_2004/model-11.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_from_2004/model-efficientnet_b2-512-14.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-eu_ua_from_2004/model-shufflenet_v2_x2_0-7.json')}",

    f"{os.path.join(CONFIGS_DIR, 'eu-ua-custom/model-efficientnet_b2-2.json')}",
    f"{os.path.join(CONFIGS_DIR, 'eu-ua-transit/model-efficientnet_b2-2.json')}",

    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-kg/model-4.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-kg/model-shufflenet_v2_x2_0-3.json')}",

    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-su/model-5.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-su/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-su/model-efficientnet_b2-416-2.json')}",

    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ru/model-4.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ru/model-shufflenet_v2_x2_0-2.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-md/model-2.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-md/model-shufflenet_v2_x2_0-2.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-kz/model-4.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-kz/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ge/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ge/model-4.json')}",
    # object detection
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ru-military/model-shufflenet_v2_x2_0-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'nomeroff-net-ocr-ru-military/model-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'eu_2lines/model-efficientnet_b2-3.json')}",
    f"{os.path.join(CONFIGS_DIR, 'su_2lines/model-efficientnet_b2-1.json')}",

    # object detection
    f"{os.path.join(CONFIGS_DIR, 'yolov11/model-x-1.json')}",
    f"{os.path.join(CONFIGS_DIR, 'yolov11_brand_np/model-x-1.json')}",
    f"{os.path.join(CONFIGS_DIR, 'yolov8/model-x-1.json')}",

    f"{os.path.join(CONFIGS_DIR, 'orientation/model_vit_16L-224x224-1.json')}",
    f"{os.path.join(CONFIGS_DIR, 'orientation/model_0_90_vit_16L-224x224-1.json')}",
    f"{os.path.join(CONFIGS_DIR, 'orientation/model_0_180_efficientnet_v2_l-100x300-1.json')}",
    # orientation classificator

]


# Add URLs from environment variable
additional_urls = os.environ.get("ADDITIONAL_MODEL_CONFIG_URLS", "")
if additional_urls:
    model_config_urls.extend(additional_urls.split(","))

# initial
local_storage = os.environ.get('LOCAL_STORAGE', os.path.join(os.path.dirname(__file__), "../../data"))
print()
modelhub = ModelHub(model_config_urls=model_config_urls,
                    local_storage=local_storage)


def get_mode_torch() -> str:
    import torch
    if torch.cuda.is_available():
        return "gpu"
    return "cpu"


def get_device_torch() -> str:
    import torch
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def get_device_name() -> str:
    import torch
    if torch.cuda.is_available():
        return torch.cuda.get_device_name(torch.cuda.current_device())
    return ""
