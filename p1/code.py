import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import torchvision

# 设置硬件设备，如果有GPU则使用，没有则使用cpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

train_ds = torchvision.datasets.MNIST('data', 
                                      train=True, 
                                      transform=torchvision.transforms.ToTensor(), # 将数据类型转化为Tensor
                                      download=True)

test_ds  = torchvision.datasets.MNIST('data', 
                                      train=False, 
                                      transform=torchvision.transforms.ToTensor(), # 将数据类型转化为Tensor
                                      download=True)

batch_size = 32

train_dl = torch.utils.data.DataLoader(train_ds, 
                                       batch_size=batch_size, 
                                       shuffle=True)

test_dl  = torch.utils.data.DataLoader(test_ds, 
                                       batch_size=batch_size)

# 取一个批次查看数据格式
# 数据的shape为：[batch_size, channel, height, weight]
# 其中batch_size为自己设定，channel，height和weight分别是图片的通道数，高度和宽度。

imgs, labels = next(iter(train_dl))
imgs.shape

torch.Size([32, 1, 28, 28])