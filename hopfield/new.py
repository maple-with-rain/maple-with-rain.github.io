import torch
import torch.nn as nn
import torch.optim as optim

# 1. 准备一些假数据
x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])

# 2. 定义模型
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1) # 输入输出维度都是1

    def forward(self, x):
        return self.linear(x)

model = LinearRegressionModel()

# 3. 定义损失函数和优化器
criterion = nn.MSELoss() # 均方误差损失
optimizer = optim.SGD(model.parameters(), lr=0.01) # 随机梯度下降

# 4. 训练循环
for epoch in range(100):
    # 前向传播
    y_pred = model(x_data)

    # 计算损失
    loss = criterion(y_pred, y_data)

    # 反向传播
    optimizer.zero_grad() # 清空上一步的梯度
    loss.backward()       # 计算当前梯度
    optimizer.step()      # 根据梯度更新参数
    

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# 5. 测试
test_x = torch.tensor([[4.0]])
print(f'Prediction for x=4: {model(test_x).item()}') # 应该接近 8.0