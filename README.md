# Awesome Point Cloud Papers

<p align="center">
  <b>点云论文索引 · 2021 年至今 · 每日自动更新</b><br>
  <sub>Curated papers on 3D point clouds and LiDAR perception, 2021–present. Synced with arXiv.</sub>
</p>

[![Papers](https://img.shields.io/badge/papers-2755-blue)](#-papers)
[![With code](https://img.shields.io/badge/with_code-155-brightgreen)](#-papers)
[![Datasets](https://img.shields.io/badge/datasets-index-orange)](DATASETS.md)
[![Update](https://img.shields.io/badge/last_update-2026-11-16-lightgrey)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> 本列表由 `scripts/build.py` 从 [`data/entries.json`](data/entries.json) 自动生成，**请勿直接编辑本文件**。
> This README is generated. Add papers by editing `data/entries.json` (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## 目录 / Contents

- [论文 / Papers](#-papers)
- [按任务浏览 / Browse by task](#-browse-by-task)
- [只看已发表 / Peer-reviewed only](docs/published.md)
- [数据集 / Datasets](DATASETS.md)
- [贡献 / Contributing](CONTRIBUTING.md)

## 按任务浏览 / Browse by task

| 任务 | 篇数 | 列表 |
|:--|--:|:--|
| `segmentation` | 447 | [查看](docs/topics/segmentation.md) |
| `detection` | 430 | [查看](docs/topics/detection.md) |
| `autonomous driving` | 291 | [查看](docs/topics/autonomous-driving.md) |
| `registration` | 286 | [查看](docs/topics/registration.md) |
| `reconstruction` | 263 | [查看](docs/topics/reconstruction.md) |
| `efficiency` | 213 | [查看](docs/topics/efficiency.md) |
| `generation` | 209 | [查看](docs/topics/generation.md) |
| `robustness` | 193 | [查看](docs/topics/robustness.md) |
| `localization` | 160 | [查看](docs/topics/localization.md) |
| `multi-modal` | 151 | [查看](docs/topics/multi-modal.md) |
| `self-supervised` | 139 | [查看](docs/topics/self-supervised.md) |
| `completion` | 132 | [查看](docs/topics/completion.md) |
| `classification` | 121 | [查看](docs/topics/classification.md) |
| `compression` | 115 | [查看](docs/topics/compression.md) |
| `tracking` | 78 | [查看](docs/topics/tracking.md) |
| `slam` | 74 | [查看](docs/topics/slam.md) |
| `dataset` | 71 | [查看](docs/topics/dataset.md) |
| `denoising` | 64 | [查看](docs/topics/denoising.md) |
| `pre-training` | 60 | [查看](docs/topics/pre-training.md) |
| `upsampling` | 55 | [查看](docs/topics/upsampling.md) |
| `gaussian-splatting` | 48 | [查看](docs/topics/gaussian-splatting.md) |
| `open-vocabulary` | 35 | [查看](docs/topics/open-vocabulary.md) |
| `monocular` | 30 | [查看](docs/topics/monocular.md) |
| `scene flow` | 30 | [查看](docs/topics/scene-flow.md) |
| `BEV` | 27 | [查看](docs/topics/bev.md) |
| `domain adaptation` | 21 | [查看](docs/topics/domain-adaptation.md) |
| `anomaly detection` | 20 | [查看](docs/topics/anomaly-detection.md) |
| `normal estimation` | 20 | [查看](docs/topics/normal-estimation.md) |
| `vision-language` | 16 | [查看](docs/topics/vision-language.md) |
| `nerf` | 14 | [查看](docs/topics/nerf.md) |
| `occupancy prediction` | 11 | [查看](docs/topics/occupancy-prediction.md) |

---

## 论文 / Papers

### 2026 <sub>(355)</sub>

<details><summary><b>CVPR</b> · 11</summary>

- [3D sans 3D Scans: Scalable Pre-training from Video-Generated Point Clouds](https://arxiv.org/abs/2512.23042) — `self-supervised` `pre-training`
- [AnyPcc: Compressing Any Point Cloud with a Single Universal Model](https://arxiv.org/abs/2510.20331) — `compression`
- [Edge Prediction for Roof Wireframe Reconstruction with Transformers](https://arxiv.org/abs/2606.02406) — `reconstruction` — Workshop
- [FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement](https://arxiv.org/abs/2512.09373) — `registration`
- [GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation](https://arxiv.org/abs/2512.23180) — `generation` `BEV` `multi-modal`
- [Geometric-Aware Hypergraph Reasoning for Novel Class Discovery in Point Cloud Segmentation](https://arxiv.org/abs/2606.07280) — `segmentation`
- [LitePT: Lighter Yet Stronger Point Transformer](https://arxiv.org/abs/2512.13689)
- [MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence](https://arxiv.org/abs/2606.02463) — Workshop
- [QVGGT: Post-Training Quantized Visual Geometry Grounded Transformer](https://arxiv.org/abs/2605.31124) — `efficiency`
- [S2AM3D: Scale-controllable Part Segmentation of 3D Point Clouds](https://arxiv.org/abs/2512.00995) — `segmentation`
- [Text-guided Feature Disentanglement for Cross-modal Gait Recognition](https://arxiv.org/abs/2605.30784)

</details>

<details><summary><b>ECCV</b> · 33</summary>

- [4D-RaDiff: Latent Point Diffusion for 4D Radar Point Cloud Generation](https://arxiv.org/abs/2512.14235) — `generation` `multi-modal`
- [Benchmarking Federated Learning and Knowledge Distillation for Point Cloud Classification](https://arxiv.org/abs/2607.01272) — `classification`
- [Bootstrapping a 4D LiDAR Annotation Tool from Video Foundation Models](https://arxiv.org/abs/2608.25418) — `segmentation` — Workshop
- [C2E: Boosting Ego-Only 3D Object Detection via Multi-Teacher Contrastive Knowledge Distillation](https://arxiv.org/abs/2607.01827) — `detection` `autonomous driving`
- [CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes](https://arxiv.org/abs/2608.18734) — `pre-training` `vision-language`
- [Comprehensive Robustness Analysis of LiDAR-based 3D Object Detection in Autonomous Driving](https://arxiv.org/abs/2607.02074) — `detection` `autonomous driving` `robustness`
- [Coordinate Frame Recovery, Per Class NMS and Null Return Modelling for Sim2Real V2X LiDAR Detection](https://arxiv.org/abs/2611.03940) — `detection` — [code](https://github.com/amanupg/urbantwin-sim2real-v2x) Workshop
- [DRS-VPT: Directly Relocalizing in a Scan with Vision Point Transformers](https://arxiv.org/abs/2609.12557) — `registration` — [code](https://github.com/ori-drs/drs-vpt)
- [Explainability-Aware Frustum Attack: Exposing Structural Vulnerabilities in LiDAR-Based 3D Object Detectors](https://arxiv.org/abs/2606.29963) — `detection`
- [FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549) — `generation` `nerf` `gaussian-splatting`
- [Geometric Refinement and Distributional Alignment for Sim2Real Roadside LiDAR Detection](https://arxiv.org/abs/2611.03936) — `detection` — [code](https://github.com/amanupg/urbantwin-sim2real-lumpi) Workshop
- [GhostPoint: Self-Supervised Representation Learning by Hallucinating Occluded LiDAR Structure](https://arxiv.org/abs/2608.14428) — `segmentation` `detection` `self-supervised` `autonomous driving`
- [Hyper-Network Neural Functional Maps for Unsupervised Robust 3D Shape Matching](https://arxiv.org/abs/2606.30131) — `robustness`
- [Learning to Tessellate: Point Cloud Generation via Recursive Spectral Partitioning](https://arxiv.org/abs/2608.02432) — `generation`
- [Mind2Cloud: EEG-to-Point Cloud Generation with Two-Granularity Diffusion Decoding](https://arxiv.org/abs/2609.13991) — `generation` `reconstruction` `denoising`
- [mmIR: Frequency-Space Inverse Rendering for 3D Millimeter-Wave Radar ADC Synthesis](https://arxiv.org/abs/2608.28913) — `multi-modal`
- [NoPA: Non-Parametric Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.00529) — `generation`
- [OmniX: Any-view and Any-time 4D Reconstruction via Feed-forward Trajectory Fields](https://arxiv.org/abs/2607.10840) — `reconstruction`
- [One Video, One World: Turning Monocular Video into Physical 4D Scenes](https://arxiv.org/abs/2606.31388) — `reconstruction` `monocular`
- [P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing](https://arxiv.org/abs/2609.03349) — `reconstruction` `self-supervised`
- [Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point Cloud Understanding](https://arxiv.org/abs/2607.19171) — `efficiency` — [code](https://github.com/JunLinChang/ECCV2026-PLT)
- [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780) — `detection` `efficiency`
- [PrintAnything: Learning an Intermediate Representation for 3D printing G-code Generation](https://arxiv.org/abs/2607.27729) — `generation`
- [RadarGen: Automotive Radar Point Cloud Generation from Cameras](https://arxiv.org/abs/2512.17897) — `generation` `BEV` `multi-modal`
- [RAF: Reliability-Aware Fusion of Camera, LiDAR, and 4D RADAR for Robust 3D Object Detection in Adverse Weather](https://arxiv.org/abs/2607.04587) — `detection` `multi-modal` `robustness`
- [Reducing the Gap Between Spatial and Space-Filling Curve Neighbors in 3D Point Cloud Segmentation](https://arxiv.org/abs/2610.19530) — `segmentation` — Workshop
- [RESOLVE: A Multi-Resolution and Multi-Modal Dataset for Roadside Cooperative Perception](https://arxiv.org/abs/2606.31895) — `multi-modal` `dataset`
- [Scale Matters: Adaptive Granularity Selection for Cross-Species 3D Plant Organ Segmentation](https://arxiv.org/abs/2608.17803) — `segmentation` — Workshop
- [Sen-Cap: Sensor-Flexible and Noise-Resilient Human Motion Capture via LiDAR-Camera Integration](https://arxiv.org/abs/2608.02285) — `multi-modal`
- [TopoField: Technical Report for ECCV 2026 SceneFun3D Challenge](https://arxiv.org/abs/2610.37218) — `segmentation` — Workshop
- [UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound](https://arxiv.org/abs/2609.11506) — `segmentation` `completion`
- [Unsupervised Point Cloud Registration via Training-Time Semantic Guidance](https://arxiv.org/abs/2609.15228) — `registration`
- [White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2509.13907) — `segmentation`

</details>

<details><summary><b>NeurIPS</b> · 8</summary>

- [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](https://arxiv.org/abs/2610.21190) — `generation` `upsampling`
- [FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection](https://arxiv.org/abs/2611.09170) — `detection`
- [LiFi: LiDAR Generation from Multi-View Images via Geometric and Semantic Collaborative Guidance](https://arxiv.org/abs/2610.19786) — `generation`
- [MemReg: Streaming Outdoor LiDAR Point Cloud Registration with Hybrid Memory Buffers](https://arxiv.org/abs/2610.12624) — `registration`
- [Register Anything Model for Generalizable and Robust Point Cloud Registration](https://arxiv.org/abs/2610.28821) — `registration` `robustness` — [code](https://github.com/qinzheng93/RegisterAnything)
- [Rethinking Radar 3D Perception: Representation Learning from Raw Spectra](https://arxiv.org/abs/2611.12334) — `multi-modal`
- [SIEVE: Overcoming Topological Obstruction in Equivariant Self-Supervised Learning](https://arxiv.org/abs/2610.21087) — `self-supervised`
- [Towards Generalizable 3D Anomaly Detection via Relational Inconsistency Modeling](https://arxiv.org/abs/2609.35059) — `detection` `anomaly detection` — [code](https://github.com/VisualScienceLab-KHU/GRIM)

</details>

<details><summary><b>ICLR</b> · 1</summary>

- [Point-Focused Attention Meets Context-Scan State Space: Robust Biological Visual Perception for Point Cloud Representation](https://arxiv.org/abs/2610.11342) — `robustness`

</details>

<details><summary><b>ICML</b> · 5</summary>

- [DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](https://arxiv.org/abs/2606.12189) — `reconstruction`
- [FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation](https://arxiv.org/abs/2605.27178) — `segmentation` `self-supervised` — [code](https://github.com/vLAR-group/FoundObj)
- [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://arxiv.org/abs/2606.12334)
- [SIMPC: Learning Self-Induced Mirror-Point Consistency for Unsupervised Point Cloud Denoising](https://arxiv.org/abs/2605.26894) — `denoising`
- [Zero-Shot 3D Question Answering via Hierarchical View-to-Token Transportation](https://arxiv.org/abs/2606.03100) — `open-vocabulary`

</details>

<details><summary><b>AAAI</b> · 20</summary>

- [3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2511.07040) — `robustness`
- [Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models](https://arxiv.org/abs/2511.15311) — `open-vocabulary` `vision-language`
- [Adaptive Agent Selection and Interaction Network for Image-to-point cloud Registration](https://arxiv.org/abs/2511.05965) — `registration` `detection`
- [BEVDilation: LiDAR-Centric Multi-Modal Fusion for 3D Object Detection](https://arxiv.org/abs/2512.02972) — `detection` `BEV` `multi-modal`
- [CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection](https://arxiv.org/abs/2511.12909) — `detection` `self-supervised` `anomaly detection`
- [Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain](https://arxiv.org/abs/2511.07029) — `classification` `autonomous driving` `robustness`
- [CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking](https://arxiv.org/abs/2511.15580) — `tracking` `compression` `autonomous driving`
- [DANCE: Density-agnostic and Class-aware Network for Point Cloud Completion](https://arxiv.org/abs/2511.07978) — `completion`
- [DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion](https://arxiv.org/abs/2511.20278) — `completion`
- [DriveLiDAR4D: Sequential and Controllable LiDAR Scene Generation for Autonomous Driving](https://arxiv.org/abs/2511.13309) — `generation` `autonomous driving`
- [Enhancing Rotation-Invariant 3D Learning with Global Pose Awareness and Attention Mechanisms](https://arxiv.org/abs/2511.08833)
- [EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios with Language Guidance](https://arxiv.org/abs/2511.11700) — `segmentation` `open-vocabulary` `efficiency`
- [Hierarchical Direction Perception via Atomic Dot-Product Operators for Rotation-Invariant Point Clouds Learning](https://arxiv.org/abs/2511.08240) — [code](https://github.com/wxszreal0/DiPVNet)
- [LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures](https://arxiv.org/abs/2511.10209) — `completion` `reconstruction` `efficiency`
- [MR-COSMO: Visual-Text Memory Recall and Direct CrOSs-MOdal Alignment Method for Query-Driven 3D Segmentation](https://arxiv.org/abs/2506.20991) — `segmentation`
- [Point Cloud Quantization through Multimodal Prompting for 3D Understanding](https://arxiv.org/abs/2511.12079) — `multi-modal` `efficiency`
- [Real-Time 3D Object Detection with Inference-Aligned Learning](https://arxiv.org/abs/2511.16140) — `detection` `efficiency`
- [Rethinking Multimodal Point Cloud Completion: A Completion-by-Correction Perspective](https://arxiv.org/abs/2511.12170) — `completion` `multi-modal`
- [Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation](https://arxiv.org/abs/2512.19088) — `segmentation` `open-vocabulary` — Workshop
- [Understanding Dynamic Scenes in Ego Centric 4D Point Clouds](https://arxiv.org/abs/2508.07251)

</details>

<details><summary><b>SIGGRAPH Asia</b> · 1</summary>

- [CRAB: Cuboid-based Representation for As-built BIM from Point Clouds](https://arxiv.org/abs/2610.29257) — `reconstruction`

</details>

<details><summary><b>ACM MM</b> · 6</summary>

- [Leveraging 2D Foundation Priors for Generalized Category Discovery under Test-Time Adaptation in 3D LiDAR Segmentation](https://arxiv.org/abs/2611.01682) — `segmentation` `autonomous driving`
- [MMCoT$^3$: Empowering 3D Scene Understanding with 3D-Text Interleaved Multi-Modal Chain-of-Thought Reasoning](https://arxiv.org/abs/2611.01676) — `multi-modal`
- [PointQ-Bench: Benchmarking Diagnostic and Interpretable Point Cloud Quality Assessment](https://arxiv.org/abs/2605.28241) — `reconstruction`
- [ProjFormer: Point Cloud Completion via Geometric-Projective Transformer and Cross-Modal Semantic Constraints](https://arxiv.org/abs/2608.15104) — `completion`
- [SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding](https://arxiv.org/abs/2608.30451) — `dataset`
- [VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction](https://arxiv.org/abs/2608.15260) — `reconstruction` — [code](https://github.com/WZ-CS/VGGT-Align)

</details>

<details><summary><b>3DV</b> · 1</summary>

- [Hierarchical Space Partition for Surface Reconstruction](https://arxiv.org/abs/2606.04891) — `reconstruction`

</details>

<details><summary><b>WACV</b> · 11</summary>

- [3D-BBDA: Backpropagation-Free Black-Box Domain Adaptation for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2611.03588) — `domain adaptation` `robustness`
- [Do We Still Need Rotation-Invariant Architectures? A Statistical Robustness Benchmark for Point Cloud Classification](https://arxiv.org/abs/2611.03952) — `classification` `robustness` `dataset`
- [Embedding Predictive Adaptation and Refinement for Multi-Modal Industrial Anomaly Detection](https://arxiv.org/abs/2611.09521) — `detection` `multi-modal` `anomaly detection`
- [GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243) — `reconstruction` `monocular`
- [RadPose: ISAC-based RF 3D Human Pose Estimation](https://arxiv.org/abs/2611.01400)
- [Recovering Black-Box Point Cloud Models from Pose Shifts via Derivative-Free Optimization](https://arxiv.org/abs/2610.34850)
- [Rohbau3D-Semantics: Dense Semantic and Instance Labels for Point Clouds of Indoor Shell Construction Scenes](https://arxiv.org/abs/2611.06180)
- [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](https://arxiv.org/abs/2610.36658) — `registration` `reconstruction`
- [SATOR: Backpropagation-Free 3D Test-Time Adaptation via Sample-Adaptive Token Routing](https://arxiv.org/abs/2610.21367)
- [VaViT: Vanilla ViT for Automotive Point Cloud Semantic Segmentation](https://arxiv.org/abs/2605.31177) — `segmentation`
- [You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows](https://arxiv.org/abs/2608.09579) — `denoising` `multi-modal` `efficiency`

</details>

<details><summary><b>BMVC</b> · 6</summary>

- [3D-MRL: Nested Multimodal 3D Representations via Matryoshka Representation Learning](https://arxiv.org/abs/2608.29285) — `open-vocabulary` `multi-modal`
- [FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence](https://arxiv.org/abs/2608.07937) — `gaussian-splatting` — [code](https://github.com/amir-sbg/FlexSplat)
- [ForestMamba: Sparse Mamba with Geometry-guided Queries for 3D Forest Point Cloud Segmentation](https://arxiv.org/abs/2606.01549) — `segmentation`
- [GEKey: Learning Geodesic Eccentric 3D Keypoints via Self-Supervision](https://arxiv.org/abs/2611.07677) — `detection`
- [Hyper^2: Unleashing Hyperbolic Geometry's Full Potential via Dual-Space Consistency](https://arxiv.org/abs/2608.22238) — `completion`
- [ReFineR: Single image to dense point cloud registration at pixel level with point splatting](https://arxiv.org/abs/2611.16583) — `registration` `detection`

</details>

<details><summary><b>ICRA</b> · 1</summary>

- [Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model](https://arxiv.org/abs/2607.06896) — `detection` `tracking` `slam` — Workshop

</details>

<details><summary><b>IROS</b> · 9</summary>

- [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](https://arxiv.org/abs/2606.31329) — [code](https://github.com/DAVIAN-Robotics/3D_HAMSTER)
- [DeeperRadar: End-to-End MIMO Radar Design and Multi-Modal Fusion for Autonomous Vehicle Perception](https://arxiv.org/abs/2607.17351) — `detection` `multi-modal`
- [DiFF: Doppler-informed Flow Matching for Human Motion Flow](https://arxiv.org/abs/2609.39098) — `generation` `scene flow` — [code](https://github.com/keroseus/DiFF)
- [FIRE-LIVWO: Robust LiDAR-Inertial-Visual-Wheel Odometry via Failure-Immune mmWave Radar Enhancement](https://arxiv.org/abs/2609.05325) — `slam` `multi-modal` `robustness`
- [Hydra++: Real-Time Hierarchical 3D Scene Graph Construction With Object-Level Shape Estimation](https://arxiv.org/abs/2607.09455) — `efficiency`
- [Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping](https://arxiv.org/abs/2609.26325) — `detection` `autonomous driving` — Workshop
- [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878) — `reconstruction`
- [Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Platform](https://arxiv.org/abs/2607.18578)
- [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919) — `self-supervised` — [code](https://github.com/rai-opensource/vernata)

</details>

<details><summary><b>RA-L</b> · 6</summary>

- [C-ARC: Continuous-Adaptive Range Clustering for Non-Repetitive LiDAR Sensors](https://arxiv.org/abs/2606.18948)
- [EquiGQNet: Fast Grasp Quality Evaluation via Shared Equivariant Point Cloud Encoding](https://arxiv.org/abs/2609.07145)
- [Geometry-Aware Fisheye-LiDAR Fusion for Robust 3D Object Detection in Low-Overlap Setups](https://arxiv.org/abs/2606.08844) — `detection` `robustness`
- [Point Cloud Segmentation for Autonomous Clip Positioning in Laparoscopic Cholecystectomy on a Phantom](https://arxiv.org/abs/2606.12048) — `segmentation`
- [PointWalker: Mapless Quadruped Locomotion Directly From Raw LiDAR Point Clouds](https://arxiv.org/abs/2610.15548)
- [UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping](https://arxiv.org/abs/2606.26928)

</details>

<details><summary><b>TPAMI</b> · 1</summary>

- [GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model](https://arxiv.org/abs/2609.19716) — [code](https://github.com/PKU-OV3-LAB/GAPromptPlus.git)

</details>

<details><summary><b>ISPRS</b> · 3</summary>

- [3D Point Cloud from Close-Range Photogrammetry for Defect Characterisation of Rubberised Concrete](https://arxiv.org/abs/2608.21468) — `anomaly detection`
- [DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring](https://arxiv.org/abs/2610.09860)
- [Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509) — `slam` `gaussian-splatting`

</details>

<details><summary><b>PR</b> · 2</summary>

- [Loss Landscape Topology Reveals Why Simple Baselines are Competitive at 3D Point Cloud Segmentation Under Class Imbalance](https://arxiv.org/abs/2607.21089) — `segmentation`
- [Physics-inspired Pseudo Anomaly Generation and Prototype Feature Guidance for 3D Anomaly Detection](https://arxiv.org/abs/2607.10544) — `detection` `generation` `anomaly detection`

</details>

<details><summary><b>arXiv</b> · 230</summary>

- [4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956) — `gaussian-splatting`
- [A Differentiable Optimization Framework for Registering Sequential Bounding Boxes with Point Cloud Stream](https://arxiv.org/abs/2609.34103) — `registration`
- [A Numerically-Robust ROS 2 Port of iG-LIO: Diagnosing and Fixing Toolchain-Induced Failures in Incremental GICP LiDAR-Inertial Odometry](https://arxiv.org/abs/2607.09947) — `robustness`
- [A Point Cloud Transformer for Remote Monitoring and Automated Assessment of Physical Rehabilitation Exercises](https://arxiv.org/abs/2606.30309)
- [A Robust Point Cloud Analysis Framework Inspired By Primary Visual Cortex](https://arxiv.org/abs/2606.14292) — `robustness`
- [A Systematic Point Cloud Edge Detection Framework for Automatic Aircraft Skin Milling](https://arxiv.org/abs/2611.04435) — `detection`
- [A Three-Dimensional Reverse-Projection Method for Sparse Point Cloud Completion and Its Application to High-Speed Train Nose Reconstruction](https://arxiv.org/abs/2610.05758) — `completion` `reconstruction`
- [A Vendor-Agnostic LiDAR Data Conversion System with Multi-Signal Detection and Multi-Format Output](https://arxiv.org/abs/2606.22881) — `detection`
- [A Vision-Language Model (VLM)-based Pipeline for End-to-End Procedural Modeling of Field-Grown Maize from Point Clouds](https://arxiv.org/abs/2610.03468) — `segmentation` `vision-language`
- [Accelerating Large-scale Bundle Adjustment for LiDAR Mapping via Parallel Computing](https://arxiv.org/abs/2608.14266)
- [Active Spiking Perception: The Membrane Potential as a Belief State for Anytime 3D Point Cloud Recognition](https://arxiv.org/abs/2608.19232)
- [ACZ-GSeg: Adaptive Concentric Zone-based Two-stage Ground Segmentation for LiDAR Point Clouds](https://arxiv.org/abs/2607.12110) — `segmentation` `detection`
- [Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration](https://arxiv.org/abs/2609.01089) — `registration` `reconstruction`
- [Adversarially Guided Diffusion for LiDAR Range Image Synthesis](https://arxiv.org/abs/2607.09787) — `segmentation` `classification` `autonomous driving` — Workshop
- [Aerial Content-Aware Sample-Adaptive Classifier for Urban Photogrammetric Point Cloud Segmentation](https://arxiv.org/abs/2611.02844) — `segmentation`
- [Aerial-ground LiDAR place recognition with patch-level self-supervised learning and expanded reciprocal re-ranking](https://arxiv.org/abs/2606.18583) — `localization` `self-supervised`
- [An Automated Georeferencing Technique for Multi-Temporal Stope Point Clouds for Downstream Geotechnical Analysis](https://arxiv.org/abs/2609.29186)
- [An Enhanced Geometric-Spectral Feature Learning Framework for Airborne Multispectral Point Cloud Classification](https://arxiv.org/abs/2606.09123) — `classification`
- [AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds](https://arxiv.org/abs/2611.03228)
- [Assessing the Operational Impact of Poisoning Attacks over Augmented 3D Point Cloud Public Datasets for Connected and Autonomous Vehicles](https://arxiv.org/abs/2607.06484)
- [Autoencoder Based Deep Clustering of Point Clouds](https://arxiv.org/abs/2611.01594) — `generation` `reconstruction`
- [Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap](https://arxiv.org/abs/2606.16570)
- [Bayesian methods and Markov chain Monte Carlo algorithms for curve reconstruction and point cloud data analysis](https://arxiv.org/abs/2608.26490) — `localization` `reconstruction`
- [Beyond Gait: Person Identification from Millimeter-Wave Point Clouds Across Activities of Daily Living](https://arxiv.org/abs/2609.08818)
- [Beyond Visibility: Real-Time Surface Accessibility Fields from Sparse LiDAR](https://arxiv.org/abs/2608.06412) — `reconstruction` `efficiency`
- [Boundary Detection for High-Dimensional Point Clouds](https://arxiv.org/abs/2610.23590) — `detection`
- [Boundary-Enhanced Segmentation of Pig Point Clouds in Commercial Housing Environments](https://arxiv.org/abs/2608.11697) — `segmentation` `completion`
- [BRICE: Brain-inspired Recurrent Illusory Contour Encoder for Point Cloud Completion](https://arxiv.org/abs/2610.23001) — `completion`
- [Camera and LiDAR BEV Fusion for Cooperative 3D Object Detection on TUMTraf V2X](https://arxiv.org/abs/2606.12981) — `detection` `BEV`
- [Camera Radar LiDAR Fusion via Point-Cloud Projection for Multi-Task Learning](https://arxiv.org/abs/2611.03942) — `multi-modal` — Workshop
- [CedarCypress3D: an annotated UAV-LiDAR dataset of individual trees in planted cedar and cypress forests](https://arxiv.org/abs/2608.30149) — `detection` `dataset`
- [Characterizing the vertical continuity of fuel strata based on TLS point clouds Gaussian decomposition and overlap metrics](https://arxiv.org/abs/2611.05102)
- [CloudDiffusion: Diffusion-Based Scene Completion in the Point Cloud Domain](https://arxiv.org/abs/2606.16048) — `completion` `reconstruction` `autonomous driving`
- [Collision-Aware and Observation-Aligned Object-Centric Scene Reconstruction from Point Cloud](https://arxiv.org/abs/2609.37260) — `generation` `reconstruction`
- [Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452) — `reconstruction` `gaussian-splatting`
- [Complexity-Calibrated Reconstruction Discrepancy for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2610.13219) — `reconstruction`
- [CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving](https://arxiv.org/abs/2608.14332) — `tracking`
- [CorrelationFlow: A Training-Free Geometric Approach for LiDAR Scene Flow Estimation](https://arxiv.org/abs/2607.29237) — `scene flow` `autonomous driving`
- [COSTA: A Cluster-Centric Paradigm for Annotation-Free Open-Set Semantic Segmentation of Aerial Point Clouds with Domain Shifts](https://arxiv.org/abs/2608.18479) — `segmentation`
- [Cross-Coordinate Correspondence Pruning for Image-to-Point Cloud Registration](https://arxiv.org/abs/2607.17200) — `registration` `detection` `efficiency`
- [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](https://arxiv.org/abs/2607.00514) — `self-supervised`
- [CUFormer: Modality-Aware CT-Ultrasound Point Cloud Registration for Orthopedic Navigation](https://arxiv.org/abs/2611.01536) — `registration`
- [CVSD-Reg: Cross-Modal Visual Semantic Prior Distillation for Robust LiDAR Registration](https://arxiv.org/abs/2608.19536) — `registration` `robustness`
- [Cyclops: LiDAR as a Camera That Dreams in Color](https://arxiv.org/abs/2608.16264) — `detection` — [code](https://github.com/IMRL/Cyclops)
- [DAL-PCQA: Enabling Distortion-Level and Language-Driven Reasoning for Point Cloud Quality Assessment](https://arxiv.org/abs/2606.07938)
- [Damage Classification for 3D Point Cloud Data via 3D Data Analysis and Vision Foundation Model-based 2D Projections](https://arxiv.org/abs/2608.08955) — `classification` `pre-training`
- [DAPointRWKV: Domain Adaptive Vision RWKV for Point Cloud Completion](https://arxiv.org/abs/2611.10353) — `completion`
- [Degree Bounds for Separating Polynomial and Neural Invariants for Point Clouds](https://arxiv.org/abs/2610.26612)
- [Denoising-Aware Temporal Point Cloud Completion for 3D Crop Architecture Recovery and Phenotypic Trait Extraction](https://arxiv.org/abs/2608.28343) — `completion` `reconstruction` `denoising`
- [Depth-Dependent Hidden-State Collapse in Dynamical System Autoencoders for LiDAR Point-Cloud Classification](https://arxiv.org/abs/2607.14463) — `classification`
- [Depth-Semantic Alignment and Affinity-Guided Fusion for Structured Radar Point Cloud Generation](https://arxiv.org/abs/2606.26743) — `detection` `tracking` `generation` `multi-modal`
- [DINE: Distance Is Not Enough -- Learning Global Deformation Priors for Robust Soft-Tissue Point Cloud Registration](https://arxiv.org/abs/2607.14946) — `registration` `robustness`
- [Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations and Goals](https://arxiv.org/abs/2608.29434)
- [DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving](https://arxiv.org/abs/2608.26589) — `registration` `localization` `autonomous driving`
- [Drones as Annotators: Amodal 3D Auto-Labeling for Ground LiDAR with Aerial Priors](https://arxiv.org/abs/2609.06819) — `autonomous driving`
- [Efficient RWKV-based Representation Learning for 3D Point Clouds](https://arxiv.org/abs/2606.10395) — `efficiency`
- [EgoNeMo: Transferable Map of Pedestrian Dynamics via Egocentric LiDAR Scan](https://arxiv.org/abs/2609.06195)
- [EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion](https://arxiv.org/abs/2609.26039) — `generation`
- [EXACT-MPPI: Exact Signed-Distance Navigation for Arbitrary-Footprint Robots from Point Clouds via Path Integral Control](https://arxiv.org/abs/2605.29663)
- [Exploring Easy Boosts for Lidar Semantic Scene Completion](https://arxiv.org/abs/2606.03992) — `completion` `occupancy prediction`
- [Fast and Accurate Outlier-Aware LiDAR Super-Resolution for SLAM Applications](https://arxiv.org/abs/2606.28607) — `slam` `upsampling`
- [Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168) — `gaussian-splatting`
- [FlashReg: GPU-Accelerated 3-Clique Point Cloud Registration for Real-Time Correspondence-to-Pose Estimation](https://arxiv.org/abs/2608.21804) — `registration` `efficiency`
- [FLIP: Real-Time and Resilient Formation Planning for Large-Scale DIstributed Swarms via Point Cloud Registration](https://arxiv.org/abs/2605.29704) — `registration` `efficiency`
- [FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data](https://arxiv.org/abs/2606.32023)
- [Fog-FWL: A Large-Scale Full-Waveform LiDAR Dataset for Recovering Fog-Hidden Objects](https://arxiv.org/abs/2611.16742) — `detection` `autonomous driving` `dataset`
- [ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation](https://arxiv.org/abs/2610.03403) — `segmentation`
- [FPSGen: Flexible Point Cloud Scene Generation with BEV-Supported Transport Flows](https://arxiv.org/abs/2607.26645) — `completion` `generation` `BEV`
- [FREE-LIVO: Physically Decoupled Yet Tightly Coupled LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2611.07463) — `slam`
- [From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation](https://arxiv.org/abs/2609.27363) — `localization` `robustness`
- [G$^2$ARD-GS: Geometry-Guided Anchor-Regularized Gaussian Splatting Distillation](https://arxiv.org/abs/2608.05704) — `gaussian-splatting`
- [Gaussian Linear Functional Manifold Method for Massive Point Cloud Data](https://arxiv.org/abs/2609.05744) — `reconstruction`
- [Generalized-CVO: Fast and Correspondence-Free Local Point Cloud Registration with Second Order Riemannian Optimization](https://arxiv.org/abs/2606.10019) — `registration`
- [GeoISF: Instance Semantic Forest Inspired Large-Scale Cross-View Geo-Localization via Ground LiDAR-to-Satellite Image](https://arxiv.org/abs/2606.28371) — `localization`
- [Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity](https://arxiv.org/abs/2609.16378)
- [Geometry Without Coordinates: LiDAR Diffusion as a 3D Feature Bridge](https://arxiv.org/abs/2609.10322) — `generation`
- [Geometry-Based Compression of Plenoptic Point Clouds](https://arxiv.org/abs/2608.11273) — `compression`
- [Geometry-Constrained Bidirectional Point Cloud Registration for Thin, Sheet-Like Heritage Artifacts](https://arxiv.org/abs/2610.07793) — `registration` `reconstruction`
- [Geometry-Preserving Blind Watermarking for Raw 3D Point Clouds](https://arxiv.org/abs/2609.32222)
- [GRAR: Glass-induced Reflection Artifact Removal in LiDAR Point Clouds](https://arxiv.org/abs/2606.10541)
- [GridFlow: Structured Latent Flow for Seamless City-Scale 3D Point Cloud Generation](https://arxiv.org/abs/2608.29793) — `generation`
- [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.25966) — `registration`
- [GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds](https://arxiv.org/abs/2606.05650) — `gaussian-splatting`
- [GSPotential: Camera Potential Field for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2608.29346) — `gaussian-splatting`
- [GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly](https://arxiv.org/abs/2610.09068) — `segmentation` `reconstruction` `denoising`
- [H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression](https://arxiv.org/abs/2609.02684) — `compression`
- [Hardware-triggered Time Synchronization of Roadside Multi-lidar, Multi-camera Measurement System for Accurate Data Alignment](https://arxiv.org/abs/2607.15889) — [code](https://github.com/shiva-THI/hardware-trigger-time-sync-lidar-cameras)
- [Heat Field Signatures: From Point Clouds to Smooth Geometry](https://arxiv.org/abs/2609.07975)
- [Hierarchical Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2608.05557) — `generation` `denoising`
- [Hierarchical Frequency-Domain Compression of Implicit Geometric Representations for Large-Scale Point Clouds](https://arxiv.org/abs/2609.32789) — `compression`
- [How Sampling Strategy Affects Imbalance Mitigation in LiDAR Segmentation: A Study of Structured vs. Random Point-Based Architectures](https://arxiv.org/abs/2608.16673) — `segmentation`
- [HuLiGen: Human LiDAR Generation from Parametric Body Models](https://arxiv.org/abs/2610.10196) — `generation`
- [Illumination-Invariant Anomaly Detection for Sub-Canopy UAV Multispectral Point Clouds](https://arxiv.org/abs/2606.09111) — `detection` `anomaly detection`
- [Image-to-Point Cloud Registration Made Easy with Rectified Flow-based LiDAR Upsampling](https://arxiv.org/abs/2607.14639) — `registration` `upsampling`
- [Implementation of Tightly-Coupled SLAM Fusion of GPS, IMU, and LiDAR for Autonomous Vehicles](https://arxiv.org/abs/2609.20321) — `slam` `localization`
- [IndoorBEV: A Lightweight Real-Time LiDAR BEV Perception System for Indoor Mobile Robots](https://arxiv.org/abs/2610.00355) — `BEV` `efficiency`
- [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](https://arxiv.org/abs/2610.19201) — `generation` `reconstruction` `efficiency`
- [IRGNN: Efficient Invariant Radar Graph Neural Network for Radar Point Cloud Object Detection](https://arxiv.org/abs/2608.14394) — `detection` `autonomous driving` `multi-modal` `efficiency`
- [Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos](https://arxiv.org/abs/2608.24093) — `reconstruction` `self-supervised`
- [Learned Radius Estimation for UDF-Based Point Cloud Reconstruction](https://arxiv.org/abs/2606.18787) — `reconstruction`
- [Learning Biomechanically Plausible Human Motion from Sparse Radar Point Clouds](https://arxiv.org/abs/2608.03637) — `multi-modal`
- [Learning Grasp Targeting from Point Clouds for Log Pile Clearing on a Hydraulic Crane](https://arxiv.org/abs/2610.07613)
- [Learning Manifolds in High-D Point Embedding for Anisotropic Surface Approximation from Unstructured Point Clouds](https://arxiv.org/abs/2607.28855) — `reconstruction`
- [Learning Motion Feasibility from Point Clouds in Cluttered Environments](https://arxiv.org/abs/2606.26700)
- [Learning to Suppress SPAD-based LiDAR Flare](https://arxiv.org/abs/2607.03247) — `detection`
- [Learning-Based 3D Reconstruction of Power Networks from Aerial Point Clouds](https://arxiv.org/abs/2609.23915) — `segmentation` `reconstruction`
- [Learning-Based Reconstruction Attacks on Coordinate-Obfuscated Point Clouds](https://arxiv.org/abs/2609.02568) — `reconstruction` — Workshop
- [LexiCan: Lexicographic Canonicalization of Point Clouds for Machine Learning Applications](https://arxiv.org/abs/2610.15171)
- [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](https://arxiv.org/abs/2611.11912) — `BEV`
- [Local-Global Joint Modeling for Point Cloud Super-Resolution Guided by Multi-Scale Spatial Priors](https://arxiv.org/abs/2611.02786) — `upsampling`
- [LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351) — `gaussian-splatting` `efficiency`
- [LOGOS: LiDAR-Only Gaussian Elevation Splatting for Unified Tiny Obstacle Segmentation](https://arxiv.org/abs/2606.21527) — `segmentation`
- [Long-Tailed 3D Point Cloud Dataset Distillation](https://arxiv.org/abs/2607.26763) — `dataset`
- [Low-Density 3D Point Cloud Classification](https://arxiv.org/abs/2611.05291) — `classification` `autonomous driving`
- [M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis](https://arxiv.org/abs/2609.30056) — `generation` `multi-modal`
- [MAGE: View-guided Point Cloud Completion with Efficient Modality Alignment and Adaptive Geometry Enhancement](https://arxiv.org/abs/2607.02568) — `completion` `efficiency`
- [MAMVI: 3D Test-Time Adaptation via Masked Multi-View Point Clouds](https://arxiv.org/abs/2606.12939)
- [Manifold4D: Denoising on Point Cloud Rendered Manifolds for Video Re-shooting](https://arxiv.org/abs/2608.28174) — `denoising` `monocular`
- [Mask 2D-3D: Adaptive Dual-Masked Autoencoder Network for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.18088) — `registration` `detection` `self-supervised`
- [MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes](https://arxiv.org/abs/2606.08744) — `localization` `BEV`
- [MedPCFM-TED: One-Step Point Cloud Flow Matching for Implant Generation via Teacher-Guided Endpoint Distillation](https://arxiv.org/abs/2609.16934) — `generation` `reconstruction`
- [MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching](https://arxiv.org/abs/2606.24433) — `completion` `generation` `reconstruction`
- [MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers](https://arxiv.org/abs/2607.24074)
- [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301) — `generation` `reconstruction` `autonomous driving` `multi-modal`
- [Motion-Saliency Complementary Masked Modeling for Point Cloud Video Understanding](https://arxiv.org/abs/2608.30279) — `self-supervised`
- [MSSP: Multi-Scale Spatially-Constrained Partition for Unsupervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2609.06959) — `segmentation`
- [Multi-level latent-diffusion adaptation for cross-region point cloud segmentation of ancient terraces](https://arxiv.org/abs/2611.18033) — `segmentation` `detection`
- [Multi-Path Mamba Diffusion for 3D Point Cloud Semantic Scene Completion](https://arxiv.org/abs/2611.04583) — `completion` `generation` `occupancy prediction`
- [Neural LiDAR Bundle Adjustment](https://arxiv.org/abs/2607.04169) — `reconstruction` `nerf`
- [On Exploring Input Resolution Scaling For Anytime LiDAR Object Detection](https://arxiv.org/abs/2607.08391) — `detection`
- [On Maximum Clique and Maximum Consensus Formulations in Point Cloud Registration](https://arxiv.org/abs/2610.27275) — `registration`
- [On the Efficacy of Self-Supervised Point Cloud Encoders for Efficient 3D Large Language Models](https://arxiv.org/abs/2607.29136) — `registration` `self-supervised` `efficiency`
- [Online Geometric Consistency Assessment of LiDAR Measurements via Recursive Bayesian Comparison](https://arxiv.org/abs/2611.10566) — `registration` `localization`
- [Optimizing 3D Gaussian Splatting via Point Cloud Upsampling](https://arxiv.org/abs/2606.00450) — `reconstruction` `gaussian-splatting` `upsampling`
- [OptimusMesh: Compact Autoregressive Mesh Generation from Point Clouds via Sparse Latent Pivots](https://arxiv.org/abs/2610.01148) — `generation` `reconstruction`
- [Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models](https://arxiv.org/abs/2607.29048) — `efficiency`
- [PARTE: Plane-Assisted Robust Transformation Estimation for Point Cloud Registration](https://arxiv.org/abs/2609.25375) — `registration` `robustness`
- [PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds](https://arxiv.org/abs/2608.05586) — `generation`
- [Paving the Way for Point Cloud Video Representation Learning Using A PDE Model](https://arxiv.org/abs/2606.01604)
- [PC$^2$-AD: Point Cloud Upsampling to Safeguard 3D Anomaly Detection with Resolution-constrained Edge Devices](https://arxiv.org/abs/2609.14722) — `detection` `upsampling` `anomaly detection` — [code](https://github.com/gyutong406-commits/PC2-AD)
- [PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2606.20455) — `dataset`
- [PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning](https://arxiv.org/abs/2608.18627)
- [PCT-Prompt: A Prompt-Guided Transformer Framework for Dense Prediction Tasks in Point Clouds](https://arxiv.org/abs/2608.16225) — `classification`
- [PESTO: Formally Correct Registration of LiDAR Point Clouds with Limited Overlap](https://arxiv.org/abs/2609.18082) — `registration`
- [PinNet: Keypoint-Aware Learned Local Descriptors with Geometric Embedding for Loop Closure in LiDAR SLAM](https://arxiv.org/abs/2606.28637) — `slam`
- [PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](https://arxiv.org/abs/2609.02860) — `segmentation` `pre-training`
- [Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516) — `generation` `autonomous driving`
- [Point Cloud Diffusion with Global and Local Reconstruction for Instance-Level 3D Anomaly Detection](https://arxiv.org/abs/2606.25740) — `detection` `reconstruction` `anomaly detection`
- [Point Cloud Upsampling through Patch-based Frequency Superposition](https://arxiv.org/abs/2606.14355) — `upsampling`
- [Point-Selection Fine-Tuning Framework for Robust Point Cloud Classification](https://arxiv.org/abs/2607.19711) — `classification` `robustness`
- [Point-Wise Geometry-Aware Transformer for Partial-to-Full Point Cloud Registration in Computer-Assisted Surgery](https://arxiv.org/abs/2606.13488) — `registration`
- [Point2Radio: A Foundation Model for Cross-Scene Radio Fields from Material-Aware Point Clouds](https://arxiv.org/abs/2607.28994) — `pre-training`
- [PointCHR: Point Cloud Analysis via Curvature-Aware Hyperbolic Rectification](https://arxiv.org/abs/2607.24052)
- [PointNDF: Cascaded Neural Displacement Fields for Point Cloud Denoising](https://arxiv.org/abs/2611.05411) — `denoising`
- [Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946) — `reconstruction`
- [PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors](https://arxiv.org/abs/2610.11612) — `registration` `open-vocabulary`
- [Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers](https://arxiv.org/abs/2609.18056) — `pre-training` `efficiency`
- [Proteus: A Truncation-Robust Entropy Model for Progressive LiDAR Compression](https://arxiv.org/abs/2608.00687) — `compression` `robustness`
- [ProtoPointNet: Prototype-Based Interpretable Classification of 3D Dental Point Clouds with Verifiable Spatial Activations](https://arxiv.org/abs/2607.12335) — `classification`
- [Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving](https://arxiv.org/abs/2610.27617) — `detection` `autonomous driving` `robustness` `efficiency`
- [PT$^3$: Prototype-Guided Self-Supervised Pretraining for Generalizable mmWave Human Point Cloud Representation](https://arxiv.org/abs/2610.38551) — `self-supervised` `pre-training`
- [PT-WNO: Point Transformer with Wavelet Neural Operator for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2606.11466) — `segmentation`
- [R1A-PC: Physics-Guided Electromagnetic Inversion of Three-Dimensional Human Point Clouds in Complex Static Environments](https://arxiv.org/abs/2610.05144)
- [R4Tun: LLM-guided adaptive segmental tunnel lining segmentation in point clouds](https://arxiv.org/abs/2609.11360) — `segmentation` `vision-language`
- [RAHF-Net: Range-Aware Heterogeneous Fusion for LiDAR-Assisted RGB Semantic Segmentation](https://arxiv.org/abs/2610.25400) — `segmentation`
- [Rail Track Extraction from Rasterized Classified Point Clouds Using a Full-Resolution, Fully Convolutional Recurrent Neural Network](https://arxiv.org/abs/2607.06829)
- [RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation](https://arxiv.org/abs/2610.29845) — `pre-training`
- [RAPA: Ray-Aware Physics Augmentation for Robust Camera-LiDAR Calibration](https://arxiv.org/abs/2611.12129) — `multi-modal` `robustness`
- [RaSFNet: Ray-aligned and Scan-aware Fusion Network for LiDAR Semantic Segmentation](https://arxiv.org/abs/2610.31186) — `segmentation` `autonomous driving`
- [Recurrent Convolutional Neural Networks for LiDAR-Based Attitude Initialization of Rotating Spacecraft](https://arxiv.org/abs/2609.24685)
- [Refine Then Fusion: Training-Free 3D Point Cloud Adaptation with Priority Refinement and Multi-Modal Knowledge Fusion](https://arxiv.org/abs/2609.21522) — `multi-modal`
- [Refining Roadside 4D Radar Vehicle Classification Using Point-Cloud Dispersion](https://arxiv.org/abs/2611.02147) — `classification` `multi-modal`
- [Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction](https://arxiv.org/abs/2610.01206) — `reconstruction`
- [ResPCC: A Loss-Resilient Neural Point Cloud Codec over Lossy Networks](https://arxiv.org/abs/2608.11845) — `compression`
- [Rethinking 3D Segmentation from Individual LiDAR Scans: Incidence-Aware Sampling on the SIP Benchmark](https://arxiv.org/abs/2608.07757) — `segmentation` `dataset`
- [RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261)
- [RhinoNet: Unsupervised Learning for Phenoscaping and Generation of High Dimensional Point Clouds](https://arxiv.org/abs/2610.23898) — `generation`
- [RigPAPR: Rig-Based Animation of Static Neural Point Clouds from a Fixed-Viewpoint Video](https://arxiv.org/abs/2606.06685) — `generation` `reconstruction` `monocular`
- [RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware Robot Perception](https://arxiv.org/abs/2608.21380)
- [Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion](https://arxiv.org/abs/2610.39516) — `segmentation` `completion` `robustness`
- [Robust Reconstruction of Power Lines from Incomplete Mobile and Aerial LiDAR Data](https://arxiv.org/abs/2611.05197) — `detection` `reconstruction` `robustness`
- [Robust Single-Parameter Point Cloud Registration using Truncated Lp Functions](https://arxiv.org/abs/2610.34271) — `registration` `robustness`
- [Role-based Effectiveness of an Epistemic Uncertainty Estimate in Training Models for Semantic Segmentation of 3D LiDAR Point Clouds](https://arxiv.org/abs/2611.05569) — `segmentation` `classification`
- [Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models](https://arxiv.org/abs/2606.16593)
- [RoughSense: Lightweight Terrain-Induced Rover Vibration Prediction Using Point Clouds and IMU Feedback](https://arxiv.org/abs/2609.03720) — `detection` `efficiency`
- [SAVTrack: Selective Vote Aggregation for Reliability-Aware Point Cloud Tracking](https://arxiv.org/abs/2609.16662) — `tracking`
- [ScaleBlind: Point Cloud Completion under Unknown Scale](https://arxiv.org/abs/2609.23404) — `completion` `reconstruction`
- [SelectAnyTree: A Promptable Instance Segmentation Model for 3D Forest LiDAR Point Clouds](https://arxiv.org/abs/2606.27491) — `segmentation`
- [Self-supervised Geometry Reasoning for LiDAR Simultaneous Localization and Mapping](https://arxiv.org/abs/2606.30166) — `slam` `localization` `self-supervised`
- [Self-Supervised Pretraining Improves Cross-Site and Cross-Scale Robustness of Point Cloud Leaf-Wood Segmentation](https://arxiv.org/abs/2607.06948) — `segmentation` `self-supervised` `pre-training` `robustness`
- [Semantic Privacy Protection with Utility Preservation for 3D Point Clouds](https://arxiv.org/abs/2609.13823)
- [Semantic-weighted ICP for LiDAR Odometry: Class-Aware Residual Reweighting for Robust Scan Registration](https://arxiv.org/abs/2606.03905) — `registration` `robustness`
- [Shape-Prior-Based Point Cloud Completion for Single-Stage Fully Sparse 3D Object Detection](https://arxiv.org/abs/2606.00688) — `detection` `completion` `autonomous driving`
- [SHReg: Strictly Rotation-Equivariant Point Cloud Registration via Spherical Harmonics](https://arxiv.org/abs/2607.23096) — `registration`
- [Sign Language Recognition Using Original and Synthetic Depth Image Based Point Cloud Data Models](https://arxiv.org/abs/2608.09400) — `monocular`
- [Sinkhorn-CPD: Robust point cloud registration via unbalanced entropic optimal transport](https://arxiv.org/abs/2606.16672) — `registration` `robustness`
- [Solution for UCF UrbanTwin LUMPI Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07590) — `detection`
- [Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07608) — `detection`
- [SpaceCache: Intermediate Feature Reuse for Efficient Semantic Segmentation on Point Cloud Streams](https://arxiv.org/abs/2610.21207) — `segmentation` `autonomous driving` `efficiency`
- [Spectral Consistency-Guided Multiview Point Cloud Registration for Low-Overlap Scenes](https://arxiv.org/abs/2609.12417) — `registration`
- [SPEM: Scan-Prior Entropy Modeling for LiDAR Point Cloud Compression](https://arxiv.org/abs/2611.16212) — `compression`
- [SRENet: Spectral Re-Entry Network for Point Cloud Action Recognition](https://arxiv.org/abs/2606.03160) — `autonomous driving`
- [SSC-Priors: Exploring Semantic and Visibility Priors to Boost Lidar Semantic Scene Completion](https://arxiv.org/abs/2609.17413) — `segmentation` `completion` `occupancy prediction`
- [SUMI: Scalable Unified Model for 3D Point Cloud Inference](https://arxiv.org/abs/2608.08115) — `completion` `reconstruction` `upsampling`
- [SuperFlex: Deformable Superquadrics for Point Cloud Decomposition](https://arxiv.org/abs/2607.01015) — `reconstruction`
- [Superquadric Primitive Decomposition of 3D point clouds via Geometric-Aware Inlier Refinement](https://arxiv.org/abs/2609.35725)
- [Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge](https://arxiv.org/abs/2608.07106) — `classification` `generation`
- [TACTIC: Temporal and Context-Aware LLM Tactical Planning for Roadside LiDAR Attacks](https://arxiv.org/abs/2609.39969) — `vision-language`
- [TAP3D: Thermal-Assisted 3D Human Point Clouds](https://arxiv.org/abs/2610.11241) — `reconstruction`
- [Test Time Adaptation Methods for Point Cloud Registration in Laparoscopic Surgery](https://arxiv.org/abs/2608.02883) — `registration`
- [Test-time Adaptation for Point Cloud Denoising under Unseen Noise](https://arxiv.org/abs/2610.27410) — `denoising`
- [TFTrack: A Template-Free Framework for Efficient 3D Point Cloud Tracking](https://arxiv.org/abs/2609.07738) — `tracking` `efficiency`
- [The Role of Radiometric Features in Cross-Site Leaf-Wood Segmentation of LiDAR Point Clouds](https://arxiv.org/abs/2609.21903) — `segmentation`
- [TokenFlow: Latent Token Rectified Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2610.27418) — `generation`
- [Toward a foundation model for forest point clouds](https://arxiv.org/abs/2609.24787) — `pre-training`
- [Transform-Aligned Learned Features for Lossy Point Cloud Attribute Compression](https://arxiv.org/abs/2609.34834) — `compression`
- [Tri-Efficient Transfer Learning for Point Cloud Videos](https://arxiv.org/abs/2606.24175) — `efficiency`
- [Uncertainty Evaluation to Support Safety of the Intended Functionality Analysis for Determining the Applicability of Performance Targets Across Triggering Conditions in ML-Based LiDAR Object Detection](https://arxiv.org/abs/2610.35092) — `detection`
- [Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence](https://arxiv.org/abs/2609.02134)
- [Unsigned Distance Maps on 2D Point Cloud Registration](https://arxiv.org/abs/2609.25932) — `registration` `slam` `localization` — [code](https://github.com/INESCTEC/ricoslam)
- [UQ-Loc: Uncertainty-Aware LiDAR Scene Coordinate Regression](https://arxiv.org/abs/2608.06307) — `localization`
- [ViCo3D: Empowering LiDAR-based Collaborative 3D Object Detection with Vision Foundation Models](https://arxiv.org/abs/2607.12959) — `detection` `BEV`
- [Viking Hill Dataset: A Lidar-Radar-Camera Dataset for Detection and Segmentation in Forest Scenes](https://arxiv.org/abs/2606.19154) — `segmentation` `detection` `multi-modal` `dataset`
- [VisTa3D: A Dataset and Benchmark for Thin Object Reconstruction from Vision, Tactile, and 3D Point Clouds](https://arxiv.org/abs/2608.20740) — `reconstruction` `dataset`
- [VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds](https://arxiv.org/abs/2607.16146) — `localization`
- [When Point Clouds Outperform Pixels: Rethinking Zero-Shot Multimodal Anomaly Detection](https://arxiv.org/abs/2609.25793) — `detection` `localization` `open-vocabulary` `multi-modal`
- [WNOJ-LIO: A White-Noise-on-Jerk Motion-Prior EKF for High-Dynamic LiDAR-IMU Fusion](https://arxiv.org/abs/2607.13405)
- [xModel-KD: Cross-modal Knowledge Distillation for 3D Scene Perception using LiDAR](https://arxiv.org/abs/2605.30111) — `segmentation`
- [ZIL: Zero-shot Image-to-LiDAR Registration](https://arxiv.org/abs/2609.22716) — `registration` `autonomous driving` `open-vocabulary`
- [ZVeC: A Zero-Shot Framework for Instance-Level Vehicle Extraction and Generative Point Cloud Completion](https://arxiv.org/abs/2609.24825) — `completion` `generation` `reconstruction` `open-vocabulary`

</details>


### 2025 <sub>(427)</sub>

<details><summary><b>CVPR</b> · 6</summary>

- [AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration](https://arxiv.org/abs/2412.05507) — `registration`
- [PerLA: Perceptive 3D Language Assistant](https://arxiv.org/abs/2411.19774)
- [Semantic-Free Procedural 3D Shapes Are Surprisingly Good Teachers](https://arxiv.org/abs/2411.17467) — `self-supervised`
- [Speedy-Splat: Fast 3D Gaussian Splatting with Sparse Pixels and Sparse Primitives](https://arxiv.org/abs/2412.00578) — `reconstruction` `gaussian-splatting`
- [V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection](https://arxiv.org/abs/2411.08402) — `detection` `denoising` `multi-modal`
- [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://arxiv.org/abs/2412.00493) — `vision-language`

</details>

<details><summary><b>ICCV</b> · 40</summary>

- [All in One: Visual-Description-Guided Unified Point Cloud Segmentation](https://arxiv.org/abs/2507.05211) — `segmentation`
- [Blended Point Cloud Diffusion for Localized Text-guided Shape Editing](https://arxiv.org/abs/2507.15399)
- [CA-I2P: Channel-Adaptive Registration Network with Global Optimal Selection](https://arxiv.org/abs/2506.21364) — `registration` `detection`
- [Curve-Aware Gaussian Splatting for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2506.21401) — `reconstruction` `gaussian-splatting` — [code](https://github.com/zhirui-gao/Curve-Gaussian)
- [Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval](https://arxiv.org/abs/2507.21489)
- [Diff$^2$I2P: Differentiable Image-to-Point Cloud Registration with Diffusion Prior](https://arxiv.org/abs/2507.06651) — `registration`
- [Domain-aware Category-level Geometry Learning Segmentation for 3D Point Clouds](https://arxiv.org/abs/2508.11265) — `segmentation`
- [DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection](https://arxiv.org/abs/2508.12330) — `detection` `autonomous driving` `multi-modal`
- [ERNet: Efficient Non-Rigid Registration Network for Point Sequences](https://arxiv.org/abs/2510.15800) — `registration` `efficiency`
- [Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation](https://arxiv.org/abs/2506.22375) — `detection`
- [FastPoint: Accelerating 3D Point Cloud Model Inference via Sample Point Distance Prediction](https://arxiv.org/abs/2507.23480)
- [From Binary to Semantic: Utilizing Large-Scale Binary Occupancy Data for 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2507.13387) — `autonomous driving` `occupancy prediction` — Workshop
- [GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631) — `gaussian-splatting`
- [Guiding Diffusion-Based Articulated Object Generation by Partial Point Cloud Alignment and Physical Plausibility Constraints](https://arxiv.org/abs/2508.00558) — `registration` `generation`
- [Harnessing Text-to-Image Diffusion Models for Point Cloud Self-Supervised Learning](https://arxiv.org/abs/2507.09102) — `generation` `self-supervised`
- [Learning Normals of Noisy Points by Local Gradient-Aware Surface Filtering](https://arxiv.org/abs/2507.03394) — `normal estimation`
- [Learning Point Cloud Representations with Pose Continuity for Depth-Based Category-Level 6D Object Pose Estimation](https://arxiv.org/abs/2508.14358) — Workshop
- [LINR-PCGC: Lossless Implicit Neural Representations for Point Cloud Geometry Compression](https://arxiv.org/abs/2507.15686) — `compression`
- [MinCD-PnP: Learning 2D-3D Correspondences with Approximate Blind PnP](https://arxiv.org/abs/2507.15257) — `registration`
- [MonoMVSNet: Monocular Priors Guided Multi-View Stereo Network](https://arxiv.org/abs/2507.11333) — `monocular`
- [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://arxiv.org/abs/2507.04047) — `reconstruction` `efficiency`
- [Open-Vocabulary Octree-Graph for 3D Scene Understanding](https://arxiv.org/abs/2411.16253) — `segmentation` `open-vocabulary`
- [OpenM3D: Open Vocabulary Multi-view Indoor 3D Object Detection without Human Annotations](https://arxiv.org/abs/2508.20063) — `detection` `open-vocabulary`
- [Point Cloud Self-supervised Learning via 3D to Multi-view Masked Learner](https://arxiv.org/abs/2311.10887) — `self-supervised`
- [PointGAC: Geometric-Aware Codebook for Masked Point Cloud Modeling](https://arxiv.org/abs/2507.04801)
- [PU-Gaussian: Point Cloud Upsampling using 3D Gaussian Representation](https://arxiv.org/abs/2509.20207) — `upsampling` — Workshop
- [PUMPS: Skeleton-Agnostic Point-based Universal Motion Pre-Training for Synthesis in Human Motion Tasks](https://arxiv.org/abs/2507.20170) — `pre-training`
- [RayletDF: Raylet Distance Fields for Generalizable 3D Surface Reconstruction from Point Clouds or Gaussians](https://arxiv.org/abs/2508.09830) — `reconstruction` `gaussian-splatting` — [code](https://github.com/vLAR-group/RayletDF)
- [Rethinking Backbone Design for Lightweight 3D Object Detection in LiDAR](https://arxiv.org/abs/2508.00744) — `detection` `autonomous driving` `efficiency` — Workshop
- [Robust 3D Object Detection using Probabilistic Point Clouds from Single-Photon LiDARs](https://arxiv.org/abs/2508.00169) — `detection` `robustness`
- [SAM4D: Segment Anything in Camera and LiDAR Streams](https://arxiv.org/abs/2506.21547) — `segmentation`
- [Self-supervised Learning of Hybrid Part-aware 3D Representations of 2D Gaussians and Superquadrics](https://arxiv.org/abs/2408.10789) — `self-supervised` — [code](https://github.com/zhirui-gao/PartGS)
- [StruMamba3D: Exploring Structural Mamba for Self-supervised Point Cloud Representation Learning](https://arxiv.org/abs/2506.21541) — `self-supervised`
- [Symmetry Understanding of 3D Shapes via Chirality Disentanglement](https://arxiv.org/abs/2508.05505)
- [Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge](https://arxiv.org/abs/2507.04123) — `detection` `autonomous driving` `efficiency`
- [Towards More Diverse and Challenging Pre-training for Point Cloud Learning: Self-Supervised Cross Reconstruction with Decoupled Views](https://arxiv.org/abs/2509.01250) — `generation` `reconstruction` `self-supervised` `pre-training`
- [TurboReg: TurboClique for Robust and Efficient Point Cloud Registration](https://arxiv.org/abs/2507.01439) — `registration` `robustness` `efficiency`
- [UPP: Unified Point-Level Prompting for Robust Point Cloud Analysis](https://arxiv.org/abs/2507.18997) — `robustness`
- [UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling](https://arxiv.org/abs/2508.14604)
- [VolumetricSMPL: A Neural Volumetric Body Model for Efficient Interactions, Contacts, and Collisions](https://arxiv.org/abs/2506.23236) — `efficiency`

</details>

<details><summary><b>ECCV</b> · 1</summary>

- [UniFlow: Zero-Shot LiDAR Scene Flow for Autonomous Vehicles](https://arxiv.org/abs/2511.18254) — `scene flow` `open-vocabulary`

</details>

<details><summary><b>NeurIPS</b> · 13</summary>

- [Avi: Action from Volumetric Inference](https://arxiv.org/abs/2510.21746) — `generation` — Workshop
- [CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning](https://arxiv.org/abs/2507.03707) — `dataset`
- [How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?](https://arxiv.org/abs/2511.05449) — `segmentation` `reconstruction`
- [Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning](https://arxiv.org/abs/2510.13307) — `segmentation`
- [Online Segment Any 3D Thing as Instance Tracking](https://arxiv.org/abs/2512.07599) — `segmentation` `tracking` — [code](https://github.com/AutoLab-SAI-SJTU/AutoSeg3D)
- [Pixel-Perfect Depth with Semantics-Prompted Diffusion Transformers](https://arxiv.org/abs/2510.07316) — `generation` `compression` `monocular`
- [PointMAC: Meta-Learned Adaptation for Robust Test-Time Point Cloud Completion](https://arxiv.org/abs/2510.10365) — `completion` `robustness`
- [Reconstructing the local density field with combined convolutional and point cloud architecture](https://arxiv.org/abs/2510.08573) — `reconstruction` — Workshop
- [RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes](https://arxiv.org/abs/2509.15123)
- [SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions](https://arxiv.org/abs/2509.15693) — `self-supervised`
- [See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model](https://arxiv.org/abs/2509.16087) — `multi-modal`
- [TriFusion-AE: Language-Guided Depth and LiDAR Fusion for Robust Point Cloud Processing](https://arxiv.org/abs/2509.18743) — `reconstruction` `denoising` `autonomous driving` `robustness` — Workshop
- [U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching](https://arxiv.org/abs/2510.25210) — `reconstruction` `denoising`

</details>

<details><summary><b>ICML</b> · 2</summary>

- [Geometry-to-Image Synthesis-Driven Generative Point Cloud Registration](https://arxiv.org/abs/2512.09407) — `registration` `generation`
- [WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting](https://arxiv.org/abs/2510.10726) — `reconstruction` — [code](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror)

</details>

<details><summary><b>AAAI</b> · 31</summary>

- [A New Adversarial Perspective for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2412.13017) — `detection` `robustness`
- [CAD-GPT: Synthesising CAD Construction Sequence with Spatial Reasoning-Enhanced Multimodal LLMs](https://arxiv.org/abs/2412.19663) — `multi-modal`
- [CloudMamba: Grouped Selective State Spaces for Point Cloud Analysis](https://arxiv.org/abs/2511.07823)
- [Cross-PCR: A Robust Cross-Source Point Cloud Registration Framework](https://arxiv.org/abs/2412.18873) — `registration` `robustness`
- [DAPoinTr: Domain Adaptive Point Transformer for Point Cloud Completion](https://arxiv.org/abs/2412.19062) — `completion`
- [Digging into Intrinsic Contextual Information for High-fidelity 3D Point Cloud Completion](https://arxiv.org/abs/2412.08326) — `completion`
- [DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation](https://arxiv.org/abs/2512.11465) — `reconstruction` `self-supervised`
- [Efficient 3D Recognition with Event-driven Spike Sparse Convolution](https://arxiv.org/abs/2412.07360) — `efficiency`
- [FlowMamba: Learning Point Cloud Scene Flow with Global Motion Propagation](https://arxiv.org/abs/2412.17366) — `scene flow`
- [GaussianPainter: Painting Point Cloud into 3D Gaussians with Normal Guidance](https://arxiv.org/abs/2412.17715) — `gaussian-splatting`
- [Generalized Zero-Shot Learning for Point Cloud Segmentation with Evidence-Based Dynamic Calibration](https://arxiv.org/abs/2509.08280) — `segmentation` `open-vocabulary`
- [HGSFusion: Radar-Camera Fusion with Hybrid Generation and Synchronization for 3D Object Detection](https://arxiv.org/abs/2412.11489) — `detection` `generation` `autonomous driving` `multi-modal`
- [Hyperbolic-constraint Point Cloud Reconstruction from Single RGB-D Images](https://arxiv.org/abs/2412.09055) — `reconstruction`
- [L4DR: LiDAR-4DRadar Fusion for Weather-Robust 3D Object Detection](https://arxiv.org/abs/2408.03677) — `detection` `robustness`
- [LiON: Learning Point-wise Abstaining Penalty for LiDAR Outlier DetectioN Using Diverse Synthetic Data](https://arxiv.org/abs/2309.10230) — `detection` `classification` `autonomous driving` — [code](https://github.com/Daniellli/LiON)
- [Multi-Modal Assistance for Unsupervised Domain Adaptation on Point Cloud 3D Object Detection](https://arxiv.org/abs/2511.07966) — `detection` `multi-modal` `domain adaptation`
- [ObjVariantEnsemble: Advancing Point Cloud LLM Evaluation in Challenging Scenes with Subtly Distinguished Objects](https://arxiv.org/abs/2412.14837) — `vision-language`
- [OLiDM: Object-aware LiDAR Diffusion Models for Autonomous Driving](https://arxiv.org/abs/2412.17226) — `autonomous driving`
- [PointCFormer: a Relation-based Progressive Feature Extraction Network for Point Cloud Completion](https://arxiv.org/abs/2412.08421) — `segmentation` `detection` `completion`
- [PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504)
- [Position-aware Guided Point Cloud Completion with CLIP Model](https://arxiv.org/abs/2412.08271) — `completion`
- [Pre-training a Density-Aware Pose Transformer for Robust LiDAR-based 3D Human Pose Estimation](https://arxiv.org/abs/2412.13454) — `autonomous driving` `pre-training` `robustness`
- [Preserving Topological and Geometric Embeddings for Point Cloud Recovery](https://arxiv.org/abs/2507.19121)
- [RaLiFlow: Scene Flow Estimation with 4D Radar and LiDAR Point Clouds](https://arxiv.org/abs/2512.10376) — `scene flow` `multi-modal`
- [RCTrans: Radar-Camera Transformer via Radar Densifier and Sequential Decoder for 3D Object Detection](https://arxiv.org/abs/2412.12799) — `detection` `multi-modal`
- [RI-MAE: Rotation-Invariant Masked AutoEncoders for Self-Supervised Point Cloud Representation Learning](https://arxiv.org/abs/2409.00353) — `self-supervised`
- [Riemann-based Multi-scale Attention Reasoning Network for Text-3D Retrieval](https://arxiv.org/abs/2408.13712)
- [SCKD: Semi-Supervised Cross-Modality Knowledge Distillation for 4D Radar Object Detection](https://arxiv.org/abs/2412.14571) — `detection` `multi-modal`
- [Sharpening Neural Implicit Functions with Frequency Consolidation Priors](https://arxiv.org/abs/2412.19720)
- [Simba: Towards High-Fidelity and Geometrically-Consistent Point Cloud Completion via Transformation Diffusion](https://arxiv.org/abs/2511.16161) — `completion`
- [Weighted Poisson-disk Resampling on Large-Scale Point Clouds](https://arxiv.org/abs/2412.09177)

</details>

<details><summary><b>IJCAI</b> · 2</summary>

- [Exploring Semantic Masked Autoencoder for Self-supervised Point Cloud Understanding](https://arxiv.org/abs/2506.21957) — `self-supervised`
- [GPI-Net: Gestalt-Guided Parallel Interaction Network via Orthogonal Geometric Consistency for Robust Point Cloud Registration](https://arxiv.org/abs/2507.14452) — `registration` `robustness`

</details>

<details><summary><b>SIGGRAPH</b> · 2</summary>

- [A Fast Volumetric Capture and Reconstruction Pipeline for Dynamic Point Clouds and Gaussian Splats](https://arxiv.org/abs/2512.15719) — `reconstruction` — [code](https://github.com/irc-hslu/capturestudio)
- [Generating real-time detailed ground visualisations from sparse aerial point clouds](https://arxiv.org/abs/2507.18664) — `efficiency`

</details>

<details><summary><b>SIGGRAPH Asia</b> · 2</summary>

- [CHARM: Control-point-based 3D Anime Hairstyle Auto-Regressive Modeling](https://arxiv.org/abs/2509.21114) — `generation`
- [Neural Visibility of Point Sets](https://arxiv.org/abs/2509.24150)

</details>

<details><summary><b>ACM MM</b> · 6</summary>

- [B4DL: A Benchmark for 4D LiDAR LLM in Spatio-Temporal Understanding](https://arxiv.org/abs/2508.05269) — `vision-language` `dataset`
- [Drawing2CAD: Sequence-to-Sequence Learning for CAD Generation from Vector Drawings](https://arxiv.org/abs/2508.18733) — `generation`
- [Enhancing Pseudo-Boxes via Data-Level LiDAR-Camera Fusion for Unsupervised 3D Object Detection](https://arxiv.org/abs/2508.20530) — `detection` `generation` `multi-modal`
- [Graph-Guided Dual-Level Augmentation for 3D Scene Segmentation](https://arxiv.org/abs/2507.22668) — `segmentation`
- [Investigating Domain Gaps for Indoor 3D Object Detection](https://arxiv.org/abs/2508.17439) — `detection`
- [RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion](https://arxiv.org/abs/2511.09878) — `completion` `occupancy prediction`

</details>

<details><summary><b>3DV</b> · 3</summary>

- [LOSC: LiDAR Open-voc Segmentation Consolidator](https://arxiv.org/abs/2507.07605) — `segmentation` `open-vocabulary`
- [Rethinking Metrics and Diffusion Architecture for 3D Point Cloud Generation](https://arxiv.org/abs/2511.05308) — `generation`
- [Self-Supervised Implicit Attention Priors for Point Cloud Reconstruction](https://arxiv.org/abs/2511.04864) — `reconstruction` `self-supervised`

</details>

<details><summary><b>WACV</b> · 8</summary>

- [CVP: Central-Peripheral Vision-Inspired Multimodal Model for Spatial Reasoning](https://arxiv.org/abs/2512.08135) — `multi-modal`
- [GFT: Graph Feature Tuning for Efficient Point Cloud Analysis](https://arxiv.org/abs/2511.10799) — `efficiency`
- [MEGA-PCC: A Mamba-based Efficient Approach for Joint Geometry and Attribute Point Cloud Compression](https://arxiv.org/abs/2512.22463) — `compression` `efficiency`
- [MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection](https://arxiv.org/abs/2509.07507) — `detection`
- [PALMS+: Modular Image-Based Floor Plan Localization Leveraging Depth Foundation Model](https://arxiv.org/abs/2511.09724) — `localization` `pre-training`
- [Point2Pose: A Generative Framework for 3D Human Pose Estimation with Multi-View Point Cloud Dataset](https://arxiv.org/abs/2512.10321) — `generation` `dataset`
- [SDT-6D: Fully Sparse Depth-Transformer for Staged End-to-End 6D Pose Estimation in Industrial Multi-View Bin Picking](https://arxiv.org/abs/2512.08430)
- [ViGG: Robust RGB-D Point Cloud Registration using Visual-Geometric Mutual Guidance](https://arxiv.org/abs/2511.22908) — `registration` `robustness`

</details>

<details><summary><b>BMVC</b> · 2</summary>

- [Hierarchical Image-Guided 3D Point Cloud Segmentation in Industrial Scenes via Multi-View Bayesian Fusion](https://arxiv.org/abs/2512.06882) — `segmentation`
- [Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift](https://arxiv.org/abs/2511.17455) — `segmentation` `multi-modal`

</details>

<details><summary><b>ICRA</b> · 7</summary>

- [Beyond Frame-wise Tracking: A Trajectory-based Paradigm for Efficient Point Cloud Tracking](https://arxiv.org/abs/2509.11453) — `tracking` `efficiency`
- [Domain Adaptation-Based Crossmodal Knowledge Distillation for 3D Semantic Segmentation](https://arxiv.org/abs/2509.00379) — `segmentation` `autonomous driving` `domain adaptation`
- [LiLa-Net: Lightweight Latent LiDAR Autoencoder for 3D Point Cloud Reconstruction](https://arxiv.org/abs/2510.02028) — `reconstruction` `efficiency`
- [PlaneHEC: Efficient Hand-Eye Calibration for Multi-view Robotic Arm via Any Point Cloud Plane Detection](https://arxiv.org/abs/2507.19851) — `detection` `efficiency`
- [Radar Tracker: Moving Instance Tracking in Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2507.03441) — `segmentation` `tracking` `multi-modal`
- [Radar Velocity Transformer: Single-scan Moving Object Segmentation in Noisy Radar Point Clouds](https://arxiv.org/abs/2507.03463) — `segmentation` `autonomous driving` `multi-modal`
- [RadarSFD: Single-Frame Diffusion with Pretrained Priors for Radar Point Clouds](https://arxiv.org/abs/2509.18068) — `pre-training` `multi-modal`

</details>

<details><summary><b>IROS</b> · 15</summary>

- [CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth](https://arxiv.org/abs/2512.14001) — `multi-modal`
- [CORENet: Cross-Modal 4D Radar Denoising Network with LiDAR Supervision for Autonomous Driving](https://arxiv.org/abs/2508.13485) — `detection` `denoising` `autonomous driving` `multi-modal`
- [DAMM-LOAM: Degeneracy Aware Multi-Metric LiDAR Odometry and Mapping](https://arxiv.org/abs/2510.13287) — `slam` `localization` `reconstruction` — Workshop
- [DPGLA: Bridging the Gap between Synthetic and Real Data for Unsupervised Domain Adaptation in 3D LiDAR Semantic Segmentation](https://arxiv.org/abs/2510.23525) — `segmentation` `domain adaptation`
- [EAROL: Environmental Augmented Perception-Aware Planning and Robust Odometry via Downward-Mounted Tilted LiDAR](https://arxiv.org/abs/2508.14554) — `localization` `robustness`
- [Estimating Continuum Robot Shape under External Loading using Spatiotemporal Neural Networks](https://arxiv.org/abs/2510.22339)
- [GBlobs: Local LiDAR Geometry for Improved Sensor Placement Generalization](https://arxiv.org/abs/2510.18539) — `detection`
- [Label-Efficient Grasp Joint Prediction with Point-JEPA](https://arxiv.org/abs/2509.13349) — `self-supervised` `efficiency` — Workshop
- [LiHRA: A LiDAR-Based HRI Dataset for Automated Risk Monitoring Methods](https://arxiv.org/abs/2509.06597) — `dataset`
- [mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera](https://arxiv.org/abs/2508.02348) — `detection` `localization` `autonomous driving` `multi-modal`
- [OREN: Octree Residual Network for Real-Time Euclidean Signed Distance Mapping](https://arxiv.org/abs/2510.18999) — `localization` `reconstruction` `efficiency`
- [Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation](https://arxiv.org/abs/2508.04033) — `detection` `localization` `multi-modal`
- [RaGNNarok: A Light-Weight Graph Neural Network for Enhancing Radar Point Clouds on Unmanned Ground Vehicles](https://arxiv.org/abs/2507.00937) — `multi-modal` `efficiency`
- [TopoLiDM: Topology-Aware LiDAR Diffusion Models for Interpretable and Realistic LiDAR Point Cloud Generation](https://arxiv.org/abs/2507.22454) — `generation` `autonomous driving` — [code](https://github.com/IRMVLab/TopoLiDM)
- [TWC-SLAM: Multi-Agent Cooperative SLAM with Text Semantics and WiFi Features Integration for Similar Indoor Environments](https://arxiv.org/abs/2510.22754) — `slam`

</details>

<details><summary><b>RA-L</b> · 8</summary>

- [Breaking the Static Assumption: A Dynamic-Aware LIO Framework Via Spatio-Temporal Normal Analysis](https://arxiv.org/abs/2510.22313) — `localization`
- [Have We Scene It All? Scene Graph-Aware Deep Point Cloud Compression](https://arxiv.org/abs/2510.08512) — `compression`
- [HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests](https://arxiv.org/abs/2511.09170) — `localization`
- [PPL: Point Cloud Supervised Proprioceptive Locomotion Reinforcement Learning for Legged Robots in Crawl Spaces](https://arxiv.org/abs/2508.09950)
- [PRISM: Pointcloud Reintegrated Inference via Segmentation and Cross-attention for Manipulation](https://arxiv.org/abs/2507.04633) — `segmentation`
- [Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2511.16091) — `slam` `gaussian-splatting` `multi-modal`
- [Real-Time Adaptive Motion Planning via Point Cloud-Guided, Energy-Based Diffusion and Potential Fields](https://arxiv.org/abs/2507.09383) — `generation` `efficiency`
- [SemRaFiner: Panoptic Segmentation in Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2507.06906) — `segmentation` `classification` `multi-modal`

</details>

<details><summary><b>TPAMI</b> · 2</summary>

- [High-quality Pseudo-labeling for Point Cloud Segmentation with Scene-level Annotation](https://arxiv.org/abs/2506.23227) — `segmentation` — [code](https://github.com/LHDuan/WSegPC)
- [Text2Loc++: Generalizing 3D Point Cloud Localization from Natural Language](https://arxiv.org/abs/2511.15308) — `localization`

</details>

<details><summary><b>TVCG</b> · 2</summary>

- [PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation](https://arxiv.org/abs/2511.21365) — `normal estimation`
- [PKSS-Align: Robust Point Cloud Registration on Pre-Kendall Shape Space](https://arxiv.org/abs/2508.04286) — `registration` `robustness`

</details>

<details><summary><b>ISPRS</b> · 3</summary>

- [L2M-Reg: Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models](https://arxiv.org/abs/2509.16832) — `registration` `detection`
- [RoofSeg: An edge-aware transformer-based network for end-to-end roof plane segmentation](https://arxiv.org/abs/2508.19003) — `segmentation` `detection` `reconstruction`
- [Uncertainty Quantification Framework for Aerial and UAV Photogrammetry through Error Propagation](https://arxiv.org/abs/2507.13486)

</details>

<details><summary><b>PR</b> · 5</summary>

- [A Lightweight 3D Anomaly Detection Method with Rotationally Invariant Features](https://arxiv.org/abs/2511.13115) — `detection` `anomaly detection` `efficiency`
- [Enhancing 3D Point Cloud Classification with ModelNet-R and Point-SkipNet](https://arxiv.org/abs/2509.05198) — `classification` `autonomous driving`
- [PointSlice: Accurate and Efficient Slice-Based Representation for 3D Object Detection from Point Clouds](https://arxiv.org/abs/2509.01487) — `segmentation` `detection` `autonomous driving` `efficiency`
- [SFGFusion: Surface Fitting Guided 3D Object Detection with 4D Radar and Camera Fusion](https://arxiv.org/abs/2510.19215) — `detection` `autonomous driving` `multi-modal`
- [Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge](https://arxiv.org/abs/2510.08316) — `segmentation`

</details>

<details><summary><b>arXiv</b> · 267</summary>

- [3D forest semantic segmentation using multispectral LiDAR and 3D deep learning](https://arxiv.org/abs/2507.08025) — `segmentation` `detection`
- [3D Human Pose and Shape Estimation from LiDAR Point Clouds: A Review](https://arxiv.org/abs/2509.12197)
- [3D Point Cloud Object Detection on Edge Devices for Split Computing](https://arxiv.org/abs/2511.02293) — `detection` `autonomous driving`
- [3DKeyAD: High-Resolution 3D Point Cloud Anomaly Detection via Keypoint-Guided Point Clustering](https://arxiv.org/abs/2507.13110) — `registration` `detection` `anomaly detection`
- [A Bag of Tricks for Efficient Implicit Neural Point Clouds](https://arxiv.org/abs/2508.19140) — `efficiency`
- [A Continuous-Time Consistency Model for 3D Point Cloud Generation](https://arxiv.org/abs/2509.01492) — `generation`
- [A Deep Learning Approach to Identify Rock Bolts in Complex 3D Point Clouds of Underground Mines Captured Using Mobile Laser Scanners](https://arxiv.org/abs/2506.20464)
- [A Graph Attention Network-Based Framework for Reconstructing Missing LiDAR Beams](https://arxiv.org/abs/2512.12410) — `reconstruction`
- [A Multi-View High-Resolution Foot-Ankle Complex Point Cloud Dataset During Gait for Occlusion-Robust 3D Completion](https://arxiv.org/abs/2507.11037) — `completion` `robustness` `dataset`
- [A Novel Grouping-Based Hybrid Color Correction Algorithm for Color Point Clouds](https://arxiv.org/abs/2511.02397) — `compression`
- [A PCA Based Model for Surface Reconstruction from Incomplete Point Clouds](https://arxiv.org/abs/2509.15675) — `reconstruction`
- [A Real-Time Multi-Model Parametric Representation of Point Clouds](https://arxiv.org/abs/2509.14773) — `detection` `efficiency`
- [A Sensor-Aware Phenomenological Framework for Lidar Degradation Simulation and SLAM Robustness Evaluation](https://arxiv.org/abs/2512.08653) — `slam` `robustness`
- [A Survey of Deep Learning-based Point Cloud Denoising](https://arxiv.org/abs/2508.17011) — `denoising` `autonomous driving`
- [A Survey of Medical Point Cloud Shape Learning: Registration, Reconstruction and Variation](https://arxiv.org/abs/2508.03057) — `registration` `reconstruction`
- [Accurate and Efficient Surface Reconstruction from Point Clouds via Geometry-Aware Local Adaptation](https://arxiv.org/abs/2511.08233) — `reconstruction` `efficiency`
- [Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model](https://arxiv.org/abs/2509.14560) — `generation` `denoising`
- [Adaptive Dual-Weighted Gravitational Point Cloud Denoising Method](https://arxiv.org/abs/2512.10386) — `detection` `reconstruction` `denoising` `autonomous driving`
- [Adaptive Point-Prompt Tuning: Fine-Tuning Heterogeneous Foundation Models for 3D Point Cloud Analysis](https://arxiv.org/abs/2509.00374)
- [Advancing Precision in Multi-Point Cloud Fusion Environments](https://arxiv.org/abs/2508.03179) — `registration`
- [AEOS: Active Environment-aware Optimal Scanning Control for UAV LiDAR-Inertial Odometry in Complex Scenes](https://arxiv.org/abs/2509.09141) — `localization`
- [AF-RLIO: Adaptive Fusion of Radar-LiDAR-Inertial Information for Robust Odometry in Challenging Environments](https://arxiv.org/abs/2507.18317) — `multi-modal` `robustness`
- [AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827) — `gaussian-splatting`
- [ALICE-LRI: A General Method for Lossless Range Image Generation for Spinning LiDAR Sensors without Calibration Metadata](https://arxiv.org/abs/2510.20708) — `generation`
- [Aligned Manifold Property and Topology Point Clouds for Learning Molecular Properties](https://arxiv.org/abs/2507.16223)
- [ALISE: Annotation-Free LiDAR Instance Segmentation for Autonomous Driving](https://arxiv.org/abs/2510.05752) — `segmentation` `autonomous driving`
- [Ambiguity-aware Point Cloud Segmentation by Adaptive Margin Contrastive Learning](https://arxiv.org/abs/2507.06592) — `segmentation` `self-supervised`
- [An Adaptive ICP LiDAR Odometry Based on Reliable Initial Pose](https://arxiv.org/abs/2509.22058) — `registration` `detection` `autonomous driving`
- [An Indoor Radio Mapping Dataset Combining 3D Point Clouds and RSSI](https://arxiv.org/abs/2511.00494) — `dataset`
- [APML: Adaptive Probabilistic Matching Loss for Robust 3D Point Cloud Reconstruction](https://arxiv.org/abs/2509.08104) — `completion` `generation` `reconstruction` `robustness`
- [Atlas Gaussian processes on restricted domains and point clouds](https://arxiv.org/abs/2511.15822)
- [Attention-Guided Multi-Scale Local Reconstruction for Point Clouds via Masked Autoencoder Self-Supervised Learning](https://arxiv.org/abs/2507.04084) — `reconstruction` `self-supervised`
- [AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via Structural Attention](https://arxiv.org/abs/2506.23611) — `reconstruction` `nerf` `gaussian-splatting`
- [Audio-3DVG: Unified Audio -- Point Cloud Fusion for 3D Visual Grounding](https://arxiv.org/abs/2507.00669)
- [BasketLiDAR: The First LiDAR-Camera Multimodal Dataset for Professional Basketball MOT](https://arxiv.org/abs/2508.15299) — `tracking` `reconstruction` `multi-modal` `dataset`
- [BATISNet: Instance Segmentation of Tooth Point Clouds with Boundary Awareness](https://arxiv.org/abs/2512.24201) — `segmentation`
- [Been There, Scanned That: Nostalgia-Driven LiDAR Compression for Self-Driving Cars](https://arxiv.org/abs/2511.00652) — `compression` `autonomous driving`
- [Bench-RNR: Dataset for Benchmarking Repetitive and Non-repetitive Scanning LiDAR for Infrastructure-based Vehicle Localization](https://arxiv.org/abs/2509.15583) — `localization` `dataset`
- [Benefit from Reference: Retrieval-Augmented Cross-modal Point Cloud Completion](https://arxiv.org/abs/2507.14485) — `completion` `generation`
- [Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders](https://arxiv.org/abs/2509.14975)
- [Bidirectional Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression](https://arxiv.org/abs/2509.14591) — `compression` `efficiency`
- [Cage-Based Deformation for Transferable and Undefendable Point Cloud Attack](https://arxiv.org/abs/2507.00690)
- [Calibrated Keyframe-Segment Selection for Descriptor-Agnostic LiDAR Loop Closure in Repetitive Environments](https://arxiv.org/abs/2512.09447) — `registration` `segmentation`
- [CALM-Net: Curvature-Aware LiDAR Point Cloud-based Multi-Branch Neural Network for Vehicle Re-Identification](https://arxiv.org/abs/2510.14576)
- [CasPoinTr: Point Cloud Completion with Cascaded Networks and Knowledge Distillation](https://arxiv.org/abs/2509.23375) — `completion` `reconstruction`
- [Characterizing Lidar Point-Cloud Adversities Using a Vector Field Visualization](https://arxiv.org/abs/2510.13619)
- [Co-Win: Joint Object Detection and Instance Segmentation in LiDAR Point Clouds via Collaborative Window Processing](https://arxiv.org/abs/2507.19691) — `segmentation` `detection` `BEV`
- [Convexity-Driven Projection for Point Cloud Dimensionality Reduction](https://arxiv.org/abs/2509.22043)
- [CRISTAL: Real-time Camera Registration in Static LiDAR Scans using Neural Rendering](https://arxiv.org/abs/2511.16349) — `registration` `localization` `efficiency`
- [Cross-Dataset Semantic Segmentation Performance Analysis: Unifying NIST Point Cloud City Datasets for 3D Deep Learning](https://arxiv.org/abs/2508.00822) — `segmentation` `dataset`
- [Cross3DReg: Towards a Large-scale Real-world Cross-source Point Cloud Registration Benchmark](https://arxiv.org/abs/2509.06456) — `registration` `dataset`
- [CURL-SLAM: Continuous and Compact LiDAR Mapping](https://arxiv.org/abs/2506.21077) — `slam` `localization`
- [D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173) — `reconstruction` `gaussian-splatting` `autonomous driving`
- [DAGLFNet: Deep Feature Attention Guided Global and Local Feature Fusion for Pseudo-Image Point Cloud Segmentation](https://arxiv.org/abs/2510.10471) — `segmentation`
- [DAP-MAE: Domain-Adaptive Point Cloud Masked Autoencoder for Effective Cross-Domain Learning](https://arxiv.org/abs/2510.21635) — `self-supervised`
- [Data-Efficient Point Cloud Semantic Segmentation Pipeline for Unimproved Roads](https://arxiv.org/abs/2508.20135) — `segmentation` `efficiency`
- [DCReg: Decoupled Characterization for Efficient Degenerate LiDAR Registration](https://arxiv.org/abs/2509.06285) — `registration` `efficiency`
- [DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring](https://arxiv.org/abs/2509.18898) — `gaussian-splatting` `robustness`
- [Decision PCR: Decision version of the Point Cloud Registration task](https://arxiv.org/abs/2507.14965) — `registration`
- [Deep Imbalanced Multi-Target Regression: 3D Point Cloud Voxel Content Estimation in Simulated Forests](https://arxiv.org/abs/2511.12740) — `detection`
- [Deep Learning based Joint Geometry and Attribute Up-sampling for Large-Scale Colored Point Clouds](https://arxiv.org/abs/2506.22749)
- [Deep learning for 3D point cloud processing - from approaches, tasks to its implications on urban and environmental applications](https://arxiv.org/abs/2509.12452)
- [Deep Learning For Point Cloud Denoising: A Survey](https://arxiv.org/abs/2508.11932) — `denoising`
- [Deep Neural Watermarking for Robust Copyright Protection in 3D Point Clouds](https://arxiv.org/abs/2510.27533) — `robustness`
- [Deep Unrolling of Sparsity-Induced RDO for 3D Point Cloud Attribute Coding](https://arxiv.org/abs/2509.08685) — `compression`
- [Denoising-While-Completing Network (DWCNet): Robust Point Cloud Completion Under Corruption](https://arxiv.org/abs/2507.16743) — `completion` `denoising` `autonomous driving` `robustness`
- [Dense-depth map guided deep Lidar-Visual Odometry with Sparse Point Clouds and Images](https://arxiv.org/abs/2507.15496) — `completion` `slam` `localization`
- [DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294) — `gaussian-splatting` `monocular` `efficiency`
- [DepthVision: Enabling Robust Vision-Language Models with GAN-Based LiDAR-to-RGB Synthesis for Autonomous Driving](https://arxiv.org/abs/2509.07463) — `autonomous driving` `vision-language` `robustness`
- [Desensitizing for Improving Corruption Robustness in Point Cloud Classification through Adversarial Training](https://arxiv.org/abs/2509.23010) — `classification` `robustness`
- [DFG-PCN: Point Cloud Completion with Degree-Flexible Point Graph](https://arxiv.org/abs/2509.23703) — `completion` `reconstruction`
- [Differentiable High-Performance Ray Tracing-Based Simulation of Radio Propagation with Point Clouds](https://arxiv.org/abs/2507.04021)
- [DiffPCN: Latent Diffusion Model Based on Multi-view Depth Images for Point Cloud Completion](https://arxiv.org/abs/2509.23723) — `completion` `generation`
- [DINOReg: Strong Point Cloud Registration with Vision Foundation Model](https://arxiv.org/abs/2509.24370) — `registration` `pre-training`
- [DisorientLiDAR: Physical Attacks on LiDAR-based Localization](https://arxiv.org/abs/2509.12595) — `localization` `autonomous driving`
- [DLBAcalib: Robust Extrinsic Calibration for Non-Overlapping LiDARs Based on Dual LBA](https://arxiv.org/abs/2507.09176) — `reconstruction` `robustness`
- [DM3D: Dynamic Mamba via Offset-Guided Feature Resampling for Point Cloud Understanding](https://arxiv.org/abs/2512.03424)
- [Dual-Branch Center-Surrounding Contrast: Rethinking Contrastive Learning for 3D Point Clouds](https://arxiv.org/abs/2512.08673) — `generation` `self-supervised`
- [Efficient Model-Based Purification Against Adversarial Attacks for LiDAR Segmentation](https://arxiv.org/abs/2508.19290) — `segmentation` `generation` `robustness` `efficiency`
- [Enhanced Sparse Point Cloud Data Processing for Privacy-aware Human Action Recognition](https://arxiv.org/abs/2508.10469) — `tracking`
- [Enhancing Tree Species Classification: Insights from YOLOv8 and Explainable AI Applied to TLS Point Cloud Projections](https://arxiv.org/abs/2512.16950) — `classification`
- [Exploring Single Domain Generalization of LiDAR-based Semantic Segmentation under Imperfect Labels](https://arxiv.org/abs/2510.09035) — `segmentation` `autonomous driving`
- [Fast globally optimal Truncated Least Squares point cloud registration with fixed rotation axis](https://arxiv.org/abs/2508.15613) — `registration`
- [Few to Big: Prototype Expansion Network via Diffusion Learner for Point Cloud Few-shot Semantic Segmentation](https://arxiv.org/abs/2509.12878) — `segmentation`
- [FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds](https://arxiv.org/abs/2511.20065) — `reconstruction` `compression` `efficiency`
- [FractalCloud: A Fractal-Inspired Architecture for Efficient Large-Scale Point Cloud Processing](https://arxiv.org/abs/2511.07665) — `autonomous driving` `efficiency` — [code](https://github.com/Yuzhe-Fu/FractalCloud)
- [From Canopy to Ground via ForestGen3D: Learning Cross-Domain Generation of 3D Forest Structure from Aerial-to-Terrestrial LiDAR](https://arxiv.org/abs/2509.16346) — `generation`
- [From Propagation to Prediction: Point-level Uncertainty Evaluation of MLS Point Clouds under Limited Ground Truth](https://arxiv.org/abs/2511.03053)
- [GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682) — `generation` `gaussian-splatting` `efficiency`
- [Generating Adversarial Point Clouds Using Diffusion Model](https://arxiv.org/abs/2507.21163) — `classification` `generation` `robustness`
- [Geo-Registration of Terrestrial LiDAR Point Clouds with Satellite Images without GNSS](https://arxiv.org/abs/2507.05999) — `registration`
- [Geometry-Aware Cross Modal Alignment for Light Field-LiDAR Semantic Segmentation](https://arxiv.org/abs/2510.06687) — `segmentation` `autonomous driving`
- [GMOR: A Lightweight Robust Point Cloud Registration Framework via Geometric Maximum Overlapping](https://arxiv.org/abs/2508.17427) — `registration` `robustness` `efficiency`
- [Graph-based Point Cloud Surface Reconstruction using B-Splines](https://arxiv.org/abs/2509.16050) — `reconstruction`
- [GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding](https://arxiv.org/abs/2506.21188)
- [Guided and Unguided Conditional Diffusion Mechanisms for Structured and Semantically-Aware 3D Point Cloud Generation](https://arxiv.org/abs/2509.17206) — `segmentation` `generation`
- [Guided Model-based LiDAR Super-Resolution for Resource-Efficient Automotive scene Segmentation](https://arxiv.org/abs/2509.01317) — `segmentation` `upsampling` `autonomous driving` `efficiency`
- [HeartFormer: Semantic-Aware Dual-Structure Transformers for 3D Four-Chamber Cardiac Point Cloud Reconstruction](https://arxiv.org/abs/2512.00264) — `reconstruction`
- [HGACNet: Hierarchical Graph Attention Network for Cross-Modal Point Cloud Completion](https://arxiv.org/abs/2509.13692) — `completion` `reconstruction`
- [Hint: hierarchical inter-frame correlation for one-shot point cloud sequence compression](https://arxiv.org/abs/2509.14859) — `compression`
- [HLS4PC: A Parametrizable Framework For Accelerating Point-Based 3D Point Cloud Models on FPGA](https://arxiv.org/abs/2512.22139) — `segmentation` `classification`
- [Human Action Recognition from Point Clouds over Time](https://arxiv.org/abs/2510.05506)
- [Human-Interpretable Uncertainty Explanations for Point Cloud Registration](https://arxiv.org/abs/2509.18786) — `registration`
- [Hybrid Long and Short Range Flows for Point Cloud Filtering](https://arxiv.org/abs/2508.08542) — `denoising`
- [HydraMamba: Multi-Head State Space Model for Global Point Cloud Learning](https://arxiv.org/abs/2507.19778)
- [HyPCV-Former: Hyperbolic Spatio-Temporal Transformer for 3D Point Cloud Video Anomaly Detection](https://arxiv.org/abs/2508.00473) — `detection` `anomaly detection`
- [IAENet: An Importance-Aware Ensemble Model for 3D Point Cloud-Based Anomaly Detection](https://arxiv.org/abs/2508.20492) — `detection` `anomaly detection`
- [IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection](https://arxiv.org/abs/2511.03267) — `detection` `anomaly detection` `dataset`
- [iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning](https://arxiv.org/abs/2509.08982) — `registration`
- [INDOOR-LiDAR: Bridging Simulation and Reality for Robot-Centric 360 degree Indoor LiDAR Perception -- A Robot-Centric Hybrid Dataset](https://arxiv.org/abs/2512.12377) — `dataset`
- [InfraDiffusion: zero-shot depth map restoration with diffusion models and prompted segmentation from sparse infrastructure point clouds](https://arxiv.org/abs/2509.03324) — `segmentation` `detection` `open-vocabulary`
- [Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS](https://arxiv.org/abs/2510.17479) — `gaussian-splatting`
- [InJecteD: Analyzing Trajectories and Drift Dynamics in Denoising Diffusion Probabilistic Models for 2D Point Cloud Generation](https://arxiv.org/abs/2509.12239) — `generation` `denoising`
- [Inland-LOAM: Voxel-Based Structural Semantic LiDAR Odometry and Mapping for Inland Waterway Navigation](https://arxiv.org/abs/2508.03672) — `slam`
- [Integrating Product Coefficients for Improved 3D LiDAR Data Classification (Part II)](https://arxiv.org/abs/2510.15219) — `classification`
- [Integrating SAM Supervision for 3D Weakly Supervised Point Cloud Segmentation](https://arxiv.org/abs/2508.19909) — `segmentation`
- [IPCD: Intrinsic Point-Cloud Decomposition](https://arxiv.org/abs/2511.09866)
- [J-SGFT: Joint Spatial and Graph Fourier Domain Learning for Point Cloud Attribute Deblocking](https://arxiv.org/abs/2511.05047) — `compression` `autonomous driving` — Workshop
- [Joint graph entropy knowledge distillation for point cloud classification and robustness against corruptions](https://arxiv.org/abs/2509.22150) — `classification` `robustness`
- [Label-Efficient Point Cloud Segmentation with Active Learning](https://arxiv.org/abs/2512.05759) — `segmentation` `efficiency`
- [LAHNet: Local Attentive Hashing Network for Point Cloud Registration](https://arxiv.org/abs/2512.00927) — `registration`
- [LDRFusion: A LiDAR-Dominant multimodal refinement framework for 3D object detection](https://arxiv.org/abs/2507.16224) — `detection` `completion` `multi-modal`
- [Leveraging CVAE for Joint Configuration Estimation of Multifingered Grippers from Point Cloud Data](https://arxiv.org/abs/2511.17276) — `generation`
- [LiDAR Point Cloud Colourisation Using Multi-Camera Fusion and Low-Light Image Enhancement](https://arxiv.org/abs/2509.25859)
- [LiDAR Point Cloud Image-based Generation Using Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2509.18917) — `detection` `generation` `denoising`
- [Lidar Variability: A Novel Dataset and Comparative Study of Solid-State and Spinning Lidars](https://arxiv.org/abs/2507.04321) — `localization` `reconstruction` `dataset`
- [LiDAR-based 3D Change Detection at City Scale](https://arxiv.org/abs/2510.21112) — `detection`
- [LiDAR-based Human Activity Recognition through Laplacian Spectral Analysis](https://arxiv.org/abs/2509.23255) — [code](https://github.com/Arritmic/oulu-pointcloud-har)
- [LiDAR-VGGT: Cross-Modal Coarse-to-Fine Fusion for Globally Consistent and Metric-Scale Dense Mapping](https://arxiv.org/abs/2511.01186) — `slam` `reconstruction`
- [LiDARDraft: Generating LiDAR Point Cloud from Versatile Inputs](https://arxiv.org/abs/2512.20105) — `generation` `autonomous driving`
- [LidarScout: Direct Out-of-Core Rendering of Massive Point Clouds](https://arxiv.org/abs/2509.20198)
- [LifelongPR: Lifelong point cloud place recognition based on sample replay and prompt learning](https://arxiv.org/abs/2507.10034) — `localization` `autonomous driving`
- [Linearized Optimal Transport for Analysis of High-Dimensional Point-Cloud and Single-Cell Data](https://arxiv.org/abs/2510.22033)
- [LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving](https://arxiv.org/abs/2511.16049) — `generation` `autonomous driving`
- [LLM-Guided Material Inference for 3D Point Clouds](https://arxiv.org/abs/2512.03237) — `vision-language`
- [MambaH-Fit: Rethinking Hyper-surface Fitting-based Point Cloud Normal Estimation via State Space Modelling](https://arxiv.org/abs/2510.09088) — `normal estimation`
- [MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation](https://arxiv.org/abs/2511.15077) — `tracking`
- [Manifold-Aware Point Cloud Completion via Geodesic-Attentive Hierarchical Feature Learning](https://arxiv.org/abs/2512.05710) — `completion` `reconstruction`
- [Masked Clustering Prediction for Unsupervised Point Cloud Pre-training](https://arxiv.org/abs/2508.08910) — `pre-training`
- [Matching the Optimal Denoiser in Point Cloud Diffusion with (Improved) Rotational Alignment](https://arxiv.org/abs/2510.03335) — `generation` `denoising`
- [Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348) — `reconstruction` `gaussian-splatting`
- [MCI-Net: A Robust Multi-Domain Context Integration Network for Point Cloud Registration](https://arxiv.org/abs/2512.23472) — `registration` `robustness`
- [Memory-Guided Point Cloud Completion for Dental Reconstruction](https://arxiv.org/abs/2512.03598) — `completion` `reconstruction`
- [MeshCoder: LLM-Powered Structured Mesh Code Generation from Point Clouds](https://arxiv.org/abs/2508.14879) — `generation` `reconstruction` `vision-language`
- [Methods for the Segmentation of Reticular Structures Using 3D LiDAR Data: A Comparative Evaluation](https://arxiv.org/abs/2507.20589) — `segmentation` `detection`
- [MFM-point: Multi-scale Flow Matching for Point Cloud Generation](https://arxiv.org/abs/2511.20041) — `generation`
- [Minkowski-MambaNet: A Point Cloud Framework with Selective State Space Models for Forest Biomass Quantification](https://arxiv.org/abs/2510.09367)
- [MLATC: Fast Hierarchical Topological Mapping from 3D LiDAR Point Clouds Based on Adaptive Resonance Theory](https://arxiv.org/abs/2511.22238)
- [Modeling high dimensional point clouds with the spherical cluster model](https://arxiv.org/abs/2512.21960)
- [ModelNet40-E: An Uncertainty-Aware Benchmark for Point Cloud Classification](https://arxiv.org/abs/2508.01269) — `classification` `dataset`
- [MOGS: Monocular Object-guided Gaussian Splatting in Large Scenes](https://arxiv.org/abs/2509.06685) — `gaussian-splatting` `autonomous driving` `monocular`
- [MS-DGCNN++: Multi-Scale Dynamic Graph Convolution with Scale-Dependent Normalization for Robust LiDAR Tree Species Classification](https://arxiv.org/abs/2507.12602) — `classification` `robustness`
- [Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles](https://arxiv.org/abs/2511.00635) — `registration` `detection` `slam` `localization`
- [Multi-modal Multi-task Pre-training for Improved Point Cloud Understanding](https://arxiv.org/abs/2507.17533) — `pre-training` `multi-modal`
- [MultiEditor: Controllable Multimodal Object Editing for Driving Scenarios Using 3D Gaussian Splatting Priors](https://arxiv.org/abs/2507.21872) — `gaussian-splatting` `autonomous driving` `multi-modal`
- [Multimodal Robust Prompt Distillation for 3D Point Cloud Models](https://arxiv.org/abs/2511.21574) — `multi-modal` `robustness`
- [Natively Trainable Sparse Attention for Hierarchical Point Cloud Datasets](https://arxiv.org/abs/2508.10758)
- [NeuralBoneReg: An Instance-Specific Label-Free Point Cloud-Based Method for Multi-Modal Bone Surface Registration](https://arxiv.org/abs/2511.14286) — `registration` `multi-modal`
- [NormalView: tree species classification from backpack and aerial lidar data using geometric projections](https://arxiv.org/abs/2512.05610) — `classification`
- [Object Pose Distribution Estimation for Determining Revolution and Reflection Uncertainty in Point Clouds](https://arxiv.org/abs/2512.07211)
- [OCCDiff: Occupancy Diffusion Model for High-Fidelity 3D Building Reconstruction from Noisy Point Clouds](https://arxiv.org/abs/2512.08506) — `generation` `reconstruction`
- [OG-PCL: Efficient Sparse Point Cloud Processing for Human Activity Recognition](https://arxiv.org/abs/2511.08910) — `efficiency`
- [OmniPlantSeg: Species Agnostic 3D Point Cloud Organ Segmentation for High-Resolution Plant Phenotyping Across Modalities](https://arxiv.org/abs/2509.21038) — `segmentation`
- [On the Impact of LiDAR Point Cloud Compression on Remote Semantic Segmentation](https://arxiv.org/abs/2509.23341) — `segmentation` `detection` `compression`
- [On-the-Fly Object-aware Representative Point Selection in Point Cloud](https://arxiv.org/abs/2508.01980)
- [Open-world Point Cloud Semantic Segmentation: A Human-in-the-loop Framework](https://arxiv.org/abs/2508.04962) — `segmentation`
- [OpenUrban3D: Annotation-Free Open-Vocabulary Semantic Segmentation of Large-Scale Urban Point Clouds](https://arxiv.org/abs/2509.10842) — `segmentation` `open-vocabulary`
- [OT-MeanFlow3D: Bridging Optimal Transport and Meanflow for Efficient 3D Point Cloud Generation](https://arxiv.org/abs/2509.22592) — `generation` `efficiency`
- [Out-of-Distribution Detection in LiDAR Semantic Segmentation Using Epistemic Uncertainty from Hierarchical GMMs](https://arxiv.org/abs/2510.08631) — `segmentation` `detection`
- [ParticleFormer: A 3D Point Cloud World Model for Multi-Object, Multi-Material Robotic Manipulation](https://arxiv.org/abs/2506.23126)
- [PCR-ORB: Enhanced ORB-SLAM3 with Point Cloud Refinement Using Deep Learning-Based Dynamic Object Filtering](https://arxiv.org/abs/2512.23318) — `tracking` `localization`
- [PI3DETR: Parametric Instance Detection of 3D Point Cloud Edges With a Geometry-Aware 3DETR](https://arxiv.org/abs/2509.03262) — `detection`
- [Pipe Reconstruction from Point Cloud Data](https://arxiv.org/abs/2506.22118) — `reconstruction`
- [PIT-QMM: A Large Multimodal Model For No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2510.07636) — `multi-modal`
- [Planning from Point Clouds over Continuous Actions for Multi-object Rearrangement](https://arxiv.org/abs/2509.04645)
- [PlantSegNeRF: A few-shot, cross-species method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching](https://arxiv.org/abs/2507.00371) — `segmentation` `reconstruction` `nerf`
- [Point Cloud Compression and Objective Quality Assessment: A Survey](https://arxiv.org/abs/2506.22902) — `compression` `autonomous driving`
- [Point cloud segmentation for 3D Clothed Human Layering](https://arxiv.org/abs/2508.05531) — `segmentation` `generation`
- [Point Cloud Segmentation of Integrated Circuits Package Substrates Surface Defects Using Causal Inference: Dataset Construction and Methodology](https://arxiv.org/abs/2511.05853) — `segmentation` `detection` `dataset`
- [Point Cloud-Based Control Barrier Functions for Model Predictive Control in Safety-Critical Navigation of Autonomous Mobile Robots](https://arxiv.org/abs/2510.02885) — `tracking`
- [Point-level Uncertainty Evaluation of Mobile Laser Scanning Point Clouds](https://arxiv.org/abs/2510.24773)
- [Point-Plane Projections for Accurate LiDAR Semantic Segmentation in Small Data Scenarios](https://arxiv.org/abs/2509.10841) — `segmentation` `autonomous driving`
- [Point-RTD: Replaced Token Denoising for Pretraining Transformer Models on Point Clouds](https://arxiv.org/abs/2509.17207) — `reconstruction` `denoising` `pre-training`
- [PointCubeNet: 3D Part-level Reasoning with 3x3x3 Point Cloud Blocks](https://arxiv.org/abs/2511.06744)
- [PointDGRWKV: Generalizing RWKV-like Architecture to Unseen Domains for Point Cloud Classification](https://arxiv.org/abs/2508.20835) — `classification`
- [PointGauss: Point Cloud-Guided Multi-Object Segmentation for Gaussian Splatting](https://arxiv.org/abs/2508.00259) — `segmentation` `gaussian-splatting`
- [PointLAMA: Latent Attention meets Mamba for Efficient Point Cloud Pretraining](https://arxiv.org/abs/2507.17296) — `pre-training` `efficiency`
- [PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning](https://arxiv.org/abs/2510.20406) — `multi-modal`
- [PointNet4D: A Lightweight 4D Point Cloud Video Backbone for Online and Offline Perception in Robotic Applications](https://arxiv.org/abs/2512.01383) — `efficiency`
- [PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction](https://arxiv.org/abs/2510.05613) — `generation`
- [PointRAFT: 3D deep learning for high-throughput prediction of potato tuber weight from partial point clouds](https://arxiv.org/abs/2512.24193)
- [PointVDP: Learning View-Dependent Projection by Fireworks Rays for 3D Point Cloud Segmentation](https://arxiv.org/abs/2507.06618) — `segmentation`
- [Pole-Image: A Self-Supervised Pole-Anchored Descriptor for Long-Term LiDAR Localization and Map Maintenance](https://arxiv.org/abs/2510.17237) — `detection` `localization` `self-supervised`
- [ProDAT: Progressive Density-Aware Tail-Drop for Point Cloud Coding](https://arxiv.org/abs/2510.17068) — `autonomous driving`
- [PUFM++: Point Cloud Upsampling via Enhanced Flow Matching](https://arxiv.org/abs/2512.20988) — `generation` `reconstruction` `upsampling`
- [Purge-Gate: Backpropagation-Free Test-Time Adaptation for Point Clouds Classification via Token Purging](https://arxiv.org/abs/2509.09785) — `classification`
- [PVINet: Point-Voxel Interlaced Network for Point Cloud Compression](https://arxiv.org/abs/2509.01097) — `compression`
- [PVNet: Point-Voxel Interaction LiDAR Scene Upsampling Via Diffusion Models](https://arxiv.org/abs/2508.17050) — `upsampling`
- [Quality-controlled registration of urban MLS point clouds reducing drift effects by adaptive fragmentation](https://arxiv.org/abs/2510.23416) — `registration`
- [Query-aware Hub Prototype Learning for Few-Shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2512.08253) — `segmentation`
- [Querying Autonomous Vehicle Point Clouds: Enhanced by 3D Object Counting with CounterNet](https://arxiv.org/abs/2507.19209) — `detection`
- [RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion](https://arxiv.org/abs/2511.07067) — `multi-modal`
- [Range-Edit: Semantic Mask Guided Outdoor LiDAR Scene Editing](https://arxiv.org/abs/2511.17269) — `autonomous driving`
- [RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation](https://arxiv.org/abs/2509.15886) — `segmentation` `autonomous driving`
- [RARE: Refine Any Registration of Pairwise Point Clouds via Zero-Shot Learning](https://arxiv.org/abs/2507.19950) — `registration` `open-vocabulary`
- [rareboost3d: a synthetic lidar dataset with enhanced rare classes](https://arxiv.org/abs/2510.10876) — `segmentation` `autonomous driving` `dataset`
- [Rate-distortion Optimized Point Cloud Preprocessing for Geometry-based Point Cloud Compression](https://arxiv.org/abs/2508.01633) — `compression`
- [Re-Densification Meets Cross-Scale Propagation: Real-Time Neural Compression of LiDAR Point Clouds](https://arxiv.org/abs/2508.20466) — `compression` `efficiency`
- [Real-time Point Cloud Data Transmission via L4S for 5G-Edge-Assisted Robotics](https://arxiv.org/abs/2511.15677) — `detection` `efficiency`
- [Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds](https://arxiv.org/abs/2511.20003) — `segmentation` `multi-modal`
- [Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching](https://arxiv.org/abs/2512.01850) — `registration` `localization` `generation` `reconstruction`
- [Registering the 4D Millimeter Wave Radar Point Clouds Via Generalized Method of Moments](https://arxiv.org/abs/2508.02187) — `registration` `multi-modal`
- [Registration-Free Monitoring of Unstructured Point Cloud Data via Intrinsic Geometrical Properties](https://arxiv.org/abs/2511.05623) — `registration` — [code](https://github.com/franci2312/RFM)
- [Relative Energy Learning for LiDAR Out-of-Distribution Detection](https://arxiv.org/abs/2511.06720) — `detection` `autonomous driving` — [code](https://github.com/343gltysprk/rel)
- [Representation Learning for Point Cloud Understanding](https://arxiv.org/abs/2512.06058)
- [Rethinking the Detail-Preserved Completion of Complex Tubular Structures based on Point Cloud: a Dataset and a Benchmark](https://arxiv.org/abs/2508.17658) — `segmentation` `detection` `completion` `dataset`
- [Rethinking the Encoding and Annotating of 3D Bounding Box: Corner-Aware 3D Object Detection from Point Clouds](https://arxiv.org/abs/2511.17619) — `detection` `BEV`
- [Revisiting Physically Realizable Adversarial Object Attack against LiDAR-based Detection: Clarifying Problem Formulation and Experimental Protocols](https://arxiv.org/abs/2507.18457) — `detection` `robustness`
- [RL-AD-Net: Reinforcement Learning Guided Adaptive Displacement in Latent Space for Refined Point Cloud Completion](https://arxiv.org/abs/2511.17054) — `completion` `denoising`
- [Robust Partial 3D Point Cloud Registration via Confidence Estimation under Global Context](https://arxiv.org/abs/2509.24275) — `registration` `robustness`
- [Robust Point Cloud Reinforcement Learning via PCA-Based Canonicalization](https://arxiv.org/abs/2510.20974) — `robustness`
- [Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration](https://arxiv.org/abs/2509.15882) — `registration` `self-supervised`
- [Self-Supervised Moving Object Segmentation of Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2511.02395) — `segmentation` `slam` `self-supervised` `autonomous driving`
- [Self-Supervised Point Cloud Completion based on Multi-View Augmentations of Single Partial Point Cloud](https://arxiv.org/abs/2509.22132) — `completion` `self-supervised`
- [SG-LDM: Semantic-Guided LiDAR Generation via Latent-Aligned Diffusion](https://arxiv.org/abs/2506.23606) — `generation`
- [SHIELD: Spherical-Projection Hybrid-Frontier Integration for Efficient LiDAR-based Drone Exploration](https://arxiv.org/abs/2512.23972) — `efficiency`
- [SIM-Net: A Multimodal Fusion Network Using Inferred 3D Object Shape Point Clouds from RGB Images for 2D Classification](https://arxiv.org/abs/2506.18683) — `classification` `multi-modal`
- [Skeleton-based Robust Registration Framework for Corrupted 3D Point Clouds](https://arxiv.org/abs/2509.24273) — `registration` `reconstruction` `autonomous driving` `robustness`
- [SkinningGS: Editable Dynamic Human Scene Reconstruction Using Gaussian Splatting Based on a Skinning Model](https://arxiv.org/abs/2506.21632) — `reconstruction` `gaussian-splatting` `monocular`
- [SNAP: Towards Segmenting Anything in Any Point Cloud](https://arxiv.org/abs/2510.11565) — `segmentation`
- [SODA: Out-of-Distribution Detection in Domain-Shifted Point Clouds via Neighborhood Propagation](https://arxiv.org/abs/2506.21892) — `detection`
- [Spira: Exploiting Voxel Data Structural Properties for Efficient Sparse Convolution in Point Cloud Networks](https://arxiv.org/abs/2511.20834) — `autonomous driving` `efficiency`
- [Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525) — `gaussian-splatting`
- [SRMambaV2: Biomimetic Attention for Sparse Point Cloud Upsampling in Autonomous Driving](https://arxiv.org/abs/2507.17479) — `upsampling` `autonomous driving`
- [SSCATeR: Sparse Scatter-Based Convolution Algorithm with Temporal Data Recycling for Real-Time 3D Object Detection in LiDAR Point Clouds](https://arxiv.org/abs/2512.08557) — `detection` `efficiency`
- [STONE: Pioneering the One-to-N Universal Backdoor Threat in 3D Point Cloud](https://arxiv.org/abs/2511.11210) — `autonomous driving`
- [STQE: Spatial-Temporal Attribute Quality Enhancement for G-PCC Compressed Dynamic Point Clouds](https://arxiv.org/abs/2507.17522) — `compression`
- [StripDet: Strip Attention-Based Lightweight 3D Object Detection from Point Cloud](https://arxiv.org/abs/2509.05954) — `detection` `efficiency`
- [StrucADT: Generating Structure-controlled 3D Point Clouds with Adjacency Diffusion Transformer](https://arxiv.org/abs/2509.23709) — `generation`
- [SuperiorGAT: Graph Attention Networks for Sparse LiDAR Point Cloud Reconstruction in Autonomous Systems](https://arxiv.org/abs/2512.22439) — `reconstruction`
- [SurfFill: Completion of LiDAR Point Clouds via Gaussian Surfel Splatting](https://arxiv.org/abs/2512.03010) — `completion` `reconstruction`
- [Symmetria: A Synthetic Dataset for Learning in Point Clouds](https://arxiv.org/abs/2510.23414) — `dataset`
- [Terrain-Aided Navigation Without Raycasting: A Sliding Grid Approach for Point Cloud Processing](https://arxiv.org/abs/2510.06470)
- [TeSO: Representing and Compressing 3D Point Cloud Scenes with Textured Surfel Octree](https://arxiv.org/abs/2508.07083) — `compression`
- [The Impact of 2D Segmentation Backbones on Point Cloud Predictions Using 4D Radar](https://arxiv.org/abs/2509.19644) — `segmentation` `autonomous driving` `multi-modal`
- [Through the Perspective of LiDAR: A Feature-Enriched and Uncertainty-Aware Annotation Pipeline for Terrestrial Point Cloud Segmentation](https://arxiv.org/abs/2510.06582) — `segmentation`
- [Topology-Aware Modeling for Unsupervised Simulation-to-Reality Point Cloud Recognition](https://arxiv.org/abs/2506.21165)
- [TopoRec: Point Cloud Recognition Using Topological Data Analysis](https://arxiv.org/abs/2506.18725) — `localization` `reconstruction` `autonomous driving`
- [Toward Using Machine Learning as a Shape Quality Metric for Liver Point Cloud Generation](https://arxiv.org/abs/2508.02482) — `generation`
- [Towards Training-Free Underwater 3D Object Detection from Sonar Point Clouds: A Comparison of Traditional and Deep Learning Approaches](https://arxiv.org/abs/2508.18293) — `detection`
- [TrackAny3D: Transferring Pretrained 3D Models for Category-unified 3D Point Cloud Tracking](https://arxiv.org/abs/2507.19908) — `tracking` `pre-training`
- [Training-Free Global Geometric Association for 4D LiDAR Panoptic Segmentation](https://arxiv.org/abs/2512.18991) — `segmentation`
- [Transferable and Undefendable Point Cloud Attacks via Medial Axis Transform](https://arxiv.org/abs/2507.18870)
- [Transmit Weights, Not Features: Orthogonal-Basis Aided Wireless Point-Cloud Transmission](https://arxiv.org/abs/2512.03819)
- [treeX: Unsupervised Tree Instance Segmentation in Dense Forest Point Clouds](https://arxiv.org/abs/2509.03633) — `segmentation`
- [UGAE: Unified Geometry and Attribute Enhancement for G-PCC Compressed Point Clouds](https://arxiv.org/abs/2510.23009) — `compression`
- [UMIGen: A Unified Framework for Egocentric Point Cloud Generation and Cross-Embodiment Robotic Imitation Learning](https://arxiv.org/abs/2511.09302) — `generation`
- [Uni-Mapper: Unified Mapping Framework for Multi-modal LiDARs in Complex and Dynamic Environments](https://arxiv.org/abs/2507.20538) — `multi-modal`
- [UniLGL: Learning Uniform Place Recognition for FOV-limited/Panoramic LiDAR Global Localization](https://arxiv.org/abs/2507.12194) — `localization`
- [Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination](https://arxiv.org/abs/2509.16639)
- [Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541) — `reconstruction` `gaussian-splatting`
- [VAD-GS: Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic Urban Scenes](https://arxiv.org/abs/2510.09364) — `gaussian-splatting`
- [Visualizing Spatial Point Clouds: A Task-Oriented Taxonomy](https://arxiv.org/abs/2510.02651)
- [Warm-Starting Optimization-Based Motion Planning for Robotic Manipulators via Point Cloud-Conditioned Flow Matching](https://arxiv.org/abs/2510.03460) — `generation`
- [Weakly-Supervised Learning for Tree Instances Segmentation in Airborne Lidar Point Clouds](https://arxiv.org/abs/2508.15646) — `segmentation`
- [Which LiDAR scanning pattern is better for roadside perception: Repetitive or Non-repetitive?](https://arxiv.org/abs/2511.00060)
- [XAI for Point Cloud Data using Perturbations based on Meaningful Segmentation](https://arxiv.org/abs/2507.22020) — `segmentation` `classification`

</details>


### 2024 <sub>(379)</sub>

→ [查看 2024 年完整列表](docs/year/2024.md)

### 2023 <sub>(496)</sub>

→ [查看 2023 年完整列表](docs/year/2023.md)

### 2022 <sub>(565)</sub>

→ [查看 2022 年完整列表](docs/year/2022.md)

### 2021 <sub>(533)</sub>

→ [查看 2021 年完整列表](docs/year/2021.md)

---

### 更早年份 / Earlier years

[2024](docs/year/2024.md) | [2023](docs/year/2023.md) | [2022](docs/year/2022.md) | [2021](docs/year/2021.md)

## 说明 / Notes

- 共 **2755** 篇（2021 年至今），其中 **155** 篇附带代码链接；年份为会议年份，纯 arXiv 为首次提交年份。
- 收录范围：点云相关（检测、分割、配准、补全、分类、跟踪、SLAM、生成、压缩、预训练等），不限于单一子方向。
- 2021 年前的经典工作未收录；数据集见 [DATASETS.md](DATASETS.md)（不受年份限制）。
- 每日自动同步：[`.github/workflows/arxiv-sync.yml`](.github/workflows/arxiv-sync.yml)。
- 灵感与对照：[zhulf0804/3D-PointCloud](https://github.com/zhulf0804/3D-PointCloud)（2024-08 起停更）。

## License

内容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布，脚本以 MIT 发布。
