import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights

model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V2)
model.fc = nn.Identity()


class embedNet(nn.Module):
    
    
