import torch
from torchvision import models
resnet101 = models.resnet101()
resnet101 = models.resnet101(pretrained=True)
# model_path = '......'
# model_data = torch.load(model_path)
# resnet101.load_state_dict(model_data:)
from PIL import Image
img = Image.open("/home/qiao/testc/testpy.png")
from torchvision import transforms
preprocess = transforms.Compose([transforms.Resize(256),transforms.ToTensor()])
img_t = preprocess(img)
batch_t = torch.unsqueeze(img_t,0)
resnet101.eval()
out = resnet101(batch_t)
print(out.shape)

