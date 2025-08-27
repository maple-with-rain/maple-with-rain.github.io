# <center><span style="color:blue">第一章 虚功原理</span></center> 
## 虚功原理
<span style='color:red'>虚功原理：</span>
约束条件下的力学平衡系统中有
$$ \sum_{i}F_i\delta x_i=0 $$ 
若将物体受力分为外界的主动力$F^\alpha$和约束条件引起的力$F^\beta$，由于约束存在$\delta x_i$只能在切线方向上变动，可将上述公式改写为$$\sum_{i}F_i^\alpha\delta x_i=\sum_{i}F_i^\beta\delta x_i=0$$
<span style='color:red'>达朗贝格原理：</span>
非平衡力学系统
    $$\sum_{i}(F_i-\dot p_i)\delta x_i=0$$

> 对于完整约束系统[^1]中，可以选取独立的广义坐标$q_i$，其数目等于系统自由度,利用爱因斯坦求和规则，主动力的虚功为:
$$F_i^\alpha\cdot\delta x_i=F^\alpha_i\cdot\frac{\partial x_i}{\partial q_j}\delta q_j=Q_j\delta q_j$$
其中定义广义力$$Q_j=F^\alpha_i\cdot \frac{\partial x_i}{\partial q_j}$$
由于$$v_i=\frac{dx_i}{dt}=\frac{\partial x_i}{\partial q_j}\dot{q_j}+\frac{\partial x_i}{\partial t}$$
有$$\frac{\partial v_i}{\partial \dot{q_j}}=\frac{\partial x_i}{\partial q_j}$$
由于
$$\dot{p_i}\cdot\delta x_i=m_i\ddot{x_i}\cdot \frac{\partial x_i}{\partial q_j}\delta q_j$$
又注意到$$m_i \ddot{\mathbf{x}}_i \cdot \frac{\partial \mathbf{x}_i}{\partial q_j}=\frac{d}{d t}\left(m_i \dot{\mathbf{x}}_i \cdot \frac{\partial \mathbf{x}_i}{\partial q_j}\right)-m_i \dot{\mathbf{x}}_i \cdot \frac{d}{d t}\left(\frac{\partial \mathbf{x}_i}{\partial q_j}\right)$$
利用该式，可得
$$\left[\frac{d}{d t} \frac{\partial T}{\partial \dot{q}_j}-\frac{\partial T}{\partial q_j}-Q_j\right] \delta q_j=0$$
进而得到欧拉-拉格朗日方程：$$\frac{d}{d t} \frac{\partial T}{\partial \dot{q}_j}-\frac{\partial T}{\partial q_j}=Q_j$$
当$F_i^\alpha$仅由不依赖于速度的势能给出，则广义力可写为：$$Q_j=-\frac{\partial V}{\partial q_j}$$上述结论可改写为：$$\frac{d}{dt}\frac{\partial L}{\partial \dot{q_j}}-\frac{\partial L}{\partial q_j}=0$$
其中L被称为拉格朗日量$$L=T-V$$

# <center><span style="color:blue">第二章 力学系统的作用量与运动方程</span></center> 





[^1]:<span style='color:blue'>完整约束系统：</span>约束方程仅依赖于系统的 位置坐标(广义坐标$q_i$)和时间t，且可表示为有限形式(而非微分形式):
$$f(q_1,q_2,…,q_n,t)=0$$
一个完整约束能够减少系统一个自由度,且一个完整约束若为微分形式，则其必定可积(存在原函数)
<span style='color:blue'>非完整约束系统：</span>约束方程显含速度(广义速度$\dot q_i$)或以不可积分的微分形式给出：
$$g(q_1,…,q_n,\dot q_1,…,\dot q_n,t)=0$$
[^2]:
[^3]:
[^4]: