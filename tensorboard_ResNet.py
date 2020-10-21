#-*-coding:utf-8-*-
import torch
import torchvision
from torch.autograd import Variable
from tensorboardX import SummaryWriter

# 模拟输入数据
input_data = Variable(torch.rand(16, 3, 224, 224))

# 从torchvision中导入已有模型
net = torchvision.models.resnet18()

# 声明writer对象，保存的文件夹，异己名称
writer = SummaryWriter(log_dir='./log', comment='resnet')
with writer:
    writer.add_graph(net, (input_data,))