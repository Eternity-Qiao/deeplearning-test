import torch
x = torch.arange(12)#张量
X = x.reshape(3,4)#python中的reshape函数，改变张量的形状
print(X)
#x.numel()#元素个数
print(torch.zeros((2,3)))#全0张量
print(torch.ones((2,3,4)))#全1张量
Y=torch.tensor([[1,2,3],[2,3,4]])#从列表中建立张量
X=torch.tensor([[1,2,3],[2,3,4]])#从列表中建立张量
print(Y)
print(Y.shape)#张量的形状
print(X + Y) #张量的加法
print(torch.cat((X,Y),dim=0))#在行上连接
print(torch.cat((X,Y),dim=1))#在列上连接
#print(X.sum())#求和
#print(X.sum(axis=0))#按列求和
#print(X.sum(axis=1))#按行求和
#print(X.mean())#求平均值
#print(X.mean(axis=0))#按列求平均值
#print(X.mean(axis=1))#按行求平均值
Z=torch.arange(4).reshape(2,2)
W=torch.arange(4).reshape(4,1)
print(Z+W) #广播机制