from .services.encoder_service import encoder_service_handler
from .common_utils import load_config

CONFIG = load_config()

def main():
    encoder_service_handler(CONFIG)

if __name__ == "__main__":
    main()
