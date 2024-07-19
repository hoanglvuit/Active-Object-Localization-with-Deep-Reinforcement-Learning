import torch.nn as nn
import torchvision

class FeatureExtractor(nn.Module):
    def __init__(self):
        super(FeatureExtractor, self).__init__() 
        vgg16 = torchvision.models.vgg16(pretrained=True)
        vgg16.eval() # to not do dropout
        self.features = list(vgg16.children())[0] 
        self.classifier = nn.Sequential(*list(vgg16.classifier.children())[:-2]) # 7x7x512
    def forward(self, x):
        x = self.features(x)
        return x
    

class DQN(nn.Module):
    def __init__(self, h, w, outputs):
        super(DQN, self).__init__()
        self.classifier = nn.Sequential(
            nn.Linear( in_features= 81 + 25088, out_features=1024),            
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear( in_features= 1024, out_features=1024),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear( in_features= 1024, out_features=9)
        )
    def forward(self, x):
        return self.classifier(x)