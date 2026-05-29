# 环境清单

这份清单用于在其他电脑上快速配置当前 `D:\Ai_learn` 项目所需的 Python 机器学习与深度学习环境。

## 当前环境

- 操作系统：Windows
- Conda：24.1.2
- Python：3.12.13
- 当前解释器：`.conda/dl_practice/python.exe`
- 主要用途：Jupyter Notebook、传统机器学习、PyTorch/MNIST/CIFAR10 练习
- GPU：NVIDIA GeForce RTX 3060 Laptop GPU
- PyTorch：2.5.1，CUDA 12.1，当前验证 `torch.cuda.is_available()` 为 `True`

## 项目用到的主要库

- Notebook：`notebook`、`jupyterlab`、`ipykernel`
- 数据处理：`numpy`、`pandas`
- 可视化：`matplotlib`
- 机器学习：`scikit-learn`、`scipy`
- 深度学习：`torch`、`torchvision`、`torchaudio`、`torchinfo`
- 进度显示：`tqdm`

## 推荐安装方式

在新电脑安装 Anaconda 或 Miniconda 后，在项目根目录执行：

```powershell
conda env create -f environment.yml
conda activate dl-practice
python -m ipykernel install --user --name dl-practice --display-name "Python (dl-practice)"
```

然后启动 Jupyter：

```powershell
jupyter lab
```

`environment.yml` 默认安装 GPU 版 PyTorch：

- `pytorch=2.5.1`
- `torchvision=0.20.1`
- `torchaudio=2.5.1`
- `pytorch-cuda=12.1`

需要 NVIDIA 显卡和可用的 NVIDIA 驱动。本机驱动显示支持 CUDA 12.3，可以运行 CUDA 12.1 版 PyTorch。

## 只使用 pip 的安装方式

如果不想使用 Conda，也可以用 Python 3.12 创建虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name ai-learn --display-name "Python (ai-learn)"
```

## 精确复现方式

如果希望尽量复现当前电脑上的所有包版本，使用 `requirements.lock.txt`：

```powershell
python -m pip install -r requirements.lock.txt
```

一般建议优先使用 `requirements.txt`；只有在课程代码或 Notebook 因版本差异报错时，再使用锁定版。

## VS Code 配置建议

当前项目的 VS Code 设置指向本机路径：

```json
"python.defaultInterpreterPath": "${workspaceFolder}\\.conda\\dl_practice\\python.exe"
```

如果在其他电脑使用 `environment.yml` 创建环境，建议在 VS Code 中手动选择 `Python (dl-practice)` 环境解释器。  
如果使用 `.venv`，可以改成：

```json
"python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe"
```

## 数据文件

项目中包含本地数据文件，例如：

- `data/studentscores.csv`
- `data/Data.csv`
- `data/datingTestSet2.txt`
- `data/MNIST/raw/*`
- `p1/data/MNIST/raw/*`
- `p2/data/cifar-10-batches-py/*`

迁移到其他电脑时，把这些数据目录一起复制即可。MNIST 和 CIFAR10 数据也可以由 `torchvision` 重新下载。大型数据目录已经在 `.gitignore` 中忽略，不建议提交到 Git。

## 快速验证

配置完成后运行：

```powershell
python -c "import numpy, pandas, matplotlib, sklearn, torch, torchvision; print('environment ok')"
```

如果输出 `environment ok`，说明主要依赖已经安装成功。

GPU 验证：

```powershell
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu')"
```
