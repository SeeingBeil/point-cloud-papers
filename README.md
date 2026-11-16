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

<details><summary><b>CVPR</b> · 21</summary>

- [Beyond the Label Itself: Latent Labels Enhance Semi-supervised Point Cloud Panoptic Segmentation](https://arxiv.org/abs/2312.08234) — `segmentation`
- [CrossSDF: 3D Reconstruction of Thin Structures From Cross-Sections](https://arxiv.org/abs/2412.04120) — `reconstruction`
- [D$^2$-World: An Efficient World Model through Decoupled Dynamic Flow](https://arxiv.org/abs/2411.17027) — `BEV` `efficiency`
- [DGC-GNN: Leveraging Geometry and Color Cues for Visual Descriptor-Free 2D-3D Matching](https://arxiv.org/abs/2306.12547)
- [Geometrically-driven Aggregation for Zero-shot 3D Point Cloud Understanding](https://arxiv.org/abs/2312.02244) — `open-vocabulary`
- [LoopDraw: a Loop-Based Autoregressive Model for Shape Synthesis and Editing](https://arxiv.org/abs/2212.04981) — Workshop
- [Low Latency Point Cloud Rendering with Learned Splatting](https://arxiv.org/abs/2409.16504) — Workshop
- [Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping](https://arxiv.org/abs/2312.04521) — `detection` `multi-modal` `anomaly detection`
- [Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation](https://arxiv.org/abs/2312.14124) — `generation`
- [OmniVec2 -- A Novel Transformer based Network for Large Scale Multimodal and Multitask Learning](https://arxiv.org/abs/2507.13364) — `multi-modal`
- [Paved2Paradise: Cost-Effective and Scalable LiDAR Simulation by Factoring the Real World](https://arxiv.org/abs/2312.01117) — Workshop
- [Point Transformer V3: Simpler, Faster, Stronger](https://arxiv.org/abs/2312.10035) — [code](https://github.com/Pointcept/PointTransformerV3)
- [PTT: Point-Trajectory Transformer for Efficient Temporal 3D Object Detection](https://arxiv.org/abs/2312.08371) — `detection` `efficiency` — [code](https://github.com/kuanchihhuang/PTT)
- [Sculpting Holistic 3D Representation in Contrastive Language-Image-3D Pre-training](https://arxiv.org/abs/2311.01734) — `self-supervised` `pre-training`
- [Selectively Dilated Convolution for Accuracy-Preserving Sparse Pillar-based Embedded 3D Object Detection](https://arxiv.org/abs/2408.13798) — `detection` `autonomous driving` — Workshop
- [SurfaceAug: Closing the Gap in Multimodal Ground Truth Sampling](https://arxiv.org/abs/2312.03808) — `multi-modal`
- [TetraSphere: A Neural Descriptor for O(3)-Invariant Point Cloud Analysis](https://arxiv.org/abs/2211.14456)
- [Text2Loc: 3D Point Cloud Localization from Natural Language](https://arxiv.org/abs/2311.15977) — `localization`
- [TULIP: Transformer for Upsampling of LiDAR Point Clouds](https://arxiv.org/abs/2312.06733) — `upsampling`
- [UniRepLKNet: A Universal Perception Large-Kernel ConvNet for Audio, Video, Point Cloud, Time-Series and Image Recognition](https://arxiv.org/abs/2311.15599) — [code](https://github.com/AILab-CVC/UniRepLKNet)
- [Zero-Shot Dual-Path Integration Framework for Open-Vocabulary 3D Instance Segmentation](https://arxiv.org/abs/2408.08591) — `segmentation` `open-vocabulary` — Workshop

</details>

<details><summary><b>ECCV</b> · 30</summary>

- [3D Single-object Tracking in Point Clouds with High Temporal Variation](https://arxiv.org/abs/2408.02049) — `tracking`
- [Bayesian Self-Training for Semi-Supervised 3D Segmentation](https://arxiv.org/abs/2409.08102) — `segmentation`
- [BelHouse3D: A Benchmark Dataset for Assessing Occlusion Robustness in 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2411.13251) — `segmentation` `robustness` `dataset` — Workshop
- [CF-PRNet: Coarse-to-Fine Prototype Refining Network for Point Cloud Completion and Reconstruction](https://arxiv.org/abs/2409.08443) — `completion` `reconstruction`
- [CloudFixer: Test-Time Adaptation for 3D Point Clouds via Diffusion-Guided Geometric Transformation](https://arxiv.org/abs/2407.16193)
- [Correspondence-Free SE(3) Point Cloud Registration in RKHS via Unsupervised Equivariant Learning](https://arxiv.org/abs/2407.20223) — `registration`
- [Cultural Heritage 3D Reconstruction with Diffusion Networks](https://arxiv.org/abs/2410.10927) — `generation` `reconstruction` — Workshop
- [D-SCo: Dual-Stream Conditional Diffusion for Monocular Hand-Held Object Reconstruction](https://arxiv.org/abs/2311.14189) — `generation` `reconstruction` `denoising` `monocular`
- [DatasetNeRF: Efficient 3D-aware Data Factory with Generative Radiance Fields](https://arxiv.org/abs/2311.12063) — `segmentation` `generation` `efficiency`
- [Diff3DETR:Agent-based Diffusion Model for Semi-supervised 3D Object Detection](https://arxiv.org/abs/2408.00286) — `detection` `generation`
- [Fast Point Cloud Geometry Compression with Context-based Residual Coding and INR-based Refinement](https://arxiv.org/abs/2408.02966) — `compression` — [code](https://github.com/hxu160/CRCIR_for_PCGC)
- [FastPCI: Motion-Structure Guided Fast Point Cloud Frame Interpolation](https://arxiv.org/abs/2410.19573) — `scene flow`
- [Formula-Supervised Visual-Geometric Pre-training](https://arxiv.org/abs/2409.13535) — `pre-training`
- [Image-to-Lidar Relational Distillation for Autonomous Driving Data](https://arxiv.org/abs/2409.00845) — `autonomous driving`
- [Learning Local Pattern Modularization for Point Cloud Reconstruction from Unseen Classes](https://arxiv.org/abs/2408.14279) — `reconstruction`
- [LEROjD: Lidar Extended Radar-Only Object Detection](https://arxiv.org/abs/2409.05564) — `detection` `multi-modal`
- [Localization and Expansion: A Decoupled Framework for Point Cloud Few-shot Semantic Segmentation](https://arxiv.org/abs/2408.13752) — `segmentation` `classification` `localization`
- [milliFlow: Scene Flow Estimation on mmWave Radar Point Cloud for Human Motion Sensing](https://arxiv.org/abs/2306.17010) — `scene flow` `multi-modal` — [code](https://github.com/Toytiny/milliFlow)
- [NICP: Neural ICP for 3D Human Registration at Scale](https://arxiv.org/abs/2312.14024) — `registration` `reconstruction`
- [OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation](https://arxiv.org/abs/2309.00616) — `segmentation` `open-vocabulary`
- [P2P-Bridge: Diffusion Bridges for 3D Point Cloud Denoising](https://arxiv.org/abs/2408.16325) — `denoising`
- [PointLLM: Empowering Large Language Models to Understand Point Clouds](https://arxiv.org/abs/2308.16911)
- [Progressive Classifier and Feature Extractor Adaptation for Unsupervised Domain Adaptation on Point Clouds](https://arxiv.org/abs/2311.16474) — `domain adaptation`
- [Rethinking LiDAR Domain Generalization: Single Source as Multiple Density Domains](https://arxiv.org/abs/2312.12098)
- [RISurConv: Rotation Invariant Surface Attention-Augmented Convolutions for 3D Point Cloud Classification and Segmentation](https://arxiv.org/abs/2408.06110) — `segmentation` `classification`
- [SelfGeo: Self-supervised and Geodesic-consistent Estimation of Keypoints on Deformable Shapes](https://arxiv.org/abs/2408.02291) — `self-supervised`
- [Subspace Prototype Guidance for Mitigating Class Imbalance in Point Cloud Semantic Segmentation](https://arxiv.org/abs/2408.10537) — `segmentation`
- [T-MAE: Temporal Masked Autoencoders for Point Cloud Representation Learning](https://arxiv.org/abs/2312.10217) — `self-supervised`
- [UMERegRobust - Universal Manifold Embedding Compatible Features for Robust Point Cloud Registration](https://arxiv.org/abs/2408.12380) — `registration` `robustness`
- [WindPoly: Polygonal Mesh Reconstruction via Winding Numbers](https://arxiv.org/abs/2407.19208) — `reconstruction`

</details>

<details><summary><b>NeurIPS</b> · 15</summary>

- [3D Focusing-and-Matching Network for Multi-Instance Point Cloud Registration](https://arxiv.org/abs/2411.07740) — `registration`
- [A Consistency-Aware Spot-Guided Transformer for Versatile and Hierarchical Point Cloud Registration](https://arxiv.org/abs/2410.10295) — `registration`
- [A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing](https://arxiv.org/abs/2410.20516) — `dataset` — Workshop
- [ImOV3D: Learning Open-Vocabulary Point Clouds 3D Object Detection from Only 2D Images](https://arxiv.org/abs/2410.24001) — `detection` `open-vocabulary` — [code](https://github.com/yangtiming/ImOV3D)
- [Multi-hypotheses Conditioned Point Cloud Diffusion for 3D Human Reconstruction from Occluded Images](https://arxiv.org/abs/2409.18364) — `reconstruction`
- [Multi-Object 3D Grounding with Dynamic Modules and Language-Informed Spatial Attention](https://arxiv.org/abs/2410.22306)
- [MultiPull: Detailing Signed Distance Functions by Pulling Multi-Level Queries at Multi-Step](https://arxiv.org/abs/2411.01208) — `reconstruction`
- [One for All: Multi-Domain Joint Training for Point Cloud Based 3D Object Detection](https://arxiv.org/abs/2411.01584) — `detection`
- [PCoTTA: Continual Test-Time Adaptation for Multi-Task Point Cloud Understanding](https://arxiv.org/abs/2411.00632)
- [Point Cloud Synthesis Using Inner Product Transforms](https://arxiv.org/abs/2410.18987) — `generation` — [code](https://github.com/aidos-lab/inner-product-transforms)
- [Point-PRC: A Prompt Learning Based Regulation Framework for Generalizable Point Cloud Analysis](https://arxiv.org/abs/2410.20406)
- [RG-SAN: Rule-Guided Spatial Awareness Network for End-to-End 3D Referring Expression Segmentation](https://arxiv.org/abs/2412.02402) — `segmentation` — [code](https://github.com/sosppxo/RG-SAN)
- [Target-Guided Adversarial Point Cloud Transformer Towards Recognition Against Real-world Corruptions](https://arxiv.org/abs/2411.00462) — `robustness` — [code](https://github.com/Roywangj/APCT)
- [Training an Open-Vocabulary Monocular 3D Object Detection Model without 3D Data](https://arxiv.org/abs/2411.15657) — `detection` `autonomous driving` `monocular` `open-vocabulary`
- [Unlearnable 3D Point Clouds: Class-wise Transformation Is All You Need](https://arxiv.org/abs/2410.03644)

</details>

<details><summary><b>ICLR</b> · 4</summary>

- [GaussianAnything: Interactive Point Cloud Flow Matching For 3D Object Generation](https://arxiv.org/abs/2411.08033) — `generation`
- [Matérn Kernels for Tunable Implicit Surface Reconstruction](https://arxiv.org/abs/2409.15466) — `reconstruction`
- [MIRACLE3D: Memory-efficient Integrated Robust Approach for Continual Learning on Point Clouds via Shape Model Construction](https://arxiv.org/abs/2410.06418) — `classification` `robustness` `efficiency`
- [Multimodality Helps Few-shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2410.22489) — `segmentation`

</details>

<details><summary><b>AAAI</b> · 15</summary>

- [A Pioneering Neural Network Method for Efficient and Robust Fluid Simulation](https://arxiv.org/abs/2412.10748) — `robustness` `efficiency`
- [BEV-MAE: Bird's Eye View Masked Autoencoders for Point Cloud Pre-training in Autonomous Driving Scenarios](https://arxiv.org/abs/2212.05758) — `detection` `self-supervised` `autonomous driving` `BEV`
- [CMG-Net: Robust Normal Estimation for Point Clouds via Chamfer Normal Distance and Multi-scale Geometry](https://arxiv.org/abs/2312.09154) — `normal estimation` `robustness`
- [EPCL: Frozen CLIP Transformer is An Efficient Point Cloud Encoder](https://arxiv.org/abs/2212.04098) — `efficiency`
- [iDet3D: Towards Efficient Interactive Object Detection for LiDAR Point Clouds](https://arxiv.org/abs/2312.15449) — `detection` `efficiency`
- [Learning Continuous Implicit Field with Local Distance Indicator for Arbitrary-Scale Point Cloud Upsampling](https://arxiv.org/abs/2312.15133) — `upsampling`
- [M3SOT: Multi-frame, Multi-field, Multi-space 3D Single Object Tracking](https://arxiv.org/abs/2312.06117) — `tracking` `autonomous driving`
- [NuScenes-QA: A Multi-modal Visual Question Answering Benchmark for Autonomous Driving Scenario](https://arxiv.org/abs/2305.14836) — `autonomous driving` `multi-modal` `dataset`
- [Point Cloud Part Editing: Segmentation, Generation, Assembly, and Selection](https://arxiv.org/abs/2312.11867) — `segmentation` `generation`
- [PointDGMamba: Domain Generalization of Point Cloud Classification via Generalized State Space Model](https://arxiv.org/abs/2408.13574) — `classification`
- [Robust 3D Tracking with Quality-Aware Shape Completion](https://arxiv.org/abs/2312.10608) — `completion` `tracking` `robustness`
- [Semantic Complete Scene Forecasting from a 4D Dynamic Point Cloud Sequence](https://arxiv.org/abs/2312.08054) — `completion`
- [SPEAL: Skeletal Prior Embedded Attention Learning for Cross-Source Point Cloud Registration](https://arxiv.org/abs/2312.08664) — `registration`
- [Towards Compact 3D Representations via Point Feature Enhancement Masked Autoencoders](https://arxiv.org/abs/2312.10726) — `self-supervised`
- [When Should We Prefer State-to-Visual DAgger Over Visual Reinforcement Learning?](https://arxiv.org/abs/2412.13662)

</details>

<details><summary><b>IJCAI</b> · 2</summary>

- [ESP-PCT: Enhanced VR Semantic Performance through Efficient Compression of Temporal and Spatial Redundancies in Point Cloud Transformers](https://arxiv.org/abs/2409.01216) — `compression` `efficiency`
- [Point Cloud Mixture-of-Domain-Experts Model for 3D Self-supervised Learning](https://arxiv.org/abs/2410.09886) — `self-supervised`

</details>

<details><summary><b>SIGGRAPH Asia</b> · 3</summary>

- [ELMO: Enhanced Real-time LiDAR Motion Capture through Upsampling](https://arxiv.org/abs/2410.06963) — `generation` `upsampling` `efficiency`
- [Neural Laplacian Operator for 3D Point Clouds](https://arxiv.org/abs/2409.06506)
- [Representing Long Volumetric Video with Temporal Gaussian Hierarchy](https://arxiv.org/abs/2412.09608) — `reconstruction`

</details>

<details><summary><b>ACM MM</b> · 4</summary>

- [On-the-fly Point Feature Representation for Point Clouds Analysis](https://arxiv.org/abs/2407.21335)
- [Positional Prompt Tuning for Efficient 3D Representation Learning](https://arxiv.org/abs/2408.11567) — `efficiency`
- [RefMask3D: Language-Guided Transformer for 3D Referring Segmentation](https://arxiv.org/abs/2407.18244) — `segmentation` — [code](https://github.com/heshuting555/RefMask3D)
- [Towards Practical Human Motion Prediction with LiDAR Point Clouds](https://arxiv.org/abs/2408.08202)

</details>

<details><summary><b>WACV</b> · 9</summary>

- [Continual Learning in 3D Point Clouds: Employing Spectral Techniques for Exemplar Selection](https://arxiv.org/abs/2409.08388) — `classification`
- [EdgeGaussians -- 3D Edge Mapping via Gaussian Splatting](https://arxiv.org/abs/2409.12886) — `gaussian-splatting`
- [PocoLoco: A Point Cloud Diffusion Model of Human Shape in Loose Clothing](https://arxiv.org/abs/2411.04249) — `generation`
- [Point-GN: A Non-Parametric Network Using Gaussian Positional Encoding for Point Cloud Classification](https://arxiv.org/abs/2412.03056) — `classification`
- [ReFu: Recursive Fusion for Exemplar-Free 3D Class-Incremental Learning](https://arxiv.org/abs/2409.12326)
- [Test-Time Adaptation of 3D Point Clouds via Denoising Diffusion Models](https://arxiv.org/abs/2411.14495) — `denoising`
- [Transientangelo: Few-Viewpoint Surface Reconstruction Using Single-Photon Lidar](https://arxiv.org/abs/2408.12191) — `reconstruction`
- [XR-MBT: Multi-modal Full Body Tracking for XR through Self-Supervision with Learned Depth Point Cloud Registration](https://arxiv.org/abs/2411.18377) — `registration` `tracking` `multi-modal`
- [ZAHA: Introducing the Level of Facade Generalization and the Large-Scale Point Cloud Facade Semantic Segmentation Benchmark Dataset](https://arxiv.org/abs/2411.04865) — `segmentation` `dataset`

</details>

<details><summary><b>BMVC</b> · 5</summary>

- [3D Point Cloud Network Pruning: When Some Weights Do not Matter](https://arxiv.org/abs/2408.14601) — `efficiency`
- [LOGen: Toward Lidar Object Generation by Point Diffusion](https://arxiv.org/abs/2412.07385) — `generation` `autonomous driving`
- [TraIL-Det: Transformation-Invariant Local Feature Networks for 3D LiDAR Object Detection with Unsupervised Pre-Training](https://arxiv.org/abs/2408.13902) — `detection` `autonomous driving` `pre-training` — [code](https://github.com/l1997i/rapid_seg)
- [Unsupervised Point Cloud Registration with Self-Distillation](https://arxiv.org/abs/2409.07558) — `registration` `autonomous driving`
- [Vision-Language Guidance for LiDAR-based Unsupervised 3D Object Detection](https://arxiv.org/abs/2408.03790) — `detection` `autonomous driving` `vision-language`

</details>

<details><summary><b>ICRA</b> · 10</summary>

- [23 DoF Grasping Policies from a Raw Point Cloud](https://arxiv.org/abs/2411.14400) — Workshop
- [A Robust Probability-based Joint Registration Method of Multiple Point Clouds Considering Local Consistency](https://arxiv.org/abs/2409.09682) — `registration` `robustness`
- [Can We Remove the Ground? Obstacle-aware Point Cloud Compression for Remote Object Detection](https://arxiv.org/abs/2410.00582) — `detection` `compression`
- [Efficient LiDAR Bundle Adjustment for Multi-Scan Alignment Utilizing Continuous-Time Trajectories](https://arxiv.org/abs/2412.11760) — `localization` `efficiency`
- [FlatFusion: Delving into Details of Sparse Transformer-based Camera-LiDAR Fusion for Autonomous Driving](https://arxiv.org/abs/2408.06832) — `autonomous driving` `multi-modal`
- [Kinematic-ICP: Enhancing LiDAR Odometry with Kinematic Constraints for Wheeled Mobile Robots Moving on Planar Surfaces](https://arxiv.org/abs/2410.10277) — `registration` `localization`
- [LiDAR-EDIT: LiDAR Data Generation by Editing the Object Layouts in Real-World Scenes](https://arxiv.org/abs/2412.00592) — `generation` `autonomous driving`
- [LiPO: LiDAR Inertial Odometry for ICP Comparison](https://arxiv.org/abs/2410.08097) — `registration`
- [MVCTrack: Boosting 3D Point Cloud Tracking via Multimodal-Guided Virtual Cues](https://arxiv.org/abs/2412.02734) — `tracking` `autonomous driving` `multi-modal`
- [Points2Plans: From Point Clouds to Long-Horizon Plans with Composable Relational Dynamics](https://arxiv.org/abs/2408.14769)

</details>

<details><summary><b>IROS</b> · 11</summary>

- [Are We Ready for Real-Time LiDAR Semantic Segmentation in Autonomous Driving?](https://arxiv.org/abs/2410.08365) — `segmentation` `detection` `reconstruction` `autonomous driving` — Workshop
- [CMR-Agent: Learning a Cross-Modal Agent for Iterative Image-to-Point Cloud Registration](https://arxiv.org/abs/2408.02394) — `registration` `localization`
- [Cross-Modal Self-Supervised Learning with Effective Contrastive Units for LiDAR Point Clouds](https://arxiv.org/abs/2409.06827) — `self-supervised` `autonomous driving`
- [DiffSSC: Semantic LiDAR Scan Completion using Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2409.18092) — `completion` `denoising` `autonomous driving`
- [DSLO: Deep Sequence LiDAR Odometry Based on Inconsistent Spatio-temporal Propagation](https://arxiv.org/abs/2409.00744)
- [Efficient Dynamic LiDAR Odometry for Mobile Robots with Structured Point Clouds](https://arxiv.org/abs/2411.18443) — `detection` `efficiency`
- [Exploiting Local Features and Range Images for Small Data Real-Time Point Cloud Semantic Segmentation](https://arxiv.org/abs/2410.10510) — `segmentation` `autonomous driving` `efficiency`
- [HeLiMOS: A Dataset for Moving Object Segmentation in 3D Point Clouds From Heterogeneous LiDAR Sensors](https://arxiv.org/abs/2408.06328) — `segmentation` `detection` `dataset`
- [Loss Distillation via Gradient Matching for Point Cloud Completion with Weighted Chamfer Distance](https://arxiv.org/abs/2409.06171) — `detection` `completion`
- [Moving Object Segmentation in Point Cloud Data using Hidden Markov Models](https://arxiv.org/abs/2410.18638) — `segmentation` `detection` — Workshop
- [Tracking Tumors under Deformation from Partial Point Clouds using Occupancy Networks](https://arxiv.org/abs/2411.02619) — `tracking`

</details>

<details><summary><b>RA-L</b> · 4</summary>

- [EPIC: A Lightweight LiDAR-Based UAV Exploration Framework for Large-Scale Scenarios](https://arxiv.org/abs/2410.14203) — `efficiency` — [code](https://github.com/SYSU-STAR/EPIC)
- [Point Cloud Compression with Bits-back Coding](https://arxiv.org/abs/2410.18115) — `compression`
- [Point Cloud Structural Similarity-based Underwater Sonar Loop Detection](https://arxiv.org/abs/2409.14020) — `detection` `localization`
- [RANSAC Back to SOTA: A Two-stage Consensus Filtering for Real-time 3D Registration](https://arxiv.org/abs/2410.15682) — `registration` `efficiency`

</details>

<details><summary><b>TPAMI</b> · 2</summary>

- [Monge-Ampere Regularization for Learning Arbitrary Shapes from Point Clouds](https://arxiv.org/abs/2410.18477) — `reconstruction` — [code](https://github.com/chuanxiang-yang/S2DF)
- [Parameter-Efficient Fine-Tuning in Spectral Domain for Point Cloud Learning](https://arxiv.org/abs/2410.08114) — `efficiency` — [code](https://github.com/jerryfeng2003/PointGST)

</details>

<details><summary><b>T-ITS</b> · 2</summary>

- [MSSF: A 4D Radar and Camera Fusion Framework With Multi-Stage Sampling for 3D Object Detection in Autonomous Driving](https://arxiv.org/abs/2411.15016) — `detection` `autonomous driving` `multi-modal`
- [PRFusion: Toward Effective and Robust Multi-Modal Place Recognition with Image and Point Cloud Fusion](https://arxiv.org/abs/2410.04939) — `localization` `autonomous driving` `multi-modal` `robustness`

</details>

<details><summary><b>TIP</b> · 1</summary>

- [TripleMixer: A 3D Point Cloud Denoising Model for Adverse Weather](https://arxiv.org/abs/2408.13802) — `denoising`

</details>

<details><summary><b>TVCG</b> · 1</summary>

- [NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds](https://arxiv.org/abs/2411.17392) — `reconstruction`

</details>

<details><summary><b>ISPRS</b> · 1</summary>

- [ARSGaussian: 3D Gaussian Splatting with LiDAR for Aerial Remote Sensing Novel View Synthesis](https://arxiv.org/abs/2412.18380) — `gaussian-splatting`

</details>

<details><summary><b>PR</b> · 1</summary>

- [MFP3D: Monocular Food Portion Estimation Leveraging 3D Point Clouds](https://arxiv.org/abs/2411.10492) — `tracking` `monocular` — Workshop

</details>

<details><summary><b>arXiv</b> · 238</summary>

- [A Generative Adversarial Network-based Method for LiDAR-Assisted Radar Image Enhancement](https://arxiv.org/abs/2409.00196) — `generation` `multi-modal` `robustness`
- [A Novel Perception Entropy Metric for Optimizing Vehicle Perception with LiDAR Deployment](https://arxiv.org/abs/2407.17942) — `detection`
- [A Real-time Degeneracy Sensing and Compensation Method for Enhanced LiDAR SLAM](https://arxiv.org/abs/2412.07513) — `registration` `slam` `localization` `autonomous driving`
- [Accelerating Point Cloud Ground Segmentation: From Mechanical to Solid-State Lidars](https://arxiv.org/abs/2408.10404) — `segmentation`
- [Adaptive LiDAR Odometry and Mapping for Autonomous Agricultural Mobile Robots in Unmanned Farms](https://arxiv.org/abs/2412.02899)
- [Advancing 3D Point Cloud Understanding through Deep Transfer Learning: A Comprehensive Survey](https://arxiv.org/abs/2407.17877)
- [Adversarial Attacks on LiDAR-Based Tracking Across Road Users: Robustness Evaluation and Target-Aware Black-Box Method](https://arxiv.org/abs/2410.20893) — `tracking` `BEV` `robustness`
- [An End-to-End Robust Point Cloud Semantic Segmentation Network with Single-Step Conditional Diffusion Models](https://arxiv.org/abs/2411.16308) — `segmentation` `denoising` `robustness`
- [An Enhanced Classification Method Based on Adaptive Multi-Scale Fusion for Long-tailed Multispectral Point Clouds](https://arxiv.org/abs/2412.11407) — `classification`
- [Analysis of Deep Learning-Based Colorization and Super-Resolution Techniques for Lidar Imagery](https://arxiv.org/abs/2409.11532) — `upsampling`
- [Att2CPC: Attention-Guided Lossy Attribute Compression of Point Clouds](https://arxiv.org/abs/2410.17823) — `compression`
- [Audio Array-Based 3D UAV Trajectory Estimation with LiDAR Pseudo-Labeling](https://arxiv.org/abs/2412.12698) — `tracking` `self-supervised`
- [Automatic marker-free registration based on similar tetrahedras for single-tree point clouds](https://arxiv.org/abs/2411.13069) — `registration`
- [Balanced Residual Distillation Learning for 3D Point Cloud Class-Incremental Semantic Segmentation](https://arxiv.org/abs/2408.01356) — `segmentation`
- [Bridging Domain Gap of Point Cloud Representations via Self-Supervised Geometric Augmentation](https://arxiv.org/abs/2409.06956) — `classification` `self-supervised` `domain adaptation`
- [CAD-Recode: Reverse Engineering CAD Code from Point Clouds](https://arxiv.org/abs/2412.14042) — `reconstruction`
- [Calibrated and Efficient Sampling-Free Confidence Estimation for LiDAR Scene Semantic Segmentation](https://arxiv.org/abs/2411.11935) — `segmentation` `autonomous driving` `efficiency`
- [CFSSeg: Closed-Form Solution for Class-Incremental Semantic Segmentation of 2D Images and 3D Point Clouds](https://arxiv.org/abs/2412.10834) — `segmentation`
- [CLIP-based Point Cloud Classification via Point Cloud to Image Translation](https://arxiv.org/abs/2408.03545) — `classification`
- [CLIP-GS: Unifying Vision-Language Representation with 3D Gaussian Splatting](https://arxiv.org/abs/2412.19142) — `reconstruction` `gaussian-splatting` `vision-language`
- [CoE: Deep Coupled Embedding for Non-Rigid Point Cloud Correspondences](https://arxiv.org/abs/2412.05557)
- [Color Enhancement for V-PCC Compressed Point Cloud via 2D Attribute Map Optimization](https://arxiv.org/abs/2412.14449) — `compression`
- [Compression of Large-Scale 3D Point Clouds Based on Joint Optimization of Point Sampling and Feature Extraction](https://arxiv.org/abs/2412.07302) — `compression`
- [Constraint-Aware Feature Learning for Parametric Point Cloud](https://arxiv.org/abs/2411.07747)
- [Contrastive masked auto-encoders based self-supervised hashing for 2D image and 3D point cloud cross-modal retrieval](https://arxiv.org/abs/2408.05711) — `self-supervised`
- [CP-VoteNet: Contrastive Prototypical VoteNet for Few-Shot Point Cloud Object Detection](https://arxiv.org/abs/2408.17036) — `detection`
- [Cross-Modal Visual Relocalization in Prior LiDAR Maps Utilizing Intensity Textures](https://arxiv.org/abs/2412.01299) — `localization`
- [CTE-MLO: Continuous-time and Efficient Multi-LiDAR Odometry with Localizability-aware Point Cloud Sampling](https://arxiv.org/abs/2408.04901) — `localization` `efficiency`
- [Curvature Diversity-Driven Deformation and Domain Alignment for Point Cloud](https://arxiv.org/abs/2410.02720)
- [DALI: Domain Adaptive LiDAR Object Detection via Distribution-level and Instance-level Pseudo Label Denoising](https://arxiv.org/abs/2412.08806) — `detection` `denoising`
- [DecoratingFusion: A LiDAR-Camera Fusion Network with the Combination of Point-level and Feature-level Fusion](https://arxiv.org/abs/2501.00220) — `detection` `autonomous driving` `multi-modal`
- [Deep Learning for 3D Point Cloud Enhancement: A Survey](https://arxiv.org/abs/2411.00857)
- [Dense Point Clouds Matter: Dust-GS for Scene Reconstruction from Sparse Viewpoints](https://arxiv.org/abs/2409.08613) — `reconstruction` `gaussian-splatting`
- [Density-aware global-local attention network for point cloud segmentation](https://arxiv.org/abs/2412.00489) — `segmentation` `autonomous driving`
- [DG-PPU: Dynamical Graphs based Post-processing of Point Clouds extracted from Knee Ultrasounds](https://arxiv.org/abs/2411.08926) — `tracking`
- [Diff-PCC: Diffusion-based Neural Compression for 3D Point Clouds](https://arxiv.org/abs/2408.10543) — `compression`
- [DiffCom: Decoupled Sparse Priors Guided Diffusion Compression for Point Clouds](https://arxiv.org/abs/2411.13860) — `reconstruction` `compression`
- [Diffusion-Occ: 3D Point Cloud Completion via Occupancy Diffusion](https://arxiv.org/abs/2408.14846) — `completion`
- [Distribution Guidance Network for Weakly Supervised Point Cloud Semantic Segmentation](https://arxiv.org/abs/2410.08091) — `segmentation`
- [Divide and Conquer: A Systematic Approach for Industrial Scale High-Definition OpenDRIVE Generation from Sparse Point Clouds](https://arxiv.org/abs/2407.18703) — `generation`
- [DualQuat-LOAM: LiDAR Odometry and Mapping parametrized on Dual Quaternions](https://arxiv.org/abs/2410.13541)
- [DV-Matcher: Deformation-based Non-Rigid Point Cloud Matching Guided by Pre-trained Visual Features](https://arxiv.org/abs/2408.08568) — `pre-training`
- [DynaSurfGS: Dynamic Surface Reconstruction with Planar-based Gaussian Splatting](https://arxiv.org/abs/2408.13972) — `reconstruction` `gaussian-splatting` — [code](https://github.com/Open3DVLab/DynaSurfGS)
- [EADReg: Probabilistic Correspondence Generation with Efficient Autoregressive Diffusion Model for Outdoor Point Cloud Registration](https://arxiv.org/abs/2411.15271) — `registration` `generation` `efficiency`
- [EEPNet: Efficient Edge Pixel-based Matching Network for Cross-Modal Dynamic Registration between LiDAR and Camera](https://arxiv.org/abs/2409.19305) — `registration` `efficiency`
- [Efficient 3D Perception on Multi-Sweep Point Cloud with Gumbel Spatial Pruning](https://arxiv.org/abs/2411.07742) — `efficiency`
- [Efficient and Scalable Point Cloud Generation with Sparse Point-Voxel Diffusion Models](https://arxiv.org/abs/2408.06145) — `generation` `efficiency`
- [Efficient Point Cloud Classification via Offline Distillation Framework and Negative-Weight Self-Distillation Technique](https://arxiv.org/abs/2409.02020) — `classification` `compression` `efficiency`
- [Efficiently Expanding Receptive Fields: Local Split Attention and Parallel Aggregation for Enhanced Large-scale Point Cloud Semantic Segmentation](https://arxiv.org/abs/2409.01662) — `segmentation`
- [EGP3D: Edge-guided Geometric Preserving 3D Point Cloud Super-resolution for RGB-D camera](https://arxiv.org/abs/2412.11680) — `reconstruction` `upsampling`
- [End-to-end learned Lossy Dynamic Point Cloud Attribute Compression](https://arxiv.org/abs/2408.10665) — `compression`
- [Enhancing Performance of Point Cloud Completion Networks with Consistency Loss](https://arxiv.org/abs/2410.07298) — `completion`
- [Enhancing Sampling Protocol for Point Cloud Classification Against Corruptions](https://arxiv.org/abs/2408.12062) — `classification`
- [Enriching thermal point clouds of buildings using semantic 3D building models](https://arxiv.org/abs/2407.21436)
- [EPContrast: Effective Point-level Contrastive Learning for Large-scale Point Cloud Understanding](https://arxiv.org/abs/2410.17207) — `self-supervised`
- [Equi-GSPR: Equivariant SE(3) Graph Network Model for Sparse Point Cloud Registration](https://arxiv.org/abs/2410.05729) — `registration` `reconstruction`
- [ES-Gaussian: Gaussian Splatting Mapping via Error Space-Based Gaussian Completion](https://arxiv.org/abs/2410.06613) — `completion` `reconstruction` `gaussian-splatting`
- [Evaluating and Improving the Robustness of LiDAR Odometry and Localization Under Real-World Corruptions](https://arxiv.org/abs/2409.10824) — `localization` `autonomous driving` `robustness`
- [Evaluating saliency scores in point clouds of natural environments by learning surface anomalies](https://arxiv.org/abs/2408.14421)
- [Evaluating the Impact of Point Cloud Colorization on Semantic Segmentation Accuracy](https://arxiv.org/abs/2410.06725) — `segmentation`
- [Evolutionary Neural Architecture Search for 3D Point Cloud Analysis](https://arxiv.org/abs/2408.05556)
- [Explainability of Point Cloud Neural Networks Using SMILE: Statistical Model-Agnostic Interpretability with Local Explanations](https://arxiv.org/abs/2410.15374)
- [Exploring contextual modeling with linear complexity for point cloud segmentation](https://arxiv.org/abs/2410.21211) — `segmentation`
- [Extracting Object Heights From LiDAR & Aerial Imagery](https://arxiv.org/abs/2408.00967) — `segmentation`
- [Fine-grained Metrics for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2407.21289) — `segmentation`
- [FlashMix: Fast Map-Free LiDAR Localization via Feature Mixing and Contrastive-Constrained Accelerated Training](https://arxiv.org/abs/2410.00702) — `localization`
- [Future Does Matter: Boosting 3D Object Detection with Temporal Motion Estimation in Point Cloud Sequences](https://arxiv.org/abs/2409.04390) — `detection` `autonomous driving`
- [Gait Sequence Upsampling using Diffusion Models for Single LiDAR Sensors](https://arxiv.org/abs/2410.08680) — `upsampling`
- [GaussianMarker: Uncertainty-Aware Copyright Protection of 3D Gaussian Splatting](https://arxiv.org/abs/2410.23718) — `gaussian-splatting`
- [GaussianPU: A Hybrid 2D-3D Upsampling Framework for Enhancing Color Point Clouds via 3D Gaussian Splatting](https://arxiv.org/abs/2409.01581) — `gaussian-splatting` `upsampling`
- [Generalizable Indoor Human Activity Recognition Method Based on Micro-Doppler Corner Point Cloud and Dynamic Graph Learning](https://arxiv.org/abs/2410.07542)
- [Generative Adversarial Synthesis of Radar Point Cloud Scenes](https://arxiv.org/abs/2410.13526) — `generation` `multi-modal` `robustness`
- [GeoFormer: Learning Point Cloud Completion with Tri-Plane Integrated Transformer](https://arxiv.org/abs/2408.06596) — `completion`
- [GPT-based Textile Pilling Classification Using 3D Point Cloud Data](https://arxiv.org/abs/2408.10496) — `classification`
- [Graph Optimality-Aware Stochastic LiDAR Bundle Adjustment with Progressive Spatial Smoothing](https://arxiv.org/abs/2410.14565)
- [Graph-based Scalable Sampling of 3D Point Cloud Attributes](https://arxiv.org/abs/2410.01027) — `compression`
- [Grasp Diffusion Network: Learning Grasp Generators from Partial Point Clouds with Diffusion Models in SO(3)xR3](https://arxiv.org/abs/2412.08398) — `generation`
- [GS-Matching: Reconsidering Feature Matching task in Point Cloud Registration](https://arxiv.org/abs/2412.04855) — `registration`
- [GS-PT: Exploiting 3D Gaussian Splatting for Comprehensive Point Cloud Understanding via Self-supervised Learning](https://arxiv.org/abs/2409.04963) — `gaussian-splatting` `self-supervised`
- [GSL-PCD: Improving Generalist-Specialist Learning with Point Cloud Feature-based Task Partitioning](https://arxiv.org/abs/2411.06733)
- [GSTran: Joint Geometric and Semantic Coherence for Point Cloud Segmentation](https://arxiv.org/abs/2408.11558) — `segmentation`
- [Hard-Label Black-Box Attacks on 3D Point Clouds](https://arxiv.org/abs/2412.00404)
- [HiSC4D: Human-centered interaction and 4D Scene Capture in Large-scale Space Using Wearable IMUs and LiDAR](https://arxiv.org/abs/2409.04398)
- [HorGait: A Hybrid Model for Accurate Gait Recognition in LiDAR Point Cloud Planar Projections](https://arxiv.org/abs/2410.08454)
- [Horticultural Temporal Fruit Monitoring via 3D Instance Segmentation and Re-Identification using Colored Point Clouds](https://arxiv.org/abs/2411.07799) — `segmentation`
- [How DREAMS are made: Emulating Satellite Galaxy and Subhalo Populations with Diffusion Models and Point Clouds](https://arxiv.org/abs/2409.02980)
- [Hyperbolic Chamfer Distance for Point Cloud Completion and Beyond](https://arxiv.org/abs/2412.17951) — `completion`
- [Impact of color and mixing proportion of synthetic point clouds on semantic segmentation](https://arxiv.org/abs/2412.19145) — `segmentation`
- [Imperceptible Adversarial Attacks on Point Clouds Guided by Point-to-Surface Field](https://arxiv.org/abs/2412.19015) — `robustness`
- [Implicit Contact Diffuser: Sequential Contact Reasoning with Latent Point Cloud Diffusion](https://arxiv.org/abs/2410.16571)
- [Implicit Neural Compression of Point Clouds](https://arxiv.org/abs/2412.10433) — `compression`
- [Improving Adversarial Robustness for 3D Point Cloud Recognition at Test-Time through Purified Self-Training](https://arxiv.org/abs/2409.14940) — `generation` `robustness`
- [Improving the Transferability of 3D Point Cloud Attack via Spectral-aware Admix and Optimization Designs](https://arxiv.org/abs/2412.12626) — `autonomous driving`
- [Inferring Neural Signed Distance Functions by Overfitting on Single Noisy Point Clouds through Finetuning Data-Driven based Priors](https://arxiv.org/abs/2410.19680)
- [Informed, Constrained, Aligned: A Field Analysis on Degeneracy-aware Point Cloud Registration in the Wild](https://arxiv.org/abs/2408.11809) — `registration` `slam` `localization`
- [Instance Segmentation of Reinforced Concrete Bridges with Synthetic Point Clouds](https://arxiv.org/abs/2409.16381) — `segmentation`
- [Interactive4D: Interactive 4D LiDAR Segmentation](https://arxiv.org/abs/2410.08206) — `segmentation`
- [Joint Point Cloud Upsampling and Cleaning with Octree-based CNNs](https://arxiv.org/abs/2410.17001) — `upsampling`
- [KAN-HyperpointNet for Point Cloud Sequence-Based 3D Human Action Recognition](https://arxiv.org/abs/2409.09444)
- [KISS-Matcher: Fast and Robust Point Cloud Registration Revisited](https://arxiv.org/abs/2409.15615) — `registration` `robustness`
- [Learned Compression for Images and Point Clouds](https://arxiv.org/abs/2409.08376) — `classification` `generation` `compression` `upsampling`
- [Learned Compression of Point Cloud Geometry and Attributes in a Single Model through Multimodal Rate-Control](https://arxiv.org/abs/2408.00599) — `reconstruction` `compression` `multi-modal`
- [Learning Disentangled Representations for Perceptual Point Cloud Quality Assessment via Mutual Information Minimization](https://arxiv.org/abs/2411.07936)
- [Learning Robotic Manipulation Policies from Point Clouds with Conditional Flow Matching](https://arxiv.org/abs/2409.07343)
- [LI-GS: Gaussian Splatting with LiDAR Incorporated for Accurate Large-Scale Reconstruction](https://arxiv.org/abs/2409.12899) — `reconstruction` `gaussian-splatting`
- [LiCROcc: Teach Radar for Accurate Semantic Occupancy Prediction using LiDAR and Camera](https://arxiv.org/abs/2407.16197) — `detection` `completion` `autonomous driving` `occupancy prediction`
- [LiDAR Inertial Odometry And Mapping Using Learned Registration-Relevant Features](https://arxiv.org/abs/2410.02961) — `registration` `slam`
- [Lidar Panoptic Segmentation in an Open World](https://arxiv.org/abs/2409.14273) — `segmentation` — [code](https://github.com/g-meghana-reddy/open-world-panoptic-segmentation)
- [LiDAR-3DGS: LiDAR Reinforced 3D Gaussian Splatting for Multimodal Radiance Field Rendering](https://arxiv.org/abs/2409.16296) — `gaussian-splatting` `multi-modal`
- [LiOn-XA: Unsupervised Domain Adaptation via LiDAR-Only Cross-Modal Adversarial Training](https://arxiv.org/abs/2410.15833) — `segmentation` `domain adaptation` `robustness`
- [LION: Linear Group RNN for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2407.18232) — `detection`
- [LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2411.12185) — `slam` `gaussian-splatting`
- [LiVisSfM: Accurate and Robust Structure-from-Motion with LiDAR and Visual Cues](https://arxiv.org/abs/2410.22213) — `registration` `slam` `reconstruction` `robustness`
- [LLM-PCGC: Large Language Model-based Point Cloud Geometry Compression](https://arxiv.org/abs/2408.08682) — `generation` `compression` `vision-language`
- [Localized Gaussians as Self-Attention Weights for Point Clouds Correspondence](https://arxiv.org/abs/2409.13291)
- [LoGDesc: Local geometric features aggregation for robust point cloud registration](https://arxiv.org/abs/2410.02420) — `registration` `robustness`
- [LSTP-Nav: Lightweight Spatiotemporal Policy for Map-free Multi-agent Navigation with LiDAR](https://arxiv.org/abs/2408.16370) — `efficiency`
- [LUDO: Low-Latency Understanding of Deformable Objects using Point Cloud Occupancy Functions](https://arxiv.org/abs/2411.08777)
- [LVBA: LiDAR-Visual Bundle Adjustment for RGB Point Cloud Mapping](https://arxiv.org/abs/2409.10868) — `localization`
- [MaFreeI2P: A Matching-Free Image-to-Point Cloud Registration Paradigm with Active Camera Pose Retrieval](https://arxiv.org/abs/2408.02392) — `registration`
- [Mahalanobis k-NN: A Statistical Lens for Robust Point-Cloud Registrations](https://arxiv.org/abs/2409.06267) — `registration` `robustness`
- [Markerless Aerial-Terrestrial Co-Registration of Forest Point Clouds using a Deformable Pose Graph](https://arxiv.org/abs/2410.09896) — `registration`
- [MATCH POLICY: A Simple Pipeline from Point Cloud Registration to Manipulation Policies](https://arxiv.org/abs/2409.15517) — `registration`
- [MBPU: A Plug-and-Play State Space Model for Point Cloud Upsamping with Fast Point Rendering](https://arxiv.org/abs/2410.15941) — `upsampling`
- [Memory-Efficient Point Cloud Registration via Overlapping Region Sampling](https://arxiv.org/abs/2410.21753) — `registration` `efficiency`
- [MICAS: Multi-grained In-Context Adaptive Sampling for 3D Point Cloud Processing](https://arxiv.org/abs/2411.16773) — `registration` `segmentation` `reconstruction` `denoising`
- [Micro-Structures Graph-Based Point Cloud Registration for Balancing Efficiency and Accuracy](https://arxiv.org/abs/2410.21857) — `registration` `efficiency`
- [MILAN: Milli-Annotations for Lidar Semantic Segmentation](https://arxiv.org/abs/2407.15797) — `segmentation` `self-supervised` `autonomous driving`
- [Mining and Transferring Feature-Geometry Coherence for Unsupervised Point Cloud Registration](https://arxiv.org/abs/2411.01870) — `registration`
- [Monocular Visual Place Recognition in LiDAR Maps via Cross-Modal State Space Model and Multi-View Matching](https://arxiv.org/abs/2410.06285) — `slam` `localization` `monocular`
- [MS-Mapping: An Uncertainty-Aware Large-Scale Multi-Session LiDAR Mapping System](https://arxiv.org/abs/2408.03723) — `autonomous driving`
- [Multilateral Cascading Network for Semantic Segmentation of Large-Scale Outdoor Point Clouds](https://arxiv.org/abs/2409.13983) — `segmentation`
- [nach0-pc: Multi-task Language Model with Molecular Point Cloud Encoder](https://arxiv.org/abs/2410.09240)
- [NARVis: Neural Accelerated Rendering for Real-Time Scientific Point Cloud Visualization](https://arxiv.org/abs/2407.19097) — `efficiency`
- [NeFF-BioNet: Crop Biomass Prediction from Point Cloud to Drone Imagery](https://arxiv.org/abs/2410.23901)
- [Neural Surface Reconstruction and Rendering for LiDAR-Visual Systems](https://arxiv.org/abs/2409.05310) — `reconstruction` `nerf`
- [NIMBA: Towards Robust and Principled Processing of Point Clouds With SSMs](https://arxiv.org/abs/2411.00151) — `robustness`
- [No-Reference Point Cloud Quality Assessment via Graph Convolutional Network](https://arxiv.org/abs/2411.07728)
- [ObitoNet: Multimodal High-Resolution Point Cloud Reconstruction](https://arxiv.org/abs/2412.18775) — `reconstruction` `multi-modal`
- [OCMG-Net: Neural Oriented Normal Refinement for Unstructured Point Clouds](https://arxiv.org/abs/2409.01100) — `normal estimation`
- [OE3DIS: Open-Ended 3D Point Cloud Instance Segmentation](https://arxiv.org/abs/2408.11747) — `segmentation` — Workshop
- [Optimized CNNs for Rapid 3D Point Cloud Object Recognition](https://arxiv.org/abs/2412.02855) — `detection`
- [Parallel Neural Computing for Scene Understanding from LiDAR Perception in Autonomous Racing](https://arxiv.org/abs/2412.18165) — `autonomous driving`
- [Particle-based 6D Object Pose Estimation from Point Clouds using Diffusion Models](https://arxiv.org/abs/2412.00835) — `generation`
- [PAVLM: Advancing Point Cloud based Affordance Understanding Via Vision-Language Model](https://arxiv.org/abs/2410.11564) — `vision-language`
- [PCDreamer: Point Cloud Completion Through Multi-view Diffusion Priors](https://arxiv.org/abs/2411.19036) — `completion`
- [PCTreeS: 3D Point Cloud Tree Species Classification Using Airborne LiDAR Images](https://arxiv.org/abs/2412.04714) — `classification`
- [Perceptual Quality Assessment of Trisoup-Lifting Encoded 3D Point Clouds](https://arxiv.org/abs/2410.06689)
- [PLANesT-3D: A new annotated dataset for segmentation of 3D plant point clouds](https://arxiv.org/abs/2407.21150) — `segmentation` `dataset`
- [PLATYPUS: Progressive Local Surface Estimator for Arbitrary-Scale Point Cloud Upsampling](https://arxiv.org/abs/2411.00432) — `upsampling` `autonomous driving`
- [PMT-MAE: Dual-Branch Self-Supervised Learning with Distillation for Efficient Point Cloud Classification](https://arxiv.org/abs/2409.02007) — `classification` `self-supervised` `efficiency`
- [PO3AD: Predicting Point Offsets toward Better 3D Point Cloud Anomaly Detection](https://arxiv.org/abs/2412.12617) — `detection` `reconstruction` `anomaly detection`
- [Point Cloud Context Analysis for Rehabilitation Grasping Assistance](https://arxiv.org/abs/2411.08169)
- [Point Cloud Denoising With Fine-Granularity Dynamic Graph Convolutional Networks](https://arxiv.org/abs/2411.14158) — `reconstruction` `denoising`
- [Point Cloud Novelty Detection Based on Latent Representations of a General Feature Extractor](https://arxiv.org/abs/2410.09861) — `detection`
- [Point Cloud Resampling with Learnable Heat Diffusion](https://arxiv.org/abs/2411.14120) — `generation`
- [Point Cloud to Mesh Reconstruction: Methods, Trade-offs, and Implementation Guide](https://arxiv.org/abs/2412.10977) — `reconstruction`
- [Point Cloud Understanding via Attention-Driven Contrastive Learning](https://arxiv.org/abs/2411.14744) — `self-supervised`
- [Point Cloud Unsupervised Pre-training via 3D Gaussian Splatting](https://arxiv.org/abs/2411.18667) — `gaussian-splatting` `self-supervised` `pre-training`
- [Point Cloud-Assisted Neural Image Compression](https://arxiv.org/abs/2412.11771) — `compression`
- [Point-GR: Graph Residual Point Cloud Network for 3D Object Classification and Segmentation](https://arxiv.org/abs/2412.03052) — `segmentation` `classification` — Workshop
- [Point-PNG: Conditional Pseudo-Negatives Generation for Point Cloud Pre-Training](https://arxiv.org/abs/2409.15832) — `generation` `self-supervised` `pre-training`
- [Point2Graph: An End-to-end Point Cloud-based 3D Open-Vocabulary Scene Graph for Robot Navigation](https://arxiv.org/abs/2409.10350) — `generation` `open-vocabulary`
- [PointCG: Self-supervised Point Cloud Learning via Joint Completion and Generation](https://arxiv.org/abs/2411.06041) — `completion` `generation` `self-supervised`
- [PointMT: Efficient Point Cloud Analysis with Hybrid MLP-Transformer Architecture](https://arxiv.org/abs/2408.05508) — `efficiency`
- [PointNCBW: Towards Dataset Ownership Verification for Point Clouds via Negative Clean-label Backdoor Watermark](https://arxiv.org/abs/2408.05500) — `dataset`
- [PointPatchRL -- Masked Reconstruction Improves Reinforcement Learning on Point Clouds](https://arxiv.org/abs/2410.18800) — `reconstruction`
- [PointVoxelFormer -- Reviving point cloud networks for 3D medical imaging](https://arxiv.org/abs/2412.17390)
- [Precise Workcell Sketching from Point Clouds Using an AR Toolbox](https://arxiv.org/abs/2410.00479) — `segmentation`
- [ProtoSeg: A Prototype-Based Point Cloud Instance Segmentation Method](https://arxiv.org/abs/2410.02352) — `segmentation`
- [PVContext: Hybrid Context Model for Point Cloud Compression](https://arxiv.org/abs/2409.12724) — `compression`
- [PX2Tooth: Reconstructing the 3D Point Cloud Teeth from a Single Panoramic X-ray](https://arxiv.org/abs/2411.03725) — `reconstruction`
- [QuadricsReg: Large-Scale Point Cloud Registration using Quadric Primitives](https://arxiv.org/abs/2412.02998) — `registration`
- [Quality Analysis of the Coding Bitrate Tradeoff Between Geometry and Attributes for Colored Point Clouds](https://arxiv.org/abs/2410.21613)
- [RadarPillars: Efficient Object Detection from 4D Radar Point Clouds](https://arxiv.org/abs/2408.05020) — `detection` `multi-modal` `efficiency`
- [Railway LiDAR semantic segmentation based on intelligent semi-automated data annotation](https://arxiv.org/abs/2410.13383) — `segmentation`
- [Real-Time 3D Object Detection Using InnovizOne LiDAR and Low-Power Hailo-8 AI Accelerator](https://arxiv.org/abs/2412.05594) — `detection` `autonomous driving` `efficiency`
- [Registration between Point Cloud Streams and Sequential Bounding Boxes via Gradient Descent](https://arxiv.org/abs/2409.09312) — `registration`
- [REGNet V2: End-to-End REgion-based Grasp Detection Network for Grippers of Different Sizes in Point Clouds](https://arxiv.org/abs/2410.09431) — `detection`
- [Reliable-loc: Robust sequential LiDAR global localization in large-scale street scenes based on verifiable cues](https://arxiv.org/abs/2411.07815) — `localization` `robustness`
- [Rendering-Oriented 3D Point Cloud Attribute Compression using Sparse Tensor-based Transformer](https://arxiv.org/abs/2411.07899) — `compression`
- [Resolving the Ambiguity of Complete-to-Partial Point Cloud Registration for Image-Guided Liver Surgery with Patches-to-Partial Matching](https://arxiv.org/abs/2412.19328) — `registration`
- [RESSCAL3D++: Joint Acquisition and Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2410.02323) — `segmentation`
- [Rethinking Attention Module Design for Point Cloud Analysis](https://arxiv.org/abs/2407.19294)
- [Revisiting Cross-Domain Problem for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2408.12708) — `detection` `autonomous driving`
- [Revisiting Point Cloud Completion: Are We Ready For The Real-World?](https://arxiv.org/abs/2411.17580) — `completion`
- [RIDE: Boosting 3D Object Detection for LiDAR Point Clouds via Rotation-Invariant Analysis](https://arxiv.org/abs/2408.15643) — `detection`
- [Robust 3D Point Clouds Classification based on Declarative Defenders](https://arxiv.org/abs/2410.09691) — `classification` `robustness`
- [Robust Point Cloud Registration in Robotic Inspection with Locally Consistent Gaussian Mixture Model](https://arxiv.org/abs/2407.17183) — `registration` `robustness`
- [Rotation Perturbation Robustness in Point Cloud Analysis: A Perspective of Manifold Distillation](https://arxiv.org/abs/2411.01748) — `robustness`
- [SA-MLP: A Low-Power Multiplication-Free Deep Network for 3D Point Cloud Classification in Resource-Constrained Environments](https://arxiv.org/abs/2409.01998) — `classification`
- [SaliencyI2PLoc: saliency-guided image-point cloud localization using contrastive learning](https://arxiv.org/abs/2412.15577) — `localization` `self-supervised`
- [Score-Based Multibeam Point Cloud Denoising](https://arxiv.org/abs/2409.13143) — `denoising`
- [SE3ET: SE(3)-Equivariant Transformer for Low-Overlap Point Cloud Registration](https://arxiv.org/abs/2407.16823) — `registration`
- [SEGT: A General Spatial Expansion Group Transformer for nuScenes Lidar-based Object Detection Task](https://arxiv.org/abs/2412.09658) — `detection`
- [Separating Drone Point Clouds From Complex Backgrounds by Cluster Filter -- Technical Report for CVPR 2024 UG2 Challenge](https://arxiv.org/abs/2412.16947) — `detection`
- [SfM-Free 3D Gaussian Splatting via Hierarchical Training](https://arxiv.org/abs/2412.01553) — `gaussian-splatting`
- [SIESEF-FusionNet: Spatial Inter-correlation Enhancement and Spatially-Embedded Feature Fusion Network for LiDAR Point Cloud Semantic Segmentation](https://arxiv.org/abs/2411.06991) — `segmentation` `autonomous driving`
- [Sight View Constraint for Robust Point Cloud Registration](https://arxiv.org/abs/2409.05065) — `registration` `robustness`
- [Sim2real Cattle Joint Estimation in 3D point clouds](https://arxiv.org/abs/2410.14419)
- [Simultaneous Diffusion Sampling for Conditional LiDAR Generation](https://arxiv.org/abs/2410.11628) — `generation`
- [SLAM2REF: Advancing Long-Term Mapping with 3D LiDAR and Reference Map Integration for Precise 6-DoF Trajectory Estimation and Map Extension](https://arxiv.org/abs/2408.15948) — `localization`
- [SLIM: Scalable and Lightweight LiDAR Mapping in Urban Environments](https://arxiv.org/abs/2409.08681) — `efficiency` — [code](https://github.com/HKUST-Aerial-Robotics/SLIM)
- [SPAC-Net: Rethinking Point Cloud Completion with Structural Prior](https://arxiv.org/abs/2411.15066) — `completion`
- [SPAC: Sampling-based Progressive Attribute Compression for Dense Point Clouds](https://arxiv.org/abs/2409.10293) — `compression`
- [Sparse Point Clouds Assisted Learned Image Compression](https://arxiv.org/abs/2412.15752) — `compression` `autonomous driving`
- [Spatial Visibility and Temporal Dynamics: Revolutionizing Field of View Prediction in Adaptive Point Cloud Video Streaming](https://arxiv.org/abs/2409.18236)
- [Spatio-Temporal 3D Point Clouds from WiFi-CSI Data via Transformer Networks](https://arxiv.org/abs/2410.16303)
- [SpheriGait: Enriching Spatial Representation via Spherical Projection for LiDAR-based Gait Recognition](https://arxiv.org/abs/2409.11869)
- [SPiKE: 3D Human Pose from Point Cloud Sequences](https://arxiv.org/abs/2409.01879)
- [Stealthy and Robust Backdoor Attack against 3D Point Clouds through Additional Point Features](https://arxiv.org/abs/2412.07511) — `robustness`
- [SynBench: A Synthetic Benchmark for Non-rigid 3D Point Cloud Registration](https://arxiv.org/abs/2409.14474) — `registration` `dataset`
- [Tensor-Train Point Cloud Compression and Efficient Approximate Nearest-Neighbor Search](https://arxiv.org/abs/2410.04462) — `compression` `efficiency`
- [Test-Time Adaptation in Point Clouds: Leveraging Sampling Variation with Weight Averaging](https://arxiv.org/abs/2411.01116) — `classification`
- [Text2LiDAR: Text-guided LiDAR Point Cloud Generation via Equirectangular Transformer](https://arxiv.org/abs/2407.19628) — `generation`
- [Textured As-Is BIM via GIS-informed Point Cloud Segmentation](https://arxiv.org/abs/2411.18898) — `segmentation`
- [TFCT-I2P: Three stream fusion network with color aware transformer for image-to-point cloud registration](https://arxiv.org/abs/2410.00360) — `registration`
- [The JPEG Pleno Learning-based Point Cloud Coding Standard: Serving Man and Machine](https://arxiv.org/abs/2409.08130) — `autonomous driving`
- [TOPGN: Real-time Transparent Obstacle Detection using Lidar Point Cloud Intensity for Autonomous Robot Navigation](https://arxiv.org/abs/2408.05608) — `detection` `efficiency`
- [Towards Explaining Uncertainty Estimates in Point Cloud Registration](https://arxiv.org/abs/2412.20612) — `registration`
- [Towards Robust Perception for Assistive Robotics: An RGB-Event-LiDAR Dataset and Multi-Modal Detection Pipeline](https://arxiv.org/abs/2408.13394) — `detection` `multi-modal` `robustness` `dataset`
- [Towards Zero-shot Point Cloud Anomaly Detection: A Multi-View Projection Framework](https://arxiv.org/abs/2409.13162) — `detection` `open-vocabulary` `anomaly detection`
- [TractShapeNet: Efficient Multi-Shape Learning with 3D Tractography Point Clouds](https://arxiv.org/abs/2410.22099) — `efficiency`
- [Trainable Pointwise Decoder Module for Point Cloud Segmentation](https://arxiv.org/abs/2408.01548) — `segmentation` `autonomous driving`
- [Training-Free Point Cloud Recognition Based on Geometric and Semantic Information Fusion](https://arxiv.org/abs/2409.04760)
- [TREND: Unsupervised 3D Representation Learning via Temporal Forecasting for LiDAR Perception](https://arxiv.org/abs/2412.03054)
- [TRLO: An Efficient LiDAR Odometry with 3D Dynamic Object Tracking and Removal](https://arxiv.org/abs/2410.13240) — `tracking` `slam` `localization` `efficiency`
- [U-Motion: Learned Point Cloud Video Compression with U-Structured Temporal Context Generation](https://arxiv.org/abs/2411.14501) — `generation` `compression`
- [UdeerLID+: Integrating LiDAR, Image, and Relative Depth with Semi-Supervised](https://arxiv.org/abs/2409.06197) — `segmentation` `autonomous driving`
- [UniRiT: Towards Few-Shot Non-Rigid Point Cloud Registration](https://arxiv.org/abs/2410.22909) — `registration`
- [Unsupervised Machine Learning for Detecting and Locating Human-Made Objects in 3D Point Cloud](https://arxiv.org/abs/2410.20006) — `detection`
- [Unsupervised Point Cloud Completion through Unbalanced Optimal Transport](https://arxiv.org/abs/2410.02671) — `completion`
- [Unsupervised semantic segmentation of urban high-density multispectral point clouds](https://arxiv.org/abs/2410.18520) — `segmentation`
- [Unsupervised UAV 3D Trajectories Estimation with Sparse Point Clouds](https://arxiv.org/abs/2412.12716) — `detection` `tracking`
- [Visual Localization in 3D Maps: Comparing Point Cloud, Mesh, and NeRF Representations](https://arxiv.org/abs/2408.11966) — `localization` `nerf`
- [VoxelTrack: Exploring Voxel Representation for 3D Point Cloud Object Tracking](https://arxiv.org/abs/2408.02263) — `tracking`
- [When 3D Partial Points Meets SAM: Tooth Point Cloud Segmentation with Sparse Labels](https://arxiv.org/abs/2409.01691) — `segmentation`
- [YOCO: You Only Calibrate Once for Accurate Extrinsic Parameter in LiDAR-Camera Systems](https://arxiv.org/abs/2407.18043) — `registration` `multi-modal`

</details>


### 2023 <sub>(496)</sub>

<details><summary><b>CVPR</b> · 39</summary>

- [3D Human Keypoints Estimation From Point Clouds in the Wild Without Human Labels](https://arxiv.org/abs/2306.04745) — `detection`
- [3D Registration with Maximal Cliques](https://arxiv.org/abs/2305.10854) — `registration` `generation`
- [ALSO: Automotive Lidar Self-supervision by Occupancy estimation](https://arxiv.org/abs/2212.05867) — `reconstruction` `self-supervised`
- [Building Rearticulable Models for Arbitrary 3D Objects from 4D Point Clouds](https://arxiv.org/abs/2306.00979)
- [DeepMapping2: Self-Supervised Large-Scale LiDAR Map Optimization](https://arxiv.org/abs/2212.06331) — `registration` `self-supervised` `autonomous driving`
- [DiffRF: Rendering-Guided 3D Radiance Field Diffusion](https://arxiv.org/abs/2212.01206) — `denoising`
- [Diffusion 3D Features (Diff3F): Decorating Untextured Shapes with Distilled Semantic Features](https://arxiv.org/abs/2311.17024)
- [DynStatF: An Efficient Feature Fusion Strategy for LiDAR 3D Object Detection](https://arxiv.org/abs/2305.15219) — `detection` `efficiency` — Workshop
- [E2PN: Efficient SE(3)-Equivariant Point Network](https://arxiv.org/abs/2206.05398) — `efficiency` — [code](https://github.com/minghanz/E2PN)
- [EDA: Explicit Text-Decoupling and Dense Alignment for 3D Visual Grounding](https://arxiv.org/abs/2209.14941)
- [EventNeRF: Neural Radiance Fields from a Single Colour Event Camera](https://arxiv.org/abs/2206.11896) — `reconstruction` `nerf`
- [GD-MAE: Generative Decoder for MAE Pre-training on LiDAR Point Clouds](https://arxiv.org/abs/2212.03010) — `generation` `pre-training`
- [GeoMAE: Masked Geometric Target Prediction for Self-supervised Point Cloud Pre-Training](https://arxiv.org/abs/2305.08808) — `reconstruction` `self-supervised` `pre-training`
- [GLiDR: Topologically Regularized Graph Generative Network for Sparse LiDAR Point Clouds](https://arxiv.org/abs/2312.00068) — `generation`
- [GraVoS: Voxel Selection for 3D Point-Cloud Detection](https://arxiv.org/abs/2208.08780) — `detection`
- [GrowSP: Unsupervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2305.16404) — `segmentation` — [code](https://github.com/vLAR-group/GrowSP)
- [LaserMix for Semi-Supervised LiDAR Semantic Segmentation](https://arxiv.org/abs/2207.00026) — `segmentation` — [code](https://github.com/ldkong1205/LaserMix)
- [Learning Signed Hyper Surfaces for Oriented Point Cloud Normal Estimation](https://arxiv.org/abs/2305.05873) — `normal estimation` — [code](https://github.com/LeoQLi/SHS-Net)
- [LidarGait: Benchmarking 3D Gait Recognition with Point Clouds](https://arxiv.org/abs/2211.10598)
- [LPFormer: LiDAR Pose Estimation Transformer with Multi-Task Network](https://arxiv.org/abs/2306.12525) — Workshop
- [MoDAR: Using Motion Forecasting for 3D Object Detection in Point Cloud Sequences](https://arxiv.org/abs/2306.03206) — `detection`
- [NeuMap: Neural Coordinate Mapping by Auto-Transdecoder for Camera Localization](https://arxiv.org/abs/2211.11177) — `localization`
- [Neural Kernel Surface Reconstruction](https://arxiv.org/abs/2305.19590) — `reconstruction`
- [On Deep Learning for Geometric and Semantic Scene Understanding Using On-Vehicle 3D LiDAR](https://arxiv.org/abs/2411.00600) — `segmentation` `autonomous driving`
- [PartSLIP: Low-Shot Part Segmentation for 3D Point Clouds via Pretrained Image-Language Models](https://arxiv.org/abs/2212.01558) — `segmentation` `pre-training`
- [PillarNeXt: Rethinking Network Designs for 3D Object Detection in LiDAR Point Clouds](https://arxiv.org/abs/2305.04925) — `detection`
- [PointCMP: Contrastive Mask Prediction for Self-supervised Learning on Point Cloud Videos](https://arxiv.org/abs/2305.04075) — `self-supervised`
- [PointConvFormer: Revenge of the Point-based Convolution](https://arxiv.org/abs/2208.02879)
- [PointVector: A Vector Representation In Point Cloud Analysis](https://arxiv.org/abs/2205.10528)
- [PVT-SSD: Single-Stage 3D Object Detector with Point-Voxel Transformer](https://arxiv.org/abs/2305.06621) — `detection`
- [PWR-Align: Leveraging Part-Whole Relationships for Part-wise Rigid Point Cloud Registration in Mixed Reality Applications](https://arxiv.org/abs/2306.06717) — `registration`
- [Reassembling Broken Objects using Breaking Curves](https://arxiv.org/abs/2306.02782) — Workshop
- [Reviewing 3D Object Detectors in the Context of High-Resolution 3+1D Radar](https://arxiv.org/abs/2308.05478) — `detection` `multi-modal` — Workshop
- [SCOOP: Self-Supervised Correspondence and Optimization-Based Scene Flow](https://arxiv.org/abs/2211.14020) — `self-supervised` `scene flow`
- [Towards Better Gradient Consistency for Neural Signed Distance Functions via Level Set Alignment](https://arxiv.org/abs/2305.11601) — [code](https://github.com/mabaorui/TowardsBetterGradient)
- [Towards Unsupervised Object Detection From LiDAR Point Clouds](https://arxiv.org/abs/2311.02007) — `detection` `autonomous driving`
- [ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding](https://arxiv.org/abs/2212.05171)
- [UltraLiDAR: Learning Compact Representations for LiDAR Completion and Generation](https://arxiv.org/abs/2311.01448) — `completion` `generation`
- [Weakly and Self-Supervised Class-Agnostic Motion Prediction for Autonomous Driving](https://arxiv.org/abs/2509.13116) — `self-supervised` `autonomous driving`

</details>

<details><summary><b>ICCV</b> · 45</summary>

- [2D-3D Interlaced Transformer for Point Cloud Segmentation with Scene-Level Supervision](https://arxiv.org/abs/2310.12817) — `segmentation`
- [2D3D-MATR: 2D-3D Matching Transformer for Detection-free Registration between Images and Point Clouds](https://arxiv.org/abs/2308.05667) — `registration` `detection`
- [3D Implicit Transporter for Temporally Consistent Keypoint Discovery](https://arxiv.org/abs/2309.05098) — `detection`
- [3DHacker: Spectrum-based Decision Boundary Generation for Hard-label 3D Point Cloud Attack](https://arxiv.org/abs/2308.07546) — `generation` `autonomous driving`
- [Ada3D : Exploiting the Spatial Redundancy with Adaptive Inference for Efficient 3D Object Detection](https://arxiv.org/abs/2307.08209) — `detection` `autonomous driving` `efficiency`
- [APNet: Urban-level Scene Segmentation of Aerial Images and Point Clouds](https://arxiv.org/abs/2309.17162) — `segmentation` — Workshop
- [AutoSynth: Learning to Generate 3D Training Data for Object Point Cloud Registration](https://arxiv.org/abs/2309.11170) — `registration`
- [CASSPR: Cross Attention Single Scan Place Recognition](https://arxiv.org/abs/2211.12542) — `localization` `autonomous driving`
- [CLIP2Point: Transfer CLIP to Point Cloud Classification with Image-Depth Pre-training](https://arxiv.org/abs/2210.01055) — `classification` `pre-training`
- [Clustering based Point Cloud Representation Learning for 3D Analysis](https://arxiv.org/abs/2307.14605) — `segmentation` `detection` — [code](https://github.com/FengZicai/Cluster3Dseg)
- [CPCM: Contextual Point Cloud Modeling for Weakly-supervised Point Cloud Semantic Segmentation](https://arxiv.org/abs/2307.10316) — `segmentation`
- [DELFlow: Dense Efficient Learning of Scene Flow for Large-Scale Point Clouds](https://arxiv.org/abs/2308.04383) — `scene flow` `efficiency` — [code](https://github.com/IRMVLab/DELFlow)
- [Density-invariant Features for Distant Point Cloud Registration](https://arxiv.org/abs/2307.09788) — `registration` `self-supervised`
- [DetZero: Rethinking Offboard 3D Object Detection with Long-term Sequential Point Clouds](https://arxiv.org/abs/2306.06023) — `detection` `tracking`
- [Distilling Coarse-to-Fine Semantic Matching Knowledge for Weakly Supervised 3D Visual Grounding](https://arxiv.org/abs/2307.09267)
- [Efficient 3D Semantic Segmentation with Superpoint Transformer](https://arxiv.org/abs/2306.08045) — `segmentation` `efficiency`
- [EP2P-Loc: End-to-End 3D Point to 2D Pixel Localization for Large-Scale Visual Localization](https://arxiv.org/abs/2309.07471) — `localization`
- [GaPro: Box-Supervised 3D Point Cloud Instance Segmentation Using Gaussian Processes as Pseudo Labelers](https://arxiv.org/abs/2307.13251) — `segmentation`
- [Generalized Few-Shot Point Cloud Segmentation Via Geometric Words](https://arxiv.org/abs/2309.11222) — `segmentation`
- [GeoUDF: Surface Reconstruction from 3D Point Clouds via Geometry-guided Distance Representation](https://arxiv.org/abs/2211.16762) — `reconstruction`
- [GPA-3D: Geometry-aware Prototype Alignment for Unsupervised Domain Adaptive 3D Object Detection from Point Clouds](https://arxiv.org/abs/2308.08140) — `detection`
- [GridPull: Towards Scalability in Learning Implicit Representations from 3D Point Clouds](https://arxiv.org/abs/2308.13175) — `reconstruction`
- [Hierarchical Point-based Active Learning for Semi-supervised Point Cloud Semantic Segmentation](https://arxiv.org/abs/2308.11166) — `segmentation`
- [KECOR: Kernel Coding Rate Maximization for Active 3D Object Detection](https://arxiv.org/abs/2307.07942) — `detection` `autonomous driving`
- [LiDAR-Camera Panoptic Segmentation via Geometry-Consistent and Semantic-Aware Alignment](https://arxiv.org/abs/2308.01686) — `segmentation` `multi-modal`
- [Masked Spatio-Temporal Structure Prediction for Self-supervised Learning on Point Cloud Videos](https://arxiv.org/abs/2308.09245) — `classification` `self-supervised`
- [MemorySeg: Online LiDAR Semantic Segmentation with a Latent Memory](https://arxiv.org/abs/2311.01556) — `segmentation`
- [P2C: Self-Supervised Point Cloud Completion from Single Partial Clouds](https://arxiv.org/abs/2307.14726) — `completion` `self-supervised`
- [PARTNER: Level up the Polar Representation for LiDAR 3D Object Detection](https://arxiv.org/abs/2308.03982) — `detection`
- [PC-Adapter: Topology-Aware Adapter for Efficient Domain Adaption on Point Clouds with Rectified Pseudo-label](https://arxiv.org/abs/2309.16936) — `self-supervised` `efficiency`
- [PG-RCNN: Semantic Surface Point Generation for 3D Object Detection](https://arxiv.org/abs/2307.12637) — `detection` `completion` `generation`
- [Point Contrastive Prediction with Semantic Clustering for Self-Supervised Learning on Point Cloud Videos](https://arxiv.org/abs/2308.09247) — `self-supervised`
- [Point-TTA: Test-Time Adaptation for Point Cloud Registration Using Multitask Meta-Auxiliary Learning](https://arxiv.org/abs/2308.16481) — `registration`
- [PointMBF: A Multi-scale Bidirectional Fusion Network for Unsupervised RGB-D Point Cloud Registration](https://arxiv.org/abs/2308.04782) — `registration`
- [Retro-FPN: Retrospective Feature Pyramid Network for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2308.09314) — `segmentation`
- [RPEFlow: Multimodal Fusion of RGB-PointCloud-Event for Joint Optical Flow and Scene Flow Estimation](https://arxiv.org/abs/2309.15082) — `scene flow` `multi-modal` — [code](https://github.com/danqu130/RPEFlow)
- [Sample-adaptive Augmentation for Point Cloud Recognition Against Real-world Corruptions](https://arxiv.org/abs/2309.10431) — [code](https://github.com/Roywangj/AdaptPoint)
- [SC3K: Self-supervised and Coherent 3D Keypoints Estimation from Rotated, Noisy, and Decimated Point Cloud Data](https://arxiv.org/abs/2308.05410) — `self-supervised` — [code](https://github.com/IITPAVIS/SC3K)
- [See More and Know More: Zero-shot Point Cloud Segmentation via Multi-modal Visual Data](https://arxiv.org/abs/2307.10782) — `segmentation` `open-vocabulary` `multi-modal`
- [Sketch and Text Guided Diffusion Model for Colored Point Cloud Generation](https://arxiv.org/abs/2308.02874) — `generation`
- [SVDFormer: Complementing Point Cloud via Self-view Augmentation and Self-structure Dual-generator](https://arxiv.org/abs/2307.08492) — `completion` `generation`
- [Take-A-Photo: 3D-to-2D Generative Pre-training of Point Cloud Models](https://arxiv.org/abs/2307.14971) — `generation` `pre-training`
- [U-RED: Unsupervised 3D Shape Retrieval and Deformation for Partial Point Clouds](https://arxiv.org/abs/2308.06383) — `classification`
- [UniSeg: A Unified Multi-Modal LiDAR Segmentation Network and the OpenPCSeg Codebase](https://arxiv.org/abs/2309.05573) — `segmentation` `multi-modal` — [code](https://github.com/PJLab-ADG/PCSeg)
- [Yes, we CANN: Constrained Approximate Nearest Neighbors for local feature-based visual localization](https://arxiv.org/abs/2306.09012) — `localization`

</details>

<details><summary><b>NeurIPS</b> · 21</summary>

- [AD-PT: Autonomous Driving Pre-Training with Large-scale Point Cloud Dataset](https://arxiv.org/abs/2306.00612) — `self-supervised` `autonomous driving` `pre-training` `dataset`
- [Annotator: A Generic Active Learning Baseline for LiDAR Semantic Segmentation](https://arxiv.org/abs/2310.20293) — `segmentation`
- [CityRefer: Geography-aware 3D Visual Grounding Dataset on City-scale Point Cloud Data](https://arxiv.org/abs/2310.18773) — `dataset`
- [ConDaFormer: Disassembled Transformer with Local Structure Enhancement for 3D Point Cloud Understanding](https://arxiv.org/abs/2312.11112) — [code](https://github.com/LHDuan/ConDaFormer)
- [Diffusion-SS3D: Diffusion Model for Semi-supervised 3D Object Detection](https://arxiv.org/abs/2312.02966) — `detection` `generation` — [code](https://github.com/luluho1208/Diffusion-SS3D)
- [E2PNet: Event to Point Cloud Registration with Spatio-Temporal Representation Learning](https://arxiv.org/abs/2311.18433) — `registration`
- [Echoes Beyond Points: Unleashing the Power of Raw Radar Data in Multi-modality Fusion](https://arxiv.org/abs/2307.16532) — `detection` `generation` `autonomous driving` `multi-modal`
- [HEDNet: A Hierarchical Encoder-Decoder Network for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2310.20234) — `detection` `autonomous driving`
- [HOH: Markerless Multimodal Human-Object-Human Handover Dataset with Large Object Count](https://arxiv.org/abs/2310.00723) — `multi-modal` `dataset`
- [MiliPoint: A Point Cloud Dataset for mmWave Radar](https://arxiv.org/abs/2309.13425) — `multi-modal` `dataset`
- [NeuralGF: Unsupervised Point Normal Estimation by Learning Neural Gradient Function](https://arxiv.org/abs/2311.00389) — `normal estimation`
- [Persistent Homology for High-dimensional Data Based on Spectral Methods](https://arxiv.org/abs/2311.03087)
- [Provable Adversarial Robustness for Group Equivariant Tasks: Graphs, Point Clouds, Molecules, and More](https://arxiv.org/abs/2312.02708) — `segmentation` `robustness`
- [Robustifying Generalizable Implicit Shape Networks with a Tunable Non-Parametric Model](https://arxiv.org/abs/2311.12967) — `reconstruction`
- [SE(3) Diffusion Model-based Point Cloud Registration for Robust 6D Object Pose Estimation](https://arxiv.org/abs/2310.17359) — `registration` `generation` `denoising` `robustness`
- [Segment Any Point Cloud Sequences by Distilling Vision Foundation Models](https://arxiv.org/abs/2306.09347) — `segmentation` — [code](https://github.com/youquanl/Segment-Any-Point-Cloud)
- [Semantic segmentation of sparse irregular point clouds for leaf/wood discrimination](https://arxiv.org/abs/2305.16963) — `segmentation` `detection`
- [Spherical Frustum Sparse Convolution Network for LiDAR Point Cloud Semantic Segmentation](https://arxiv.org/abs/2311.17491) — `segmentation`
- [Spiking PointNet: Spiking Neural Networks for Point Clouds](https://arxiv.org/abs/2310.06232)
- [Transient Neural Radiance Fields for Lidar View Synthesis and 3D Reconstruction](https://arxiv.org/abs/2307.09555) — `reconstruction` `nerf`
- [Uni3DETR: Unified 3D Detection Transformer](https://arxiv.org/abs/2310.05699) — `detection`

</details>

<details><summary><b>ICLR</b> · 7</summary>

- [AGILE3D: Attention Guided Interactive Multi-object 3D Segmentation](https://arxiv.org/abs/2306.00977) — `segmentation` `classification`
- [FreeReg: Image-to-Point Cloud Registration Leveraging Pretrained Diffusion Models and Monocular Depth Estimators](https://arxiv.org/abs/2310.03420) — `registration` `monocular` `pre-training`
- [Multi-View Representation is What You Need for Point-Cloud Pre-Training](https://arxiv.org/abs/2306.02558) — `pre-training`
- [Point2SSM: Learning Morphological Variations of Anatomies from Point Cloud](https://arxiv.org/abs/2305.14486)
- [Pre-Training LiDAR-Based 3D Object Detectors Through Colorization](https://arxiv.org/abs/2310.14592) — `detection` `autonomous driving` `pre-training`
- [SpikePoint: An Efficient Point-based Spiking Neural Network for Event Cameras Action Recognition](https://arxiv.org/abs/2310.07189) — `efficiency`
- [ZeroFlow: Scalable Scene Flow via Distillation](https://arxiv.org/abs/2305.10424) — `detection` `scene flow`

</details>

<details><summary><b>ICML</b> · 3</summary>

- [Equivariant vs. Invariant Layers: A Comparison of Backbone and Pooling for Point Cloud Classification](https://arxiv.org/abs/2306.05553) — `classification` — Workshop
- [Sample Complexity Bounds for Estimating Probability Divergences under Invariances](https://arxiv.org/abs/2311.02868) — `generation`
- [Stable and Consistent Prediction of 3D Characteristic Orientation via Invariant Residual Learning](https://arxiv.org/abs/2306.11406)

</details>

<details><summary><b>AAAI</b> · 7</summary>

- [Contrastive Predictive Autoencoders for Dynamic Point Cloud Self-Supervised Learning](https://arxiv.org/abs/2305.12959) — `generation` `reconstruction` `self-supervised`
- [GLT-T: Global-Local Transformer Voting for 3D Single Object Tracking in Point Clouds](https://arxiv.org/abs/2211.10927) — `tracking` — [code](https://github.com/haooozi/GLT-T)
- [LWSIS: LiDAR-guided Weakly Supervised Instance Segmentation for Autonomous Driving](https://arxiv.org/abs/2212.03504) — `segmentation` `autonomous driving`
- [NeAF: Learning Neural Angle Fields for Point Normal Estimation](https://arxiv.org/abs/2211.16869) — `normal estimation` — [code](https://github.com/lisj575/NeAF)
- [Rethinking Rotation Invariance with Point Cloud Registration](https://arxiv.org/abs/2301.00149) — `registration`
- [SSDA3D: Semi-supervised Domain Adaptation for 3D Object Detection from Point Cloud](https://arxiv.org/abs/2212.02845) — `detection` `autonomous driving` `domain adaptation`
- [Weakly Supervised 3D Multi-person Pose Estimation for Large-scale Scenes based on Monocular Camera and Single LiDAR](https://arxiv.org/abs/2211.16951) — `localization` `monocular`

</details>

<details><summary><b>SIGGRAPH</b> · 1</summary>

- [Adaptive Local Basis Functions for Shape Completion](https://arxiv.org/abs/2307.08348) — `completion`

</details>

<details><summary><b>SIGGRAPH Asia</b> · 1</summary>

- [Neural Gradient Learning and Optimization for Oriented Point Normal Estimation](https://arxiv.org/abs/2309.09211) — `normal estimation`

</details>

<details><summary><b>ACM MM</b> · 5</summary>

- [Boosting Few-shot 3D Point Cloud Segmentation via Query-Guided Enhancement](https://arxiv.org/abs/2308.03177) — `segmentation`
- [Context-Aware Indoor Point Cloud Object Generation through User Instructions](https://arxiv.org/abs/2311.16501) — `generation`
- [MSECNet: Accurate and Robust Normal Estimation for 3D Point Clouds by Multi-Scale Edge Conditioning](https://arxiv.org/abs/2308.02237) — `reconstruction` `normal estimation` `robustness`
- [Screen-based 3D Subjective Experiment Software](https://arxiv.org/abs/2308.03698)
- [SUG: Single-dataset Unified Generalization for 3D Point Cloud Classification](https://arxiv.org/abs/2305.09160) — `classification` `dataset` — [code](https://github.com/SiyuanHuang95/SUG)

</details>

<details><summary><b>3DV</b> · 4</summary>

- [BEVContrast: Self-Supervision in BEV Space for Automotive Lidar Point Clouds](https://arxiv.org/abs/2310.17281) — `BEV`
- [Mixing-Denoising Generalizable Occupancy Networks](https://arxiv.org/abs/2311.12125) — `reconstruction` `denoising`
- [Test-Time Augmentation for 3D Point Cloud Classification and Segmentation](https://arxiv.org/abs/2311.13152) — `segmentation` `classification`
- [ZeroPS: High-quality Cross-modal Knowledge Transfer for Zero-Shot 3D Part Segmentation](https://arxiv.org/abs/2311.14262) — `segmentation` `open-vocabulary`

</details>

<details><summary><b>WACV</b> · 2</summary>

- [Registered and Segmented Deformable Object Reconstruction from a Single View Point Cloud](https://arxiv.org/abs/2311.07357) — `registration` `reconstruction`
- [U3DS$^3$: Unsupervised 3D Semantic Scene Segmentation](https://arxiv.org/abs/2311.06018) — `segmentation`

</details>

<details><summary><b>BMVC</b> · 3</summary>

- [3D-QAE: Fully Quantum Auto-Encoding of 3D Point Clouds](https://arxiv.org/abs/2311.05604)
- [A-Scan2BIM: Assistive Scan to Building Information Modeling](https://arxiv.org/abs/2311.18166)
- [Towards Robust Few-shot Point Cloud Semantic Segmentation](https://arxiv.org/abs/2309.11228) — `segmentation` `robustness`

</details>

<details><summary><b>ICRA</b> · 14</summary>

- [A Data-efficient Framework for Robotics Large-scale LiDAR Scene Parsing](https://arxiv.org/abs/2312.02208) — `efficiency`
- [COIN-LIO: Complementary Intensity-Augmented LiDAR Inertial Odometry](https://arxiv.org/abs/2310.01235) — `registration`
- [Do we need scan-matching in radar odometry?](https://arxiv.org/abs/2310.18117) — `multi-modal`
- [FF-LOGO: Cross-Modality Point Cloud Registration with Feature Filtering and Local to Global Optimization](https://arxiv.org/abs/2309.08966) — `registration`
- [LiDAR Data Synthesis with Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2309.09256) — `completion` `generation` `denoising`
- [Mask4Former: Mask Transformer for 4D Panoptic Segmentation](https://arxiv.org/abs/2309.16133) — `segmentation` `tracking`
- [MGTR: Multi-Granular Transformer for Motion Prediction with LiDAR](https://arxiv.org/abs/2312.02409) — `autonomous driving`
- [Neural Informed RRT*: Learning-based Path Planning with Point Cloud State Representations under Admissible Ellipsoidal Constraints](https://arxiv.org/abs/2309.14595)
- [Out of Sight, Still in Mind: Reasoning and Planning about Unobserved Objects with Video Tracking Enabled Memory Models](https://arxiv.org/abs/2309.15278) — `tracking`
- [Proximity and Visuotactile Point Cloud Fusion for Contact Patches in Extreme Deformation](https://arxiv.org/abs/2307.03839)
- [QuadricsNet: Learning Concise Representation for Geometric Primitives in Point Clouds](https://arxiv.org/abs/2309.14211)
- [RaTrack: Moving Object Detection and Tracking with 4D Radar Point Cloud](https://arxiv.org/abs/2309.09737) — `detection` `tracking` `multi-modal`
- [RCM-Fusion: Radar-Camera Multi-Level Fusion for 3D Object Detection](https://arxiv.org/abs/2307.10249) — `detection` `multi-modal`
- [Robust 3D Object Detection from LiDAR-Radar Point Clouds via Cross-Modal Feature Augmentation](https://arxiv.org/abs/2309.17336) — `detection` `generation` `multi-modal` `robustness`

</details>

<details><summary><b>IROS</b> · 9</summary>

- [Converting Depth Images and Point Clouds for Feature-based Pose Estimation](https://arxiv.org/abs/2310.14924) — `registration`
- [Deep Robust Multi-Robot Re-localisation in Natural Environments](https://arxiv.org/abs/2307.13950) — `localization` `robustness`
- [GraNet: A Multi-Level Graph Network for 6-DoF Grasp Pose Generation in Cluttered Scenes](https://arxiv.org/abs/2312.03345) — `generation`
- [Irregular Change Detection in Sparse Bi-Temporal Point Clouds using Learned Place Recognition Descriptors and Point-to-Voxel Comparison](https://arxiv.org/abs/2306.15416) — `detection` `localization`
- [Point2Point : A Framework for Efficient Deep Learning on Hilbert sorted Point Clouds with applications in Spatio-Temporal Occupancy Prediction](https://arxiv.org/abs/2306.16306) — `occupancy prediction` `efficiency`
- [SUIT: Learning Significance-guided Information for 3D Temporal Detection](https://arxiv.org/abs/2307.01807) — `detection` `autonomous driving`
- [SuPerPM: A Surgical Perception Framework Based on Deep Point Matching Learned from Physical Constrained Simulation Data](https://arxiv.org/abs/2309.13863) — `tracking`
- [T-UDA: Temporal Unsupervised Domain Adaptation in Sequential Point Clouds](https://arxiv.org/abs/2309.08302) — `domain adaptation`
- [Test-Time Adaptation for Point Cloud Upsampling Using Meta-Learning](https://arxiv.org/abs/2308.16484) — `upsampling`

</details>

<details><summary><b>RA-L</b> · 12</summary>

- [CoFiI2P: Coarse-to-Fine Correspondences for Image-to-Point Cloud Registration](https://arxiv.org/abs/2309.14660) — `registration` `localization`
- [Concavity-Induced Distance for Unoriented Point Cloud Decomposition](https://arxiv.org/abs/2306.11051)
- [Cross-Modal Information-Guided Network using Contrastive Learning for Point Cloud Registration](https://arxiv.org/abs/2311.01202) — `registration` `self-supervised`
- [D2S: Representing sparse descriptors and 3D coordinates for camera relocalization](https://arxiv.org/abs/2307.15250) — `localization`
- [Energy-based Detection of Adverse Weather Effects in LiDAR Data](https://arxiv.org/abs/2305.16129) — `detection`
- [Incremental Multimodal Surface Mapping via Self-Organizing Gaussian Mixture Models](https://arxiv.org/abs/2309.10900) — `reconstruction` `multi-modal`
- [LCPR: A Multi-Scale Attention-Based LiDAR-Camera Fusion Network for Place Recognition](https://arxiv.org/abs/2311.03198) — `localization` `multi-modal`
- [Motion-to-Matching: A Mixed Paradigm for 3D Single Object Tracking](https://arxiv.org/abs/2308.11875) — `tracking`
- [Multi-Correlation Siamese Transformer Network with Dense Connection for 3D Single Object Tracking](https://arxiv.org/abs/2312.11051) — `tracking` `autonomous driving`
- [Pose-Graph Attentional Graph Neural Network for Lidar Place Recognition](https://arxiv.org/abs/2309.00168) — `localization`
- [RMS: Redundancy-Minimizing Point Cloud Sampling for Real-Time Pose Estimation](https://arxiv.org/abs/2312.07337) — `efficiency`
- [STTracker: Spatio-Temporal Tracker for 3D Single Object Tracking](https://arxiv.org/abs/2306.17440) — `tracking`

</details>

<details><summary><b>TPAMI</b> · 2</summary>

- [A Survey of Label-Efficient Deep Learning for 3D Point Clouds](https://arxiv.org/abs/2305.19812) — `efficiency`
- [Compositional Semantic Mix for Domain Adaptation in Point Cloud Segmentation](https://arxiv.org/abs/2308.14619) — `segmentation` `domain adaptation`

</details>

<details><summary><b>IJCV</b> · 1</summary>

- [A Review and A Robust Framework of Data-Efficient 3D Scene Parsing with Traditional/Learned 3D Descriptors](https://arxiv.org/abs/2312.01262) — `segmentation` `detection` `robustness` `efficiency`

</details>

<details><summary><b>TIP</b> · 1</summary>

- [Prototype Adaption and Projection for Few- and Zero-shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2305.14335) — `segmentation` `open-vocabulary`

</details>

<details><summary><b>ISPRS</b> · 9</summary>

- [A boundary-aware point clustering approach in Euclidean and embedding spaces for roof plane segmentation](https://arxiv.org/abs/2309.03722) — `segmentation` `reconstruction`
- [A Critical Analysis of Internal Reliability for Uncertainty Quantification of Dense Image Matching in Multi-view Stereo](https://arxiv.org/abs/2309.09379)
- [DC3DCD: unsupervised learning for multiclass 3D point cloud change detection](https://arxiv.org/abs/2305.05421) — `detection`
- [Deep Unsupervised Learning for 3D ALS Point Cloud Change Detection](https://arxiv.org/abs/2305.03529) — `detection`
- [JSMNet Improving Indoor Point Cloud Semantic and Instance Segmentation through Self-Attention and Multiscale](https://arxiv.org/abs/2309.07425) — `segmentation`
- [Nothing Stands Still: A Spatiotemporal Benchmark on 3D Point Cloud Registration Under Large Geometric and Temporal Change](https://arxiv.org/abs/2311.09346) — `registration` `dataset`
- [PolyGNN: Polyhedron-based Graph Neural Network for 3D Building Reconstruction from Point Clouds](https://arxiv.org/abs/2307.08636) — `classification` `reconstruction`
- [Research on self-cross transformer model of point cloud change detecter](https://arxiv.org/abs/2309.07444)
- [SCP: Scene Completion Pre-training for 3D Object Detection](https://arxiv.org/abs/2309.06199) — `detection` `completion` `autonomous driving` `pre-training`

</details>

<details><summary><b>TGRS</b> · 1</summary>

- [Benchmarking Deep Learning Architectures for Urban Vegetation Point Cloud Semantic Segmentation from MLS](https://arxiv.org/abs/2306.10274) — `segmentation`

</details>

<details><summary><b>PR</b> · 6</summary>

- [Advancements in Point Cloud Data Augmentation for Deep Learning: A Survey](https://arxiv.org/abs/2308.12113) — `segmentation` `detection` `classification`
- [Correlation Pyramid Network for 3D Single Object Tracking](https://arxiv.org/abs/2305.09195) — `tracking` `autonomous driving`
- [Cross-modal and Cross-domain Knowledge Transfer for Label-free 3D Segmentation](https://arxiv.org/abs/2309.10649) — `segmentation`
- [Learnable Chamfer Distance for Point Cloud Reconstruction](https://arxiv.org/abs/2312.16582) — `reconstruction`
- [MarS3D: A Plug-and-Play Motion-Aware Model for Semantic Segmentation on Multi-Scan 3D Point Clouds](https://arxiv.org/abs/2307.09316) — `segmentation`
- [Rotation-Invariant Completion Network](https://arxiv.org/abs/2308.11979) — `completion`

</details>

<details><summary><b>arXiv</b> · 303</summary>

- [$p$-Poisson surface reconstruction in curl-free flow from point clouds](https://arxiv.org/abs/2310.20095) — `reconstruction`
- [2DDATA: 2D Detection Annotations Transmittable Aggregation for Semantic Segmentation on Point Cloud](https://arxiv.org/abs/2309.11755) — `segmentation` `detection`
- [3D objects and scenes classification, recognition, segmentation, and reconstruction using 3D point cloud data: A review](https://arxiv.org/abs/2306.05978) — `segmentation` `classification` `reconstruction`
- [3D Pose Estimation of Tomato Peduncle Nodes using Deep Keypoint Detection and Point Cloud](https://arxiv.org/abs/2311.04699) — `detection`
- [3D Scene Graph Prediction on Point Clouds Using Knowledge Graphs](https://arxiv.org/abs/2308.06719)
- [3D Shape-Based Myocardial Infarction Prediction Using Point Cloud Classification Networks](https://arxiv.org/abs/2307.07298) — `classification`
- [3D-BBS: Global Localization for 3D Point Cloud Scan Matching Using Branch-and-Bound Algorithm](https://arxiv.org/abs/2310.10023) — `localization`
- [4DSR-GCN: 4D Video Point Cloud Upsampling using Graph Convolutional Networks](https://arxiv.org/abs/2306.01081) — `compression` `upsampling`
- [6D Assembly Pose Estimation by Point Cloud Registration for Robot Manipulation](https://arxiv.org/abs/2312.02593) — `registration` `detection`
- [A Comprehensive Review on Tree Detection Methods Using Point Cloud and Aerial Imagery from Unmanned Aerial Vehicles](https://arxiv.org/abs/2309.16375) — `detection`
- [A Conditional Denoising Diffusion Probabilistic Model for Point Cloud Upsampling](https://arxiv.org/abs/2312.02719) — `classification` `reconstruction` `upsampling` `denoising`
- [A denoised Mean Teacher for domain adaptive point cloud registration](https://arxiv.org/abs/2306.14749) — `registration`
- [A Dynamic Points Removal Benchmark in Point Cloud Maps](https://arxiv.org/abs/2307.07260) — `localization` `dataset` — [code](https://github.com/KTH-RPL/DynamicMap_Benchmark.git)
- [A Ground Segmentation Method Based on Point Cloud Map for Unstructured Roads](https://arxiv.org/abs/2309.08164) — `segmentation` `detection`
- [A Hybrid Semantic-Geometric Approach for Clutter-Resistant Floorplan Generation from Building Point Clouds](https://arxiv.org/abs/2305.15420) — `generation`
- [A point cloud approach to generative modeling for galaxy surveys at the field level](https://arxiv.org/abs/2311.17141) — `generation`
- [A Spatiotemporal Correspondence Approach to Unsupervised LiDAR Segmentation with Traffic Applications](https://arxiv.org/abs/2308.12433) — `segmentation`
- [A Strong Baseline for Point Cloud Registration via Direct Superpoints Matching](https://arxiv.org/abs/2307.01362) — `registration`
- [A Unified Framework for 3D Point Cloud Visual Grounding](https://arxiv.org/abs/2308.11887) — `segmentation`
- [A Unified Generative Framework for Realistic Lidar Simulation in Autonomous Driving Systems](https://arxiv.org/abs/2312.15817) — `generation` `autonomous driving`
- [A9 Intersection Dataset: All You Need for Urban 3D Camera-LiDAR Roadside Perception](https://arxiv.org/abs/2306.09266) — `autonomous driving` `multi-modal` `dataset`
- [Activating Frequency and ViT for 3D Point Cloud Quality Assessment without Reference](https://arxiv.org/abs/2312.05972) — `compression`
- [Active search and coverage using point-cloud reinforcement learning](https://arxiv.org/abs/2312.11410)
- [Adaptive Denoising-Enhanced LiDAR Odometry for Degeneration Resilience in Diverse Terrains](https://arxiv.org/abs/2309.14641) — `slam` `localization` `denoising`
- [Adaptive Multi-step Refinement Network for Robust Point Cloud Registration](https://arxiv.org/abs/2312.03053) — `registration` `robustness`
- [Adaptive Topological Feature via Persistent Homology: Filtration Learning for Point Clouds](https://arxiv.org/abs/2307.09259)
- [Addressing Data Misalignment in Image-LiDAR Fusion on Point Cloud Segmentation](https://arxiv.org/abs/2309.14932) — `segmentation` `autonomous driving`
- [Advancements in 3D Lane Detection Using LiDAR Point Clouds: From Data Collection to Model Development](https://arxiv.org/abs/2309.13596) — `detection`
- [Adversarial Attacks and Defenses on 3D Point Cloud Classification: A Survey](https://arxiv.org/abs/2307.00309) — `classification` `robustness`
- [AGAR: Attention Graph-RNN for Adaptative Motion Prediction of Point Clouds of Deformable Objects](https://arxiv.org/abs/2307.09936)
- [Aggressive saliency-aware point cloud compression](https://arxiv.org/abs/2307.10741) — `compression`
- [Analysis of LiDAR Configurations on Off-road Semantic Segmentation Performance](https://arxiv.org/abs/2306.16551) — `segmentation`
- [Arbitrary point cloud upsampling via Dual Back-Projection Network](https://arxiv.org/abs/2307.08992) — `upsampling`
- [Artificial Neural Network for Estimation of Physical Parameters of Sea Water using LiDAR Waveforms](https://arxiv.org/abs/2312.10068) — `detection` `reconstruction`
- [Attention-Guided Lidar Segmentation and Odometry Using Image-to-Point Cloud Saliency Transfer](https://arxiv.org/abs/2308.14332) — `segmentation` `autonomous driving`
- [Automated forest inventory: analysis of high-density airborne LiDAR point clouds with 3D deep learning](https://arxiv.org/abs/2312.15084)
- [Automated spacing measurement of formwork system members with 3D point cloud data](https://arxiv.org/abs/2305.19275) — `completion`
- [Automatic coarse co-registration of point clouds from diverse scan geometries: a test of detectors and descriptors](https://arxiv.org/abs/2308.14047) — `registration`
- [Automatic extraction and 3D reconstruction of split wire from point cloud data based on improved DPC algorithm](https://arxiv.org/abs/2401.08587) — `reconstruction`
- [Autonomous Point Cloud Segmentation for Power Lines Inspection in Smart Grid](https://arxiv.org/abs/2308.07283) — `segmentation`
- [Benchmarking and Analyzing Robust Point Cloud Recognition: Bag of Tricks for Defending Adversarial Examples](https://arxiv.org/abs/2307.16361) — `robustness`
- [Bidirectional Knowledge Reconfiguration for Lightweight Point Cloud Analysis](https://arxiv.org/abs/2310.05125) — `efficiency`
- [Body and Head Orientation Estimation from Low-Resolution Point Clouds in Surveillance Settings](https://arxiv.org/abs/2311.00343)
- [BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions](https://arxiv.org/abs/2312.14706) — `dataset`
- [BPNet: Bézier Primitive Segmentation on 3D Point Clouds](https://arxiv.org/abs/2307.04013) — `segmentation`
- [BuilDiff: 3D Building Shape Generation using Single-Image Conditional Point Cloud Diffusion Models](https://arxiv.org/abs/2309.00158) — `generation`
- [Building3D: An Urban-Scale Dataset and Benchmarks for Learning Roof Structures from Point Clouds](https://arxiv.org/abs/2307.11914) — `dataset`
- [Calib-Anything: Zero-training LiDAR-Camera Extrinsic Calibration Method Using Segment Anything](https://arxiv.org/abs/2306.02656) — `segmentation` `detection` `multi-modal`
- [Camera-LiDAR Fusion with Latent Contact for Place Recognition in Challenging Cross-Scenes](https://arxiv.org/abs/2310.10371) — `localization` `multi-modal`
- [Can point cloud networks learn statistical shape models of anatomies?](https://arxiv.org/abs/2305.05610) — `generation`
- [Change of Scenery: Unsupervised LiDAR Change Detection for Mobile Robots](https://arxiv.org/abs/2309.10924) — `segmentation` `detection`
- [Classification Method of Road Surface Condition and Type with LiDAR Using Spatiotemporal Information](https://arxiv.org/abs/2308.05965) — `classification`
- [Cloud-RAIN: Point Cloud Analysis with Reflectional Invariance](https://arxiv.org/abs/2305.07814)
- [CMDFusion: Bidirectional Fusion Network with Cross-modality Knowledge Distillation for LIDAR Semantic Segmentation](https://arxiv.org/abs/2307.04091) — `segmentation`
- [Collect-and-Distribute Transformer for 3D Point Cloud Analysis](https://arxiv.org/abs/2306.01257) — [code](https://github.com/haibo-qiu/CDFormer)
- [Colmap-PCD: An Open-source Tool for Fine Image-to-point cloud Registration](https://arxiv.org/abs/2310.05504) — `registration` `reconstruction` `monocular`
- [Comparing roughness maps generated by five roughness descriptors for LiDAR-derived digital elevation models](https://arxiv.org/abs/2312.17407)
- [Comparison of Point Cloud and Image-based Models for Calorimeter Fast Simulation](https://arxiv.org/abs/2307.04780) — `generation`
- [Correcting Motion Distortion for LIDAR HD-Map Localization](https://arxiv.org/abs/2308.13694) — `localization`
- [Cross-BERT for Point Cloud Pretraining](https://arxiv.org/abs/2312.04891) — `pre-training`
- [Cross-source Point Cloud Registration: Challenges, Progress and Prospects](https://arxiv.org/abs/2305.13570) — `registration`
- [CSI: Enhancing the Robustness of 3D Point Cloud Recognition against Corruption](https://arxiv.org/abs/2310.03360) — `robustness`
- [D-Net: Learning for Distinctive Point Clouds by Self-Attentive Point Searching and Learnable Feature Fusion](https://arxiv.org/abs/2305.05842)
- [DBDNet:Partial-to-Partial Point Cloud Registration with Dual Branches Decoupling](https://arxiv.org/abs/2310.11733) — `registration`
- [Decoupled Local Aggregation for Point Cloud Learning](https://arxiv.org/abs/2308.16532)
- [Deep Learning-based 3D Point Cloud Classification: A Systematic Survey and Outlook](https://arxiv.org/abs/2311.02608) — `classification` `autonomous driving`
- [Deep Learning-based Compressed Domain Multimedia for Man and Machine: A Taxonomy and Application to Point Cloud Classification](https://arxiv.org/abs/2310.18849) — `classification` `compression`
- [Deep Semantic Graph Matching for Large-scale Outdoor Point Clouds Registration](https://arxiv.org/abs/2308.05314) — `registration`
- [DeepIPCv2: LiDAR-powered Robust Environmental Perception and Navigational Control for Autonomous Vehicle](https://arxiv.org/abs/2307.06647) — `segmentation` `autonomous driving` `robustness`
- [DeepPointMap: Advancing LiDAR SLAM with Unified Neural Descriptors](https://arxiv.org/abs/2312.02684) — `slam` `localization`
- [DeepTreeGANv2: Iterative Pooling of Point Clouds](https://arxiv.org/abs/2312.00042) — `generation`
- [Detection and Classification of Pole-like Landmarks for Domain-invariant 3D Point Cloud Map Matching](https://arxiv.org/abs/2305.06845) — `detection` `classification` `localization`
- [Diff-PCR: Diffusion-Based Correspondence Searching in Doubly Stochastic Matrix Space for Point Cloud Registration](https://arxiv.org/abs/2401.00436) — `registration`
- [Differentiable Registration of Images and LiDAR Point Clouds with VoxelPoint-to-Pixel Matching](https://arxiv.org/abs/2312.04060) — `registration` — [code](https://github.com/junshengzhou/VP2P-Match)
- [DiffPMAE: Diffusion Masked Autoencoders for Point Cloud Reconstruction](https://arxiv.org/abs/2312.03298) — `reconstruction` `compression`
- [DIPR: Efficient Point Cloud Registration via Dynamic Iteration](https://arxiv.org/abs/2312.02877) — `registration` `efficiency`
- [DMNR: Unsupervised De-noising of Point Clouds Corrupted by Airborne Particles](https://arxiv.org/abs/2305.05991) — `autonomous driving`
- [DPMix: Mixture of Depth and Point Cloud Video Experts for 4D Action Segmentation](https://arxiv.org/abs/2307.16803) — `segmentation`
- [DualGenerator: Information Interaction-based Generative Network for Point Cloud Completion](https://arxiv.org/abs/2305.09132) — `completion` `generation`
- [Dynamic Clustering Transformer Network for Point Cloud Segmentation](https://arxiv.org/abs/2306.08073) — `segmentation`
- [Edge Aware Learning for 3D Point Cloud](https://arxiv.org/abs/2309.13472) — `segmentation` `classification`
- [EdgeCalib: Multi-Frame Weighted Edge Features for Automatic Targetless LiDAR-Camera Calibration](https://arxiv.org/abs/2310.16629) — `multi-modal`
- [Efficient and Deterministic Search Strategy Based on Residual Projections for Point Cloud Registration with Correspondences](https://arxiv.org/abs/2305.11716) — `registration` `efficiency`
- [Efficient Real-time Smoke Filtration with 3D LiDAR for Search and Rescue with Autonomous Heterogeneous Robotic Systems](https://arxiv.org/abs/2308.07264) — `localization` `efficiency`
- [Ego-Motion Estimation and Dynamic Motion Separation from 3D Point Clouds for Accumulating Data and Improving 3D Object Detection](https://arxiv.org/abs/2308.15357) — `detection`
- [ELiOT : End-to-end Lidar Odometry using Transformer Framework](https://arxiv.org/abs/2307.11998) — `registration`
- [Empir3D : A Framework for Multi-Dimensional Point Cloud Assessment](https://arxiv.org/abs/2306.03660)
- [End-to-end 2D-3D Registration between Image and LiDAR Point Cloud for Vehicle Localization](https://arxiv.org/abs/2306.11346) — `registration` `localization` — [code](https://github.com/IRMVLab/I2PNet)
- [End-to-End 3D Object Detection using LiDAR Point Cloud](https://arxiv.org/abs/2312.15377) — `detection` `tracking`
- [Evaluating the point cloud of individual trees generated from images based on Neural Radiance fields (NeRF) method](https://arxiv.org/abs/2312.03372) — `reconstruction` `nerf`
- [Exact Point Cloud Downsampling for Fast and Accurate Global Trajectory Optimization](https://arxiv.org/abs/2307.02948) — `registration`
- [Explore In-Context Learning for 3D Point Cloud Understanding](https://arxiv.org/abs/2306.08659) — [code](https://github.com/fanglaosi/Point-In-Context)
- [ExpPoint-MAE: Better interpretability and performance for self-supervised point cloud transformers](https://arxiv.org/abs/2306.10798) — `self-supervised`
- [FAKEPCD: Fake Point Cloud Detection via Source Attribution](https://arxiv.org/abs/2312.11213) — `detection` `generation`
- [Fast and Accurate Deep Loop Closing and Relocalization for Reliable LiDAR SLAM](https://arxiv.org/abs/2309.08086) — `slam`
- [Fast Point Cloud to Mesh Reconstruction for Deformable Object Tracking](https://arxiv.org/abs/2311.02749) — `tracking` `reconstruction`
- [Fast Training of Diffusion Transformer with Extreme Masking for 3D Point Clouds Generation](https://arxiv.org/abs/2312.07231) — `generation`
- [Feature Adversarial Distillation for Point Cloud Classification](https://arxiv.org/abs/2306.14221) — `classification` `robustness`
- [FF-LINS: A Consistent Frame-to-Frame Solid-State-LiDAR-Inertial State Estimator](https://arxiv.org/abs/2307.06632)
- [FGFusion: Fine-Grained Lidar-Camera Fusion for 3D Object Detection](https://arxiv.org/abs/2309.11804) — `detection` `autonomous driving` `multi-modal` — [code](https://github.com/XavierGrool/FGFusion)
- [Fine-grained Text and Image Guided Point Cloud Completion with CLIP Model](https://arxiv.org/abs/2308.08754) — `completion`
- [FreePoint: Unsupervised Point Cloud Instance Segmentation](https://arxiv.org/abs/2305.06973) — `segmentation`
- [FrePolad: Frequency-Rectified Point Latent Diffusion for Point Cloud Generation](https://arxiv.org/abs/2311.12090) — `generation` `denoising`
- [FusionViT: Hierarchical 3D Object Detection via LiDAR-Camera Vision Transformer Fusion](https://arxiv.org/abs/2311.03620) — `detection` `multi-modal`
- [GAN-Based LiDAR Intensity Simulation](https://arxiv.org/abs/2311.15415) — `autonomous driving`
- [GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting](https://arxiv.org/abs/2311.14521) — `nerf` `gaussian-splatting` — [code](https://github.com/buaacyw/GaussianEditor)
- [Globally solving the Gromov-Wasserstein problem for point clouds in low dimensional Euclidean spaces](https://arxiv.org/abs/2307.09057)
- [Graph Structure from Point Clouds: Geometric Attention is All You Need](https://arxiv.org/abs/2307.16662)
- [GRJointNET: Synergistic Completion and Part Segmentation on 3D Incomplete Point Clouds](https://arxiv.org/abs/2311.13997) — `segmentation` `completion`
- [GTNet: Graph Transformer Network for 3D Point Cloud Classification and Semantic Segmentation](https://arxiv.org/abs/2305.15213) — `segmentation` `classification`
- [Hamiltonian Dynamics Learning from Point Cloud Observations for Nonholonomic Mobile Robot Control](https://arxiv.org/abs/2309.09163)
- [HD2Reg: Hierarchical Descriptors and Detectors for Point Cloud Registration](https://arxiv.org/abs/2305.03487) — `registration`
- [HDMNet: A Hierarchical Matching Network with Double Attention for Large-scale Outdoor LiDAR Point Cloud Registration](https://arxiv.org/abs/2310.18874) — `registration`
- [Hierarchical Adaptive Voxel-guided Sampling for Real-time Applications in Large-scale Point Clouds](https://arxiv.org/abs/2305.14306) — `efficiency`
- [High-Resolution Cranial Defect Reconstruction by Iterative, Low-Resolution, Point Cloud Completion Transformers](https://arxiv.org/abs/2308.03813) — `completion` `reconstruction` `anomaly detection`
- [HRHD-HK: A benchmark dataset of high-rise and high-density urban scenes for 3D semantic segmentation of photogrammetric point clouds](https://arxiv.org/abs/2307.07976) — `segmentation` `dataset` — Workshop
- [HumanReg: Self-supervised Non-rigid Registration of Human Point Cloud](https://arxiv.org/abs/2312.05462) — `registration` `self-supervised`
- [Hyperspherical Embedding for Point Cloud Completion](https://arxiv.org/abs/2307.05634) — `completion`
- [Improved Multi-Scale Grid Rendering of Point Clouds for Radar Object Detection Networks](https://arxiv.org/abs/2305.15836) — `detection` `multi-modal`
- [Improving LiDAR 3D Object Detection via Range-based Point Cloud Density Optimization](https://arxiv.org/abs/2306.05663) — `detection`
- [Improving Neural Radiance Field using Near-Surface Sampling with Point Cloud Generation](https://arxiv.org/abs/2310.04152) — `generation` `nerf`
- [Improving Video Violence Recognition with Human Interaction Learning on 3D Skeleton Point Clouds](https://arxiv.org/abs/2308.13866)
- [Influence of Camera-LiDAR Configuration on 3D Object Detection for Autonomous Driving](https://arxiv.org/abs/2310.05245) — `detection` `autonomous driving` `multi-modal`
- [InstaLoc: One-shot Global Lidar Localisation in Indoor Environments through Instance Learning](https://arxiv.org/abs/2305.09552) — `localization`
- [InstructP2P: Learning to Edit 3D Point Clouds with Text Instructions](https://arxiv.org/abs/2306.07154) — `generation`
- [Intrinsic Image Decomposition Using Point Cloud Representation](https://arxiv.org/abs/2307.10924) — [code](https://github.com/xyxingx/PoInt-Net)
- [Invariant Training 2D-3D Joint Hard Samples for Few-Shot Point Cloud Recognition](https://arxiv.org/abs/2308.09694)
- [iPUNet:Iterative Cross Field Guided Point Cloud Upsampling](https://arxiv.org/abs/2310.09092) — `upsampling`
- [Joint Intrinsic and Extrinsic LiDAR-Camera Calibration in Targetless Environments Using Plane-Constrained Bundle Adjustment](https://arxiv.org/abs/2308.12629) — `registration` `multi-modal`
- [Joint Learning for Scattered Point Cloud Understanding with Hierarchical Self-Distillation](https://arxiv.org/abs/2312.16902)
- [KDD-LOAM: Jointly Learned Keypoint Detector and Descriptors Assisted LiDAR Odometry and Mapping](https://arxiv.org/abs/2309.15394) — `registration` `detection`
- [LabelFormer: Object Trajectory Refinement for Offboard Perception from LiDAR Point Clouds](https://arxiv.org/abs/2311.01444) — `autonomous driving`
- [Language-Conditioned Affordance-Pose Detection in 3D Point Clouds](https://arxiv.org/abs/2309.10911) — `detection`
- [Language-Guided 3D Object Detection in Point Cloud for Autonomous Driving](https://arxiv.org/abs/2305.15765) — `detection` `autonomous driving`
- [Learned Gridification for Efficient Point Cloud Processing](https://arxiv.org/abs/2307.14354) — `efficiency`
- [Learned Nonlinear Predictor for Critically Sampled 3D Point Cloud Attribute Compression](https://arxiv.org/abs/2311.13539) — `compression`
- [Learned Point Cloud Compression for Classification](https://arxiv.org/abs/2308.05959) — `segmentation` `detection` `classification` `compression`
- [Learning Dynamic Point Cloud Compression via Hierarchical Inter-frame Block Matching](https://arxiv.org/abs/2305.05356) — `compression`
- [Learning Signed Distance Functions from Noisy 3D Point Clouds via Noise to Noise Mapping](https://arxiv.org/abs/2306.01405) — [code](https://github.com/mabaorui/Noise2NoiseMapping)
- [Learning to Adapt SAM for Segmenting Cross-domain Point Clouds](https://arxiv.org/abs/2310.08820) — `segmentation`
- [Learning-Based Biharmonic Augmentation for Point Cloud Classification](https://arxiv.org/abs/2311.06070) — `classification`
- [LEF: Late-to-Early Temporal Fusion for LiDAR 3D Object Detection](https://arxiv.org/abs/2309.16870) — `detection`
- [LEGO: Learning and Graph-Optimized Modular Tracker for Online Multi-Object Tracking with Point Clouds](https://arxiv.org/abs/2308.09908) — `detection` `tracking`
- [LEST: Large-scale LiDAR Semantic Segmentation with Transformer](https://arxiv.org/abs/2307.09367) — `segmentation` `autonomous driving`
- [Leveraging Large-Scale Pretrained Vision Foundation Models for Label-Efficient 3D Point Cloud Segmentation](https://arxiv.org/abs/2311.01989) — `segmentation` `open-vocabulary` `pre-training` `efficiency`
- [LiCamPose: Combining Multi-View LiDAR and RGB Cameras for Robust Single-timestamp 3D Human Pose Estimation](https://arxiv.org/abs/2312.06409) — `robustness`
- [Lidar Annotation Is All You Need](https://arxiv.org/abs/2311.04777) — `segmentation` `autonomous driving`
- [LiDAR View Synthesis for Robust Vehicle Navigation Without Expert Labels](https://arxiv.org/abs/2308.01424) — `autonomous driving` `robustness`
- [LiDAR-based curb detection for ground truth annotation in automated driving validation](https://arxiv.org/abs/2312.00534) — `detection`
- [LiDAR-based Outdoor Crowd Management for Smart Campus on the Edge](https://arxiv.org/abs/2311.18077) — `detection`
- [LiDAR-based Person Re-identification](https://arxiv.org/abs/2312.03033)
- [LiDAR-BEVMTN: Real-Time LiDAR Bird's-Eye View Multi-Task Perception Network for Autonomous Driving](https://arxiv.org/abs/2307.08850) — `segmentation` `detection` `autonomous driving` `efficiency`
- [LiDAR-Generated Images Derived Keypoints Assisted Point Cloud Registration Scheme in Odometry Estimation](https://arxiv.org/abs/2309.10436) — `registration` `detection` `slam` `localization`
- [LiDAR-HMR: 3D Human Mesh Recovery from LiDAR](https://arxiv.org/abs/2311.11971) — [code](https://github.com/soullessrobot/LiDAR-HMR)
- [LieDetect: Detection of representation orbits of compact Lie groups from point clouds](https://arxiv.org/abs/2309.03086) — `detection` `reconstruction`
- [Light-LOAM: A Lightweight LiDAR Odometry and Mapping based on Graph-Matching](https://arxiv.org/abs/2310.04162) — `slam` `localization` `efficiency`
- [Lightweight super resolution network for point cloud geometry compression](https://arxiv.org/abs/2311.00970) — `reconstruction` `compression` `upsampling` `efficiency`
- [LiLO: Lightweight and low-bias LiDAR Odometry method based on spherical range image filtering](https://arxiv.org/abs/2311.07291) — `efficiency`
- [LISNeRF Mapping: LiDAR-based Implicit Mapping via Semantic Neural Fields for Large-Scale 3D Scenes](https://arxiv.org/abs/2311.02313) — `reconstruction`
- [Living in a Material World: Learning Material Properties from Full-Waveform Flash Lidar Data for Semantic Segmentation](https://arxiv.org/abs/2305.04334) — `segmentation`
- [LMD: Light-weight Prediction Quality Estimation for Object Detection in Lidar Point Clouds](https://arxiv.org/abs/2306.07835) — `detection` `autonomous driving` `efficiency`
- [Low Latency Instance Segmentation by Continuous Clustering for LiDAR Sensors](https://arxiv.org/abs/2311.13976) — `segmentation`
- [Low-Resource White-Box Semantic Segmentation of Supporting Towers on 3D Point Clouds via Signature Shape Identification](https://arxiv.org/abs/2306.07809) — `segmentation`
- [LXL: LiDAR Excluded Lean 3D Object Detection with 4D Imaging Radar and Camera Fusion](https://arxiv.org/abs/2307.00724) — `detection` `autonomous driving` `multi-modal`
- [Marking anything: application of point cloud in extracting video target features](https://arxiv.org/abs/2306.07559)
- [MaskBEV: Joint Object Detection and Footprint Completion for Bird's-eye View 3D Point Clouds](https://arxiv.org/abs/2307.01864) — `detection` `completion` `BEV`
- [Mesh-LOAM: Real-time Mesh-Based LiDAR Odometry and Mapping](https://arxiv.org/abs/2312.15630) — `reconstruction` `efficiency`
- [Modeling 3D cardiac contraction and relaxation with point cloud deformation networks](https://arxiv.org/abs/2307.10927)
- [MotionBEV: Attention-Aware Online LiDAR Moving Object Segmentation with Bird's Eye View based Appearance and Motion Features](https://arxiv.org/abs/2305.07336) — `segmentation` `BEV`
- [MOVIN: Real-time Motion Capture using a Single LiDAR](https://arxiv.org/abs/2309.09314) — `tracking` `efficiency`
- [Multi-class point cloud completion networks for 3D cardiac anatomy reconstruction from cine magnetic resonance images](https://arxiv.org/abs/2307.08535) — `completion` `reconstruction`
- [Multi-objective point cloud autoencoders for explainable myocardial infarction prediction](https://arxiv.org/abs/2307.11017)
- [Multi-Session, Localization-oriented and Lightweight LiDAR Mapping Using Semantic Lines and Planes](https://arxiv.org/abs/2307.07126) — `localization` `efficiency`
- [MUN-FRL: A Visual Inertial LiDAR Dataset for Aerial Autonomous Navigation and Mapping](https://arxiv.org/abs/2310.08435) — `dataset`
- [MV-DeepSDF: Implicit Modeling with Multi-Sweep Point Clouds for 3D Vehicle Reconstruction in Autonomous Driving](https://arxiv.org/abs/2309.16715) — `reconstruction` `autonomous driving`
- [NDT-Map-Code: A 3D global descriptor for real-time loop closure detection in lidar SLAM](https://arxiv.org/abs/2307.08221) — `detection` `slam` `localization` `efficiency`
- [Neural FIM for learning Fisher Information Metrics from point cloud data](https://arxiv.org/abs/2306.06062)
- [Neural Poisson Surface Reconstruction: Resolution-Agnostic Shape Reconstruction from Point Clouds](https://arxiv.org/abs/2308.01766) — `reconstruction`
- [Neural-Singular-Hessian: Implicit Neural Representation of Unoriented Point Clouds by Enforcing Singular Hessian](https://arxiv.org/abs/2309.01793) — `reconstruction`
- [NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance](https://arxiv.org/abs/2312.00846) — `reconstruction` `gaussian-splatting`
- [No-Reference Point Cloud Quality Assessment via Weighted Patch Quality Prediction](https://arxiv.org/abs/2305.07829)
- [NSM4D: Neural Scene Model Based Online 4D Point Cloud Sequence Understanding](https://arxiv.org/abs/2310.08326) — `autonomous driving`
- [OAAFormer: Robust and Efficient Point Cloud Registration Through Overlapping-Aware Attention in Transformer](https://arxiv.org/abs/2310.09817) — `registration` `robustness` `efficiency`
- [Object Re-Identification from Point Clouds](https://arxiv.org/abs/2305.10210) — `tracking` `autonomous driving`
- [OccNeRF: Advancing 3D Occupancy Prediction in LiDAR-Free Environments](https://arxiv.org/abs/2312.09243) — `autonomous driving` `occupancy prediction` — [code](https://github.com/LinShan-Bin/OccNeRF)
- [On the Efficacy of 3D Point Cloud Reinforcement Learning](https://arxiv.org/abs/2306.06799)
- [Once-Training-All-Fine: No-Reference Point Cloud Quality Assessment via Domain-relevance Degradation Description](https://arxiv.org/abs/2307.01567)
- [One-Nearest Neighborhood Guides Inlier Estimation for Unsupervised Point Cloud Registration](https://arxiv.org/abs/2307.14019) — `registration` `self-supervised`
- [OneFormer3D: One Transformer for Unified Point Cloud Segmentation](https://arxiv.org/abs/2311.14405) — `segmentation`
- [Optimizing Implicit Neural Representations from Point Clouds via Energy-Based Models](https://arxiv.org/abs/2311.02601) — `reconstruction`
- [Optimizing the Placement of Roadside LiDARs for Autonomous Driving](https://arxiv.org/abs/2310.07247) — `autonomous driving`
- [Overlap Bias Matching is Necessary for Point Cloud Registration](https://arxiv.org/abs/2308.09364) — `registration`
- [P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds](https://arxiv.org/abs/2310.02638) — `reconstruction`
- [P2M2-Net: Part-Aware Prompt-Guided Multimodal Point Cloud Completion](https://arxiv.org/abs/2312.17611) — `completion` `generation` `multi-modal`
- [PANet: LiDAR Panoptic Segmentation with Sparse Instance Proposal and Aggregation](https://arxiv.org/abs/2306.15348) — `segmentation` `autonomous driving`
- [Partial Symmetry Detection for 3D Geometry using Contrastive Learning with Geodesic Point Cloud Patches](https://arxiv.org/abs/2312.08230) — `detection` `completion` `generation` `self-supervised`
- [Partial Transport for Point-Cloud Registration](https://arxiv.org/abs/2309.15787) — `registration`
- [Patch-Wise Point Cloud Generation: A Divide-and-Conquer Approach](https://arxiv.org/abs/2307.12049) — `generation` `autonomous driving`
- [PatchMixer: Rethinking network design to boost generalization for 3D point cloud understanding](https://arxiv.org/abs/2307.15692)
- [PBWR: Parametric Building Wireframe Reconstruction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2311.12062) — `reconstruction`
- [PCRDiffusion: Diffusion Probabilistic Models for Point Cloud Registration](https://arxiv.org/abs/2312.06063) — `registration` `denoising`
- [pCTFusion: Point Convolution-Transformer Fusion with Semantic Aware Loss for Outdoor LiDAR Point Cloud Segmentation](https://arxiv.org/abs/2307.14777) — `segmentation`
- [PeP: a Point enhanced Painting method for unified point cloud tasks](https://arxiv.org/abs/2310.07591)
- [Point Cloud Completion Guided by Prior Knowledge via Causal Inference](https://arxiv.org/abs/2305.17770) — `completion`
- [Point Cloud Denoising and Outlier Detection with Local Geometric Structure by Dynamic Graph CNN](https://arxiv.org/abs/2310.07376) — `detection` `denoising`
- [Point Cloud Network: An Order of Magnitude Improvement in Linear Layer Parameter Count](https://arxiv.org/abs/2309.12996)
- [Point Cloud Pre-training with Diffusion Models](https://arxiv.org/abs/2311.14960) — `pre-training`
- [Point Cloud Segmentation Using Transfer Learning with RandLA-Net: A Case Study on Urban Areas](https://arxiv.org/abs/2312.11880) — `segmentation`
- [Point Cloud Semantic Segmentation with Sparse and Inhomogeneous Annotations](https://arxiv.org/abs/2312.06259) — `segmentation`
- [Point Cloud Video Anomaly Detection Based on Point Spatio-Temporal Auto-Encoder](https://arxiv.org/abs/2306.04466) — `detection` `anomaly detection`
- [Point Clouds Are Specialized Images: A Knowledge Transfer Approach for 3D Understanding](https://arxiv.org/abs/2307.15569) — `self-supervised`
- [Point Deformable Network with Enhanced Normal Embedding for Point Cloud Analysis](https://arxiv.org/abs/2312.13071)
- [Point-Bind & Point-LLM: Aligning Point Cloud with Multi-modality for 3D Understanding, Generation, and Instruction Following](https://arxiv.org/abs/2309.00615) — `generation` `vision-language` — [code](https://github.com/ZiyuGuo99/Point-Bind_Point-LLM)
- [Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds](https://arxiv.org/abs/2312.04962) — `segmentation` `reconstruction`
- [PointeNet: A Lightweight Framework for Effective and Efficient Point Cloud Analysis](https://arxiv.org/abs/2312.12743) — `efficiency`
- [PointGPT: Auto-regressively Generative Pre-training from Point Clouds](https://arxiv.org/abs/2305.11487) — `generation` `pre-training`
- [PointHPS: Cascaded 3D Human Pose and Shape Estimation from Point Clouds](https://arxiv.org/abs/2308.14492)
- [PointHR: Exploring High-Resolution Architectures for 3D Point Cloud Segmentation](https://arxiv.org/abs/2310.07743) — `segmentation` — [code](https://github.com/haibo-qiu/PointHR)
- [PointJEM: Self-supervised Point Cloud Understanding for Reducing Feature Redundancy via Joint Entropy Maximization](https://arxiv.org/abs/2312.03339) — `self-supervised`
- [PointMoment:Mixed-Moment-based Self-Supervised Representation Learning for 3D Point Clouds](https://arxiv.org/abs/2312.03350) — `self-supervised`
- [Points for Energy Renovation (PointER): A LiDAR-Derived Point Cloud Dataset of One Million English Buildings Linked to Energy Characteristics](https://arxiv.org/abs/2306.16020) — `dataset` — [code](https://github.com/kdmayer/PointER)
- [PointSSC: A Cooperative Vehicle-Infrastructure Point Cloud Benchmark for Semantic Scene Completion](https://arxiv.org/abs/2309.12708) — `completion` `occupancy prediction` `dataset`
- [PolarNet: 3D Point Clouds for Language-Guided Robotic Manipulation](https://arxiv.org/abs/2309.15596)
- [Polyhedral Surface: Self-supervised Point Cloud Reconstruction Based on Polyhedral Surface](https://arxiv.org/abs/2310.14560) — `reconstruction` `self-supervised`
- [Poster: Making Edge-assisted LiDAR Perceptions Robust to Lossy Point Cloud Compression](https://arxiv.org/abs/2309.04549) — `detection` `localization` `compression` `robustness`
- [PotholeGuard: A Pothole Detection Approach by Point Cloud Semantic Segmentation](https://arxiv.org/abs/2311.02641) — `segmentation` `detection`
- [PRED: Pre-training via Semantic Rendering on LiDAR Point Clouds](https://arxiv.org/abs/2311.04501) — `autonomous driving` `pre-training`
- [PSGformer: Enhancing 3D Point Cloud Instance Segmentation via Precise Semantic Guidance](https://arxiv.org/abs/2307.07708) — `segmentation`
- [PU-Ray: Domain-Independent Point Cloud Upsampling via Ray Marching on Neural Implicit Surface](https://arxiv.org/abs/2310.08755) — `upsampling`
- [PV-SSD: A Multi-Modal Point Cloud Feature Fusion Method for Projection Features and Variable Receptive Field Voxel Features](https://arxiv.org/abs/2308.06791) — `detection` `classification` `autonomous driving` `multi-modal`
- [Pyramid Semantic Graph-based Global Point Cloud Registration with Low Overlap](https://arxiv.org/abs/2307.12116) — `registration`
- [Q-REG: End-to-End Trainable Point Cloud Registration with Surface Curvature](https://arxiv.org/abs/2309.16023) — `registration`
- [Quantity-Aware Coarse-to-Fine Correspondence for Image-to-Point Cloud Registration](https://arxiv.org/abs/2307.07142) — `registration`
- [Quatro++: Robust Global Registration Exploiting Ground Segmentation for Loop Closing in LiDAR SLAM](https://arxiv.org/abs/2311.00928) — `registration` `segmentation` `slam` `robustness`
- [Radar Instance Transformer: Reliable Moving Instance Segmentation in Sparse Radar Point Clouds](https://arxiv.org/abs/2309.16435) — `segmentation` `multi-modal`
- [Real3D-AD: A Dataset of Point Cloud Anomaly Detection](https://arxiv.org/abs/2309.13226) — `detection` `anomaly detection` `dataset`
- [Realistic Rainy Weather Simulation for LiDARs in CARLA Simulator](https://arxiv.org/abs/2312.12772)
- [RecolorCloud: A Point Cloud Tool for Recoloring, Segmentation, and Conversion](https://arxiv.org/abs/2310.12470) — `segmentation`
- [Regress Before Construct: Regress Autoencoder for Point Cloud Self-supervised Learning](https://arxiv.org/abs/2310.03670) — `self-supervised`
- [Reinforcement Learning-Driven Linker Design via Fast Attention-based Point Cloud Alignment](https://arxiv.org/abs/2306.08166) — `registration`
- [Relightable 3D Gaussians: Realistic Point Cloud Relighting with BRDF Decomposition and Ray Tracing](https://arxiv.org/abs/2311.16043)
- [Revisiting Poisson-disk Subsampling for Massive Point Cloud Decimation](https://arxiv.org/abs/2311.17604)
- [Risk-optimized Outlier Removal for Robust 3D Point Cloud Classification](https://arxiv.org/abs/2307.10875) — `classification` `robustness`
- [Roadside LiDAR Assisted Cooperative Localization for Connected Autonomous Vehicles](https://arxiv.org/abs/2311.07913) — `registration` `localization`
- [Robust Estimation of Surface Curvature Information from Point Cloud Data](https://arxiv.org/abs/2306.00299) — `normal estimation` `robustness`
- [Robust Lifelong Indoor LiDAR Localization using the Area Graph](https://arxiv.org/abs/2308.05593) — `localization` `robustness`
- [Robust Point Cloud Processing through Positional Embedding](https://arxiv.org/abs/2309.00339) — `detection` `robustness`
- [Robust-DefReg: A Robust Deformable Point Cloud Registration Method based on Graph Convolutional Neural Networks](https://arxiv.org/abs/2306.04701) — `registration` `robustness`
- [Robustifying Point Cloud Networks by Refocusing](https://arxiv.org/abs/2308.05525)
- [Rotation-Invariant Random Features Provide a Strong Baseline for Machine Learning on 3D Point Clouds](https://arxiv.org/abs/2308.06271) — `classification`
- [SCA-PVNet: Self-and-Cross Attention Based Aggregation of Point Cloud and Multi-View for 3D Object Retrieval](https://arxiv.org/abs/2307.10601)
- [SCP: Spherical-Coordinate-based Learned Point Cloud Compression](https://arxiv.org/abs/2308.12535) — `compression`
- [SE-LIO: Semantics-enhanced Solid-State-LiDAR-Inertial Odometry for Tree-rich Environments](https://arxiv.org/abs/2312.01809) — `segmentation`
- [Segmentation of Drone Collision Hazards in Airborne RADAR Point Clouds Using PointNet](https://arxiv.org/abs/2311.03221) — `segmentation` `multi-modal`
- [Select-and-Combine (SAC): A Novel Multi-Stereo Depth Fusion Algorithm for Point Cloud Generation via Efficient Local Markov Netlets](https://arxiv.org/abs/2308.12138) — `generation` `reconstruction` `efficiency`
- [Self-supervised adversarial masking for 3D point cloud representation learning](https://arxiv.org/abs/2307.05325) — `self-supervised` `robustness`
- [Self-Supervised Learning for Point Clouds Data: A Survey](https://arxiv.org/abs/2305.11881) — `detection` `localization` `self-supervised`
- [Self-supervised Learning for Pre-Training 3D Point Clouds: A Survey](https://arxiv.org/abs/2305.04691) — `self-supervised` `autonomous driving` `pre-training`
- [Self-Supervised Pre-Training Boosts Semantic Scene Segmentation on LiDAR Data](https://arxiv.org/abs/2309.02139) — `segmentation` `self-supervised` `pre-training`
- [SelFLoc: Selective Feature Fusion for Large-scale Point Cloud-based Place Recognition](https://arxiv.org/abs/2306.01205) — `localization`
- [Semantic Segmentation of Radar Detections using Convolutions on Point Clouds](https://arxiv.org/abs/2305.12775) — `segmentation` `detection` `autonomous driving` `multi-modal`
- [Semantic Segmentation on 3D Point Clouds with High Density Variations](https://arxiv.org/abs/2307.01489) — `segmentation` `upsampling`
- [Semantics-aware LiDAR-Only Pseudo Point Cloud Generation for 3D Object Detection](https://arxiv.org/abs/2309.08932) — `detection` `generation`
- [SG-GAN: Fine Stereoscopic-Aware Generation for 3D Brain Point Cloud Up-sampling from a Single Image](https://arxiv.org/abs/2305.12646) — `generation` `reconstruction`
- [SGNet: Salient Geometric Network for Point Cloud Registration](https://arxiv.org/abs/2309.06207) — `registration`
- [SHARP Challenge 2023: Solving CAD History and pArameters Recovery from Point clouds and 3D scans. Overview, Datasets, Metrics, and Baselines](https://arxiv.org/abs/2308.15966)
- [Simple Baselines for Projection-based Full-reference and No-reference Point Cloud Quality Assessment](https://arxiv.org/abs/2310.17147) — `compression`
- [Smooth, exact rotational symmetrization for deep learning on point clouds](https://arxiv.org/abs/2305.19302)
- [SMRVIS: Point cloud extraction from 3-D ultrasound for non-destructive testing](https://arxiv.org/abs/2306.04668) — `segmentation`
- [SphereNet: Learning a Noise-Robust and General Descriptor for Point Cloud Registration](https://arxiv.org/abs/2307.09351) — `registration` `robustness`
- [Spherical Mask: Coarse-to-Fine 3D Point Cloud Instance Segmentation with Spherical Representation](https://arxiv.org/abs/2312.11269) — `segmentation`
- [SSC3OD: Sparsely Supervised Collaborative 3D Object Detection from LiDAR Point Clouds](https://arxiv.org/abs/2307.00717) — `detection` `autonomous driving`
- [SSFlowNet: Semi-supervised Scene Flow Estimation On Point Clouds With Pseudo Label](https://arxiv.org/abs/2312.15271) — `scene flow`
- [Subjective Quality Evaluation of Point Clouds Using a Head Mounted Display](https://arxiv.org/abs/2310.19179)
- [Synergizing Contrastive Learning and Optimal Transport for 3D Point Cloud Domain Adaptation](https://arxiv.org/abs/2308.14126) — `self-supervised` `domain adaptation`
- [Target-free Extrinsic Calibration of Event-LiDAR Dyad using Edge Correspondences](https://arxiv.org/abs/2305.04017) — `autonomous driving`
- [Task-Oriented Grasping with Point Cloud Representation of Objects](https://arxiv.org/abs/2309.11689)
- [Template-free Articulated Neural Point Clouds for Reposable View Synthesis](https://arxiv.org/abs/2305.19065) — `reconstruction` `nerf`
- [Tensorformer: Normalized Matrix Attention Transformer for High-quality Point Cloud Reconstruction](https://arxiv.org/abs/2306.15989) — `reconstruction`
- [TimePillars: Temporally-Recurrent 3D LiDAR Object Detection](https://arxiv.org/abs/2312.17260) — `detection` `autonomous driving`
- [Tinto: Multisensor Benchmark for 3D Hyperspectral Point Cloud Segmentation in the Geosciences](https://arxiv.org/abs/2305.09928) — `segmentation` `dataset`
- [Towards accurate instance segmentation in large-scale LiDAR point clouds](https://arxiv.org/abs/2307.02877) — `segmentation`
- [TractCloud: Registration-free tractography parcellation with a novel local-global streamline point cloud representation](https://arxiv.org/abs/2307.09000) — `registration`
- [Transcending Grids: Point Clouds and Surface Representations Powering Neurological Processing](https://arxiv.org/abs/2305.15426)
- [Transferring CLIP's Knowledge into Zero-Shot Point Cloud Semantic Segmentation](https://arxiv.org/abs/2312.07221) — `segmentation` `open-vocabulary`
- [Transformation Decoupling Strategy based on Screw Theory for Deterministic Point Cloud Registration with Gravity Prior](https://arxiv.org/abs/2311.01432) — `registration`
- [TreeLearn: A deep learning method for segmenting individual trees from ground-based LiDAR forest point clouds](https://arxiv.org/abs/2309.08471) — `segmentation`
- [TTPOINT: A Tensorized Point Cloud Network for Lightweight Action Recognition with Event Cameras](https://arxiv.org/abs/2308.09993) — `efficiency`
- [UNeR3D: Versatile and Scalable 3D RGB Point Cloud Generation from 2D Images in Unsupervised Reconstruction](https://arxiv.org/abs/2312.06706) — `generation` `reconstruction`
- [Unleash the Potential of 3D Point Cloud Modeling with A Calibrated Local Geometry-driven Distance Metric](https://arxiv.org/abs/2306.00552)
- [Unsupervised Change Detection for Space Habitats Using 3D Point Clouds](https://arxiv.org/abs/2312.02396) — `detection` — [code](https://github.com/nasa/isaac)
- [Using Lidar Intensity for Robot Navigation](https://arxiv.org/abs/2309.07014)
- [Variational Autoencoding of Dental Point Clouds](https://arxiv.org/abs/2307.10895)
- [VET: Visual Error Tomography for Point Cloud Completion and High-Quality Neural Rendering](https://arxiv.org/abs/2311.04634) — `completion`
- [Visual Point Cloud Forecasting enables Scalable Autonomous Driving](https://arxiv.org/abs/2312.17655) — `autonomous driving`
- [VNI-Net: Vector Neurons-based Rotation-Invariant Descriptor for LiDAR Place Recognition](https://arxiv.org/abs/2308.12870) — `slam` `localization`
- [VTPNet for 3D deep learning on point cloud](https://arxiv.org/abs/2305.06115)
- [Weakly Supervised Point Cloud Segmentation via Conservative Propagation of Scene-level Labels](https://arxiv.org/abs/2312.06799) — `segmentation`
- [Weakly Supervised Point Clouds Transformer for 3D Object Detection](https://arxiv.org/abs/2309.04105) — `segmentation` `detection`
- [Weighted Point Cloud Normal Estimation](https://arxiv.org/abs/2305.04007) — `normal estimation`
- [When 3D Bounding-Box Meets SAM: Point Cloud Instance Segmentation with Weak-and-Noisy Supervision](https://arxiv.org/abs/2309.00828) — `segmentation`
- [X4D-SceneFormer: Enhanced Scene Understanding on 4D Point Cloud Videos through Cross-modal Knowledge Transfer](https://arxiv.org/abs/2312.07378)
- [ZeroReg: Zero-Shot Point Cloud Registration with Foundation Models](https://arxiv.org/abs/2312.03032) — `registration` `open-vocabulary`

</details>


### 2022 <sub>(565)</sub>

<details><summary><b>CVPR</b> · 52</summary>

- [3D-SPS: Single-Stage 3D Visual Grounding via Referred Point Progressive Selection](https://arxiv.org/abs/2204.06272) — `detection`
- [3D-VField: Adversarial Augmentation of Point Clouds for Domain Generalization in 3D Object Detection](https://arxiv.org/abs/2112.04764) — `detection` `robustness`
- [3DeformRS: Certifying Spatial Deformations on Point Clouds](https://arxiv.org/abs/2204.05687) — `autonomous driving`
- [AziNorm: Exploiting the Radial Symmetry of Point Cloud for Azimuth-Normalized 3D Perception](https://arxiv.org/abs/2203.13090)
- [Boosting 3D Object Detection by Simulating Multimodality on Point Clouds](https://arxiv.org/abs/2206.14971) — `detection`
- [Bridged Transformer for Vision and Point Cloud 3D Object Detection](https://arxiv.org/abs/2210.01391) — `detection`
- [CAT-Det: Contrastively Augmented Transformer for Multi-modal 3D Object Detection](https://arxiv.org/abs/2204.00325) — `detection` `autonomous driving` `multi-modal`
- [Critical Regularizations for Neural Surface Reconstruction in the Wild](https://arxiv.org/abs/2206.03087) — `reconstruction`
- [Deformation and Correspondence Aware Unsupervised Synthetic-to-Real Scene Flow Estimation for Point Clouds](https://arxiv.org/abs/2203.16895) — `scene flow` `autonomous driving`
- [Density-preserving Deep Point Cloud Compression](https://arxiv.org/abs/2204.12684) — `compression`
- [Equivariant Point Cloud Analysis via Learning Orientations for Message Passing](https://arxiv.org/abs/2203.14486)
- [Fast Point Transformer](https://arxiv.org/abs/2112.04702)
- [Focal Sparse Convolutional Networks for 3D Object Detection](https://arxiv.org/abs/2204.12463) — `detection` — [code](http://github.com/dvlab-research/FocalsConv)
- [GeoTransformer: Fast and Robust Point Cloud Registration with Geometric Transformer](https://arxiv.org/abs/2308.03768) — `registration` `detection` `robustness`
- [IDEA-Net: Dynamic 3D Point Cloud Interpolation via Deep Embedding Alignment](https://arxiv.org/abs/2203.11590)
- [Image-to-Lidar Self-Supervised Distillation for Autonomous Driving Data](https://arxiv.org/abs/2203.16258) — `segmentation` `detection` `self-supervised` `autonomous driving`
- [Investigating the Impact of Multi-LiDAR Placement on Object Detection for Autonomous Driving](https://arxiv.org/abs/2105.00373) — `detection` `autonomous driving`
- [Learning a Structured Latent Space for Unsupervised Point Cloud Completion](https://arxiv.org/abs/2203.15580) — `completion`
- [Learning Local Displacements for Point Cloud Completion](https://arxiv.org/abs/2203.16600) — `completion`
- [Learning Multi-View Aggregation In the Wild for Large-Scale 3D Semantic Segmentation](https://arxiv.org/abs/2204.07548) — `segmentation` — [code](https://github.com/drprojects/DeepViewAgg)
- [LiDAR Snowfall Simulation for Robust 3D Object Detection](https://arxiv.org/abs/2203.15118) — `detection` `autonomous driving` `robustness`
- [Multi-View Transformer for 3D Visual Grounding](https://arxiv.org/abs/2204.02174)
- [Neural Points: Point Cloud Representation with Neural Fields for Arbitrary Upsampling](https://arxiv.org/abs/2112.04148) — `upsampling`
- [No Pain, Big Gain: Classify Dynamic Point Cloud Sequences with Static Models by Fitting Feature-level Space-time Surfaces](https://arxiv.org/abs/2203.11113) — `classification` `tracking` `scene flow` — [code](https://github.com/jx-zhong-for-academic-purpose/Kinet)
- [Not All Points Are Equal: Learning Highly Efficient Point-based Detectors for 3D LiDAR Point Clouds](https://arxiv.org/abs/2203.11139) — `detection` `efficiency` — [code](https://github.com/yifanzhang713/IA-SSD)
- [NPBG++: Accelerating Neural Point-Based Graphics](https://arxiv.org/abs/2203.13318)
- [OccAM's Laser: Occlusion-based Attribution Maps for 3D Object Detectors on LiDAR Data](https://arxiv.org/abs/2204.06577) — `detection` — [code](https://github.com/dschinagl/occam)
- [Point Cloud Color Constancy](https://arxiv.org/abs/2111.11280)
- [Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling](https://arxiv.org/abs/2111.14819) — `pre-training`
- [Point-to-Voxel Knowledge Distillation for LiDAR Semantic Segmentation](https://arxiv.org/abs/2206.02099) — `segmentation` — [code](https://github.com/cardwing/Codes-for-PVKD)
- [Point2Cyl: Reverse Engineering 3D Objects from Point Clouds to Extrusion Cylinders](https://arxiv.org/abs/2112.09329)
- [Point2Seq: Detecting 3D Objects as Sequences](https://arxiv.org/abs/2203.13394) — `detection`
- [RCP: Recurrent Closest Point for Scene Flow Estimation on 3D Point Clouds](https://arxiv.org/abs/2205.11028) — `registration` `scene flow`
- [Reconstructing Surfaces for Sparse Point Clouds with On-Surface Priors](https://arxiv.org/abs/2204.10603) — `reconstruction`
- [REGTR: End-to-end Point Cloud Correspondences with Transformers](https://arxiv.org/abs/2203.14517) — `registration`
- [Revealing Occlusions with 4D Neural Fields](https://arxiv.org/abs/2204.10916) — `monocular`
- [RIDDLE: Lidar Data Compression with Range Image Deep Delta Encoding](https://arxiv.org/abs/2206.01738) — `compression` `autonomous driving`
- [SAR-Net: Shape Alignment and Recovery Network for Category-level 6D Object Pose and Size Estimation](https://arxiv.org/abs/2106.14193)
- [SC^2-PCR: A Second Order Spatial Compatibility for Efficient and Robust Point Cloud Registration](https://arxiv.org/abs/2203.14453) — `registration` `robustness` `efficiency`
- [Self-Supervised 3D Scene Flow Estimation and Motion Prediction using Local Rigidity Prior](https://arxiv.org/abs/2310.11284) — `self-supervised` `scene flow`
- [SemAffiNet: Semantic-Affine Transformation for Point Cloud Segmentation](https://arxiv.org/abs/2205.13490) — `segmentation`
- [Sparse Fuse Dense: Towards High Quality 3D Detection with Depth Completion](https://arxiv.org/abs/2203.09780) — `detection` `completion`
- [Stratified Transformer for 3D Point Cloud Segmentation](https://arxiv.org/abs/2203.14508) — `segmentation` — [code](https://github.com/dvlab-research/Stratified-Transformer)
- [Surface Reconstruction from Point Clouds by Learning Predictive Context Priors](https://arxiv.org/abs/2204.11015) — `reconstruction`
- [Surface Representation for Point Clouds](https://arxiv.org/abs/2205.05740) — [code](https://github.com/hancyran/RepSurf)
- [TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers](https://arxiv.org/abs/2203.11496) — `detection` `autonomous driving` `multi-modal` `robustness` — [code](https://github.com/XuyangBai/TransFusion)
- [Uni6D: A Unified CNN Framework without Projection Breakdown for 6D Pose Estimation](https://arxiv.org/abs/2203.14531)
- [UNIST: Unpaired Neural Implicit Shape Translation Network](https://arxiv.org/abs/2112.05381)
- [VISTA: Boosting 3D Object Detection via Dual Cross-VIew SpaTial Attention](https://arxiv.org/abs/2203.09704) — `detection` `autonomous driving` `BEV`
- [Voxel Set Transformer: A Set-to-Set Approach to 3D Object Detection from Point Clouds](https://arxiv.org/abs/2203.10314) — `detection`
- [WarpingGAN: Warping Multiple Uniform Priors for Adversarial 3D Point Cloud Generation](https://arxiv.org/abs/2203.12917) — `generation` `robustness`
- [ZZ-Net: A Universal Rotation Equivariant Architecture for 2D Point Clouds](https://arxiv.org/abs/2111.15341)

</details>

<details><summary><b>ECCV</b> · 53</summary>

- [2DPASS: 2D Priors Assisted Semantic Segmentation on LiDAR Point Clouds](https://arxiv.org/abs/2207.04397) — `segmentation` `autonomous driving`
- [3D Siamese Transformer Network for Single Object Tracking on Point Clouds](https://arxiv.org/abs/2207.11995) — `tracking`
- [A Closer Look at Invariances in Self-supervised Pre-training for 3D Vision](https://arxiv.org/abs/2207.04997) — `self-supervised` `pre-training`
- [AutoAlignV2: Deformable Feature Aggregation for Dynamic Multi-Modal 3D Object Detection](https://arxiv.org/abs/2207.10316) — `detection` `localization` `autonomous driving` `multi-modal`
- [Autoregressive Uncertainty Modeling for 3D Bounding Box Prediction](https://arxiv.org/abs/2210.07424)
- [Bi-PointFlowNet: Bidirectional Learning for Point Cloud Based Scene Flow Estimation](https://arxiv.org/abs/2207.07522) — `scene flow`
- [Bottom Up Top Down Detection Transformers for Language Grounding in Images and Point Clouds](https://arxiv.org/abs/2112.08879) — `detection`
- [Capturing, Reconstructing, and Simulating: the UrbanScene3D Dataset](https://arxiv.org/abs/2107.04286) — `reconstruction` `dataset`
- [CATRE: Iterative Point Clouds Alignment for Category-level Object Pose Refinement](https://arxiv.org/abs/2207.08082)
- [CenterFormer: Center-based Transformer for 3D Object Detection](https://arxiv.org/abs/2209.05588) — `detection`
- [CoSMix: Compositional Semantic Mix for Domain Adaptation in 3D LiDAR Segmentation](https://arxiv.org/abs/2207.09778) — `segmentation` `autonomous driving` `domain adaptation`
- [CPO: Change Robust Panorama to Point Cloud Localization](https://arxiv.org/abs/2207.05317) — `localization` `generation` `robustness`
- [diffConv: Analyzing Irregular Point Clouds with an Irregular View](https://arxiv.org/abs/2111.14658)
- [Domain Randomization-Enhanced Depth Simulation and Restoration for Perceiving and Grasping Specular and Transparent Objects](https://arxiv.org/abs/2208.03792)
- [Dual Adaptive Transformations for Weakly Supervised Point Cloud Segmentation](https://arxiv.org/abs/2207.09084) — `segmentation`
- [Dynamic 3D Scene Analysis by Point Cloud Accumulation](https://arxiv.org/abs/2207.12394) — `segmentation` `reconstruction`
- [ExtrudeNet: Unsupervised Inverse Sketch-and-Extrude for Shape Parsing](https://arxiv.org/abs/2209.15632)
- [FBNet: Feedback Network for Point Cloud Completion](https://arxiv.org/abs/2210.03974) — `completion` — [code](https://github.com/hikvision-research/3DVision)
- [Few 'Zero Level Set'-Shot Learning of Shape Signed Distance Functions in Feature Space](https://arxiv.org/abs/2207.04161) — `reconstruction`
- [Geodesic-Former: a Geodesic-Guided Few-shot 3D Point Cloud Instance Segmenter](https://arxiv.org/abs/2207.10859) — `segmentation`
- [GIPSO: Geometrically Informed Propagation for Online Adaptation in 3D LiDAR Segmentation](https://arxiv.org/abs/2207.09763) — `segmentation` `autonomous driving`
- [Homogeneous Multi-modal Feature Fusion and Interaction for 3D Object Detection](https://arxiv.org/abs/2210.09615) — `detection` `autonomous driving` `multi-modal`
- [Improving RGB-D Point Cloud Registration by Learning Multi-scale Local Linear Transformation](https://arxiv.org/abs/2208.14893) — `registration`
- [Is Geometry Enough for Matching in Visual Localization?](https://arxiv.org/abs/2203.12979) — `localization`
- [Label-Guided Auxiliary Training Improves 3D Object Detector](https://arxiv.org/abs/2207.11753) — `detection`
- [Learning to Generate Realistic LiDAR Point Clouds](https://arxiv.org/abs/2209.03954) — `generation` `denoising`
- [LiDAR Distillation: Bridging the Beam-Induced Domain Gap for 3D Object Detection](https://arxiv.org/abs/2203.14956) — `detection` `domain adaptation` — [code](https://github.com/weiyithu/LiDAR-Distillation)
- [Lidar Point Cloud Guided Monocular 3D Object Detection](https://arxiv.org/abs/2104.09035) — `detection` `autonomous driving` `monocular`
- [LidarNAS: Unifying and Searching Neural Architectures for 3D Point Clouds](https://arxiv.org/abs/2210.05018) — `autonomous driving`
- [Masked Discrimination for Self-Supervised Learning on Point Clouds](https://arxiv.org/abs/2203.11183) — `self-supervised` — [code](https://github.com/haotian-liu/MaskPoint)
- [MatchNorm: Learning-based Point Cloud Registration for 6D Object Pose Estimation in the Real World](https://arxiv.org/abs/2203.15309) — `registration`
- [MeshMAE: Masked Autoencoders for 3D Mesh Data Analysis](https://arxiv.org/abs/2207.10228) — `self-supervised`
- [MonteBoxFinder: Detecting and Filtering Primitives to Fit a Noisy Point Cloud](https://arxiv.org/abs/2207.14268) — `detection` — [code](https://github.com/MichaelRamamonjisoa/MonteBoxFinder)
- [MPPNet: Multi-Frame Feature Intertwining with Proxy Points for 3D Temporal Object Detection](https://arxiv.org/abs/2205.05979) — `detection` `autonomous driving`
- [Open-world Semantic Segmentation for LIDAR Point Clouds](https://arxiv.org/abs/2207.01452) — `segmentation` `autonomous driving`
- [Point Primitive Transformer for Long-Term 4D Point Cloud Video Understanding](https://arxiv.org/abs/2208.00281)
- [Point Scene Understanding via Disentangled Instance Mesh Reconstruction](https://arxiv.org/abs/2203.16832) — `reconstruction`
- [PointInst3D: Segmenting 3D Instances by Points](https://arxiv.org/abs/2204.11402) — `segmentation` — [code](https://github.com/tonghe90/PointInst3D)
- [PointMixer: MLP-Mixer for Point Cloud Understanding](https://arxiv.org/abs/2111.11187)
- [PointTree: Transformation-Robust Point Cloud Encoder with Relaxed K-D Trees](https://arxiv.org/abs/2208.05962) — `robustness`
- [ProposalContrast: Unsupervised Pre-training for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2207.12654) — `detection` `pre-training` — [code](https://github.com/yinjunbo/ProposalContrast)
- [PseudoAugment: Learning to Use Unlabeled Data for Data Augmentation in Point Clouds](https://arxiv.org/abs/2210.13428) — `detection`
- [RBP-Pose: Residual Bounding Box Projection for Category-Level Pose Estimation](https://arxiv.org/abs/2208.00237)
- [RFNet-4D++: Joint Object Reconstruction and Flow Estimation from 4D Point Clouds with Cross-Attention Spatio-Temporal Features](https://arxiv.org/abs/2203.16482) — `reconstruction`
- [RPR-Net: A Point Cloud-based Rotation-aware Large Scale Place Recognition Network](https://arxiv.org/abs/2108.12790) — `slam` `localization` — Workshop
- [Salient Object Detection for Point Clouds](https://arxiv.org/abs/2207.11889) — `detection`
- [SeedFormer: Patch Seeds based Point Cloud Completion with Upsample Transformer](https://arxiv.org/abs/2207.10315) — `completion` `generation` `upsampling`
- [SLiDE: Self-supervised LiDAR De-snowing through Reconstruction Difficulty](https://arxiv.org/abs/2208.04043) — `segmentation` `reconstruction` `self-supervised`
- [SPE-Net: Boosting Point Cloud Analysis via Rotation Robustness Enhancement](https://arxiv.org/abs/2211.08250) — `robustness` — [code](https://github.com/ZhaofanQiu/SPE-Net)
- [SQN: Weakly-Supervised Semantic Segmentation of Large-Scale 3D Point Clouds](https://arxiv.org/abs/2104.04891) — `segmentation`
- [SuperLine3D: Self-supervised Line Segmentation and Description for LiDAR Point Cloud](https://arxiv.org/abs/2208.01925) — `registration` `segmentation` `self-supervised`
- [SWFormer: Sparse Window Transformer for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2210.07372) — `detection` `autonomous driving`
- [What Matters for 3D Scene Flow Network](https://arxiv.org/abs/2207.09143) — `scene flow`

</details>

<details><summary><b>NeurIPS</b> · 26</summary>

- [3DOS: Towards 3D Open Set Learning -- Benchmarking and Understanding Semantic Novelty Detection on Point Clouds](https://arxiv.org/abs/2207.11554) — `segmentation` `detection` `classification` — [code](https://github.com/antoalli/3D_OS)
- [A Benchmark for Out of Distribution Detection in Point Cloud 3D Semantic Segmentation](https://arxiv.org/abs/2211.06241) — `segmentation` `detection` `autonomous driving` `dataset` — Workshop
- [Analyzing Deep Learning Representations of Point Clouds for Real-Time In-Vehicle LiDAR Perception](https://arxiv.org/abs/2210.14612) — `efficiency` — Workshop
- [BEVFusion: A Simple and Robust LiDAR-Camera Fusion Framework](https://arxiv.org/abs/2205.13790) — `detection` `multi-modal` `robustness`
- [CAP-UDF: Learning Unsigned Distance Functions Progressively from Raw Point Clouds with Consistency-Aware Field Optimization](https://arxiv.org/abs/2210.02757) — `reconstruction` — [code](https://github.com/junshengzhou/CAP-UDF)
- [Contrastive Self-Supervised Learning for Skeleton Representations](https://arxiv.org/abs/2211.05304) — `self-supervised` — Workshop
- [Cross-modal Learning for Image-Guided Point Cloud Shape Completion](https://arxiv.org/abs/2209.09552) — `completion` `reconstruction`
- [Diffusion Curvature for Estimating Local Curvature in High Dimensional Data](https://arxiv.org/abs/2206.03977)
- [Do graph neural networks learn traditional jet substructure?](https://arxiv.org/abs/2211.09912) — Workshop
- [Fully Convolutional One-Stage 3D Object Detection on LiDAR Range Images](https://arxiv.org/abs/2205.13764) — `detection` `autonomous driving` `BEV`
- [HSurf-Net: Normal Estimation for 3D Point Clouds by Learning Hyper Surfaces](https://arxiv.org/abs/2210.07158) — `normal estimation`
- [LION: Latent Point Diffusion Models for 3D Shape Generation](https://arxiv.org/abs/2210.06978) — `generation` `denoising`
- [Look Around and Refer: 2D Synthetic Semantics Knowledge Distillation for 3D Visual Grounding](https://arxiv.org/abs/2211.14241)
- [Non-rigid Point Cloud Registration with Neural Deformation Pyramid](https://arxiv.org/abs/2205.12796) — `registration` — [code](https://github.com/rabbityl/DeformationPyramid)
- [OGC: Unsupervised 3D Object Segmentation from Rigid Dynamics of Point Clouds](https://arxiv.org/abs/2210.04458) — `segmentation` — [code](https://github.com/vLAR-group/OGC)
- [P2P: Tuning Pre-trained Image Models for Point Cloud Analysis with Point-to-Pixel Prompting](https://arxiv.org/abs/2208.02812) — `pre-training`
- [Point Transformer V2: Grouped Vector Attention and Partition-based Pooling](https://arxiv.org/abs/2210.05666)
- [Point-M2AE: Multi-scale Masked Autoencoders for Hierarchical Point Cloud Pre-training](https://arxiv.org/abs/2205.14401) — `self-supervised` `pre-training`
- [PointNeXt: Revisiting PointNet++ with Improved Training and Scaling Strategies](https://arxiv.org/abs/2206.04670) — [code](https://github.com/guochengqian/pointnext)
- [Prototypical VoteNet for Few-Shot 3D Point Cloud Object Detection](https://arxiv.org/abs/2210.05593) — `detection`
- [Rethinking the compositionality of point clouds through regularization in the hyperbolic space](https://arxiv.org/abs/2209.10318)
- [SageMix: Saliency-Guided Mixup for Point Clouds](https://arxiv.org/abs/2210.06944)
- [SCONE: Surface Coverage Optimization in Unknown Environments by Volumetric Integration](https://arxiv.org/abs/2208.10449) — `reconstruction` — [code](https://github.com/Anttwo/SCONE)
- [SNAKE: Shape-aware Neural 3D Keypoint Field](https://arxiv.org/abs/2206.01724) — `detection` `reconstruction` — [code](https://github.com/zhongcl-thu/SNAKE)
- [Sparse2Dense: Learning to Densify 3D Features for 3D Object Detection](https://arxiv.org/abs/2211.13067) — `detection` — [code](https://github.com/stevewongv/Sparse2Dense)
- [Stress-Testing Point Cloud Registration on Automotive LiDAR](https://arxiv.org/abs/2204.07719) — `registration` `autonomous driving` — [code](https://github.com/AmnonDrory/LidarRegistration) Workshop

</details>

<details><summary><b>ICLR</b> · 4</summary>

- [Equivariant Descriptor Fields: SE(3)-Equivariant Energy-Based Models for End-to-End Visual Robotic Manipulation Learning](https://arxiv.org/abs/2206.08321)
- [Hindsight is 20/20: Leveraging Past Traversals to Aid 3D Perception](https://arxiv.org/abs/2203.11405) — `detection` `autonomous driving` — [code](https://github.com/YurongYou/Hindsight)
- [Interpretable Geometric Deep Learning via Learnable Randomness Injection](https://arxiv.org/abs/2210.16966)
- [Representation-Agnostic Shape Fields](https://arxiv.org/abs/2203.10259) — [code](https://github.com/seanywang0408/RASF)

</details>

<details><summary><b>ICML</b> · 2</summary>

- [Implicit Neural Spatial Representations for Time-dependent PDEs](https://arxiv.org/abs/2210.00124)
- [The Manifold Scattering Transform for High-Dimensional Point Cloud Data](https://arxiv.org/abs/2206.10078) — Workshop

</details>

<details><summary><b>AAAI</b> · 10</summary>

- [Attention-based Transformation from Latent Features to Point Clouds](https://arxiv.org/abs/2112.05324) — `completion` `generation`
- [Behind the Curtain: Learning Occluded Shapes for 3D Object Detection](https://arxiv.org/abs/2112.02205) — `detection`
- [Boosting Point Clouds Rendering via Radiance Mapping](https://arxiv.org/abs/2210.15107) — `nerf`
- [End-to-end Learning the Partial Permutation Matrix for Robust 3D Point Cloud Registration](https://arxiv.org/abs/2110.15250) — `registration` `robustness`
- [MGTANet: Encoding Sequential LiDAR Points Using Long Short-Term Motion-Guided Temporal Attention for 3D Object Detection](https://arxiv.org/abs/2212.00442) — `detection`
- [PointCA: Evaluating the Robustness of 3D Point Cloud Completion Models Against Adversarial Examples](https://arxiv.org/abs/2211.12294) — `segmentation` `completion` `robustness`
- [Self-Supervised Robust Scene Flow Estimation via the Alignment of Probability Density Functions](https://arxiv.org/abs/2203.12193) — `self-supervised` `scene flow` `robustness`
- [Semantic Segmentation for Point Cloud Scenes via Dilated Graph Feature Aggregation and Pyramid Decoders](https://arxiv.org/abs/2204.04944) — `segmentation` — Workshop
- [SVT-Net: Super Light-Weight Sparse Voxel Transformer for Large Scale Place Recognition](https://arxiv.org/abs/2105.00149) — `slam` `localization` `efficiency`
- [Transfer Learning from Synthetic to Real LiDAR Point Cloud for Semantic Segmentation](https://arxiv.org/abs/2107.05399) — `segmentation`

</details>

<details><summary><b>IJCAI</b> · 2</summary>

- [Reconstruction-Aware Prior Distillation for Semi-supervised Point Cloud Completion](https://arxiv.org/abs/2204.09186) — `completion` `reconstruction`
- [Spatiality-guided Transformer for 3D Dense Captioning on Point Clouds](https://arxiv.org/abs/2204.10688) — `detection`

</details>

<details><summary><b>SIGGRAPH</b> · 2</summary>

- [Deep Billboards towards Lossless Real2Sim in Virtual Reality](https://arxiv.org/abs/2208.08861)
- [Shape Completion with Points in the Shadow](https://arxiv.org/abs/2209.08345) — `completion`

</details>

<details><summary><b>SIGGRAPH Asia</b> · 3</summary>

- [Morig: Motion-aware rigging of character meshes from point clouds](https://arxiv.org/abs/2210.09463)
- [RFEPS: Reconstructing Feature-line Equipped Polygonal Surface](https://arxiv.org/abs/2212.03600) — `reconstruction`
- [SHRED: 3D Shape Region Decomposition with Learned Local Operations](https://arxiv.org/abs/2206.03480) — `segmentation`

</details>

<details><summary><b>ACM MM</b> · 4</summary>

- [Ada3Diff: Defending against 3D Adversarial Point Clouds via Adaptive Diffusion](https://arxiv.org/abs/2211.16247) — `denoising` `autonomous driving` `robustness`
- [Boosting Single-Frame 3D Object Detection by Simulating Multi-Frame Point Clouds](https://arxiv.org/abs/2207.01030) — `detection`
- [GRASP-Net: Geometric Residual Analysis and Synthesis for Point Cloud Compression](https://arxiv.org/abs/2209.04401) — `compression` — Workshop
- [Zero-shot point cloud segmentation by transferring geometric primitives](https://arxiv.org/abs/2210.09923) — `segmentation` `open-vocabulary`

</details>

<details><summary><b>3DV</b> · 5</summary>

- [Arbitrary Point Cloud Upsampling with Spherical Mixture of Gaussians](https://arxiv.org/abs/2208.05274) — `upsampling`
- [Efficient Human Pose Estimation via 3D Event Point Cloud](https://arxiv.org/abs/2206.04511) — `efficiency` — [code](https://github.com/MasterHow/EventPointPose)
- [Neural Point-based Shape Modeling of Humans in Challenging Clothing](https://arxiv.org/abs/2209.06814)
- [Pix4Point: Image Pretrained Standard Transformers for 3D Point Cloud Understanding](https://arxiv.org/abs/2208.12259) — `pre-training`
- [SVNet: Where SO(3) Equivariance Meets Binarization on Point Cloud Representation](https://arxiv.org/abs/2209.05924) — `autonomous driving`

</details>

<details><summary><b>WACV</b> · 9</summary>

- [Centroid Distance Keypoint Detector for Colored Point Clouds](https://arxiv.org/abs/2210.01298) — `detection`
- [GaIA: Graphical Information Gain based Attention Network for Weakly Supervised Point Cloud Semantic Segmentation](https://arxiv.org/abs/2210.01558) — `segmentation`
- [Li3DeTr: A LiDAR based 3D Detection Transformer](https://arxiv.org/abs/2210.15365) — `detection` `autonomous driving`
- [MAELi: Masked Autoencoder for Large-Scale LiDAR Point Clouds](https://arxiv.org/abs/2212.07207) — `self-supervised`
- [MonoDVPS: A Self-Supervised Monocular Depth Estimation Approach to Depth-aware Video Panoptic Segmentation](https://arxiv.org/abs/2210.07577) — `segmentation` `self-supervised` `monocular`
- [Overlap-guided Gaussian Mixture Models for Point Cloud Registration](https://arxiv.org/abs/2210.09836) — `registration`
- [PointInverter: Point Cloud Reconstruction and Editing via a Generative Model with Shape Priors](https://arxiv.org/abs/2211.08702) — `generation` `reconstruction`
- [PointNeuron: 3D Neuron Reconstruction via Geometry and Topology Learning of Point Clouds](https://arxiv.org/abs/2210.08305) — `segmentation` `reconstruction`
- [Self-Distillation for Unsupervised 3D Domain Adaptation](https://arxiv.org/abs/2210.08226) — `classification` `domain adaptation`

</details>

<details><summary><b>BMVC</b> · 6</summary>

- [APSNet: Attention Based Point Cloud Sampling](https://arxiv.org/abs/2210.05638)
- [Challenging the Universal Representation of Deep Models for 3D Point Cloud Registration](https://arxiv.org/abs/2211.16301) — `registration` — Workshop
- [DA-CIL: Towards Domain Adaptive Class-Incremental 3D Object Detection](https://arxiv.org/abs/2212.02057) — `detection`
- [Data Augmentation-free Unsupervised Learning for 3D Point Cloud Understanding](https://arxiv.org/abs/2210.02798)
- [Energy-Based Residual Latent Transport for Unsupervised Point Cloud Completion](https://arxiv.org/abs/2211.06820) — `completion` `generation`
- [EpipolarNVS: leveraging on Epipolar geometry for single-image Novel View Synthesis](https://arxiv.org/abs/2210.13077)

</details>

<details><summary><b>ICRA</b> · 13</summary>

- [3D Reconstruction-Based Seed Counting of Sorghum Panicles for Agricultural Inspection](https://arxiv.org/abs/2211.07748) — `reconstruction`
- [Analyzing Infrastructure LiDAR Placement with Realistic LiDAR Simulation Library](https://arxiv.org/abs/2211.15975)
- [BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation](https://arxiv.org/abs/2205.13542) — `autonomous driving`
- [Center Feature Fusion: Selective Multi-Sensor Fusion of Center-based Objects](https://arxiv.org/abs/2209.12880) — `detection`
- [Coarse-to-Fine Point Cloud Registration with SE(3)-Equivariant Representations](https://arxiv.org/abs/2210.02045) — `registration`
- [Dynamic Control Barrier Function-based Model Predictive Control to Safety-Critical Obstacle-Avoidance of Mobile Robot](https://arxiv.org/abs/2209.08539) — `detection`
- [Fast Staircase Detection and Estimation using 3D Point Clouds with Multi-detection Merging for Heterogeneous Robots](https://arxiv.org/abs/2211.00610) — `detection`
- [High Resolution Point Clouds from mmWave Radar](https://arxiv.org/abs/2206.09273) — `multi-modal`
- [HiTPR: Hierarchical Transformer for Place Recognition in Point Cloud](https://arxiv.org/abs/2204.05481) — `detection` `slam` `localization`
- [Interactive Object Segmentation in 3D Point Clouds](https://arxiv.org/abs/2204.07183) — `segmentation`
- [Learning to Estimate 3-D States of Deformable Linear Objects from Single-Frame Occluded Point Clouds](https://arxiv.org/abs/2210.01433)
- [PCB-RandNet: Rethinking Random Sampling for LIDAR Semantic Segmentation in Autonomous Driving Scene](https://arxiv.org/abs/2209.13797) — `segmentation` `autonomous driving` — [code](https://github.com/huixiancheng/PCB-RandNet)
- [Topologically Persistent Features-based Object Recognition in Cluttered Indoor Environments](https://arxiv.org/abs/2205.07479) — Workshop

</details>

<details><summary><b>IROS</b> · 17</summary>

- [An Extrinsic Calibration Method between LiDAR and GNSS/INS for Autonomous Driving](https://arxiv.org/abs/2209.07694) — `autonomous driving`
- [An Integrated LiDAR-SLAM System for Complex Environment with Noisy Point Clouds](https://arxiv.org/abs/2212.05705) — `slam` `localization`
- [BoxGraph: Semantic Place Recognition and Pose Estimation from 3D LiDAR](https://arxiv.org/abs/2206.15154) — `segmentation` `localization`
- [Challenges of SLAM in extremely unstructured environments: the DLR Planetary Stereo, Solid-State LiDAR, Inertial Dataset](https://arxiv.org/abs/2207.06815) — `slam` `dataset`
- [Elevation State-Space: Surfel-Based Navigation in Uneven Environments for Mobile Robots](https://arxiv.org/abs/2208.08202)
- [EVOPS Benchmark: Evaluation of Plane Segmentation from RGBD and LiDAR Data](https://arxiv.org/abs/2204.05799) — `segmentation` `slam` `dataset`
- [Gravity-constrained point cloud registration](https://arxiv.org/abs/2203.13799) — `registration` `slam` `localization`
- [How Do We Fail? Stress Testing Perception in Autonomous Vehicles](https://arxiv.org/abs/2203.14155)
- [Koopman pose predictions for temporally consistent human walking estimations](https://arxiv.org/abs/2205.02737) — `tracking`
- [LapSeg3D: Weakly Supervised Semantic Segmentation of Point Clouds Representing Laparoscopic Scenes](https://arxiv.org/abs/2207.07418) — `segmentation`
- [LiSnowNet: Real-time Snow Removal for LiDAR Point Cloud](https://arxiv.org/abs/2211.10023) — `autonomous driving` `efficiency`
- [PaintNet: Unstructured Multi-Path Learning from 3D Point Clouds for Robotic Spray Painting](https://arxiv.org/abs/2211.06930)
- [Patchwork++: Fast and Robust Ground Segmentation Solving Partial Under-Segmentation Using 3D Point Cloud](https://arxiv.org/abs/2207.11919) — `segmentation` `detection` `robustness`
- [PFilter: Building Persistent Maps through Feature Filtering for Fast and Accurate LiDAR-based SLAM](https://arxiv.org/abs/2208.14848) — `registration` `slam` `localization`
- [SemanticBEVFusion: Rethink LiDAR-Camera Fusion in Unified Bird's-Eye View Representation for 3D Object Detection](https://arxiv.org/abs/2212.04675) — `detection` `autonomous driving` `multi-modal`
- [SSP-Pose: Symmetry-Aware Shape Prior Deformation for Direct Category-Level Object Pose Estimation](https://arxiv.org/abs/2208.06661)
- [Unsupervised confidence for LiDAR depth maps and applications](https://arxiv.org/abs/2210.03118) — `autonomous driving` — [code](https://github.com/andreaconti/lidar-confidence)

</details>

<details><summary><b>RA-L</b> · 19</summary>

- [A Credible and Robust approach to Ego-Motion Estimation using an Automotive Radar](https://arxiv.org/abs/2204.04149) — `multi-modal` `robustness`
- [BIMS-PU: Bi-Directional and Multi-Scale Point Cloud Upsampling](https://arxiv.org/abs/2206.12648) — `upsampling`
- [Exploiting More Information in Sparse Point Cloud for 3D Single Object Tracking](https://arxiv.org/abs/2210.00519) — `tracking`
- [Gaussian Radar Transformer for Semantic Segmentation in Noisy Radar Data](https://arxiv.org/abs/2212.03690) — `segmentation` `multi-modal`
- [GMF: General Multimodal Fusion Framework for Correspondence Outlier Rejection](https://arxiv.org/abs/2211.00207) — `registration` `multi-modal`
- [GraffMatch: Global Matching of 3D Lines and Planes for Wide Baseline LiDAR Registration](https://arxiv.org/abs/2212.12745) — `registration` `detection`
- [Hyperbolic Cosine Transformer for LiDAR 3D Object Detection](https://arxiv.org/abs/2211.05580) — `detection`
- [Implicit and Efficient Point Cloud Completion for 3D Single Object Tracking](https://arxiv.org/abs/2209.00522) — `completion` `tracking` `localization` `efficiency`
- [PADLoC: LiDAR-Based Deep Loop Closure Detection and Registration Using Panoptic Attention](https://arxiv.org/abs/2209.09699) — `registration` `segmentation` `detection` `slam`
- [Point Cloud Change Detection With Stereo V-SLAM:Dataset, Metrics and Baseline](https://arxiv.org/abs/2207.00246) — `detection` `slam` `localization` `dataset`
- [Real-time Neural Dense Elevation Mapping for Urban Terrain with Uncertainty Estimations](https://arxiv.org/abs/2208.03467) — `reconstruction` `efficiency`
- [Real3D-Aug: Point Cloud Augmentation by Placing Real Objects with Occlusion Handling for 3D Detection and Segmentation](https://arxiv.org/abs/2206.07634) — `segmentation` `detection`
- [Receding Moving Object Segmentation in 3D LiDAR Data Using Sparse 4D Convolutions](https://arxiv.org/abs/2206.04129) — `segmentation`
- [Spectral Geometric Verification: Re-Ranking Point Cloud Retrieval for Metric Localization](https://arxiv.org/abs/2210.04432) — `localization`
- [SphereVLAD++: Attention-based and Signal-enhanced Viewpoint Invariant Descriptor](https://arxiv.org/abs/2207.02958) — `localization` `autonomous driving`
- [Teachers in concordance for pseudo-labeling of 3D sequential data](https://arxiv.org/abs/2207.06079) — `autonomous driving`
- [TRAVEL: Traversable Ground and Above-Ground Object Segmentation Using Graph Representation of 3D LiDAR Scans](https://arxiv.org/abs/2206.03190) — `segmentation`
- [Uncertainty Estimation for 3D Dense Prediction via Cross-Point Embeddings](https://arxiv.org/abs/2209.14602)
- [You Only Label Once: 3D Box Adaptation from Point Cloud to Image via Semi-Supervised Learning](https://arxiv.org/abs/2211.09302) — `detection`

</details>

<details><summary><b>TPAMI</b> · 8</summary>

- [Flattening-Net: Deep Regular 2D Representation for 3D Point Cloud Analysis](https://arxiv.org/abs/2212.08892)
- [Incomplete Gamma Kernels: Generalizing Locally Optimal Projection Operators](https://arxiv.org/abs/2205.01087) — `denoising`
- [Learning Canonical Embeddings for Unsupervised Shape Correspondence with Locally Linear Transformations](https://arxiv.org/abs/2209.02152)
- [Point Cloud Attacks in Graph Spectral Domain: When 3D Geometry Meets Graph Signal Processing](https://arxiv.org/abs/2207.13326)
- [Refine-Net: Normal Refinement Neural Network for Noisy Point Clouds](https://arxiv.org/abs/2203.12514) — `generation` `reconstruction`
- [Robust Point Cloud Registration Framework Based on Deep Graph Matching(TPAMI Version)](https://arxiv.org/abs/2211.04696) — `registration` `robustness`
- [Robust Point Cloud Segmentation with Noisy Annotations](https://arxiv.org/abs/2212.03242) — `segmentation` `robustness`
- [Scalable SoftGroup for 3D Instance Segmentation on Point Clouds](https://arxiv.org/abs/2209.08263) — `segmentation`

</details>

<details><summary><b>IJCV</b> · 1</summary>

- [CompleteDT: Point Cloud Completion with Dense Augment Inference Transformers](https://arxiv.org/abs/2205.14999) — `completion`

</details>

<details><summary><b>TIP</b> · 2</summary>

- [3D Cascade RCNN: High Quality Object Detection in Point Clouds](https://arxiv.org/abs/2211.08248) — `detection` — [code](https://github.com/caiqi/Cascasde-3D)
- [Learning A Locally Unified 3D Point Cloud for View Synthesis](https://arxiv.org/abs/2209.05013)

</details>

<details><summary><b>TVCG</b> · 2</summary>

- [Contrastive Learning for Joint Normal Estimation and Point Cloud Filtering](https://arxiv.org/abs/2208.06811) — `self-supervised` `normal estimation` — [code](https://github.com/ddsediri/CLJNEPCF)
- [PointVST: Self-Supervised Pre-training for 3D Point Clouds via View-Specific Point-to-Image Translation](https://arxiv.org/abs/2212.14197) — `generation` `self-supervised` `pre-training`

</details>

<details><summary><b>ISPRS</b> · 4</summary>

- [Beyond single receptive field: A receptive field fusion-and-stratification network for airborne laser scanning point cloud classification](https://arxiv.org/abs/2207.10278) — `classification`
- [Building Change Detection using Multi-Temporal Airborne LiDAR Data](https://arxiv.org/abs/2204.12535) — `detection`
- [CroCo: Cross-Modal Contrastive learning for localization of Earth Observation data](https://arxiv.org/abs/2204.07052) — `localization` `self-supervised`
- [Graph-theoretical approach to robust 3D normal extraction of LiDAR data](https://arxiv.org/abs/2205.11460) — `robustness`

</details>

<details><summary><b>PR</b> · 4</summary>

- [Composite Convolution: a Flexible Operator for Deep Learning on 3D Point Clouds](https://arxiv.org/abs/2209.11796) — `compression`
- [Global Hierarchical Attention for 3D Point Cloud Analysis](https://arxiv.org/abs/2208.03791)
- [NeuralMeshing: Differentiable Meshing of Implicit Neural Representations](https://arxiv.org/abs/2210.02382) — `generation`
- [One-Shot Neural Fields for 3D Object Understanding](https://arxiv.org/abs/2210.12126) — `reconstruction` — Workshop

</details>

<details><summary><b>arXiv</b> · 317</summary>

- [3D LiDAR Aided GNSS NLOS Mitigation for Reliable GNSS-RTK Positioning in Urban Canyons](https://arxiv.org/abs/2212.05477)
- [3D Object Detection with a Self-supervised Lidar Scene Flow Backbone](https://arxiv.org/abs/2205.00705) — `detection` `self-supervised` `scene flow`
- [3D Point Cloud Pre-training with Knowledge Distillation from 2D Images](https://arxiv.org/abs/2212.08974) — `pre-training`
- [3D Scalable Quantum Convolutional Neural Networks for Point Cloud Data Processing in Classification Applications](https://arxiv.org/abs/2210.09728) — `classification`
- [3D Scene Flow Estimation on Pseudo-LiDAR: Bridging the Gap on Estimating Point Motion](https://arxiv.org/abs/2209.13130) — `scene flow`
- [3D Segmentation of Humans in Point Clouds with Synthetic Data](https://arxiv.org/abs/2212.00786) — `segmentation`
- [3D-OAE: Occlusion Auto-Encoders for Self-Supervised Learning on Point Clouds](https://arxiv.org/abs/2203.14084) — `reconstruction` `self-supervised` — [code](https://github.com/junshengzhou/3D-OAE)
- [3D-VFD: A Victim-free Detector against 3D Adversarial Point Clouds](https://arxiv.org/abs/2205.08738) — `detection` `robustness`
- [3DAC: Learning Attribute Compression for Point Clouds](https://arxiv.org/abs/2203.09931) — `compression`
- [3DGTN: 3D Dual-Attention GLocal Transformer Network for Point Cloud Classification and Segmentation](https://arxiv.org/abs/2209.11255) — `segmentation` `classification`
- [3DMODT: Attention-Guided Affinities for Joint Detection & Tracking in 3D Point Clouds](https://arxiv.org/abs/2211.00746) — `detection` `tracking`
- [3DVerifier: Efficient Robustness Verification for 3D Point Cloud Models](https://arxiv.org/abs/2207.07539) — `robustness` `efficiency`
- [4DAC: Learning Attribute Compression for Dynamic Point Clouds](https://arxiv.org/abs/2204.11723) — `compression`
- [4DenoiseNet: Adverse Weather Denoising from Adjacent Point Clouds](https://arxiv.org/abs/2209.07121) — `detection` `denoising` `autonomous driving`
- [A Comparative Study of Feature Expansion Unit for 3D Point Cloud Upsampling](https://arxiv.org/abs/2205.09594) — `upsampling`
- [A Light-Weight LiDAR-Inertial SLAM System with Loop Closing](https://arxiv.org/abs/2212.05743) — `slam` `efficiency`
- [A Near Sensor Edge Computing System for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2207.05888) — `segmentation` `autonomous driving`
- [A New Outlier Removal Strategy Based on Reliability of Correspondence Graph for Fast Point Cloud Registration](https://arxiv.org/abs/2205.07404) — `registration`
- [A No-reference Quality Assessment Metric for Point Cloud Based on Captured Video Sequences](https://arxiv.org/abs/2206.05054) — `compression` — Workshop
- [A Realism Metric for Generated LiDAR Point Clouds](https://arxiv.org/abs/2208.14958) — `generation`
- [A Representation Separation Perspective to Correspondences-free Unsupervised 3D Point Cloud Registration](https://arxiv.org/abs/2203.13239) — `registration`
- [A Survey of Robust 3D Object Detection Methods in Point Clouds](https://arxiv.org/abs/2204.00106) — `detection` `robustness`
- [Accurate Fruit Localisation for Robotic Harvesting using High Resolution LiDAR-Camera Fusion](https://arxiv.org/abs/2205.00404) — `localization` `multi-modal`
- [Accurate Ground-Truth Depth Image Generation via Overfit Training of Point Cloud Registration using Local Frame Sets](https://arxiv.org/abs/2207.07016) — `registration` `generation`
- [Adaptive Edge-to-Edge Interaction Learning for Point Cloud Analysis](https://arxiv.org/abs/2211.10888) — `segmentation` `classification`
- [Adaptive Feature Fusion for Cooperative Perception using LiDAR Point Clouds](https://arxiv.org/abs/2208.00116)
- [AdaSplats: Adaptive Splatting of Point Clouds for Accurate 3D Modeling and Real-time High-Fidelity LiDAR Simulation](https://arxiv.org/abs/2203.09155) — `segmentation` `detection` `tracking` `localization`
- [Advanced Feature Learning on Point Clouds using Multi-resolution Features and Learnable Pooling](https://arxiv.org/abs/2205.09962)
- [AGConv: Adaptive Graph Convolution on 3D Point Clouds](https://arxiv.org/abs/2206.04665)
- [AGO-Net: Association-Guided 3D Point Cloud Object Detection Network](https://arxiv.org/abs/2208.11658) — `detection`
- [An Adjustable Farthest Point Sampling Method for Approximately-sorted Point Cloud Data](https://arxiv.org/abs/2208.08795)
- [An Efficient FPGA Accelerator for Point Cloud](https://arxiv.org/abs/2210.07803) — `autonomous driving` `efficiency`
- [An Interpretable Joint Nonnegative Matrix Factorization-Based Point Cloud Distance Measure](https://arxiv.org/abs/2207.05112)
- [An unsupervised, open-source workflow for 2D and 3D building mapping from airborne LiDAR data](https://arxiv.org/abs/2205.14585)
- [APP-Net: Auxiliary-point-based Push and Pull Operations for Efficient Point Cloud Classification](https://arxiv.org/abs/2205.00847) — `classification` `efficiency`
- [AS-PD: An Arbitrary-Size Downsampling Framework for Point Clouds](https://arxiv.org/abs/2211.01110)
- [AssembleRL: Learning to Assemble Furniture from Their Point Clouds](https://arxiv.org/abs/2209.07268)
- [Attention-Enhanced Cross-modal Localization Between 360 Images and Point Clouds](https://arxiv.org/abs/2212.02757) — `localization` `autonomous driving`
- [Automated Reconstruction of 3D Open Surfaces from Sparse Point Clouds](https://arxiv.org/abs/2210.15059) — `reconstruction` — Workshop
- [Automatic Segmentation of Aircraft Dents in Point Clouds](https://arxiv.org/abs/2205.01614) — `segmentation`
- [Bidirectional Feature Globalization for Few-shot Semantic Segmentation of 3D Point Cloud Scenes](https://arxiv.org/abs/2208.06671) — `segmentation`
- [Blind Quality Assessment of 3D Dense Point Clouds with Structure Guided Resampling](https://arxiv.org/abs/2208.14603)
- [BoundED: Neural Boundary and Edge Detection in 3D Point Clouds via Local Neighborhood Statistics](https://arxiv.org/abs/2210.13305) — `detection` `autonomous driving`
- [BTO-RRT: A rapid, optimal, smooth and point cloud-based path planning algorithm](https://arxiv.org/abs/2211.06801)
- [CAGroup3D: Class-Aware Grouping for 3D Object Detection on Point Clouds](https://arxiv.org/abs/2210.04264) — `detection`
- [CAM/CAD Point Cloud Part Segmentation via Few-Shot Learning](https://arxiv.org/abs/2207.01218) — `segmentation`
- [CARNet:Compression Artifact Reduction for Point Cloud Attribute](https://arxiv.org/abs/2209.08276) — `reconstruction` `compression`
- [CasFusionNet: A Cascaded Network for Point Cloud Semantic Scene Completion by Dense Feature Fusion](https://arxiv.org/abs/2211.13702) — `completion` `occupancy prediction`
- [Category-Level Global Camera Pose Estimation with Multi-Hypothesis Point Cloud Correspondences](https://arxiv.org/abs/2209.14419) — `registration`
- [CENet: Toward Concise and Efficient LiDAR Semantic Segmentation for Autonomous Driving](https://arxiv.org/abs/2207.12691) — `segmentation` `autonomous driving` `efficiency`
- [Centimeter-level Positioning by Instantaneous Lidar-aided GNSS Ambiguity Resolution](https://arxiv.org/abs/2204.12103)
- [CloudAttention: Efficient Multi-Scale Attention Scheme For 3D Point Cloud Learning](https://arxiv.org/abs/2208.00524) — `efficiency`
- [CloudVision: DNN-based Visual Localization of Autonomous Robots using Prebuilt LiDAR Point Cloud](https://arxiv.org/abs/2209.01605) — `slam` `localization`
- [Cluster-Based Autoencoders for Volumetric Point Clouds](https://arxiv.org/abs/2211.01009)
- [COARSE3D: Class-Prototypes for Contrastive Learning in Weakly-Supervised 3D Point Cloud Segmentation](https://arxiv.org/abs/2210.01784) — `segmentation` `self-supervised`
- [Common Corruption Robustness of Point Cloud Detectors: Benchmark and Enhancement](https://arxiv.org/abs/2210.05896) — `detection` `autonomous driving` `robustness` `dataset`
- [Complete-to-Partial 4D Distillation for Self-Supervised Point Cloud Sequence Representation Learning](https://arxiv.org/abs/2212.05330) — `self-supervised`
- [Completing Partial Point Clouds with Outliers by Collaborative Completion and Segmentation](https://arxiv.org/abs/2203.09772) — `segmentation` `completion`
- [Completing point cloud from few points by Wasserstein GAN and Transformers](https://arxiv.org/abs/2211.12746) — `completion`
- [Context-Aware Data Augmentation for LIDAR 3D Object Detection](https://arxiv.org/abs/2211.10850) — `detection`
- [Contextual Modeling for 3D Dense Captioning on Point Clouds](https://arxiv.org/abs/2210.03925)
- [Continual Learning for Pose-Agnostic Object Recognition in 3D Point Clouds](https://arxiv.org/abs/2209.04840)
- [Continual learning on 3D point clouds with random compressed rehearsal](https://arxiv.org/abs/2205.08013) — `compression`
- [Contrastive Learning of Features between Images and LiDAR](https://arxiv.org/abs/2206.12071) — `localization` `self-supervised`
- [Convolutional Neural Network-based Efficient Dense Point Cloud Generation using Unsigned Distance Fields](https://arxiv.org/abs/2203.11537) — `generation` `efficiency`
- [CorAl: Introspection for Robust Radar and Lidar Perception in Diverse Environments Using Differential Entropy](https://arxiv.org/abs/2205.05975) — `localization` `multi-modal` `robustness`
- [CorrI2P: Deep Image-to-Point Cloud Registration via Dense Correspondence](https://arxiv.org/abs/2207.05483) — `registration`
- [CP3: Unifying Point Cloud Completion by Pretrain-Prompt-Predict Paradigm](https://arxiv.org/abs/2207.05359) — `completion` `generation` `pre-training`
- [Cross-modal Learning of Graph Representations using Radar Point Cloud for Long-Range Gesture Recognition](https://arxiv.org/abs/2203.17066) — `multi-modal` — Workshop
- [CSDN: Cross-modal Shape-transfer Dual-refinement Network for Point Cloud Completion](https://arxiv.org/abs/2208.00751) — `completion`
- [CU-Net: Real-Time High-Fidelity Color Upsampling for Point Clouds](https://arxiv.org/abs/2209.06112) — `upsampling` `efficiency`
- [CURL: Continuous, Ultra-compact Representation for LiDAR](https://arxiv.org/abs/2205.06059)
- [CXTrack: Improving 3D Point Cloud Tracking with Contextual Information](https://arxiv.org/abs/2211.08542) — `tracking` `autonomous driving`
- [D-Align: Dual Query Co-attention Network for 3D Object Detection Based on Multi-frame Point Cloud Sequence](https://arxiv.org/abs/2210.00087) — `detection`
- [D-DPCC: Deep Dynamic Point Cloud Compression via 3D Motion Prediction](https://arxiv.org/abs/2205.01135) — `compression`
- [Data-driven Loop Closure Detection in Bathymetric Point Clouds for Underwater SLAM](https://arxiv.org/abs/2209.08578) — `detection` `slam` `localization`
- [Deep Algebraic Fitting for Multiple Circle Primitives Extraction from Raw Point Clouds](https://arxiv.org/abs/2204.00920)
- [Deep Geometry Post-Processing for Decompressed Point Clouds](https://arxiv.org/abs/2204.13952) — `compression`
- [Design equivariant neural networks for 3D point cloud](https://arxiv.org/abs/2205.00630)
- [Detection of Condensed Vehicle Gas Exhaust in LiDAR Point Clouds](https://arxiv.org/abs/2207.04908) — `detection` `autonomous driving`
- [Determining Accessible Sidewalk Width by Extracting Obstacle Information from Point Clouds](https://arxiv.org/abs/2211.04108) — [code](https://github.com/Amsterdam-AI-Team/Urban_PointCloud_Sidewalk_Width) Workshop
- [DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation](https://arxiv.org/abs/2211.09423)
- [DiffCloud: Real-to-Sim from Point Clouds with Differentiable Simulation and Rendering of Deformable Objects](https://arxiv.org/abs/2204.03139)
- [Diffusion Unit: Interpretable Edge Enhancement and Suppression Learning for 3D Point Cloud Segmentation](https://arxiv.org/abs/2209.09483) — `segmentation`
- [Divide and Conquer: 3D Point Cloud Instance Segmentation With Point-Wise Binarization](https://arxiv.org/abs/2207.11209) — `segmentation`
- [DL-SLOT: Dynamic LiDAR SLAM and object tracking based on collaborative graph optimization](https://arxiv.org/abs/2212.02077) — `tracking` `slam` `localization` `autonomous driving`
- [DONEX: Real-time occupancy grid based dynamic echo classification for 3D point cloud](https://arxiv.org/abs/2212.04265) — `classification` `autonomous driving` `efficiency`
- [Dynamic Point Cloud Compression with Cross-Sectional Approach](https://arxiv.org/abs/2204.11409) — `compression`
- [Dynamic Point Cloud Denoising via Gradient Fields](https://arxiv.org/abs/2204.08755) — `reconstruction` `denoising` `autonomous driving`
- [ECM-OPCC: Efficient Context Model for Octree-based Point Cloud Compression](https://arxiv.org/abs/2211.10916) — `compression` `efficiency`
- [Eff-3DPSeg: 3D organ-level plant shoot segmentation using annotation-efficient point clouds](https://arxiv.org/abs/2212.10263) — `segmentation` `efficiency`
- [Effective Early Stopping of Point Cloud Neural Networks](https://arxiv.org/abs/2209.15308)
- [Effective Utilisation of Multiple Open-Source Datasets to Improve Generalisation Performance of Point Cloud Segmentation Models](https://arxiv.org/abs/2211.15877) — `segmentation`
- [Efficient and Consistent Bundle Adjustment on Lidar Point Clouds](https://arxiv.org/abs/2209.08854) — `efficiency`
- [Efficient dynamic point cloud coding using Slice-Wise Segmentation](https://arxiv.org/abs/2208.08061) — `segmentation` `compression` `efficiency`
- [Efficient Extrinsic Calibration of Multi-Sensor 3D LiDAR Systems for Autonomous Vehicles using Static Objects Information](https://arxiv.org/abs/2211.02614) — `efficiency`
- [Efficient LiDAR Point Cloud Geometry Compression Through Neighborhood Point Attention](https://arxiv.org/abs/2208.12573) — `compression` `efficiency`
- [Efficient Spatial-Temporal Information Fusion for LiDAR-Based 3D Moving Object Segmentation](https://arxiv.org/abs/2207.02201) — `segmentation` `autonomous driving` `efficiency` — [code](https://github.com/haomo-ai/MotionSeg3D)
- [Efficient Stereo Depth Estimation for Pseudo LiDAR: A Self-Supervised Approach Based on Multi-Input ResNet Encoder](https://arxiv.org/abs/2205.08089) — `localization` `self-supervised` `efficiency`
- [Enhanced Low-resolution LiDAR-Camera Calibration Via Depth Interpolation and Supervised Contrastive Learning](https://arxiv.org/abs/2211.03932) — `self-supervised` `multi-modal`
- [Enhancing Local Feature Learning Using Diffusion for 3D Point Cloud Understanding](https://arxiv.org/abs/2207.01174)
- [Enhancing Local Geometry Learning for 3D Point Cloud via Decoupling Convolution](https://arxiv.org/abs/2207.01181)
- [EPCS: Endpoint-based Part-aware Curve Skeleton Extraction for Low-quality Point Clouds](https://arxiv.org/abs/2211.09488) — `detection`
- [Evaluating Point Cloud from Moving Camera Videos: A No-Reference Metric](https://arxiv.org/abs/2208.14085) — `compression`
- [Evolutionary Multitasking with Solution Space Cutting for Point Cloud Registration](https://arxiv.org/abs/2212.05679) — `registration`
- [Explaining Deep Neural Networks for Point Clouds using Gradient-based Visualisations](https://arxiv.org/abs/2207.12984)
- [Exploring Point-BEV Fusion for 3D Point Cloud Object Tracking with Transformer](https://arxiv.org/abs/2208.05216) — `tracking` `autonomous driving` `BEV`
- [Exploring Singularities in point clouds with the graph Laplacian: An explicit approach](https://arxiv.org/abs/2301.00201)
- [Fast and Scalable Human Pose Estimation using mmWave Point Cloud](https://arxiv.org/abs/2205.00097)
- [Fast Point Cloud Generation with Straight Flows](https://arxiv.org/abs/2212.01747) — `generation` `denoising`
- [Fast-Image2Point: Towards Real-Time Point Cloud Reconstruction of a Single Image using 3D Supervision](https://arxiv.org/abs/2209.10029) — `reconstruction` `efficiency`
- [Feature-based model selection for object detection from point cloud data](https://arxiv.org/abs/2209.12419) — `detection`
- [FEC: Fast Euclidean Clustering for Point Cloud Segmentation](https://arxiv.org/abs/2208.07678) — `segmentation`
- [Few-shot Class-incremental Learning for 3D Point Cloud Objects](https://arxiv.org/abs/2205.15225)
- [Fiducial Tag Localization on a 3D LiDAR Prior Map](https://arxiv.org/abs/2209.01072) — `localization`
- [Fine-resolution landscape-scale biomass mapping using a spatiotemporal patchwork of LiDAR coverages](https://arxiv.org/abs/2205.08530)
- [Fitting and recognition of geometric primitives in segmented 3D point clouds using a localized voting procedure](https://arxiv.org/abs/2205.15426)
- [Flow-based GAN for 3D Point Cloud Generation from a Single Image](https://arxiv.org/abs/2210.04072) — `generation`
- [Frame Mining: a Free Lunch for Learning Robotic Manipulation from 3D Point Clouds](https://arxiv.org/abs/2210.07442)
- [Frequency-Selective Geometry Upsampling of Point Clouds](https://arxiv.org/abs/2205.01458) — `upsampling`
- [Frequency-Selective Mesh-to-Mesh Resampling for Color Upsampling of Point Clouds](https://arxiv.org/abs/2203.09224) — `upsampling`
- [FreSCo: Frequency-Domain Scan Context for LiDAR-based Place Recognition with Translation and Rotation Invariance](https://arxiv.org/abs/2206.12628) — `detection` `localization`
- [From a few Accurate 2D Correspondences to 3D Point Clouds](https://arxiv.org/abs/2206.08749) — `reconstruction`
- [From One to Many: Dynamic Cross Attention Networks for LiDAR and Camera Fusion](https://arxiv.org/abs/2209.12254) — `autonomous driving`
- [FusionRCNN: LiDAR-Camera Fusion for Two-stage 3D Object Detection](https://arxiv.org/abs/2209.10733) — `detection` `autonomous driving` `multi-modal`
- [GeoGCN: Geometric Dual-domain Graph Convolution Network for Point Cloud Denoising](https://arxiv.org/abs/2210.15913) — `denoising`
- [GeoSegNet: Point Cloud Semantic Segmentation via Geometric Encoder-Decoder Modeling](https://arxiv.org/abs/2207.06766) — `segmentation`
- [GFNet: Geometric Flow Network for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2207.02605) — `segmentation` `BEV`
- [GiNGR: Generalized Iterative Non-Rigid Point Cloud and Surface Registration Using Gaussian Process Regression](https://arxiv.org/abs/2203.09986) — `registration`
- [Global Consistent Point Cloud Registration Based on Lie-algebraic Cohomology](https://arxiv.org/abs/2208.07103) — `registration`
- [GPA-Net:No-Reference Point Cloud Quality Assessment with Multi-task Graph Convolutional Network](https://arxiv.org/abs/2210.16478) — `compression`
- [Gradient-based Point Cloud Denoising with Uniformity](https://arxiv.org/abs/2207.10279) — `denoising`
- [Graph Neural Network and Spatiotemporal Transformer Attention for 3D Video Object Detection from Point Clouds](https://arxiv.org/abs/2207.12659) — `detection`
- [GraphFit: Learning Multi-scale Graph-Convolutional Representation for Point Cloud Normal Estimation](https://arxiv.org/abs/2207.11484) — `normal estimation`
- [HAVANA: Hard negAtiVe sAmples aware self-supervised coNtrastive leArning for Airborne laser scanning point clouds semantic segmentation](https://arxiv.org/abs/2210.10626) — `segmentation` `self-supervised`
- [HPGNN: Using Hierarchical Graph Neural Networks for Outdoor Point Cloud Processing](https://arxiv.org/abs/2206.02153)
- [Hypergraph Convolutional Network based Weakly Supervised Point Cloud Semantic Segmentation with Scene-Level Annotations](https://arxiv.org/abs/2211.01174) — `segmentation`
- [Image Understands Point Cloud: Weakly Supervised 3D Semantic Segmentation via Association Learning](https://arxiv.org/abs/2209.07774) — `segmentation`
- [ImLiDAR: Cross-Sensor Dynamic Message Propagation Network for 3D Object Detection](https://arxiv.org/abs/2211.09518) — `detection`
- [ImLoveNet: Misaligned Image-supported Registration Network for Low-overlap Point Cloud Pairs](https://arxiv.org/abs/2207.00826) — `registration`
- [Imperceptible and Robust Backdoor Attack in 3D Point Cloud](https://arxiv.org/abs/2208.08052) — `robustness`
- [Indirect Point Cloud Registration: Aligning Distance Fields using a Pseudo Third Point Ses](https://arxiv.org/abs/2205.15954) — `registration` `reconstruction` — [code](https://github.com/Jarrome/IFR)
- [Information fusion approach for biomass estimation in a plateau mountainous forest using a synergistic system comprising UAS-based digital camera and LiDAR](https://arxiv.org/abs/2204.06746)
- [Inter-Frame Compression for Dynamic Point Cloud Geometry Coding](https://arxiv.org/abs/2207.12554) — `compression` `autonomous driving`
- [IPDAE: Improved Patch-Based Deep Autoencoder for Lossy Point Cloud Geometry Compression](https://arxiv.org/abs/2208.02519) — `compression` `autonomous driving`
- [Isomorphic mesh generation from point clouds with multilayer perceptrons](https://arxiv.org/abs/2210.14157) — `generation`
- [IT/IST/IPLeiria Response to the Call for Proposals on JPEG Pleno Point Cloud Coding](https://arxiv.org/abs/2208.02716)
- [Joint Data and Feature Augmentation for Self-Supervised Representation Learning on Point Clouds](https://arxiv.org/abs/2211.01184) — `self-supervised`
- [Keypoint Cascade Voting for Point Cloud Based 6DoF Pose Estimation](https://arxiv.org/abs/2210.08123) — `segmentation`
- [KSS-ICP: Point Cloud Registration based on Kendall Shape Space](https://arxiv.org/abs/2211.02807) — `registration` `reconstruction`
- [LACV-Net: Semantic Segmentation of Large-Scale Point Cloud Scene via Local Adaptive and Comprehensive VLAD](https://arxiv.org/abs/2210.05870) — `segmentation` `autonomous driving`
- [LAKe-Net: Topology-Aware Point Cloud Completion by Localizing Aligned Keypoints](https://arxiv.org/abs/2203.16771) — `completion`
- [LAPTNet: LiDAR-Aided Perspective Transform Network](https://arxiv.org/abs/2211.14445)
- [Large-Scale LiDAR Consistent Mapping using Hierachical LiDAR Bundle Adjustment](https://arxiv.org/abs/2209.11939) — `reconstruction`
- [Lateral Ego-Vehicle Control without Supervision using Point Clouds](https://arxiv.org/abs/2203.10662)
- [LBF:Learnable Bilateral Filter For Point Cloud Denoising](https://arxiv.org/abs/2210.15950) — `denoising`
- [LCPFormer: Towards Effective 3D Point Cloud Analysis via Local Context Propagation in Transformers](https://arxiv.org/abs/2210.12755)
- [Learning a Task-specific Descriptor for Robust Matching of 3D Point Clouds](https://arxiv.org/abs/2210.14899) — `robustness`
- [Learning Category-Level Manipulation Tasks from Point Clouds with Dynamic Graph CNNs](https://arxiv.org/abs/2209.06331)
- [Learning Dense Features for Point Cloud Registration Using a Graph Attention Network](https://arxiv.org/abs/2206.06731) — `registration` `tracking` `localization` `reconstruction`
- [Learning Digital Terrain Models from Point Clouds: ALS2DTM Dataset and Rasterization-based GAN](https://arxiv.org/abs/2206.03778) — `dataset`
- [Learning Feature Descriptors for Pre- and Intra-operative Point Cloud Matching for Laparoscopic Liver Registration](https://arxiv.org/abs/2211.03688) — `registration`
- [Learning Latent Part-Whole Hierarchies for Point Clouds](https://arxiv.org/abs/2211.07082)
- [Learning Neural Volumetric Field for Point Cloud Geometry Compression](https://arxiv.org/abs/2212.05589) — `compression`
- [Learning Scene Flow in 3D Point Clouds with Noisy Pseudo Labels](https://arxiv.org/abs/2203.12655) — `self-supervised` `scene flow`
- [Learning Spatial and Temporal Variations for 4D Point Cloud Segmentation](https://arxiv.org/abs/2207.04673) — `segmentation` `autonomous driving`
- [Learning to Estimate 3D Human Pose from Point Cloud](https://arxiv.org/abs/2212.12910)
- [Learning to Predict on Octree for Scalable Point Cloud Geometry Coding](https://arxiv.org/abs/2209.02226) — `compression` `denoising`
- [Learning to Simulate Realistic LiDARs](https://arxiv.org/abs/2209.10986) — `generation`
- [Learning-based Lossless Point Cloud Geometry Coding using Sparse Tensors](https://arxiv.org/abs/2204.05043) — `compression`
- [LESS: Label-Efficient Semantic Segmentation for LiDAR Point Clouds](https://arxiv.org/abs/2210.08064) — `segmentation` `autonomous driving` `efficiency`
- [Let Images Give You More:Point Cloud Cross-Modal Training for Shape Analysis](https://arxiv.org/abs/2210.04208)
- [Leveraging Single-View Images for Unsupervised 3D Point Cloud Completion](https://arxiv.org/abs/2212.00564) — `completion`
- [LiDAR Road-Atlas: An Efficient Map Representation for General 3D Urban Environment](https://arxiv.org/abs/2204.05727) — `efficiency`
- [LiDAR-aid Inertial Poser: Large-scale Human Motion Capture by Sparse Inertial and LiDAR Sensors](https://arxiv.org/abs/2205.15410)
- [LiDAR-MIMO: Efficient Uncertainty Estimation for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2206.00214) — `detection` `efficiency`
- [LidarAugment: Searching for Scalable 3D LiDAR Data Augmentations](https://arxiv.org/abs/2210.13488)
- [LiDARCap: Long-range Marker-less 3D Human Motion Capture with LiDAR Point Clouds](https://arxiv.org/abs/2203.14698)
- [LidarCLIP or: How I Learned to Talk to Point Clouds](https://arxiv.org/abs/2212.06858)
- [LinK3D: Linear Keypoints Representation for 3D LiDAR Point Cloud](https://arxiv.org/abs/2206.05927) — `registration` `detection`
- [LOCUS 2.0: Robust and Computationally Efficient Lidar Odometry for Real-Time Underground 3D Mapping](https://arxiv.org/abs/2205.11784) — `localization` `robustness` `efficiency`
- [Lossless Compression of Point Cloud Sequences Using Sequence Optimized CNN Models](https://arxiv.org/abs/2206.01297) — `compression`
- [MAPLE: Masked Pseudo-Labeling autoEncoder for Semi-supervised Point Cloud Action Recognition](https://arxiv.org/abs/2209.00407)
- [MARSIM: A light-weight point-realistic simulator for LiDAR-based UAVs](https://arxiv.org/abs/2211.10716) — `efficiency`
- [Masked Autoencoder for Self-Supervised Pre-training on Lidar Point Clouds](https://arxiv.org/abs/2207.00531) — `detection` `self-supervised` `pre-training`
- [Masked Autoencoders in 3D Point Cloud Representation Learning](https://arxiv.org/abs/2207.01545) — `self-supervised`
- [Masked Surfel Prediction for Self-Supervised Point Cloud Learning](https://arxiv.org/abs/2207.03111) — `self-supervised` — [code](https://github.com/YBZh/MaskSurf)
- [Meta Architecture for Point Cloud Analysis](https://arxiv.org/abs/2211.14462)
- [Meta-Sampler: Almost-Universal yet Task-Oriented Sampling for Point Clouds](https://arxiv.org/abs/2203.16001)
- [Metricizing the Euclidean Space towards Desired Distance Relations in Point Clouds](https://arxiv.org/abs/2211.03674)
- [MM-PCQA: Multi-Modal Learning for No-reference Point Cloud Quality Assessment](https://arxiv.org/abs/2209.00244) — `multi-modal`
- [MODNet: Multi-offset Point Cloud Denoising Network Customized for Multi-scale Patches](https://arxiv.org/abs/2208.14160) — `denoising`
- [MonoSIM: Simulating Learning Behaviors of Heterogeneous Point Cloud Object Detectors for Monocular 3D Object Detection](https://arxiv.org/abs/2208.09446) — `detection` `autonomous driving` `monocular`
- [Motion estimation and filtered prediction for dynamic point cloud attribute compression](https://arxiv.org/abs/2210.08262) — `compression`
- [Multi-Frequency-Aware Patch Adversarial Learning for Neural Point Cloud Rendering](https://arxiv.org/abs/2210.03693) — `robustness`
- [Multi-scale Network with Attentional Multi-resolution Fusion for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2206.13628) — `segmentation`
- [Multi-view Point Cloud Registration based on Evolutionary Multitasking with Bi-Channel Knowledge Sharing Mechanism](https://arxiv.org/abs/2205.02996) — `registration` `reconstruction`
- [Multiscale Latent-Guided Entropy Model for LiDAR Point Cloud Compression](https://arxiv.org/abs/2209.12512) — `compression`
- [NDD: A 3D Point Cloud Descriptor Based on Normal Distribution for Loop Closure Detection](https://arxiv.org/abs/2209.12513) — `detection`
- [Neural Shape Compiler: A Unified Framework for Transforming between Text, Point Cloud, and Program](https://arxiv.org/abs/2212.12952)
- [NeuralBF: Neural Bilateral Filtering for Top-down Instance Segmentation on Point Clouds](https://arxiv.org/abs/2207.09978) — `segmentation` `generation`
- [No-reference Point Cloud Geometry Quality Assessment Based on Pairwise Rank Learning](https://arxiv.org/abs/2211.01205) — `reconstruction` `denoising`
- [Normal Transformer: Extracting Surface Geometry from LiDAR Points Enhanced by Visual Semantics](https://arxiv.org/abs/2211.10580) — `normal estimation` `autonomous driving`
- [Number-Adaptive Prototype Learning for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2210.09948) — `segmentation`
- [Object Scan Context: Object-centric Spatial Descriptor for Place Recognition within 3D Point Cloud Map](https://arxiv.org/abs/2206.03062) — `slam` `localization`
- [Object Segmentation of Cluttered Airborne LiDAR Point Clouds](https://arxiv.org/abs/2210.16081) — `segmentation`
- [Occupancy-MAE: Self-supervised Pre-training Large-scale LiDAR Point Clouds with Masked Occupancy Autoencoders](https://arxiv.org/abs/2206.09900) — `self-supervised` `autonomous driving` `pre-training`
- [One Class One Click: Quasi Scene-level Weakly Supervised Point Cloud Semantic Segmentation with Active Learning](https://arxiv.org/abs/2211.12657) — `segmentation`
- [Online Pole Segmentation on Range Images for Long-term LiDAR Localization in Urban Environments](https://arxiv.org/abs/2208.07364) — `segmentation` `localization`
- [Open-Set Semi-Supervised Learning for 3D Point Cloud Understanding](https://arxiv.org/abs/2205.01006)
- [Optimized SC-F-LOAM: Optimized Fast LiDAR Odometry and Mapping Using Scan Context](https://arxiv.org/abs/2204.04932) — `detection` `slam`
- [OST: Efficient One-stream Network for 3D Single Object Tracking in Point Clouds](https://arxiv.org/abs/2210.08518) — `tracking` `efficiency`
- [P2Net: A Post-Processing Network for Refining Semantic Segmentation of LiDAR Point Cloud based on Consistency of Consecutive Frames](https://arxiv.org/abs/2212.00567) — `segmentation`
- [PaGO-LOAM: Robust Ground-Optimized LiDAR Odometry](https://arxiv.org/abs/2206.00266) — `segmentation` `robustness`
- [PathFusion: Path-consistent Lidar-Camera Deep Feature Fusion](https://arxiv.org/abs/2212.06244) — `detection` `multi-modal`
- [PCDNF: Revisiting Learning-based Point Cloud Denoising via Joint Normal Filtering](https://arxiv.org/abs/2209.00798) — `denoising`
- [PCGen: Point Cloud Generator for LiDAR Simulation](https://arxiv.org/abs/2210.08738) — `generation`
- [PCKRF: Point Cloud Completion and Keypoint Refinement With Fusion Data for 6D Pose Estimation](https://arxiv.org/abs/2210.03437) — `registration` `completion`
- [PCQA-GRAPHPOINT: Efficients Deep-Based Graph Metric For Point Cloud Quality Assessment](https://arxiv.org/abs/2211.02459) — `compression`
- [Performance Evaluation of 3D Keypoint Detectors and Descriptors on Coloured Point Clouds in Subsea Environments](https://arxiv.org/abs/2209.12881)
- [PIDS: Joint Point Interaction-Dimension Search for 3D Point Cloud](https://arxiv.org/abs/2211.15759)
- [PlaneSLAM: Plane-based LiDAR SLAM for Motion Planning in Structured 3D Environments](https://arxiv.org/abs/2209.08248) — `slam` `localization`
- [Planning with Spatial-Temporal Abstraction from Point Clouds for Deformable Object Manipulation](https://arxiv.org/abs/2210.15751)
- [Point Cloud Compression with Sibling Context and Surface Priors](https://arxiv.org/abs/2205.00760) — `compression`
- [Point Cloud Quality Assessment using 3D Saliency Maps](https://arxiv.org/abs/2209.15475) — `detection`
- [Point Cloud Recognition with Position-to-Structure Attention Transformers](https://arxiv.org/abs/2210.02030)
- [Point Cloud Registration of non-rigid objects in sparse 3D Scans with applications in Mixed Reality](https://arxiv.org/abs/2212.03856) — `registration`
- [Point Cloud Registration-Driven Robust Feature Matching for 3D Siamese Object Tracking](https://arxiv.org/abs/2209.06395) — `registration` `tracking` `localization` `robustness`
- [Point Cloud Scene Completion with Joint Color and Semantic Estimation from Single RGB-D Image](https://arxiv.org/abs/2210.05891) — `segmentation` `completion` `reconstruction`
- [Point Cloud Semantic Segmentation using Multi Scale Sparse Convolution Neural Network](https://arxiv.org/abs/2205.01550) — `segmentation`
- [Point Cloud Upsampling via Cascaded Refinement Network](https://arxiv.org/abs/2210.03942) — `upsampling` — [code](https://github.com/hikvision-research/3DVision)
- [Point-DAE: Denoising Autoencoders for Self-supervised Point Cloud Learning](https://arxiv.org/abs/2211.06841) — `self-supervised` `denoising` — [code](https://github.com/YBZh/Point-DAE)
- [Point-E: A System for Generating 3D Point Clouds from Complex Prompts](https://arxiv.org/abs/2212.08751) — `generation`
- [Point-Syn2Real: Semi-Supervised Synthetic-to-Real Cross-Domain Learning for Object Classification in 3D Point Clouds](https://arxiv.org/abs/2210.17009) — `classification` `autonomous driving`
- [Point-Voxel Adaptive Feature Abstraction for Robust Point Cloud Classification](https://arxiv.org/abs/2210.15514) — `classification` `robustness`
- [PointACL:Adversarial Contrastive Learning for Robust Point Clouds Representation under Adversarial Attack](https://arxiv.org/abs/2209.06971) — `self-supervised` `robustness`
- [PointCaM: Cut-and-Mix for Open-Set Point Cloud Learning](https://arxiv.org/abs/2212.02011)
- [PointCAT: Contrastive Adversarial Training for Robust Point Cloud Recognition](https://arxiv.org/abs/2209.07788) — `robustness`
- [PointCLM: A Contrastive Learning-based Framework for Multi-instance Point Cloud Registration](https://arxiv.org/abs/2209.00219) — `registration` `self-supervised`
- [PointCMC: Cross-Modal Multi-Scale Correspondences Learning for Point Cloud Understanding](https://arxiv.org/abs/2211.12032) — `self-supervised`
- [PointDP: Diffusion-driven Purification against Adversarial Attacks on 3D Point Cloud Recognition](https://arxiv.org/abs/2208.09801) — `autonomous driving` `robustness`
- [PointMCD: Boosting Deep Point Cloud Encoders via Multi-view Cross-modal Distillation for 3D Shape Recognition](https://arxiv.org/abs/2207.03128)
- [PointNorm: Dual Normalization is All You Need for Point Cloud Analysis](https://arxiv.org/abs/2207.06324)
- [PointPillars Backbone Type Selection For Fast and Accurate LiDAR Object Detection](https://arxiv.org/abs/2209.15252) — `detection`
- [PointResNet: Residual Network for 3D Point Cloud Segmentation and Classification](https://arxiv.org/abs/2211.11040) — `segmentation` `classification`
- [Points2NeRF: Generating Neural Radiance Fields from 3D point cloud](https://arxiv.org/abs/2206.01290) — `registration` `nerf`
- [PointSee: Image Enhances Point Cloud](https://arxiv.org/abs/2211.01664) — `detection`
- [PolarMix: A General Data Augmentation Technique for LiDAR Point Clouds](https://arxiv.org/abs/2208.00223) — `detection`
- [Ponder: Point Cloud Pre-training via Neural Rendering](https://arxiv.org/abs/2301.00157) — `self-supervised` `pre-training`
- [POS-BERT: Point Cloud One-Stage BERT Pre-Training](https://arxiv.org/abs/2204.00989) — `pre-training`
- [Progressive Knowledge Transfer Based on Human Visual Perception Mechanism for Perceptual Quality Assessment of Point Clouds](https://arxiv.org/abs/2211.16646)
- [Prototype-Aware Heterogeneous Task for Point Cloud Completion](https://arxiv.org/abs/2209.01733) — `completion`
- [Pseudo-LiDAR for Visual Odometry](https://arxiv.org/abs/2209.01567) — `slam`
- [PSNet: Fast Data Structuring for Hierarchical Deep Learning on Point Cloud](https://arxiv.org/abs/2205.14965)
- [PST: Plant segmentation transformer for 3D point clouds of rapeseed plants at the podding stage](https://arxiv.org/abs/2206.13082) — `segmentation`
- [PSTNet: Point Spatio-Temporal Convolution on Point Cloud Sequences](https://arxiv.org/abs/2205.13713)
- [PU-EVA: An Edge Vector based Approximation Solution for Flexible-scale Point Cloud Upsampling](https://arxiv.org/abs/2204.10750) — `reconstruction` `upsampling`
- [PU-MFA : Point Cloud Up-sampling via Multi-scale Features Attention](https://arxiv.org/abs/2208.10968)
- [Push-the-Boundary: Boundary-aware Feature Propagation for Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2212.12402) — `segmentation`
- [R2P: A Deep Learning Model from mmWave Radar to Point Cloud](https://arxiv.org/abs/2207.10690) — `detection` `multi-modal`
- [RaLiBEV: Radar and LiDAR BEV Fusion Learning for Anchor Box Free Object Detection Systems](https://arxiv.org/abs/2211.06108) — `detection` `autonomous driving` `BEV` `multi-modal`
- [RangeSeg: Range-Aware Real Time Segmentation of 3D LiDAR Point Clouds](https://arxiv.org/abs/2205.01570) — `segmentation` `autonomous driving`
- [RangeUDF: Semantic Surface Reconstruction from 3D Point Clouds](https://arxiv.org/abs/2204.09138) — `reconstruction`
- [Rate-Distortion Modeling for Bit Rate Constrained Point Cloud Compression](https://arxiv.org/abs/2211.10646) — `compression`
- [Rate-Distortion Optimal Transform Coefficient Selection for Unoccupied Regions in Video-Based Point Cloud Compression](https://arxiv.org/abs/2206.12186) — `compression`
- [Resolving Class Imbalance for LiDAR-based Object Detector by Dynamic Weight Average and Contextual Ground Truth Sampling](https://arxiv.org/abs/2210.03331) — `detection` `autonomous driving`
- [RGB-L: Enhancing Indirect Visual SLAM using LiDAR-based Dense Depth Maps](https://arxiv.org/abs/2212.02085) — `slam` `generation`
- [RIGA: Rotation-Invariant and Globally-Aware Descriptors for Point Cloud Registration](https://arxiv.org/abs/2209.13252) — `registration`
- [RMS-FlowNet: Efficient and Robust Multi-Scale Scene Flow Estimation for Large-Scale Point Clouds](https://arxiv.org/abs/2204.00354) — `scene flow` `robustness` `efficiency`
- [Road Markings Segmentation from LIDAR Point Clouds using Reflectivity Information](https://arxiv.org/abs/2211.01105) — `segmentation` `detection`
- [Robust Structured Declarative Classifiers for 3D Point Clouds: Defending Adversarial Attacks with Implicit Gradients](https://arxiv.org/abs/2203.15245) — `classification` `reconstruction` `denoising` `robustness`
- [SARNet: Semantic Augmented Registration of Large-Scale Urban Point Clouds](https://arxiv.org/abs/2206.13117) — `registration`
- [sat2pc: Estimating Point Cloud of Building Roofs from 2D Satellite Images](https://arxiv.org/abs/2205.12464) — `generation`
- [Self-Supervised Arbitrary-Scale Point Clouds Upsampling via Implicit Neural Representation](https://arxiv.org/abs/2204.08196) — `self-supervised` `upsampling`
- [Self-Supervised Learning with Multi-View Rendering for 3D Point Cloud Analysis](https://arxiv.org/abs/2210.15904) — `self-supervised`
- [Self-supervised Point Cloud Completion on Real Traffic Scenes via Scene-concerned Bottom-up Mechanism](https://arxiv.org/abs/2203.10569) — `completion` `self-supervised`
- [Self-Supervised Pre-training of 3D Point Cloud Networks with Image Data](https://arxiv.org/abs/2211.11801) — `segmentation` `self-supervised` `pre-training` — Workshop
- [Semantic Geometric Fusion Multi-object Tracking and Lidar Odometry in Dynamic Environment](https://arxiv.org/abs/2204.11621) — `detection` `tracking` `slam` `localization`
- [Semantic localization on BIM-generated maps using a 3D LiDAR sensor](https://arxiv.org/abs/2205.00816) — `localization`
- [Semi-signed prioritized neural fitting for surface reconstruction from unoriented point clouds](https://arxiv.org/abs/2206.06715) — `reconstruction`
- [Sequential Point Clouds: A Survey](https://arxiv.org/abs/2204.09337) — `autonomous driving`
- [SeRP: Self-Supervised Representation Learning Using Perturbed Point Clouds](https://arxiv.org/abs/2209.06067) — `self-supervised`
- [SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds](https://arxiv.org/abs/2206.07636)
- [Shrinking unit: a Graph Convolution-Based Unit for CNN-like 3D Point Cloud Feature Extractors](https://arxiv.org/abs/2209.12770) — `segmentation` `detection` `classification` — [code](https://github.com/albertotamajo/Shrinking-unit)
- [SoftPool++: An Encoder-Decoder Network for Point Cloud Completion](https://arxiv.org/abs/2205.03899) — `completion`
- [Sparse Tensor-based Point Cloud Attribute Compression](https://arxiv.org/abs/2204.01023) — `compression`
- [SPCNet: Stepwise Point Cloud Completion Network](https://arxiv.org/abs/2209.01746) — `completion`
- [Surface Reconstruction from Point Clouds: A Survey and a Benchmark](https://arxiv.org/abs/2205.02413) — `reconstruction` `dataset`
- [Synthetic Point Cloud Generation for Class Segmentation Applications](https://arxiv.org/abs/2205.03738) — `segmentation` `generation`
- [Synthetic-to-Real Domain Generalized Semantic Segmentation for 3D Indoor Point Clouds](https://arxiv.org/abs/2212.04668) — `segmentation`
- [TCDM: Transformational Complexity Based Distortion Metric for Perceptual Point Cloud Quality Assessment](https://arxiv.org/abs/2210.04671)
- [Teacher-Student Network for 3D Point Cloud Anomaly Detection with Few Normal Samples](https://arxiv.org/abs/2210.17258) — `detection` `anomaly detection`
- [Temporal and Spatial Online Integrated Calibration for Camera and LiDAR](https://arxiv.org/abs/2207.10454) — `autonomous driving`
- [The use of Octree in point cloud analysis with application to cultural heritage](https://arxiv.org/abs/2301.06936) — `compression`
- [Time and Cost-Efficient Bathymetric Mapping System using Sparse Point Cloud Generation and Automatic Object Detection](https://arxiv.org/abs/2210.10263) — `detection` `localization` `generation` `efficiency`
- [ToolFlowNet: Robotic Manipulation with Tools via Predicting Tool Flow from Point Clouds](https://arxiv.org/abs/2211.09006) — `segmentation` `classification`
- [TorchSparse: Efficient Point Cloud Inference Engine](https://arxiv.org/abs/2204.10319) — `autonomous driving` `efficiency`
- [Tracking and Reconstructing Hand Object Interactions from Point Cloud Sequences in the Wild](https://arxiv.org/abs/2209.12009) — `tracking` `reconstruction`
- [Transformers for Multi-Object Tracking on Point Clouds](https://arxiv.org/abs/2205.15730) — `detection` `tracking`
- [Transformers for Object Detection in Large Point Clouds](https://arxiv.org/abs/2209.15258) — `detection` `autonomous driving`
- [Transformers in 3D Point Clouds: A Survey](https://arxiv.org/abs/2205.07417)
- [Uncertainty-aware LiDAR Panoptic Segmentation](https://arxiv.org/abs/2210.04472) — `segmentation` `autonomous driving`
- [Understanding Key Point Cloud Features for Development Three-dimensional Adversarial Attacks](https://arxiv.org/abs/2210.14164) — `robustness`
- [UnPWC-SVDLO: Multi-SVD on PointPWC for Unsupervised Lidar Odometry](https://arxiv.org/abs/2205.08150) — `autonomous driving`
- [Unsupervised Domain Adaptation for Point Cloud Semantic Segmentation via Graph Matching](https://arxiv.org/abs/2208.04510) — `segmentation` `domain adaptation`
- [Upsampling Autoencoder for Self-Supervised Point Cloud Learning](https://arxiv.org/abs/2203.10768) — `self-supervised` `upsampling`
- [UTOPIC: Uncertainty-aware Overlap Prediction Network for Partial Point Cloud Registration](https://arxiv.org/abs/2208.02712) — `registration`
- [Visualizing Global Explanations of Point Cloud DNNs](https://arxiv.org/abs/2203.09505) — `autonomous driving`
- [VRNet: Learning the Rectified Virtual Corresponding Points for 3D Point Cloud Registration](https://arxiv.org/abs/2203.13241) — `registration`
- [Weakly Supervised 3D Point Cloud Segmentation via Multi-Prototype Learning](https://arxiv.org/abs/2205.03137) — `segmentation`
- [Weakly Supervised Semantic Segmentation for Large-Scale Point Cloud](https://arxiv.org/abs/2212.04744) — `segmentation`
- [Weighted Bayesian Gaussian Mixture Model for Roadside LiDAR Object Detection](https://arxiv.org/abs/2204.09804) — `detection`
- [WGICP: Differentiable Weighted GICP-Based Lidar Odometry](https://arxiv.org/abs/2209.09777)
- [What Can be Seen is What You Get: Structure Aware Point Cloud Augmentation](https://arxiv.org/abs/2206.09664) — `segmentation`
- [White Matter Tracts are Point Clouds: Neuropsychological Score Prediction and Critical Region Localization via Geometric Deep Learning](https://arxiv.org/abs/2207.02402) — `localization`
- [Window Normalization: Enhancing Point Cloud Understanding by Unifying Inconsistent Point Densities](https://arxiv.org/abs/2212.02287)
- [X-ICP: Localizability-Aware LiDAR Registration for Robust Localization in Extreme Environments](https://arxiv.org/abs/2211.16335) — `registration` `localization` `robustness`

</details>


### 2021 <sub>(533)</sub>

<details><summary><b>CVPR</b> · 47</summary>

- [3D Spatial Recognition without Spatially Labeled 3D](https://arxiv.org/abs/2105.06461) — `segmentation` `detection` `generation`
- [4D Panoptic LiDAR Segmentation](https://arxiv.org/abs/2102.12472) — `segmentation` `autonomous driving`
- [AFDetV2: Rethinking the Necessity of the Second Stage for Object Detection from Point Clouds](https://arxiv.org/abs/2112.09205) — `detection`
- [Back-tracing Representative Points for Voting-based 3D Object Detection in Point Clouds](https://arxiv.org/abs/2104.06114) — `detection`
- [Bidirectional Projection Network for Cross Dimension Scene Understanding](https://arxiv.org/abs/2103.14326)
- [Cloud Sphere: A 3D Shape Representation via Progressive Deformation](https://arxiv.org/abs/2112.11133)
- [Cycle4Completion: Unpaired Point Cloud Completion using Cycle Transformation with Missing Region Coding](https://arxiv.org/abs/2103.07838) — `completion`
- [DeepI2P: Image-to-Point Cloud Registration via Deep Classification](https://arxiv.org/abs/2104.03501) — `registration` `classification`
- [Denoise and Contrast for Category Agnostic Shape Completion](https://arxiv.org/abs/2103.16671) — `completion` `denoising`
- [Diffusion Probabilistic Models for 3D Point Cloud Generation](https://arxiv.org/abs/2103.01458) — `completion` `generation` `upsampling`
- [Equivariant Point Network for 3D Point Cloud Analysis](https://arxiv.org/abs/2103.14147)
- [FESTA: Flow Estimation via Spatial-Temporal Attention for Scene Point Clouds](https://arxiv.org/abs/2104.00798) — `scene flow` `autonomous driving`
- [HCRF-Flow: Scene Flow from Point Clouds with Continuous High-order CRFs and Position-aware Flow Embedding](https://arxiv.org/abs/2105.07751) — `scene flow`
- [High-level camera-LiDAR fusion for 3D object detection with machine learning](https://arxiv.org/abs/2105.11060) — `segmentation` `detection` `autonomous driving` `monocular` — Workshop
- [How Privacy-Preserving are Line Clouds? Recovering Scene Details from 3D Lines](https://arxiv.org/abs/2103.05086) — `localization`
- [HVPR: Hybrid Voxel-Point Representation for Single-stage 3D Object Detection](https://arxiv.org/abs/2104.00902) — `detection`
- [Inferring CAD Modeling Sequences Using Zone Graphs](https://arxiv.org/abs/2104.03900)
- [K-Lane: Lidar Lane Dataset and Benchmark for Urban Roads and Highways](https://arxiv.org/abs/2110.11048) — `detection` `autonomous driving` `dataset`
- [Learning Parallel Dense Correspondence from Spatio-Temporal Descriptors for Efficient and Robust 4D Reconstruction](https://arxiv.org/abs/2103.16341) — `reconstruction` `robustness` `efficiency`
- [Lepard: Learning partial point cloud matching in rigid and deformable scenes](https://arxiv.org/abs/2111.12591) — [code](https://github.com/rabbityl/lepard)
- [LiDAR R-CNN: An Efficient and Universal 3D Object Detector](https://arxiv.org/abs/2103.15297) — `detection` `autonomous driving` `efficiency`
- [Locally Aware Piecewise Transformation Fields for 3D Human Mesh Registration](https://arxiv.org/abs/2104.08160) — `registration`
- [MetaSets: Meta-Learning on Point Sets for Generalizable Representations](https://arxiv.org/abs/2204.07311)
- [Multi-instance Point Cloud Registration by Efficient Correspondence Clustering](https://arxiv.org/abs/2111.14582) — `registration` `efficiency`
- [Omni-supervised Point Cloud Segmentation via Gradual Receptive Field Component Reasoning](https://arxiv.org/abs/2105.10203) — `segmentation`
- [One Thing One Click: A Self-Training Approach for Weakly Supervised 3D Semantic Segmentation](https://arxiv.org/abs/2104.02246) — `segmentation`
- [PAConv: Position Adaptive Convolution with Dynamic Kernel Assembling on Point Clouds](https://arxiv.org/abs/2103.14635)
- [Panoptic-PolarNet: Proposal-free LiDAR Point Cloud Panoptic Segmentation](https://arxiv.org/abs/2103.14962) — `segmentation` `detection`
- [Person-MinkUNet: 3D Person Detection with LiDAR Point Cloud](https://arxiv.org/abs/2107.06780) — `detection` — Workshop
- [Point Cloud Upsampling via Disentangled Refinement](https://arxiv.org/abs/2106.04779) — `upsampling`
- [PointDSC: Robust Point Cloud Registration using Deep Spatial Consistency](https://arxiv.org/abs/2103.05465) — `registration` `robustness`
- [PointGuard: Provably Robust 3D Point Cloud Classification](https://arxiv.org/abs/2103.03046) — `classification` `autonomous driving` `robustness`
- [ReAgent: Point Cloud Registration using Imitation and Reinforcement Learning](https://arxiv.org/abs/2103.15231) — `registration`
- [Regularization Strategy for Point Cloud via Rigidly Mixed Sample](https://arxiv.org/abs/2102.01929)
- [Robust Point Cloud Registration Framework Based on Deep Graph Matching](https://arxiv.org/abs/2103.04256) — `registration` `robustness` — [code](https://github.com/fukexue/RGM)
- [RPSRNet: End-to-End Trainable Rigid Point Set Registration Network using Barnes-Hut $2^D$-Tree Representation](https://arxiv.org/abs/2104.05328) — `registration`
- [SE-SSD: Self-Ensembling Single-Stage Object Detector From Point Cloud](https://arxiv.org/abs/2104.09804) — `detection`
- [Self-Point-Flow: Self-Supervised Scene Flow Estimation from Point Clouds with Optimal Transport and Random Walk](https://arxiv.org/abs/2105.08248) — `self-supervised` `scene flow`
- [Self-Supervised Pillar Motion Learning for Autonomous Driving](https://arxiv.org/abs/2104.08683) — `self-supervised` `autonomous driving`
- [Semantic Segmentation for Real Point Cloud Scenes via Bilateral Augmentation and Adaptive Fusion](https://arxiv.org/abs/2103.07074) — `segmentation`
- [SeqNetVLAD vs PointNetVLAD: Image Sequence vs 3D Point Clouds for Day-Night Place Recognition](https://arxiv.org/abs/2106.11481) — `localization` — Workshop
- [ST3D: Self-training for Unsupervised Domain Adaptation on 3D Object Detection](https://arxiv.org/abs/2103.05346) — `detection` `domain adaptation`
- [StablePose: Learning 6D Object Poses from Geometrically Stable Patches](https://arxiv.org/abs/2102.09334)
- [TPCN: Temporal Point Cloud Networks for Motion Forecasting](https://arxiv.org/abs/2103.03067)
- [Variational Relational Point Completion Network](https://arxiv.org/abs/2104.10154) — `completion`
- [View-Guided Point Cloud Completion](https://arxiv.org/abs/2104.05666) — `completion`
- [VoxelContext-Net: An Octree based Framework for Point Cloud Compression](https://arxiv.org/abs/2105.02158) — `compression`

</details>

<details><summary><b>ICCV</b> · 62</summary>

- [(Just) A Spoonful of Refinements Helps the Registration Error Go Down](https://arxiv.org/abs/2108.03257) — `registration`
- [4D-Net for Learned Multi-Modal Alignment](https://arxiv.org/abs/2109.01066) — `detection` `multi-modal`
- [A Robust Loss for Point Cloud Registration](https://arxiv.org/abs/2108.11682) — `registration` `robustness`
- [A Technical Survey and Evaluation of Traditional Point Cloud Clustering Methods for LiDAR Panoptic Segmentation](https://arxiv.org/abs/2108.09522) — `segmentation` `autonomous driving` — [code](https://github.com/placeforyiming/ICCVW21-LiDAR-Panoptic-Segmentation-TradiCV-Survey-of-Point-Cloud-Cluster) Workshop
- [AdaFit: Rethinking Learning-based Normal Estimation on Point Clouds](https://arxiv.org/abs/2108.05836) — `normal estimation`
- [Adaptive Graph Convolution for Point Cloud Analysis](https://arxiv.org/abs/2108.08035)
- [An End-to-End Transformer Model for 3D Object Detection](https://arxiv.org/abs/2109.08141) — `detection`
- [Box-Aware Feature Enhancement for Single Object Tracking on Point Clouds](https://arxiv.org/abs/2108.04728) — `tracking`
- [CAPTRA: CAtegory-level Pose Tracking for Rigid and Articulated Objects from Point Clouds](https://arxiv.org/abs/2104.03437) — `tracking`
- [CPFN: Cascaded Primitive Fitting Networks for High-Resolution Point Clouds](https://arxiv.org/abs/2109.00113)
- [CSG-Stump: A Learning Friendly CSG-Like Representation for Interpretable Shape Parsing](https://arxiv.org/abs/2108.11305)
- [Deep Hough Voting for Robust Global Registration](https://arxiv.org/abs/2109.04310) — `registration` `robustness`
- [Deep Hybrid Self-Prior for Full 3D Mesh Generation](https://arxiv.org/abs/2108.08017) — `generation` `reconstruction`
- [Deep Models with Fusion Strategies for MVP Point Cloud Registration](https://arxiv.org/abs/2110.09129) — `registration` — Workshop
- [DeepCAD: A Deep Generative Network for Computer-Aided Design Models](https://arxiv.org/abs/2105.09492) — `generation`
- [DRINet: A Dual-Representation Iterative Learning Network for Point Cloud Segmentation](https://arxiv.org/abs/2108.04023) — `segmentation`
- [Dynamical Pose Estimation](https://arxiv.org/abs/2103.06182) — `registration` — [code](https://github.com/hankyang94/DAMP)
- [Exploring Simple 3D Multi-Object Tracking for Autonomous Driving](https://arxiv.org/abs/2108.10312) — `detection` `tracking` `autonomous driving`
- [Fog Simulation on Real LiDAR Point Clouds for 3D Object Detection in Adverse Weather](https://arxiv.org/abs/2108.05249) — `detection`
- [Fooling LiDAR Perception via Adversarial Trajectory Perturbation](https://arxiv.org/abs/2103.15326) — `robustness`
- [Guided Point Contrastive Learning for Semi-supervised Point Cloud Semantic Segmentation](https://arxiv.org/abs/2110.08188) — `segmentation` `self-supervised`
- [Hierarchical Aggregation for 3D Instance Segmentation](https://arxiv.org/abs/2108.02350) — `segmentation`
- [HPNet: Deep Primitive Segmentation Using Hybrid Representations](https://arxiv.org/abs/2105.10620) — `segmentation`
- [HRegNet: A Hierarchical Network for Large-scale Outdoor LiDAR Point Cloud Registration](https://arxiv.org/abs/2107.11992) — `registration`
- [Improving 3D Object Detection with Channel-wise Transformer](https://arxiv.org/abs/2108.10723) — `detection`
- [InstanceRefer: Cooperative Holistic Understanding for Visual Grounding on Point Clouds through Instance Multi-level Contextual Referring](https://arxiv.org/abs/2103.01128) — `localization` — [code](https://github.com/CurryYuan/InstanceRefer)
- [Learning Inner-Group Relations on Point Clouds](https://arxiv.org/abs/2108.12468)
- [Learning with Noisy Labels for Robust Point Cloud Segmentation](https://arxiv.org/abs/2107.14230) — `segmentation` `robustness`
- [LIGA-Stereo: Learning LiDAR Geometry Aware Representations for Stereo-based 3D Detector](https://arxiv.org/abs/2108.08258) — `detection`
- [LSG-CPD: Coherent Point Drift with Local Surface Geometry for Point Cloud Registration](https://arxiv.org/abs/2103.15039) — `registration`
- [MCTS with Refinement for Proposals Selection Games in Scene Understanding](https://arxiv.org/abs/2207.03204) — `reconstruction` — [code](https://github.com/vevenom/MonteScene)
- [ME-PCN: Point Completion Conditioned on Mask Emptiness](https://arxiv.org/abs/2108.08187) — `completion`
- [MonteFloor: Extending MCTS for Reconstructing Accurate Large-Scale Floor Plans](https://arxiv.org/abs/2103.11161) — `reconstruction`
- [Multi-View Partial (MVP) Point Cloud Challenge 2021 on Completion and Registration: Methods and Results](https://arxiv.org/abs/2112.12053) — `registration` `completion` `reconstruction` — [code](https://github.com/paul007pl/MVP_Benchmark) Workshop
- [Out-of-Core Surface Reconstruction via Global $TGV$ Minimization](https://arxiv.org/abs/2107.14790) — `reconstruction`
- [P2-Net: Joint Description and Detection of Local Features for Pixel and Point Matching](https://arxiv.org/abs/2103.01055) — `detection`
- [PCAM: Product of Cross-Attention Matrices for Rigid Registration of Point Clouds](https://arxiv.org/abs/2110.01269) — `registration`
- [PICCOLO: Point Cloud-Centric Omnidirectional Localization](https://arxiv.org/abs/2108.06545) — `localization`
- [Point Cloud Augmentation with Weighted Local Transformations](https://arxiv.org/abs/2110.05379)
- [Point-Based Modeling of Human Clothing](https://arxiv.org/abs/2104.08230)
- [Point-set Distances for Learning Representations of 3D Point Clouds](https://arxiv.org/abs/2102.04014)
- [PointBA: Towards Backdoor Attacks in 3D Point Cloud](https://arxiv.org/abs/2103.16074)
- [PoinTr: Diverse Point Cloud Completion with Geometry-Aware Transformers](https://arxiv.org/abs/2108.08839) — `completion`
- [Progressive Seed Generation Auto-encoder for Unsupervised Point Cloud Learning](https://arxiv.org/abs/2112.05213) — `generation` `reconstruction`
- [Pyramid R-CNN: Towards Better Performance and Adaptability for 3D Object Detection](https://arxiv.org/abs/2109.02499) — `detection`
- [RandomRooms: Unsupervised Pre-training from Synthetic Shapes and Randomized Layouts for 3D Object Detection](https://arxiv.org/abs/2108.07794) — `detection` `pre-training`
- [ReDAL: Region-based and Diversity-aware Active Learning for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2107.11769) — `segmentation` — [code](https://github.com/tsunghan-wu/ReDAL)
- [Robustness Certification for Point Cloud Models](https://arxiv.org/abs/2103.16652) — `autonomous driving` `robustness`
- [SA-ConvONet: Sign-Agnostic Optimization of Convolutional Occupancy Networks](https://arxiv.org/abs/2105.03582) — `reconstruction`
- [Sampling Network Guided Cross-Entropy Method for Unsupervised Point Cloud Registration](https://arxiv.org/abs/2109.06619) — `registration`
- [SAT: 2D Semantics Assisted Training for 3D Visual Grounding](https://arxiv.org/abs/2105.11450)
- [Score-Based Point Cloud Denoising](https://arxiv.org/abs/2107.10981) — `reconstruction` `denoising`
- [SnowflakeNet: Point Cloud Completion by Snowflake Point Deconvolution with Skip-Transformer](https://arxiv.org/abs/2108.04444) — `completion`
- [Sparse-to-dense Feature Matching: Intra and Inter domain Cross-modal Learning in Domain Adaptation for 3D Semantic Segmentation](https://arxiv.org/abs/2107.14724) — `segmentation` `domain adaptation`
- [Spatio-temporal Self-Supervised Representation Learning for 3D Point Clouds](https://arxiv.org/abs/2109.00179) — `self-supervised`
- [Temporally-Coherent Surface Reconstruction via Metric-Consistent Atlases](https://arxiv.org/abs/2104.06950) — `reconstruction`
- [Towards Efficient Point Cloud Graph Neural Networks Through Architectural Simplification](https://arxiv.org/abs/2108.06317) — `efficiency` — Workshop
- [Unsupervised Learning of Fine Structure Generation for 3D Point Clouds by 2D Projection Matching](https://arxiv.org/abs/2108.03746) — `generation` — [code](https://github.com/chenchao15/2D)
- [Vis2Mesh: Efficient Mesh Reconstruction from Unstructured Point Clouds of Large Scenes with Learned Virtual View Visibility](https://arxiv.org/abs/2108.08378) — `completion` `generation` `reconstruction` `efficiency`
- [Voxel Transformer for 3D Object Detection](https://arxiv.org/abs/2109.02497) — `detection` `localization`
- [Voxel-based Network for Shape Completion by Leveraging Edge Generation](https://arxiv.org/abs/2108.09936) — `completion` `generation`
- [Walk in the Cloud: Learning Curves for Point Clouds Shape Analysis](https://arxiv.org/abs/2105.01288)

</details>

<details><summary><b>NeurIPS</b> · 11</summary>

- [3D Siamese Voxel-to-BEV Tracker for Sparse Point Clouds](https://arxiv.org/abs/2111.04426) — `tracking` `localization` `BEV`
- [Accurate Point Cloud Registration with Robust Optimal Transport](https://arxiv.org/abs/2111.00648) — `registration` `robustness`
- [ASSANet: An Anisotropic Separable Set Abstraction for Efficient Point Cloud Representation Learning](https://arxiv.org/abs/2110.10538) — `efficiency` — [code](https://github.com/guochengqian/ASSANet)
- [CoFiNet: Reliable Coarse-to-fine Correspondences for Robust Point Cloud Registration](https://arxiv.org/abs/2110.14076) — `registration` `robustness`
- [Density-aware Chamfer Distance as a Comprehensive Metric for Point Cloud Completion](https://arxiv.org/abs/2111.12702) — `completion`
- [Garment4D: Garment Reconstruction from Point Cloud Sequences](https://arxiv.org/abs/2112.04159) — `reconstruction` — [code](https://github.com/hongfz16/Garment4D)
- [Instance Segmentation GNNs for One-Shot Conformal Tracking at the LHC](https://arxiv.org/abs/2103.06509) — `segmentation` `detection` `tracking` — Workshop
- [Multimodal Virtual Point 3D Detection](https://arxiv.org/abs/2111.06881) — `detection` `autonomous driving` `multi-modal`
- [Object DGCNN: 3D Object Detection using Dynamic Graphs](https://arxiv.org/abs/2110.06923) — `detection`
- [PolarStream: Streaming Lidar Object Detection and Segmentation with Polar Pillars](https://arxiv.org/abs/2106.07545) — `segmentation` `detection` — [code](https://github.com/motional/polarstream)
- [Shape As Points: A Differentiable Poisson Solver](https://arxiv.org/abs/2106.03452) — `reconstruction` — [code](https://github.com/autonomousvision/shape_as_points)

</details>

<details><summary><b>ICLR</b> · 4</summary>

- [A Conditional Point Diffusion-Refinement Paradigm for 3D Point Cloud Completion](https://arxiv.org/abs/2112.03530) — `completion` — [code](https://github.com/ZhaoyangLyu/Point_Diffusion_Refinement)
- [Deep Convolution for Irregularly Sampled Temporal Point Clouds](https://arxiv.org/abs/2105.00137)
- [Deep Point Cloud Reconstruction](https://arxiv.org/abs/2111.11704) — `reconstruction` `denoising`
- [Voint Cloud: Multi-View Point Cloud Representation for 3D Understanding](https://arxiv.org/abs/2111.15363) — `segmentation` `classification` — [code](https://github.com/ajhamdi/vointcloud)

</details>

<details><summary><b>ICML</b> · 3</summary>

- [Representation Topology Divergence: A Method for Comparing Neural Network Representations](https://arxiv.org/abs/2201.00058)
- [Revisiting Point Cloud Shape Classification with a Simple and Effective Baseline](https://arxiv.org/abs/2106.05304) — `classification`
- [Scalable Certified Segmentation via Randomized Smoothing](https://arxiv.org/abs/2107.00228) — `segmentation`

</details>

<details><summary><b>AAAI</b> · 8</summary>

- [Adversarial Attack for Asynchronous Event-based Data](https://arxiv.org/abs/2112.13534) — `autonomous driving` `robustness`
- [Boundary-Aware Geometric Encoding for Semantic Segmentation of Point Clouds](https://arxiv.org/abs/2101.02381) — `segmentation`
- [DeepDT: Learning Geometry From Delaunay Triangulation for Surface Reconstruction](https://arxiv.org/abs/2101.10353) — `reconstruction`
- [DetarNet: Decoupling Translation and Rotation by Siamese Network for Point Cloud Registration](https://arxiv.org/abs/2112.14059) — `registration`
- [Investigate Indistinguishable Points in Semantic Segmentation of 3D Point Cloud](https://arxiv.org/abs/2103.10339) — `segmentation`
- [SCTN: Sparse Convolution-Transformer Network for Scene Flow Estimation](https://arxiv.org/abs/2105.04447) — `scene flow`
- [SimIPU: Simple 2D Image and 3D Point Cloud Unsupervised Pre-Training for Spatial-Aware Visual Representations](https://arxiv.org/abs/2112.04680) — `pre-training`
- [SSPC-Net: Semi-supervised Semantic 3D Point Cloud Segmentation Network](https://arxiv.org/abs/2104.07861) — `segmentation` — [code](https://github.com/MMCheng/SSPC-Net)

</details>

<details><summary><b>IJCAI</b> · 5</summary>

- [2nd Place Solution for IJCAI-PRICAI 2020 3D AI Challenge: 3D Object Reconstruction from A Single Image](https://arxiv.org/abs/2105.13575) — `reconstruction`
- [Planning with Learned Dynamic Model for Unsupervised Point Cloud Registration](https://arxiv.org/abs/2108.02613) — `registration`
- [Point-based Acoustic Scattering for Interactive Sound Propagation via Surface Encoding](https://arxiv.org/abs/2105.08177)
- [PointLIE: Locally Invertible Embedding for Point Cloud Sampling and Recovery](https://arxiv.org/abs/2104.14769)
- [VR3Dense: Voxel Representation Learning for 3D Object Detection and Monocular Dense Depth Reconstruction](https://arxiv.org/abs/2104.05932) — `detection` `reconstruction` `autonomous driving` `monocular` — Workshop

</details>

<details><summary><b>SIGGRAPH</b> · 3</summary>

- [DeltaConv: Anisotropic Operators for Geometric Deep Learning on Point Clouds](https://arxiv.org/abs/2111.08799)
- [Orienting Point Clouds with Dipole Propagation](https://arxiv.org/abs/2105.01604)
- [SP-GAN: Sphere-Guided 3D Shape Generation and Manipulation](https://arxiv.org/abs/2108.04476) — `generation`

</details>

<details><summary><b>ACM MM</b> · 6</summary>

- [Neighbor-Vote: Improving Monocular 3D Object Detection through Neighbor Distance Voting](https://arxiv.org/abs/2107.02493) — `detection` `generation` `autonomous driving` `monocular`
- [Patch-Based Deep Autoencoder for Point Cloud Geometry Compression](https://arxiv.org/abs/2110.09109) — `reconstruction` `compression`
- [PC$^2$-PU: Patch Correlation and Point Correlation for Effective Point Cloud Upsampling](https://arxiv.org/abs/2109.09337) — `upsampling`
- [Self-Contrastive Learning with Hard Negative Sampling for Self-supervised Point Cloud Learning](https://arxiv.org/abs/2107.01886) — `self-supervised`
- [SSPU-Net: Self-Supervised Point Cloud Upsampling via Differentiable Rendering](https://arxiv.org/abs/2108.00454) — `self-supervised` `upsampling`
- [You Only Hypothesize Once: Point Cloud Registration with Rotation-equivariant Descriptors](https://arxiv.org/abs/2109.00182) — `registration`

</details>

<details><summary><b>3DV</b> · 13</summary>

- [3D Point Cloud Registration with Multi-Scale Architecture and Unsupervised Transfer Learning](https://arxiv.org/abs/2103.14533) — `registration`
- [AA3DNet: Attention Augmented Real Time 3D Object Detection](https://arxiv.org/abs/2107.12137) — `detection`
- [DeepBBS: Deep Best Buddies for Point Cloud Registration](https://arxiv.org/abs/2110.03016) — `registration`
- [DPC: Unsupervised Deep Point Correspondence via Cross and Self Construction](https://arxiv.org/abs/2110.08636)
- [DSP-SLAM: Object Oriented SLAM with Deep Shape Priors](https://arxiv.org/abs/2108.09481) — `slam`
- [Generative Zero-Shot Learning for Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2108.06230) — `segmentation` `classification` `generation` `open-vocabulary` — [code](https://github.com/valeoai/3DGenZ)
- [Investigating Attention Mechanism in 3D Point Cloud Object Detection](https://arxiv.org/abs/2108.00620) — `detection` `autonomous driving`
- [LiDAR-based Recurrent 3D Semantic Segmentation with Temporal Memory Alignment](https://arxiv.org/abs/2103.02263) — `segmentation`
- [NeeDrop: Self-supervised Shape Representation from Sparse Point Clouds using Needle Dropping](https://arxiv.org/abs/2111.15207) — `self-supervised`
- [Occlusion Guided Self-supervised Scene Flow Estimation on 3D Point Clouds](https://arxiv.org/abs/2104.04724) — `self-supervised` `scene flow` `autonomous driving`
- [Point Discriminative Learning for Data-efficient 3D Point Cloud Analysis](https://arxiv.org/abs/2108.02104) — `classification` `efficiency`
- [RefRec: Pseudo-labels Refinement via Shape Reconstruction for Unsupervised 3D Domain Adaptation](https://arxiv.org/abs/2110.11036) — `classification` `reconstruction` `domain adaptation` — [code](https://github.com/CVLAB-Unibo/RefRec)
- [Representing Shape Collections with Alignment-Aware Linear Models](https://arxiv.org/abs/2109.01605)

</details>

<details><summary><b>WACV</b> · 2</summary>

- [EllipsoidNet: Ellipsoid Representation for Point Cloud Classification and Segmentation](https://arxiv.org/abs/2103.02517) — `segmentation` `classification`
- [Geometry-Aware Hierarchical Bayesian Learning on Manifolds](https://arxiv.org/abs/2111.00184) — `classification`

</details>

<details><summary><b>BMVC</b> · 10</summary>

- [Cascading Feature Extraction for Fast Point Cloud Registration](https://arxiv.org/abs/2110.12204) — `registration`
- [DeepUME: Learning the Universal Manifold Embedding for Robust Point Cloud Registration](https://arxiv.org/abs/2112.09938) — `registration` `robustness`
- [FAST3D: Flow-Aware Self-Training for 3D Object Detectors](https://arxiv.org/abs/2110.09355) — `autonomous driving`
- [Local and Global Point Cloud Reconstruction for 3D Hand Pose Estimation](https://arxiv.org/abs/2112.06389) — `reconstruction`
- [Multimodal Semi-Supervised Learning for 3D Objects](https://arxiv.org/abs/2110.11601) — `classification` `multi-modal`
- [On Automatic Data Augmentation for 3D Point Cloud Classification](https://arxiv.org/abs/2112.06029) — `classification` `generation`
- [POEM: 1-bit Point-wise Operations based on Expectation-Maximization for Efficient Point Cloud Processing](https://arxiv.org/abs/2111.13386) — `efficiency`
- [Self-Supervised Point Cloud Completion via Inpainting](https://arxiv.org/abs/2111.10701) — `completion` `tracking` `self-supervised`
- [Two Heads are Better than One: Geometric-Latent Attention for Point Cloud Classification and Segmentation](https://arxiv.org/abs/2111.00231) — `segmentation` `classification`
- [VIN: Voxel-based Implicit Network for Joint 3D Object Detection and Segmentation for Lidars](https://arxiv.org/abs/2107.02980) — `segmentation` `detection`

</details>

<details><summary><b>ICRA</b> · 21</summary>

- [A Divide-and-Merge Point Cloud Clustering Algorithm for LiDAR Panoptic Segmentation](https://arxiv.org/abs/2109.08224) — `segmentation` `autonomous driving` — [code](https://github.com/placeforyiming/Divide-and-Merge-LiDAR-Panoptic-Cluster)
- [CloudAAE: Learning 6D Object Pose Regression with On-line Data Synthesis on Point Clouds](https://arxiv.org/abs/2103.01977)
- [CPSeg: Cluster-free Panoptic Segmentation of 3D LiDAR Point Clouds](https://arxiv.org/abs/2111.01723) — `segmentation` `autonomous driving`
- [DC-Loc: Accurate Automotive Radar Based Metric Localization with Explicit Doppler Compensation](https://arxiv.org/abs/2112.14887) — `localization` `multi-modal`
- [Detecting and Mapping Trees in Unstructured Environments with a Stereo Camera and Pseudo-Lidar](https://arxiv.org/abs/2103.15967) — `detection`
- [ERASOR: Egocentric Ratio of Pseudo Occupancy-based Dynamic Object Removal for Static 3D Point Cloud Map Building](https://arxiv.org/abs/2103.04316)
- [Exploiting Local Geometry for Feature and Graph Construction for Better 3D Point Cloud Processing with Graph Neural Networks](https://arxiv.org/abs/2103.15226)
- [FGR: Frustum-Aware Geometric Reasoning for Weakly Supervised 3D Vehicle Detection](https://arxiv.org/abs/2105.07647) — `detection`
- [How to Build a Curb Dataset with LiDAR Data for Autonomous Driving](https://arxiv.org/abs/2110.03968) — `detection` `autonomous driving` `dataset`
- [Learning the Next Best View for 3D Point Clouds via Topological Features](https://arxiv.org/abs/2103.02789)
- [Learning Visual Shape Control of Novel 3D Deformable Objects from Partial-View Point Clouds](https://arxiv.org/abs/2110.04685)
- [Lifting 2D Object Locations to 3D by Discounting LiDAR Outliers across Objects and Views](https://arxiv.org/abs/2109.07945)
- [LiTAMIN2: Ultra Light LiDAR-based SLAM using Geometric Approximation applied with KL-Divergence](https://arxiv.org/abs/2103.00784) — `registration` `detection` `tracking` `slam`
- [LoGG3D-Net: Locally Guided Global Descriptor Learning for 3D Place Recognition](https://arxiv.org/abs/2109.08336) — `slam` `localization`
- [RGB Matters: Learning 7-DoF Grasp Poses on Monocular RGBD Images](https://arxiv.org/abs/2103.02184) — `monocular`
- [Robust Place Recognition using an Imaging Lidar](https://arxiv.org/abs/2103.02111) — `localization` `robustness`
- [SA-LOAM: Semantic-aided LiDAR SLAM with Loop Closure](https://arxiv.org/abs/2106.11516) — `segmentation` `detection` `slam`
- [Simple But Effective Redundant Odometry for Autonomous Vehicles](https://arxiv.org/abs/2105.11783) — `monocular` — [code](https://github.com/PRBonn/MutiverseOdometry)
- [Superpoint-guided Semi-supervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2107.03601) — `segmentation`
- [Teat Pose Estimation via RGBD Segmentation for Automated Milking](https://arxiv.org/abs/2105.09843) — `segmentation` — Workshop
- [Volumetric Propagation Network: Stereo-LiDAR Fusion for Long-Range Depth Estimation](https://arxiv.org/abs/2103.12964)

</details>

<details><summary><b>IROS</b> · 15</summary>

- [Active Visuo-Tactile Point Cloud Registration for Accurate Pose Estimation of Objects in an Unknown Workspace](https://arxiv.org/abs/2108.04015) — `registration`
- [CRLF: Automatic Calibration and Refinement based on Line Feature for LiDAR and Camera in Road Scenes](https://arxiv.org/abs/2103.04558)
- [FIDNet: LiDAR Point Cloud Semantic Segmentation with Fully Interpolation Decoding](https://arxiv.org/abs/2109.03787) — `segmentation` — [code](https://github.com/placeforyiming/IROS21-FIDNet-SemanticKITTI)
- [Graph-Guided Deformation for Point Cloud Completion](https://arxiv.org/abs/2112.01840) — `completion` `generation`
- [Identification and Avoidance of Static and Dynamic Obstacles on Point Cloud for UAVs Navigation](https://arxiv.org/abs/2105.06622)
- [Learning to Detect Multi-Modal Grasps for Dexterous Grasping in Dense Clutter](https://arxiv.org/abs/2106.03919) — `detection` `multi-modal`
- [Moving Object Segmentation in 3D LiDAR Data: A Learning-based Approach Exploiting Sequential Data](https://arxiv.org/abs/2105.08971) — `segmentation`
- [Multi-View Fusion for Multi-Level Robotic Scene Understanding](https://arxiv.org/abs/2103.13539)
- [On Enhancing Ground Surface Detection from Sparse Lidar Point Cloud](https://arxiv.org/abs/2105.11649) — `detection` `autonomous driving`
- [PLUMENet: Efficient 3D Object Detection from Stereo Images](https://arxiv.org/abs/2101.06594) — `detection` `autonomous driving` `efficiency`
- [PTT: Point-Track-Transformer Module for 3D Single Object Tracking in Point Clouds](https://arxiv.org/abs/2108.06455) — `tracking`
- [Similarity-Aware Fusion Network for 3D Semantic Segmentation](https://arxiv.org/abs/2107.01579) — `segmentation`
- [Sparse PointPillars: Maintaining and Exploiting Input Sparsity to Improve Runtime on Embedded Systems](https://arxiv.org/abs/2106.06882) — `detection` `BEV`
- [SpectGRASP: Robotic Grasping by Spectral Correlation](https://arxiv.org/abs/2107.12492)
- [SSC: Semantic Scan Context for Large-Scale Place Recognition](https://arxiv.org/abs/2107.00382) — `slam` `localization`

</details>

<details><summary><b>RA-L</b> · 12</summary>

- [BVMatch: Lidar-based Place Recognition Using Bird's-eye View Images](https://arxiv.org/abs/2109.00317) — `localization`
- [Cross-Modal Contrastive Learning of Representations for Navigation using Lightweight, Low-Cost Millimeter Wave Radar for Adverse Environmental Conditions](https://arxiv.org/abs/2101.03525) — `self-supervised` `multi-modal` `efficiency`
- [Direct LiDAR Odometry: Fast Localization with Dense Point Clouds](https://arxiv.org/abs/2110.00605) — `localization`
- [Efficient LiDAR Odometry for Autonomous Driving](https://arxiv.org/abs/2104.10879) — `registration` `localization` `autonomous driving` `efficiency`
- [Fast and Robust Registration of Partially Overlapping Point Clouds](https://arxiv.org/abs/2112.09922) — `registration` `slam` `robustness`
- [ICM-3D: Instantiated Category Modeling for 3D Instance Segmentation](https://arxiv.org/abs/2108.11771) — `segmentation`
- [iCurb: Imitation Learning-based Detection of Road Curbs using Aerial Images for Autonomous Driving](https://arxiv.org/abs/2103.17118) — `detection` `autonomous driving`
- [Loop closure detection using local 3D deep descriptors](https://arxiv.org/abs/2111.00440) — `detection` `localization`
- [LRGNet: Learnable Region Growing for Class-Agnostic Point Cloud Segmentation](https://arxiv.org/abs/2103.09160) — `segmentation`
- [RANSIC: Fast and Highly Robust Estimation for Rotation Search and Point Cloud Registration using Invariant Compatibility](https://arxiv.org/abs/2104.09133) — `registration` `robustness`
- [Stein ICP for Uncertainty Estimation in Point Cloud Matching](https://arxiv.org/abs/2106.03287)
- [TriVoC: Efficient Voting-based Consensus Maximization for Robust Point Cloud Registration with Extreme Outlier Ratios](https://arxiv.org/abs/2111.00657) — `registration` `robustness` `efficiency`

</details>

<details><summary><b>TPAMI</b> · 4</summary>

- [Cylindrical and Asymmetrical 3D Convolution Networks for LiDAR-based Perception](https://arxiv.org/abs/2109.05441) — `segmentation` `detection` — [code](https://github.com/xinge008/Cylinder3D)
- [EPNet++: Cascade Bi-directional Fusion for Multi-Modal 3D Object Detection](https://arxiv.org/abs/2112.11088) — `detection` `multi-modal`
- [Learning Semantic Segmentation of Large-Scale Point Clouds with Random Sampling](https://arxiv.org/abs/2107.02389) — `segmentation`
- [Revisiting Transformation Invariant Geometric Deep Learning: An Initial Representation Perspective](https://arxiv.org/abs/2112.12345)

</details>

<details><summary><b>IJCV</b> · 1</summary>

- [PV-RCNN++: Point-Voxel Feature Set Abstraction With Local Vector Representation for 3D Object Detection](https://arxiv.org/abs/2102.00463) — `detection` — [code](https://github.com/open-mmlab/OpenPCDet)

</details>

<details><summary><b>TVCG</b> · 3</summary>

- [Consistent Two-Flow Network for Tele-Registration of Point Clouds](https://arxiv.org/abs/2106.00329) — `registration`
- [Meta-PU: An Arbitrary-Scale Upsampling Network for Point Cloud](https://arxiv.org/abs/2102.04317) — `reconstruction` `upsampling`
- [WSDesc: Weakly Supervised 3D Local Descriptor Learning for Point Cloud Registration](https://arxiv.org/abs/2108.02740) — `registration`

</details>

<details><summary><b>ISPRS</b> · 4</summary>

- [3D Surface Reconstruction From Multi-Date Satellite Images](https://arxiv.org/abs/2102.02502) — `reconstruction`
- [GlobalMatch: Registration of Forest Terrestrial Point Clouds by Global Matching of Relative Stem Positions](https://arxiv.org/abs/2112.11121) — `registration`
- [Reconstructing Compact Building Models from Point Clouds Using Deep Implicit Fields](https://arxiv.org/abs/2112.13142) — `reconstruction`
- [Weakly Supervised Pseudo-Label assisted Learning for ALS Point Cloud Semantic Segmentation](https://arxiv.org/abs/2105.01919) — `segmentation`

</details>

<details><summary><b>PR</b> · 5</summary>

- [BADet: Boundary-Aware 3D Object Detection from Point Clouds](https://arxiv.org/abs/2104.10330) — `detection`
- [Continuous Conditional Random Field Convolution for Point Cloud Segmentation](https://arxiv.org/abs/2110.06085) — `segmentation`
- [GSIP: Green Semantic Segmentation of Large-Scale Indoor Point Clouds](https://arxiv.org/abs/2109.11835) — `segmentation`
- [MKConv: Multidimensional Feature Representation for Point Cloud Analysis](https://arxiv.org/abs/2107.12655)
- [Quantifying point cloud realism through adversarially learned latent representations](https://arxiv.org/abs/2109.11775) — `classification` `generation`

</details>

<details><summary><b>arXiv</b> · 294</summary>

- ["Zero-Shot" Point Cloud Upsampling](https://arxiv.org/abs/2106.13765) — `upsampling` `open-vocabulary`
- [3D Adversarial Attacks Beyond Point Cloud](https://arxiv.org/abs/2104.12146) — `robustness`
- [3D LiDAR Aided GNSS NLOS Mitigation in Urban Canyons](https://arxiv.org/abs/2112.06108)
- [3D Medical Point Transformer: Introducing Convolution to Attention Networks for Medical Point Cloud Analysis](https://arxiv.org/abs/2112.04863) — `detection`
- [3D Object Detection Combining Semantic and Geometric Features from Point Clouds](https://arxiv.org/abs/2110.04704) — `detection`
- [3D Point Cloud Completion with Geometric-Aware Adversarial Augmentation](https://arxiv.org/abs/2109.10161) — `completion` `classification` `reconstruction` `autonomous driving`
- [3D point cloud segmentation using GIS](https://arxiv.org/abs/2108.06306) — `segmentation`
- [3D-SiamRPN: An End-to-End Learning Method for Real-Time 3D Single Object Tracking Using Raw Point Cloud](https://arxiv.org/abs/2108.05630) — `tracking` `efficiency`
- [6-DOF Feature based LIDAR SLAM using ORB Features from Rasterized Images of 3D LIDAR Point Cloud](https://arxiv.org/abs/2103.10678) — `detection` `slam`
- [A Biologically-Inspired Simultaneous Localization and Mapping System Based on LiDAR Sensor](https://arxiv.org/abs/2109.12910) — `slam` `localization`
- [A comprehensive survey on point cloud registration](https://arxiv.org/abs/2103.02690) — `registration`
- [A deep perceptual metric for 3D point clouds](https://arxiv.org/abs/2102.12839) — `compression`
- [A Fast Location Algorithm for Very Sparse Point Clouds Based on Object Detection](https://arxiv.org/abs/2110.10901) — `detection` `monocular`
- [A Learnable Self-supervised Task for Unsupervised Domain Adaptation on Point Clouds](https://arxiv.org/abs/2104.05164) — `self-supervised` `domain adaptation`
- [A new weakly supervised approach for ALS point cloud semantic segmentation](https://arxiv.org/abs/2110.01462) — `segmentation`
- [A Point Cloud Generative Model via Tree-Structured Graph Convolutions for 3D Brain Shape Reconstruction](https://arxiv.org/abs/2107.09923) — `generation` `reconstruction`
- [A Point-to-Distribution Joint Geometry and Color Metric for Point Cloud Quality Assessment](https://arxiv.org/abs/2108.00054) — Workshop
- [A procedure for automated tree pruning suggestion using LiDAR scans of fruit trees](https://arxiv.org/abs/2102.03700) — `efficiency`
- [A QoE Model in Point Cloud Video Streaming](https://arxiv.org/abs/2111.02985)
- [A real-time global re-localization framework for 3D LiDAR SLAM](https://arxiv.org/abs/2109.00200) — `slam` `localization` `efficiency`
- [A Robust Scheme for 3D Point Cloud Copy Detection](https://arxiv.org/abs/2110.00972) — `detection` `robustness`
- [ABD-Net: Attention Based Decomposition Network for 3D Point Cloud Decomposition](https://arxiv.org/abs/2108.04221) — `classification`
- [AdaFusion: Visual-LiDAR Fusion with Adaptive Weights for Place Recognition](https://arxiv.org/abs/2111.11739) — `localization`
- [Adaptive Channel Encoding for Point Cloud Analysis](https://arxiv.org/abs/2112.02509)
- [Adaptive Channel Encoding Transformer for Point Cloud Analysis](https://arxiv.org/abs/2112.02507)
- [Adaptive Lidar Scan Frame Integration: Tracking Known MAVs in 3D Point Clouds](https://arxiv.org/abs/2103.04069) — `tracking` `localization`
- [Advanced Geometry Surface Coding for Dynamic Point Cloud Compression](https://arxiv.org/abs/2103.06549) — `compression`
- [Adversarial Attack by Limited Point Cloud Surface Modifications](https://arxiv.org/abs/2110.03745) — `robustness`
- [Adversarial Attacks on Camera-LiDAR Models for 3D Car Detection](https://arxiv.org/abs/2103.09448) — `detection` `multi-modal` `robustness`
- [AeroTraj: Trajectory Planning for Fast, and Accurate 3D Reconstruction Using a Drone-based LiDAR](https://arxiv.org/abs/2104.08634) — `slam` `reconstruction`
- [An Efficient Hypergraph Approach to Robust Point Cloud Resampling](https://arxiv.org/abs/2103.06999) — `robustness` `efficiency`
- [An Improved Discriminative Optimization for 3D Rigid Point Cloud Registration](https://arxiv.org/abs/2104.08854) — `registration`
- [An Unsupervised Optical Flow Estimation For LiDAR Image Sequences](https://arxiv.org/abs/2105.13879) — `segmentation` `compression`
- [Anatomical Landmarks Localization for 3D Foot Point Clouds](https://arxiv.org/abs/2110.00937) — `localization`
- [Anchor-free 3D Single Stage Detector with Mask-Guided Attention for Point Cloud](https://arxiv.org/abs/2108.03634) — `detection`
- [Angle Based Feature Learning in GNN for 3D Object Detection using Point Cloud](https://arxiv.org/abs/2108.00780) — `detection`
- [Approach for modeling single branches of meadow orchard trees with 3D point clouds](https://arxiv.org/abs/2104.05282)
- [ART-SLAM: Accurate Real-Time 6DoF LiDAR SLAM](https://arxiv.org/abs/2109.05483) — `slam` `autonomous driving` `efficiency`
- [AttDLNet: Attention-based DL Network for 3D LiDAR Place Recognition](https://arxiv.org/abs/2106.09637) — `detection` `slam` `localization`
- [Attention Models for Point Clouds in Deep Learning: A Survey](https://arxiv.org/abs/2102.10788)
- [Attribute Artifacts Removal for Geometry-based Point Cloud Compression](https://arxiv.org/abs/2112.00560) — `compression`
- [Auto4D: Learning to Label 4D Objects from Sequential Point Clouds](https://arxiv.org/abs/2101.06586)
- [Automatic labelling of urban point clouds using data fusion](https://arxiv.org/abs/2108.13757) — `segmentation` — [code](https://github.com/Amsterdam-AI-Team/Urban_PointCloud_Processing) Workshop
- [AWCD: An Efficient Point Cloud Processing Approach via Wasserstein Curvature](https://arxiv.org/abs/2105.04402) — `denoising` `efficiency`
- [Background-Aware 3D Point Cloud Segmentationwith Dynamic Point Feature Aggregation](https://arxiv.org/abs/2111.07248) — `segmentation` `classification`
- [Be your own Benchmark: No-Reference Trajectory Metric on Registered Point Clouds](https://arxiv.org/abs/2106.11351) — `dataset`
- [BEVDetNet: Bird's Eye View LiDAR Point Cloud based Real-time 3D Object Detection for Autonomous Driving](https://arxiv.org/abs/2104.10780) — `detection` `autonomous driving` `efficiency`
- [Bridging the Gap: Point Clouds for Merging Neurons in Connectomics](https://arxiv.org/abs/2112.02039) — `segmentation`
- [City-scale Scene Change Detection using Point Clouds](https://arxiv.org/abs/2103.14314) — `detection`
- [CloudWalker: Random walks for 3D point cloud shape analysis](https://arxiv.org/abs/2112.01050)
- [CoFi: Coarse-to-Fine ICP for LiDAR Localization in an Efficient Long-lasting Point Cloud Map](https://arxiv.org/abs/2110.10194) — `localization` `efficiency`
- [Comprehensive Visual Question Answering on Point Clouds through Compositional Scene Manipulation](https://arxiv.org/abs/2112.11691)
- [CorAl -- Are the point clouds Correctly Aligned?](https://arxiv.org/abs/2109.09820) — `registration`
- [Correspondence-Free Point Cloud Registration with SO(3)-Equivariant Implicit Shape Representations](https://arxiv.org/abs/2107.10296) — `registration`
- [COTReg:Coupled Optimal Transport based Point Cloud Registration](https://arxiv.org/abs/2112.14381) — `registration`
- [CpT: Convolutional Point Transformer for 3D Point Cloud Processing](https://arxiv.org/abs/2111.10866)
- [Cross-Level Cross-Scale Cross-Attention Network for Point Cloud Representation](https://arxiv.org/abs/2104.13053)
- [CT-block: a novel local and global features extractor for point cloud](https://arxiv.org/abs/2111.15400)
- [Cylindrical coordinates for LiDAR point cloud compression](https://arxiv.org/abs/2106.11237) — `compression`
- [D3DLO: Deep 3D LiDAR Odometry](https://arxiv.org/abs/2101.12242)
- [DANIEL: A Fast and Robust Consensus Maximization Method for Point Cloud Registration with High Outlier Ratios](https://arxiv.org/abs/2110.05075) — `registration` `robustness`
- [Deep Evaluation Metric: Learning to Evaluate Simulated Radar Point Clouds for Virtual Testing of Autonomous Driving](https://arxiv.org/abs/2104.06772) — `autonomous driving` `multi-modal`
- [Deep Learning Based 3D Point Cloud Regression for Estimating Forest Biomass](https://arxiv.org/abs/2112.11335)
- [Deep Point Cloud Normal Estimation via Triplet Learning](https://arxiv.org/abs/2110.10494) — `normal estimation`
- [DeepCompress: Efficient Point Cloud Geometry Compression](https://arxiv.org/abs/2106.01504) — `detection` `compression` `autonomous driving` `efficiency`
- [DeepPoint: A Deep Learning Model for 3D Reconstruction in Point Clouds via mmWave Radar](https://arxiv.org/abs/2109.09188) — `detection` `reconstruction` `multi-modal`
- [Dense Supervision Propagation for Weakly Supervised Semantic Segmentation on 3D Point Clouds](https://arxiv.org/abs/2107.11267) — `segmentation`
- [Detecting Backdoor Attacks Against Point Cloud Classifiers](https://arxiv.org/abs/2110.10354) — `detection` `autonomous driving`
- [DFC: Deep Feature Consistency for Robust Point Cloud Registration](https://arxiv.org/abs/2111.07597) — `registration` `segmentation` `classification` `robustness`
- [Differentiable Convolution Search for Point Cloud Processing](https://arxiv.org/abs/2108.12856)
- [DiGS : Divergence guided shape implicit neural representation for unoriented point clouds](https://arxiv.org/abs/2106.10811) — `reconstruction`
- [Direct simple computation of middle surface between 3D point clouds and/or discrete surfaces by tracking sources in distance function calculation algorithms](https://arxiv.org/abs/2112.09808) — `detection` `tracking`
- [DLA-Net: Learning Dual Local Attention Features for Semantic Segmentation of Large-Scale Building Facade Point Clouds](https://arxiv.org/abs/2106.00376) — `segmentation` `reconstruction`
- [DLL: Direct LIDAR Localization. A map-based localization approach for aerial robots](https://arxiv.org/abs/2103.06112) — `registration` `localization` — [code](https://github.com/robotics-upo/dll)
- [Domain Adaptation on Point Clouds via Geometry-Aware Implicits](https://arxiv.org/abs/2112.09343) — `autonomous driving` `domain adaptation`
- [DPointNet: A Density-Oriented PointNet for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2102.03747) — `detection`
- [DRINet++: Efficient Voxel-as-point Point Cloud Segmentation](https://arxiv.org/abs/2111.08318) — `segmentation` `efficiency`
- [DSOR: A Scalable Statistical Filter for Removing Falling Snow from LiDAR Point Clouds in Severe Winter Weather](https://arxiv.org/abs/2109.07078)
- [DSPoint: Dual-scale Point Cloud Recognition with High-frequency Fusion](https://arxiv.org/abs/2111.10332)
- [Dual Transformer for Point Cloud Analysis](https://arxiv.org/abs/2104.13044)
- [Dual-Neighborhood Deep Fusion Network for Point Cloud Analysis](https://arxiv.org/abs/2108.09228) — `classification`
- [DV-Det: Efficient 3D Point Cloud Object Detection with Dynamic Voxelization](https://arxiv.org/abs/2107.12707) — `detection` `efficiency`
- [Dynamic Convolution for 3D Point Cloud Instance Segmentation](https://arxiv.org/abs/2107.08392) — `segmentation`
- [Edge and Corner Detection in Unorganized Point Clouds for Robotic Pick and Place Applications](https://arxiv.org/abs/2104.09099) — `detection`
- [EditVAE: Unsupervised Part-Aware Controllable 3D Point Cloud Shape Generation](https://arxiv.org/abs/2110.06679) — `generation`
- [Efficient 3D Deep LiDAR Odometry](https://arxiv.org/abs/2111.02135) — `efficiency`
- [Efficient 3D Point Cloud Feature Learning for Large-Scale Place Recognition](https://arxiv.org/abs/2101.02374) — `localization` `efficiency` — [code](https://github.com/fpthink/EPC-Net)
- [Efficient Urban-scale Point Clouds Segmentation with BEV Projection](https://arxiv.org/abs/2109.09074) — `segmentation` `BEV` `efficiency`
- [EfficientLPS: Efficient LiDAR Panoptic Segmentation](https://arxiv.org/abs/2102.08009) — `segmentation` `efficiency`
- [EgoNN: Egocentric Neural Network for Point Cloud Based 6DoF Relocalization at the City Scale](https://arxiv.org/abs/2110.12486)
- [Enabling 3D Object Detection with a Low-Resolution LiDAR](https://arxiv.org/abs/2105.01765) — `detection` `localization` `autonomous driving`
- [Explainability-Aware One Point Attack for Point Cloud Neural Networks](https://arxiv.org/abs/2110.04158)
- [False Positive Detection and Prediction Quality Estimation for LiDAR Point Cloud Segmentation](https://arxiv.org/abs/2110.15681) — `segmentation` `detection`
- [Fast and Accurate Normal Estimation for Point Cloud via Patch Stitching](https://arxiv.org/abs/2103.16066) — `normal estimation`
- [Fast Point Voxel Convolution Neural Network with Selective Feature Fusion for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2109.11614) — `segmentation`
- [Fast tree skeleton extraction using voxel thinning based on tree point cloud](https://arxiv.org/abs/2110.09028) — `classification`
- [FatNet: A Feature-attentive Network for 3D Point Cloud Processing](https://arxiv.org/abs/2104.03427)
- [Few-Data Guided Learning Upon End-to-End Point Cloud Network for 3D Face Recognition](https://arxiv.org/abs/2103.16927)
- [Few-Shot Meta-Learning on Point Cloud for Semantic Segmentation](https://arxiv.org/abs/2104.02979) — `segmentation` `autonomous driving`
- [FINet: Dual Branches Feature Interaction for Partial-to-Partial Point Cloud Registration](https://arxiv.org/abs/2106.03479) — `registration`
- [Fit4CAD: A point cloud benchmark for fitting simple geometric primitives in CAD objects](https://arxiv.org/abs/2105.06858) — `dataset`
- [FPPN: Future Pseudo-LiDAR Frame Prediction for Autonomous Driving](https://arxiv.org/abs/2112.04401) — `autonomous driving`
- [FPS-Net: A Convolutional Fusion Network for Large-Scale LiDAR Point Cloud Segmentation](https://arxiv.org/abs/2103.00738) — `segmentation`
- [Free-form Description Guided 3D Visual Graph Network for Object Grounding in Point Cloud](https://arxiv.org/abs/2103.16381)
- [From a Point Cloud to a Simulation Model: Bayesian Segmentation and Entropy based Uncertainty Estimation for 3D Modelling](https://arxiv.org/abs/2102.02488) — `segmentation` `generation`
- [From Voxel to Point: IoU-guided 3D Object Detection for Point Cloud with Voxel-to-Point Decoder](https://arxiv.org/abs/2108.03648) — `detection`
- [Frustum Fusion: Pseudo-LiDAR and LiDAR Fusion for 3D Detection](https://arxiv.org/abs/2111.04780) — `detection`
- [Full Transformer Framework for Robust Point Cloud Registration with Deep Information Interaction](https://arxiv.org/abs/2112.09385) — `registration` `robustness`
- [GA-NET: Global Attention Network for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2107.03101) — `segmentation`
- [Generate Point Clouds with Multiscale Details from Graph-Represented Structures](https://arxiv.org/abs/2112.06433) — `generation`
- [Generating Photo-realistic Images from LiDAR Point Clouds with Generative Adversarial Networks](https://arxiv.org/abs/2112.11245) — `generation` `robustness`
- [Generating Unrestricted 3D Adversarial Point Clouds](https://arxiv.org/abs/2111.08973) — `generation` `autonomous driving` `robustness`
- [Generation For Adaption: A GAN-Based Approach for 3D Domain Adaption with Point Cloud Data](https://arxiv.org/abs/2102.07373) — `classification` `generation`
- [GenReg: Deep Generative Method for Fast Point Cloud Registration](https://arxiv.org/abs/2111.11783) — `registration` `generation`
- [Geometric Algebra Attention Networks for Small Point Clouds](https://arxiv.org/abs/2110.02393)
- [Geometry-Aware Self-Training for Unsupervised Domain Adaptationon Object Point Clouds](https://arxiv.org/abs/2108.09169)
- [Go with the Flows: Mixtures of Normalizing Flows for Point Cloud Generation and Reconstruction](https://arxiv.org/abs/2106.03135) — `generation` `reconstruction`
- [Graph-Based Depth Denoising & Dequantization for Point Cloud Enhancement](https://arxiv.org/abs/2111.04946) — `denoising`
- [GreenPCO: An Unsupervised Lightweight Point Cloud Odometry Method](https://arxiv.org/abs/2112.04054) — `detection` `slam` `efficiency`
- [GSECnet: Ground Segmentation of Point Clouds for Edge Computing](https://arxiv.org/abs/2104.01766) — `segmentation` — [code](https://github.com/SAMMiCA/GSECnet)
- [Have I been here before? Learning to Close the Loop with LiDAR Data in Graph-Based SLAM](https://arxiv.org/abs/2103.06713) — `detection` `slam`
- [Helmholtzian Eigenmap: Topological feature discovery & edge flow learning from point cloud data](https://arxiv.org/abs/2103.07626)
- [HIDA: Towards Holistic Indoor Understanding for the Visually Impaired via Semantic Instance Segmentation with a Wearable Solid-State LiDAR Sensor](https://arxiv.org/abs/2107.03180) — `segmentation`
- [High-Fidelity Point Cloud Completion with Low-Resolution Recovery and Noise-Aware Upsampling](https://arxiv.org/abs/2112.11271) — `completion` `upsampling`
- [HyperPocket: Generative Point Cloud Completion](https://arxiv.org/abs/2102.05973) — `registration` `completion` `generation`
- [ICOS: Efficient and Highly Robust Rotation Search and Point Cloud Registration with Correspondences](https://arxiv.org/abs/2104.14763) — `registration` `robustness` `efficiency`
- [IMFNet: Interpretable Multimodal Fusion for Point Cloud Registration](https://arxiv.org/abs/2111.09624) — `registration` `multi-modal`
- [Imperceptible Transfer Attack and Defense on 3D Point Cloud Classification](https://arxiv.org/abs/2111.10990) — `classification`
- [Intensity Harmonization for Airborne LiDAR](https://arxiv.org/abs/2105.01793)
- [Interpreting Representation Quality of DNNs for 3D Point Cloud Processing](https://arxiv.org/abs/2111.03549)
- [IRON: Invariant-based Highly Robust Point Cloud Registration](https://arxiv.org/abs/2103.04357) — `registration` `robustness`
- [Joint 3D Object Detection and Tracking Using Spatio-Temporal Representation of Camera Image and LiDAR Point Clouds](https://arxiv.org/abs/2112.07116) — `detection` `tracking`
- [Joint Geometry and Color Projection-based Point Cloud Quality Metric](https://arxiv.org/abs/2108.02481) — `compression`
- [Joint Symmetry Detection and Shape Matching for Non-Rigid Point Cloud](https://arxiv.org/abs/2112.02713) — `detection`
- [Juggling With Representations: On the Information Transfer Between Imagery, Point Clouds, and Meshes for Multi-Modal Semantics](https://arxiv.org/abs/2103.07348) — `segmentation` `multi-modal`
- [Label-Efficient Point Cloud Semantic Segmentation: An Active Learning Approach](https://arxiv.org/abs/2101.06931) — `segmentation` `efficiency`
- [labelCloud: A Lightweight Domain-Independent Labeling Tool for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2103.04970) — `detection` `autonomous driving` `efficiency`
- [Language-Level Semantics Conditioned 3D Point Cloud Segmentation](https://arxiv.org/abs/2107.00430) — `segmentation` `generation`
- [LatticeNet: Fast Spatio-Temporal Point Cloud Segmentation Using Permutohedral Lattices](https://arxiv.org/abs/2108.03917) — `segmentation`
- [LCDNet: Deep Loop Closure Detection and Point Cloud Registration for LiDAR SLAM](https://arxiv.org/abs/2103.05056) — `registration` `detection` `slam` `localization`
- [Learning general and distinctive 3D local deep descriptors for point cloud registration](https://arxiv.org/abs/2105.10382) — `registration`
- [Learning Rotation-Invariant Representations of Point Clouds Using Aligned Edge Convolutional Neural Networks](https://arxiv.org/abs/2101.00483)
- [Learning Scene Dynamics from Point Cloud Sequences](https://arxiv.org/abs/2111.08755) — `scene flow` — [code](https://github.com/BestSonny/SPCM)
- [Learning without Forgetting for 3D Point Cloud Objects](https://arxiv.org/abs/2106.14275)
- [Lidar Light Scattering Augmentation (LISA): Physics-based Simulation of Adverse Weather Conditions for 3D Object Detection](https://arxiv.org/abs/2107.07004) — `detection` `autonomous driving`
- [Lidar Scan Registration Robust to Extreme Motions](https://arxiv.org/abs/2105.01215) — `registration` `localization` `robustness`
- [Lidar with Velocity: Correcting Moving Objects Point Cloud Distortion from Oscillating Scanning Lidars by Fusion with Camera](https://arxiv.org/abs/2111.09497) — `tracking` `autonomous driving`
- [LIF-Seg: LiDAR and Camera Image Fusion for 3D LiDAR Semantic Segmentation](https://arxiv.org/abs/2108.07511) — `segmentation` `autonomous driving`
- [LiODOM: Adaptive Local Mapping for Robust LiDAR-Only Odometry](https://arxiv.org/abs/2111.03393) — `detection` `localization` `robustness`
- [Lite-HDSeg: LiDAR Semantic Segmentation Using Lite Harmonic Dense Convolutions](https://arxiv.org/abs/2103.08852) — `segmentation` `autonomous driving`
- [Local Aggressive Adversarial Attacks on 3D Point Cloud](https://arxiv.org/abs/2105.09090) — `robustness`
- [Lossless Coding of Point Cloud Geometry using a Deep Generative Model](https://arxiv.org/abs/2107.00400) — `generation` `compression`
- [Lossless Point Cloud Attribute Compression with Normal-based Intra Prediction](https://arxiv.org/abs/2106.12236) — `compression` `autonomous driving`
- [LT-mapper: A Modular Framework for LiDAR-based Lifelong Mapping](https://arxiv.org/abs/2107.07712) — `detection` `slam`
- [LVAC: Learned Volumetric Attribute Compression for Point Clouds using Coordinate Based Networks](https://arxiv.org/abs/2111.08988) — `compression`
- [Machine Learning in LiDAR 3D point clouds](https://arxiv.org/abs/2101.09318) — `detection` `classification`
- [MinkLoc++: Lidar and Monocular Image Fusion for Place Recognition](https://arxiv.org/abs/2104.05327) — `localization` `monocular`
- [MinkLoc3D-SI: 3D LiDAR place recognition with sparse convolutions, spherical coordinates, and intensity](https://arxiv.org/abs/2112.06539) — `localization`
- [Model-Centric Volumetric Point Cloud Attributes](https://arxiv.org/abs/2106.15539) — `autonomous driving`
- [Model-free Vehicle Tracking and State Estimation in Point Cloud Sequences](https://arxiv.org/abs/2103.06028) — `tracking` `autonomous driving`
- [MPED: Quantifying Point Cloud Distortion based on Multiscale Potential Energy Discrepancy](https://arxiv.org/abs/2103.02850)
- [Multi Point-Voxel Convolution (MPVConv) for Deep Learning on Point Clouds](https://arxiv.org/abs/2107.13152)
- [Multi-Echo LiDAR for 3D Object Detection](https://arxiv.org/abs/2107.11470) — `detection`
- [Multi-resolution deep learning pipeline for dense large scale point clouds](https://arxiv.org/abs/2109.11311)
- [Multi-resolution intra-predictive coding of 3D point cloud attributes](https://arxiv.org/abs/2106.08562) — `compression`
- [Multimodal Colored Point Cloud to Image Alignment](https://arxiv.org/abs/2110.03249) — `reconstruction` `multi-modal`
- [Multiscale deep context modeling for lossless point cloud geometry compression](https://arxiv.org/abs/2104.09859) — `generation` `compression` — Workshop
- [Multiway Non-rigid Point Cloud Registration via Learned Functional Map Synchronization](https://arxiv.org/abs/2111.12878) — `registration`
- [Music source separation conditioned on 3D point clouds](https://arxiv.org/abs/2102.02028)
- [NDT-Transformer: Large-Scale 3D Point Cloud Localisation using the Normal Distribution Transform Representation](https://arxiv.org/abs/2103.12292) — `detection` `slam` `localization` `autonomous driving`
- [Neighborhood Spatial Aggregation MC Dropout for Efficient Uncertainty-aware Semantic Segmentation in Point Clouds](https://arxiv.org/abs/2201.07676) — `segmentation` `efficiency`
- [Neural Network Modeling of Probabilities for Coding the Octree Representation of Point Clouds](https://arxiv.org/abs/2106.06482) — `compression`
- [No-Reference Point Cloud Quality Assessment via Domain Adaptation](https://arxiv.org/abs/2112.02851) — `domain adaptation`
- [No-Reference Quality Assessment for 3D Colored Point Cloud and Mesh Models](https://arxiv.org/abs/2107.02041) — `compression`
- [Noise Injection-based Regularization for Point Cloud Processing](https://arxiv.org/abs/2103.15027)
- [Object Removal Attacks on LiDAR-based 3D Object Detectors](https://arxiv.org/abs/2102.03722)
- [Offboard 3D Object Detection from Point Cloud Sequences](https://arxiv.org/abs/2103.05073) — `detection`
- [OMNet: Learning Overlapping Mask for Partial-to-Partial Point Cloud Registration](https://arxiv.org/abs/2103.00937) — `registration`
- [On Adversarial Robustness of Point Cloud Semantic Segmentation](https://arxiv.org/abs/2112.05871) — `segmentation` `autonomous driving` `robustness`
- [Online Range Image-based Pole Extractor for Long-term LiDAR Localization in Urban Environments](https://arxiv.org/abs/2108.08621) — `localization`
- [OpenGF: An Ultra-Large-Scale Ground Filtering Dataset Built Upon Open ALS Point Clouds Around the World](https://arxiv.org/abs/2101.09641) — `generation` `dataset`
- [Optimal Target Shape for LiDAR Pose Estimation](https://arxiv.org/abs/2109.01181) — `tracking` `slam` `localization`
- [Pairwise Point Cloud Registration using Graph Matching and Rotation-invariant Features](https://arxiv.org/abs/2105.02151) — `registration`
- [PALMAR: Towards Adaptive Multi-inhabitant Activity Recognition in Point-Cloud Technology](https://arxiv.org/abs/2106.11902)
- [Panoptic nuScenes: A Large-Scale Benchmark for LiDAR Panoptic Segmentation and Tracking](https://arxiv.org/abs/2109.03805) — `segmentation` `tracking` `dataset`
- [PAPooling: Graph-based Position Adaptive Aggregation of Local Geometry in Point Clouds](https://arxiv.org/abs/2111.14067)
- [Paris-CARLA-3D: A Real and Synthetic Outdoor Point Cloud Dataset for Challenging Tasks in 3D Mapping](https://arxiv.org/abs/2111.11348) — `dataset`
- [Parts2Words: Learning Joint Embedding of Point Clouds and Texts by Bidirectional Matching between Parts and Words](https://arxiv.org/abs/2107.01872)
- [Patchwork: Concentric Zone-based Region-wise Ground Segmentation with Ground Likelihood Estimation Using a 3D LiDAR Sensor](https://arxiv.org/abs/2108.05560) — `segmentation`
- [Pattern-Aware Data Augmentation for LiDAR 3D Object Detection](https://arxiv.org/abs/2112.00050) — `detection` `autonomous driving`
- [PC-DAN: Point Cloud based Deep Affinity Network for 3D Multi-Object Tracking (Accepted as an extended abstract in JRDB-ACT Workshop at CVPR21)](https://arxiv.org/abs/2106.07552) — `detection` `tracking`
- [PC2WF: 3D Wireframe Reconstruction from Raw Point Clouds](https://arxiv.org/abs/2103.02766) — `reconstruction`
- [Pedestrian Detection in 3D Point Clouds using Deep Neural Networks](https://arxiv.org/abs/2105.01151) — `detection` `autonomous driving`
- [Perceptual Quality Assessment of Colored 3D Point Clouds](https://arxiv.org/abs/2111.05474)
- [PIG-Net: Inception based Deep Learning Architecture for 3D Point Cloud Segmentation](https://arxiv.org/abs/2101.11987) — `segmentation` `classification`
- [PillarSegNet: Pillar-based Semantic Grid Map Estimation using Sparse LiDAR Data](https://arxiv.org/abs/2105.04169) — `segmentation`
- [Pix2Point: Learning Outdoor 3D Using Sparse Point Clouds and Optimal Transport](https://arxiv.org/abs/2107.14498) — `reconstruction` `monocular`
- [Pixel-level Extrinsic Self Calibration of High Resolution LiDAR and Camera in Targetless Environments](https://arxiv.org/abs/2103.01627)
- [PixSet : An Opportunity for 3D Computer Vision to Go Beyond Point Clouds With a Full-Waveform LiDAR Dataset](https://arxiv.org/abs/2102.12010) — `autonomous driving` `dataset`
- [PnP-3D: A Plug-and-Play for 3D Point Clouds](https://arxiv.org/abs/2108.07378)
- [Point Cloud Audio Processing](https://arxiv.org/abs/2105.02469) — [code](https://github.com/SubramaniKrishna/point-cloud-audio)
- [Point Cloud based Hierarchical Deep Odometry Estimation](https://arxiv.org/abs/2103.03394) — `registration` `detection`
- [Point Cloud Failure Criterion for Composites using k-Nearest Neighbor Classification](https://arxiv.org/abs/2106.02714) — `classification`
- [Point Cloud Instance Segmentation with Semi-supervised Bounding-Box Mining](https://arxiv.org/abs/2111.15210) — `segmentation`
- [Point Cloud Learning with Transformer](https://arxiv.org/abs/2104.13636) — `segmentation`
- [Point Cloud Registration using Representative Overlapping Points](https://arxiv.org/abs/2107.02583) — `registration`
- [Point Cloud Segmentation Using Sparse Temporal Local Attention](https://arxiv.org/abs/2112.00289) — `segmentation`
- [Point Cloud Subsampling Parallelization for Unified Memory Platforms](https://arxiv.org/abs/2102.11084)
- [Point Cloud Transformers applied to Collider Physics](https://arxiv.org/abs/2102.05073)
- [Point Cloud Upsampling and Normal Estimation using Deep Learning for Robust Surface Reconstruction](https://arxiv.org/abs/2102.13391) — `reconstruction` `upsampling` `normal estimation` `robustness`
- [Point-Cloud Deep Learning of Porous Media for Permeability Prediction](https://arxiv.org/abs/2107.14038)
- [PointCaps: Raw Point Cloud Processing using Capsule Networks with Euclidean Distance Routing](https://arxiv.org/abs/2112.11258) — `segmentation` `classification` `reconstruction`
- [PointCLIP: Point Cloud Understanding by CLIP](https://arxiv.org/abs/2112.02413) — `open-vocabulary`
- [PointCutMix: Regularization Strategy for Point Cloud Classification](https://arxiv.org/abs/2101.01461) — `classification`
- [PointManifoldCut: Point-wise Augmentation in the Manifold for Point Clouds](https://arxiv.org/abs/2109.07324) — `segmentation`
- [Points2Sound: From mono to binaural audio using 3D point cloud scenes](https://arxiv.org/abs/2104.12462) — `generation` — [code](https://github.com/francesclluis/points2sound)
- [Points2Vec: Unsupervised Object-level Feature Learning from Point Clouds](https://arxiv.org/abs/2102.04136)
- [Poisoning MorphNet for Clean-Label Backdoor Attack to Point Clouds](https://arxiv.org/abs/2105.04839)
- [Potential Convolution: Embedding Point Clouds into Potential Fields](https://arxiv.org/abs/2104.01754) — `segmentation` `classification`
- [PQ-Transformer: Jointly Parsing 3D Objects and Layouts from Point Clouds](https://arxiv.org/abs/2109.05566) — `detection` — [code](https://github.com/OPEN-AIR-SUN/PQ-Transformer)
- [PRA-Net: Point Relation-Aware Network for 3D Point Cloud Analysis](https://arxiv.org/abs/2112.04903)
- [Practical, Fast and Robust Point Cloud Registration for 3D Scene Stitching and Object Localization](https://arxiv.org/abs/2111.04228) — `registration` `localization` `robustness`
- [PRANet: Point Cloud Registration with an Artificial Agent](https://arxiv.org/abs/2109.11349) — `registration` `localization`
- [Pre-Clustering Point Clouds of Crop Fields Using Scalable Methods](https://arxiv.org/abs/2107.10950)
- [PriFit: Learning to Fit Primitives Improves Few Shot Point Cloud Segmentation](https://arxiv.org/abs/2112.13942) — `segmentation`
- [Probabilistic Rainfall Estimation from Automotive Lidar](https://arxiv.org/abs/2104.11467)
- [PTTR: Relational 3D Point Cloud Object Tracking with Transformer](https://arxiv.org/abs/2112.02857) — `tracking`
- [PU-Flow: a Point Cloud Upsampling Network with Normalizing Flows](https://arxiv.org/abs/2107.05893) — `upsampling`
- [PU-Transformer: Point Cloud Upsampling Transformer](https://arxiv.org/abs/2111.12242) — `upsampling`
- [PVT: Point-Voxel Transformer for Point Cloud Learning](https://arxiv.org/abs/2108.06076)
- [R-PCC: A Baseline for Range Image-based Point Cloud Compression](https://arxiv.org/abs/2109.07717) — `compression`
- [R-PointHop: A Green, Accurate, and Unsupervised Point Cloud Registration Method](https://arxiv.org/abs/2103.08129) — `registration` `classification`
- [RadarScenes: A Real-World Radar Point Cloud Data Set for Automotive Applications](https://arxiv.org/abs/2104.02493) — `multi-modal`
- [RAI-Net: Range-Adaptive LiDAR Point Cloud Frame Interpolation Network](https://arxiv.org/abs/2106.00496) — `upsampling`
- [RailLoMer: Rail Vehicle Localization and Mapping with LiDAR-IMU-Odometer-GNSS Data Fusion](https://arxiv.org/abs/2111.15043) — `localization`
- [Range-Aware Attention Network for LiDAR-based 3D Object Detection with Auxiliary Point Density Level Estimation](https://arxiv.org/abs/2111.09515) — `detection` `autonomous driving` `BEV`
- [Real-Time Ground-Plane Refined LiDAR SLAM](https://arxiv.org/abs/2110.11517) — `tracking` `slam` `efficiency`
- [Real-time Identification and Simultaneous Avoidance of Static and Dynamic Obstacles on Point Cloud for UAVs Navigation](https://arxiv.org/abs/2110.10360) — `efficiency`
- [Refining the bounding volumes for lossless compression of voxelized point clouds geometry](https://arxiv.org/abs/2106.00828) — `reconstruction` `compression`
- [Rendering Point Clouds with Compute Shaders and Vertex Order Optimization](https://arxiv.org/abs/2104.07526)
- [Rethinking Point Cloud Filtering: A Non-Local Position Based Approach](https://arxiv.org/abs/2110.07253)
- [Revisiting LiDAR Registration and Reconstruction: A Range Image Perspective](https://arxiv.org/abs/2112.02779) — `registration` `reconstruction`
- [Revisiting Point Cloud Simplification: A Learnable Feature Preserving Approach](https://arxiv.org/abs/2109.14982)
- [RibSeg Dataset and Strong Point Cloud Baselines for Rib Segmentation from CT Scans](https://arxiv.org/abs/2109.09521) — `segmentation` `dataset` — [code](https://github.com/M3DV/RibSeg)
- [Robust Extrinsic Symmetry Estimation in 3D Point Clouds](https://arxiv.org/abs/2109.09927) — `detection` `reconstruction` `compression` `robustness`
- [Robust Partial-to-Partial Point Cloud Registration in a Full Range](https://arxiv.org/abs/2111.15606) — `registration` `robustness` — [code](https://github.com/paul007pl/GMCNet)
- [Rotation Transformation Network: Learning View-Invariant Point Cloud for Classification and Segmentation](https://arxiv.org/abs/2107.03105) — `segmentation` `classification`
- [RPG: Learning Recursive Point Cloud Generation](https://arxiv.org/abs/2105.14322) — `generation`
- [RPVNet: A Deep and Efficient Range-Point-Voxel Fusion Network for LiDAR Point Cloud Segmentation](https://arxiv.org/abs/2103.12978) — `segmentation` `efficiency`
- [S3Net: 3D LiDAR Sparse Semantic Segmentation Network](https://arxiv.org/abs/2103.08745) — `segmentation` `autonomous driving` `BEV`
- [Scalable Scene Flow from Point Clouds in the Real World](https://arxiv.org/abs/2103.01306) — `scene flow`
- [SE-MD: A Single-encoder multiple-decoder deep network for point cloud generation from 2D images](https://arxiv.org/abs/2106.15325) — `generation`
- [Seeing Glass: Joint Point Cloud and Depth Completion for Transparent Objects](https://arxiv.org/abs/2110.00087) — `completion`
- [Self-Ensemling for 3D Point Cloud Domain Adaption](https://arxiv.org/abs/2112.05301) — `autonomous driving`
- [Self-supervised 3D Human Mesh Recovery from Noisy Point Clouds](https://arxiv.org/abs/2107.07539) — `self-supervised`
- [Self-supervised Point Cloud Prediction Using 3D Spatio-temporal Convolutional Networks](https://arxiv.org/abs/2110.04076) — `self-supervised`
- [Self-supervised Point Cloud Representation Learning via Separating Mixed Shapes](https://arxiv.org/abs/2109.00452) — `self-supervised`
- [Semantic Segmentation-assisted Scene Completion for LiDAR Point Clouds](https://arxiv.org/abs/2109.11453) — `segmentation` `completion` `autonomous driving`
- [Semantics-aware Multi-modal Domain Translation:From LiDAR Point Clouds to Panoramic Color Images](https://arxiv.org/abs/2106.13974) — `segmentation` `generation` `multi-modal`
- [Semi-supervised Implicit Scene Completion from Sparse LiDAR](https://arxiv.org/abs/2111.14798) — `completion` — [code](https://github.com/OPEN-AIR-SUN/SISC)
- [Sequential Point Cloud Prediction in Interactive Scenarios: A Survey](https://arxiv.org/abs/2109.07342) — `autonomous driving`
- [SIENet: Spatial Information Enhancement Network for 3D Object Detection from Point Cloud](https://arxiv.org/abs/2103.15396) — `detection`
- [Simulated LiDAR Repositioning: a novel point cloud data augmentation method](https://arxiv.org/abs/2111.10650)
- [Sparse Tensor-based Multiscale Representation for Point Cloud Geometry Compression](https://arxiv.org/abs/2111.10633) — `compression`
- [Spatial-Temporal Transformer for 3D Point Cloud Sequences](https://arxiv.org/abs/2110.09783) — `segmentation`
- [Spatio-temporal Graph-RNN for Point Cloud Prediction](https://arxiv.org/abs/2102.07482)
- [SPNet: Multi-Shell Kernel Convolution for Point Cloud Semantic Segmentation](https://arxiv.org/abs/2109.11610) — `segmentation`
- [Style-based Point Generator with Adversarial Rendering for Point Cloud Completion](https://arxiv.org/abs/2103.02535) — `completion` `generation` `robustness`
- [Surrogate Model-Based Explainability Methods for Point Cloud NNs](https://arxiv.org/abs/2107.13459) — `autonomous driving`
- [Tesla-Rapture: A Lightweight Gesture Recognition System from mmWave Radar Point Clouds](https://arxiv.org/abs/2109.06448) — `multi-modal` `efficiency`
- [The Devils in the Point Clouds: Studying the Robustness of Point Cloud Convolutions](https://arxiv.org/abs/2101.07832) — `robustness`
- [The Hessigheim 3D (H3D) Benchmark on Semantic Segmentation of High-Resolution 3D Point Clouds and Textured Meshes from UAV LiDAR and Multi-View-Stereo](https://arxiv.org/abs/2102.05346) — `segmentation` `detection` `dataset`
- [Three dimensional unique identifier based automated georeferencing and coregistration of point clouds in underground environment](https://arxiv.org/abs/2102.10731)
- [Towards Automatic Sizing for PPE with a Point Cloud Based Variational Autoencoder](https://arxiv.org/abs/2105.10067)
- [Towards Efficient Graph Convolutional Networks for Point Cloud Handling](https://arxiv.org/abs/2104.05706) — `efficiency`
- [Towards Universal Physical Attacks On Cascaded Camera-Lidar 3D Object Detection Models](https://arxiv.org/abs/2101.10747) — `detection` `autonomous driving` `multi-modal`
- [TransLoc3D : Point Cloud based Large-scale Place Recognition using Adaptive Receptive Fields](https://arxiv.org/abs/2105.11605) — `localization` `autonomous driving`
- [TreeGCN-ED: Encoding Point Cloud using a Tree-Structured Graph Network](https://arxiv.org/abs/2110.03170) — `segmentation` `classification`
- [UnDeepLIO: Unsupervised Deep Lidar-Inertial Odometry](https://arxiv.org/abs/2109.01533)
- [Unsupervised Contrastive Learning with Simple Transformation for 3D Point Cloud Data](https://arxiv.org/abs/2110.06632) — `self-supervised`
- [Unsupervised Learning for Cuboid Shape Abstraction via Joint Segmentation from Point Clouds](https://arxiv.org/abs/2106.03437) — `segmentation`
- [UnsupervisedR&R: Unsupervised Point Cloud Registration via Differentiable Rendering](https://arxiv.org/abs/2102.11870) — `registration` `slam`
- [VA-GCN: A Vector Attention Graph Convolution Network for learning on Point Clouds](https://arxiv.org/abs/2106.00227)
- [Vegetation Stratum Occupancy Prediction from Airborne LiDAR 3D Point Clouds](https://arxiv.org/abs/2112.13583) — `occupancy prediction`
- [Visual Enhanced 3D Point Cloud Reconstruction from A Single Image](https://arxiv.org/abs/2108.07685) — `reconstruction` `monocular`
- [VoteHMR: Occlusion-Aware Voting Network for Robust 3D Human Mesh Recovery from Partial Point Clouds](https://arxiv.org/abs/2110.08729) — `robustness`
- [Voxel Structure-based Mesh Reconstruction from a 3D Point Cloud](https://arxiv.org/abs/2104.10622) — `detection` `reconstruction`
- [VPFNet: Improving 3D Object Detection with Virtual Point based LiDAR and Stereo Data Fusion](https://arxiv.org/abs/2111.14382) — `detection`
- [Which One is Better: Assessing Objective Metrics for Point Cloud Compression](https://arxiv.org/abs/2109.07158) — `compression`
- [Whole Slide Images are 2D Point Clouds: Context-Aware Survival Prediction using Patch-based Graph Convolutional Networks](https://arxiv.org/abs/2107.13048)
- [Wood-leaf classification of tree point cloud based on intensity and geometrical information](https://arxiv.org/abs/2108.01002) — `classification`
- [You Only Group Once: Efficient Point-Cloud Processing with Token Representation and Relation Inference Module](https://arxiv.org/abs/2103.09975) — `efficiency` — [code](https://github.com/chenfengxu714/YOGO.git)
- [Z2P: Instant Visualization of Point Clouds](https://arxiv.org/abs/2105.14548) — `reconstruction`
- [Zero-Shot Learning on 3D Point Cloud Objects and Beyond](https://arxiv.org/abs/2104.04980) — `classification` `open-vocabulary`

</details>


---

## 说明 / Notes

- 共 **2755** 篇（2021 年至今），其中 **155** 篇附带代码链接；年份为会议年份，纯 arXiv 为首次提交年份。
- 收录范围：点云相关（检测、分割、配准、补全、分类、跟踪、SLAM、生成、压缩、预训练等），不限于单一子方向。
- 2021 年前的经典工作未收录；数据集见 [DATASETS.md](DATASETS.md)（不受年份限制）。
- 每日自动同步：[`.github/workflows/arxiv-sync.yml`](.github/workflows/arxiv-sync.yml)。
- 灵感与对照：[zhulf0804/3D-PointCloud](https://github.com/zhulf0804/3D-PointCloud)（2024-08 起停更）。

## License

内容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布，脚本以 MIT 发布。
