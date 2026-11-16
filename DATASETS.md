# 数据集索引 / Datasets

点云相关常用数据集。年份为首次公开年份（可能有 ±1 偏差），以官方主页为准。

> 表中链接均为官方主页或官方仓库。发现失效或想补充，欢迎 [PR](CONTRIBUTING.md)。

## 分类与部件分割 / Classification & Part Segmentation

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| ModelNet40 | 合成物体分类 | 2015 | [modelnet.cs.princeton.edu](https://modelnet.cs.princeton.edu) |
| ModelNet40-C | 分类鲁棒性基准 | 2023 | [github.com/jisms/ModelNet40-C](https://github.com/jisms/ModelNet40-C) |
| ShapeNetCore | 合成物体分类/重建 | 2015 | [shapenet.org](https://www.shapenet.org/) |
| ShapeNet Part | 部件分割 | 2016 | [项目页](https://cs.stanford.edu/~ericyi/project_page/part_annotation/index.html) |
| PartNet | 层次化部件分割 | 2019 | [partnet.cs.stanford.edu](https://partnet.cs.stanford.edu/) |
| ScanObjectNN | 真实扫描物体分类 | 2019 | [hkust-vgd.github.io/scanobjectnn](https://hkust-vgd.github.io/scanobjectnn/) |

## 室内场景 / Indoor Scenes

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| NYUv2 | RGB-D 室内分割 | 2012 | [cs.nyu.edu](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) |
| SUN RGB-D | 室内检测/分割 | 2015 | [rgbd.cs.princeton.edu](https://rgbd.cs.princeton.edu/) |
| S3DIS | 室内语义分割 | 2016 | [buildingparser.stanford.edu](http://buildingparser.stanford.edu/dataset.html) |
| ScanNet | 室内分割/检测/重建 | 2017 | [scan-net.org](http://www.scan-net.org/) |
| Matterport3D | 室内重建/导航 | 2017 | [matterport.com](https://matterport.com/3d-space) |
| Replica | 高保真室内重建 | 2019 | [github.com/facebookresearch/Replica-Dataset](https://github.com/facebookresearch/Replica-Dataset) |
| HM3D | 室内导航（Habitat） | 2021 | [aihabitat.org/datasets/hm3d](https://aihabitat.org/datasets/hm3d/) |
| ScanNet++ | 高保真室内 DSLR 扫描 | 2023 | [kaldir.vc.in.tum.de/scannetpp](https://kaldir.vc.in.tum.de/scannetpp/) |

## 自动驾驶 / Autonomous Driving

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| KITTI | 检测/分割/里程计 | 2012 | [cvlibs.net/datasets/kitti](http://www.cvlibs.net/datasets/kitti/) |
| Oxford RobotCar | 长期定位 | 2016 | [robotcar-dataset.robots.ox.ac.uk](https://robotcar-dataset.robots.ox.ac.uk/) |
| SemanticKITTI | LiDAR 语义分割 | 2019 | [semantic-kitti.org](http://semantic-kitti.org/) |
| Argoverse 2 | 检测/预测 | 2021 | [argoverse.org](https://www.argoverse.org/) |
| ONCE | 大规模 3D 检测 | 2021 | [once-for-auto-driving.github.io](https://once-for-auto-driving.github.io/) |
| nuScenes | 检测/跟踪/分割 | 2020 | [nuscenes.org](https://www.nuscenes.org) |
| Waymo Open Dataset | 检测/跟踪/预测 | 2020 | [waymo.com/open](https://waymo.com/open/) |
| WOD-E2E / WOMD | 端到端/运动预测 | 2023 | [waymo.com/open](https://waymo.com/open/) |
| ScribbleKITTI | 弱监督分割 | 2022 | [github.com/ouenal/scribblekitti](https://github.com/ouenal/scribblekitti) |

## 室外/城市/航空 / Outdoor, Urban & Aerial

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| Semantic3D | 城市语义分割 | 2017 | [semantic3d.net](http://www.semantic3d.net/) |
| Toronto-3D | 城市道路分割 | 2020 | [github.com/WeikaiTan/Toronto-3D](https://github.com/WeikaiTan/Toronto-3D) |
| SensatUrban | 城市级摄影测量 | 2021 | [github.com/QingyongHu/SensatUrban](https://github.com/QingyongHu/SensatUrban) |
| STPLS3D | 合成+真实航空点云 | 2022 | [stpls3d.com](https://www.stpls3d.com) |
| DALES | 航空 LiDAR 分割 | 2020 | [laserscanninginstitute.github.io/DALES](https://laserscanninginstitute.github.io/DALES/) |

## 配准与重建 / Registration & Reconstruction

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| FAUST | 非刚性人体配准 | 2014 | [faust.is.tue.mpg.de](http://faust.is.tue.mpg.de/) |
| ICL-NUIM | RGB-D SLAM/重建 | 2014 | [项目页](https://www.doc.ic.ac.uk/~ahanda/VaFRIC/iclnuim.html) |
| Redwood | 室内重建 | 2016 | [redwood-data.org/3dscan](http://redwood-data.org/3dscan/) |
| 3DMatch | 局部特征/配准 | 2017 | [3dmatch.cs.princeton.edu](http://3dmatch.cs.princeton.edu/) |
| 3DLoMatch | 低重叠配准 | 2021 | [github.com/prs-eth/Predator](https://github.com/prs-eth/Predator) |

## 补全与生成 / Completion & Generation

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| PCN | 点云补全 | 2018 | [github.com/wentaoyuan/pcn](https://github.com/wentaoyuan/pcn) |
| Completion3D | 补全基准 | 2019 | [completion3d.stanford.edu](https://completion3d.stanford.edu/) |
| MVP | 补全（多视图先验） | 2021 | [mvp-dataset.github.io](https://mvp-dataset.github.io/) |
| Objaverse | 大规模 3D 物体 | 2023 | [objaverse.allenai.org](https://objaverse.allenai.org) |
| OmniObject3D | 大规模真实 3D 扫描 | 2023 | [omniobject3d.github.io](https://omniobject3d.github.io) |

## 占据与场景补全 / Occupancy & SSC

| 数据集 | 任务 | 年份 | 主页 |
|:--|:--|--:|:--|
| Occ3D | 3D 占据预测 | 2023 | [tsinghua-mars-lab.github.io/Occ3D](https://tsinghua-mars-lab.github.io/Occ3D/) |
| OpenOccupancy | 环视占据基准 | 2023 | [github.com/JeffWang987/OpenOccupancy](https://github.com/JeffWang987/OpenOccupancy) |
| SSCBench | 语义场景补全基准 | 2023 | [github.com/ai4ce/SSCBench](https://github.com/ai4ce/SSCBench) |

---

## 常用工具链 / Toolchain

| 工具 | 用途 | 链接 |
|:--|:--|:--|
| Open3D | 点云/网格处理与可视化 | [open3d.org](https://www.open3d.org/) |
| PCL | C++ 点云库 | [pointclouds.org](https://pointclouds.org/) |
| OpenPCDet | LiDAR 检测框架 | [github.com/open-mmlab/OpenPCDet](https://github.com/open-mmlab/OpenPCDet) |
| MMDetection3D | 统一 3D 检测工具箱 | [github.com/open-mmlab/mmdetection3d](https://github.com/open-mmlab/mmdetection3d) |
| Pointcept | 点云分割/检测框架 | [github.com/Pointcept/Pointcept](https://github.com/Pointcept/Pointcept) |
| Torch-Points3D | 点云深度学习框架 | [github.com/torch-points3d/torch-points3d](https://github.com/torch-points3d/torch-points3d) |
| MinkowskiEngine | 稀疏卷积 | [github.com/NVIDIA/MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) |
| CloudCompare | 点云查看/编辑 | [cloudcompare.org](https://www.cloudcompare.org/) |
