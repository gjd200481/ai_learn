# 环境清单

这份清单用于在其他电脑上快速配置当前 `D:\Ai_learn` 项目所需的 Python 机器学习环境。

## 当前环境

- 操作系统：Windows
- Conda：26.1.1
- Python：3.12.13
- 当前解释器：`.conda/dl_practice/python.exe`
- 主要用途：Jupyter Notebook、传统机器学习、PyTorch/MNIST 练习

## 项目用到的主要库

- Notebook：`jupyter`、`ipykernel`、`ipywidgets`
- 数据处理：`numpy`、`pandas`
- 可视化：`matplotlib`
- 机器学习：`scikit-learn`、`scipy`
- 深度学习：`torch`、`torchvision`、`torchaudio`、`torchinfo`
- 进度显示：`tqdm`

## 推荐安装方式

在新电脑安装 Anaconda 或 Miniconda 后，在项目根目录执行：

```powershell
conda env create -f environment.yml
conda activate ai-learn
python -m ipykernel install --user --name ai-learn --display-name "Python (ai-learn)"
```

然后启动 Jupyter：

```powershell
jupyter lab
```

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

如果在其他电脑使用 `environment.yml` 创建环境，建议在 VS Code 中手动选择 `ai-learn` 环境解释器。  
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

迁移到其他电脑时，把这些数据目录一起复制即可。MNIST 数据也可以由 `torchvision` 重新下载。

## 快速验证

配置完成后运行：

```powershell
python -c "import numpy, pandas, matplotlib, sklearn, torch, torchvision; print('environment ok')"
```

如果输出 `environment ok`，说明主要依赖已经安装成功。
