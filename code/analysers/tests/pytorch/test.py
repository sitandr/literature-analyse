import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def init(self):
        super(Net, self).init()
        # 1 канал ввода изображения, 
        # 6 каналов вывода, 
        # 5x5 квадратное сверточное ядро
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # аффинная операция: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Максимальное объединение через (2, 2) окно
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # Если размер - это квадрат,
        # тогда вы можете задать только одно число
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        # все измерения, исключая измерение пакета
        size = x.size()[1:]  
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()

params = list(net.parameters())

