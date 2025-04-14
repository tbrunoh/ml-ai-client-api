import torch
from ts.torch_handler.base_handler import BaseHandler

import torchvision.transforms as transforms
from PIL import Image
import io
from mlaist.models.model import SkinToneCNNModel 
from mlaicore.utils.utils import Utils
from dotenv import load_dotenv
import os
load_dotenv()

class SkinToneHandler(BaseHandler):
    def initialize(self, context):
        """Initialize the model and other artifacts."""
        self.device = Utils.set_accelerator()
        model_path = os.getenv("SKINTONE_MODEL_PATH")
        
        # Load the model
        self.model = SkinToneCNNModel(num_classes=10, image_size=512, channels=3)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.to(self.device)
        self.model.eval()
        
        # Define the preprocessing transformations
        self.transform = transforms.Compose([
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])
    
    def preprocess(self, data):
        """Preprocess the input data."""
        images = []
        for row in data:
            image = row.get("data") or row.get("body")
            if isinstance(image, (bytearray, bytes)):
                image = Image.open(io.BytesIO(image)).convert("RGB")
            else:
                raise ValueError("Unsupported input format")
            images.append(self.transform(image).unsqueeze(0))
        return torch.cat(images).to(self.device)
    
    def inference(self, inputs):
        """Perform inference on the preprocessed inputs."""
        with torch.no_grad():
            outputs = self.model(inputs)
            _, predicted_classes = torch.max(outputs, 1)
        return predicted_classes.tolist()
    
    def postprocess(self, inference_output):
        """Postprocess the inference results."""
        return [{"num": pred} for pred in inference_output]