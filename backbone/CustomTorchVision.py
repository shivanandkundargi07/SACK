import math
from torch import nn
from torch.nn import functional as F

from backbone import MammothBackbone, register_backbone, xavier
import torchvision.models as models


class TorchVisionBackbone(MammothBackbone):
    def __init__(self,
                model_name, num_classes, pretrained, weights=None):
        super(TorchVisionBackbone,self).__init__()
        self.model_name = model_name
        self.num_classes = num_classes
        self.pretrained = pretrained
        self.weights = weights
        if not hasattr(models, self.model_name):
            raise ValueError(f"Model {model_name} not found in torchvision.models")
        self.model = getattr(models, model_name)(pretrained=pretrained)

        if "resnet" in self.model_name or "wide_resnet" in self.model_name:
            in_features = self.model.fc.in_features
            self.model.fc = nn.Idenity()
            self.classifier = nn.Linear(in_features, self.num_classes)
        if "vit" in self.model_name:
            in_features = self.model.head.in_features
            self.model.head = nn.Identity()
            self.classifier = nn.Linear(in_features, self.num_classes)
        if "efficientnet" in self.model_name:
            in_features = self.model._fc.in_features
            self.model._fc = nn.Identity()
            self.classifier = nn.Linear(in_features, self.num_classes)
    def forward(self, x, returnt='out'):
        features = self.model(x)
        logits = self.classifier(features)
        if returnt == 'out':
            return logits
        elif returnt == 'features':
            return features
        else:
            raise ValueError(f"Invalid returnt value {returnt}")

        
     

