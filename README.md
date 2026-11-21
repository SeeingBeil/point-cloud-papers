# Awesome Point Cloud Papers

<p align="center">
  <b>点云论文索引 · 2021 年至今 · 每日自动更新</b><br>
  <sub>Curated papers on 3D point clouds and LiDAR perception, 2021–present. Synced with arXiv.</sub>
</p>

[![Papers](https://img.shields.io/badge/papers-4338-blue)](#-papers)
[![With code](https://img.shields.io/badge/with_code-242-brightgreen)](#-papers)
[![Datasets](https://img.shields.io/badge/datasets-index-orange)](DATASETS.md)
[![Update](https://img.shields.io/badge/last_update-2026-11-21-lightgrey)](#)
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
| `segmentation` | 685 | [查看](docs/topics/segmentation.md) |
| `detection` | 637 | [查看](docs/topics/detection.md) |
| `autonomous driving` | 474 | [查看](docs/topics/autonomous-driving.md) |
| `reconstruction` | 429 | [查看](docs/topics/reconstruction.md) |
| `registration` | 426 | [查看](docs/topics/registration.md) |
| `efficiency` | 354 | [查看](docs/topics/efficiency.md) |
| `generation` | 326 | [查看](docs/topics/generation.md) |
| `robustness` | 285 | [查看](docs/topics/robustness.md) |
| `localization` | 264 | [查看](docs/topics/localization.md) |
| `multi-modal` | 239 | [查看](docs/topics/multi-modal.md) |
| `classification` | 212 | [查看](docs/topics/classification.md) |
| `self-supervised` | 204 | [查看](docs/topics/self-supervised.md) |
| `compression` | 200 | [查看](docs/topics/compression.md) |
| `completion` | 188 | [查看](docs/topics/completion.md) |
| `tracking` | 125 | [查看](docs/topics/tracking.md) |
| `dataset` | 121 | [查看](docs/topics/dataset.md) |
| `gaussian-splatting` | 108 | [查看](docs/topics/gaussian-splatting.md) |
| `slam` | 108 | [查看](docs/topics/slam.md) |
| `denoising` | 86 | [查看](docs/topics/denoising.md) |
| `upsampling` | 82 | [查看](docs/topics/upsampling.md) |
| `pre-training` | 81 | [查看](docs/topics/pre-training.md) |
| `open-vocabulary` | 63 | [查看](docs/topics/open-vocabulary.md) |
| `monocular` | 50 | [查看](docs/topics/monocular.md) |
| `scene flow` | 47 | [查看](docs/topics/scene-flow.md) |
| `BEV` | 41 | [查看](docs/topics/bev.md) |
| `nerf` | 38 | [查看](docs/topics/nerf.md) |
| `domain adaptation` | 35 | [查看](docs/topics/domain-adaptation.md) |
| `anomaly detection` | 32 | [查看](docs/topics/anomaly-detection.md) |
| `vision-language` | 29 | [查看](docs/topics/vision-language.md) |
| `normal estimation` | 27 | [查看](docs/topics/normal-estimation.md) |
| `occupancy prediction` | 13 | [查看](docs/topics/occupancy-prediction.md) |

---

## 论文 / Papers

### 2026 <sub>(645)</sub>

<details><summary><b>CVPR</b> · 57</summary>

- [3D sans 3D Scans: Scalable Pre-training from Video-Generated Point Clouds](https://arxiv.org/abs/2512.23042) — `self-supervised` `pre-training`
- [A Semantically Disentangled Unified Model for Multi-category 3D Anomaly Detection](https://arxiv.org/abs/2603.25159) — `detection` `localization` `reconstruction` `anomaly detection`
- [Action-Geometry Prediction with 3D Geometric Prior for Bimanual Manipulation](https://arxiv.org/abs/2602.23814)
- [Adapting Point Cloud Analysis via Multimodal Bayesian Distribution Learning](https://arxiv.org/abs/2603.22070) — `multi-modal`
- [AnyPcc: Compressing Any Point Cloud with a Single Universal Model](https://arxiv.org/abs/2510.20331) — `compression`
- [APC: Transferable and Efficient Adversarial Point Counterattack for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2604.15708) — `robustness` `efficiency`
- [AvatarPointillist: AutoRegressive 4D Gaussian Avatarization](https://arxiv.org/abs/2604.04787) — `gaussian-splatting`
- [Back to Point: Exploring Point-Language Models for Zero-Shot 3D Anomaly Detection](https://arxiv.org/abs/2603.21511) — `detection` `open-vocabulary` `anomaly detection`
- [BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting](https://arxiv.org/abs/2602.21105) — `reconstruction` `gaussian-splatting`
- [BuildAnyPoint: 3D Building Structured Abstraction from Diverse Point Clouds](https://arxiv.org/abs/2602.23645) — `generation` `reconstruction`
- [Bézier Degradation Modeling for LiDAR-based Human Motion Capture](https://arxiv.org/abs/2605.19620) — `reconstruction` `autonomous driving`
- [C-GenReg: Training-Free 3D Point Cloud Registration by Multi-View-Consistent Geometry-to-Image Generation with Probabilistic Modalities Fusion](https://arxiv.org/abs/2604.16680) — `registration` `generation`
- [CLIPoint3D: Language-Grounded Few-Shot Unsupervised 3D Point Cloud Domain Adaptation](https://arxiv.org/abs/2602.20409) — `vision-language` `domain adaptation`
- [ComPose: A Unified Completion-Pose Framework for Robust Category-Level Object Pose Estimation](https://arxiv.org/abs/2605.25553) — `completion` `robustness`
- [Curvature-Aware Captioning:Leveraging Geodesic Attention for 3D Scene Understanding](https://arxiv.org/abs/2605.08808)
- [Deformation-based In-Context Learning for Point Cloud Understanding](https://arxiv.org/abs/2604.02845) — [code](https://github.com/linchengxing/DeformPIC)
- [Direction-aware 3D Large Multimodal Models](https://arxiv.org/abs/2602.19063) — `multi-modal`
- [Edge Prediction for Roof Wireframe Reconstruction with Transformers](https://arxiv.org/abs/2606.02406) — `reconstruction` — Workshop
- [Efficient Encoder-Free Fourier-based 3D Large Multimodal Model](https://arxiv.org/abs/2602.23153) — `multi-modal` `efficiency`
- [EvObj: Learning Evolving Object-centric Representations for 3D Instance Segmentation without Scene Supervision](https://arxiv.org/abs/2605.13152) — `segmentation` — [code](https://github.com/vLAR-group/EvObj)
- [Expanding mmWave Datasets for Human Pose Estimation with Unlabeled Data and LiDAR Datasets](https://arxiv.org/abs/2603.14507)
- [FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement](https://arxiv.org/abs/2512.09373) — `registration`
- [GaussianDWM: 3D Gaussian Driving World Model for Unified Scene Understanding and Multi-Modal Generation](https://arxiv.org/abs/2512.23180) — `generation` `BEV` `multi-modal`
- [GaussianGrow: Geometry-aware Gaussian Growing from 3D Point Clouds with Text Guidance](https://arxiv.org/abs/2604.05721) — `generation` `gaussian-splatting`
- [Geometric-Aware Hypergraph Reasoning for Novel Class Discovery in Point Cloud Segmentation](https://arxiv.org/abs/2606.07280) — `segmentation`
- [Ghost-FWL: A Large-Scale Full-Waveform LiDAR Dataset for Ghost Detection and Removal](https://arxiv.org/abs/2603.28224) — `detection` `localization` `autonomous driving` `dataset`
- [Ghosts in the Point Clouds: De-glaring LiDAR in the Transient Domain](https://arxiv.org/abs/2605.24753)
- [GS-CLIP: Zero-shot 3D Anomaly Detection by Geometry-Aware Prompt and Synergistic View Representation Learning](https://arxiv.org/abs/2602.19206) — `detection` `open-vocabulary` `anomaly detection`
- [Hg-I2P: Bridging Modalities for Generalizable Image-to-Point-Cloud Registration via Heterogeneous Graphs](https://arxiv.org/abs/2603.27969) — `registration`
- [Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant and Efficient Point Cloud Analysis](https://arxiv.org/abs/2603.17538) — `efficiency`
- [LitePT: Lighter Yet Stronger Point Transformer](https://arxiv.org/abs/2512.13689)
- [Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding](https://arxiv.org/abs/2603.20739)
- [MASER: Modality-Adaptive Specialist Routing for Embodied 3D Spatial Intelligence](https://arxiv.org/abs/2606.02463) — Workshop
- [MVGGT: Multimodal Visual Geometry Grounded Transformer for Multiview 3D Referring Expression Segmentation](https://arxiv.org/abs/2601.06874) — `segmentation` `multi-modal`
- [Neu-PiG: Neural Preconditioned Grids for Fast Dynamic Surface Reconstruction on Long Sequences](https://arxiv.org/abs/2602.22212) — `reconstruction` — [code](https://github.com/vc-bonn/neu-pig)
- [On the Feasibility and Opportunity of Autoregressive 3D Object Detection](https://arxiv.org/abs/2603.07985) — `detection` `generation`
- [PCSTracker: Long-Term Scene Flow Estimation for Point Cloud Sequences](https://arxiv.org/abs/2603.19762) — `scene flow`
- [PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520) — `segmentation` `gaussian-splatting` `autonomous driving`
- [Points-to-3D: Structure-Aware 3D Generation with Point Cloud Priors](https://arxiv.org/abs/2603.18782) — `generation`
- [PointTPA: Dynamic Network Parameter Adaptation for 3D Scene Understanding](https://arxiv.org/abs/2604.04933) — [code](https://github.com/H-EmbodVis/PointTPA)
- [PQDT: Pseudo-Query Dual Transformer for Robust Point Cloud Restoration](https://arxiv.org/abs/2605.25127) — `robustness`
- [QD-PCQA: Quality-Aware Domain Adaptation for Point Cloud Quality Assessment](https://arxiv.org/abs/2603.03726) — `domain adaptation`
- [QVGGT: Post-Training Quantized Visual Geometry Grounded Transformer](https://arxiv.org/abs/2605.31124) — `efficiency`
- [Revisiting Radar Perception With Spectral Point Clouds](https://arxiv.org/abs/2604.08282) — `multi-modal` — Workshop
- [S2AM3D: Scale-controllable Part Segmentation of 3D Point Clouds](https://arxiv.org/abs/2512.00995) — `segmentation`
- [SCOPE: Scene-Contextualized Incremental Few-Shot 3D Segmentation](https://arxiv.org/abs/2603.06572) — `segmentation`
- [STS-Mixer: Spatio-Temporal-Spectral Mixer for 4D Point Cloud Video Understanding](https://arxiv.org/abs/2604.11637)
- [Temporally Consistent Long-Term Memory for 3D Single Object Tracking](https://arxiv.org/abs/2604.13789) — `tracking`
- [Text-guided Feature Disentanglement for Cross-modal Gait Recognition](https://arxiv.org/abs/2605.30784)
- [Towards Foundation Models for 3D Scene Understanding: Instance-Aware Self-Supervised Learning for Point Clouds](https://arxiv.org/abs/2603.25165) — `localization` `self-supervised`
- [Two Steps Are All You Need: Efficient 3D Point Cloud Anomaly Detection with Consistency Models](https://arxiv.org/abs/2605.05372) — `detection` `anomaly detection` `efficiency` — Workshop
- [UniCorrn: Unified Correspondence Transformer Across 2D and 3D](https://arxiv.org/abs/2605.04044)
- [Unsupervised Multi-agent and Single-agent Perception from Cooperative Views](https://arxiv.org/abs/2604.05354)
- [UST-Hand: An Uncertainty-aware Spatiotemporal Point Cloud Interaction Network for 3D Self-supervised Hand Pose Estimation](https://arxiv.org/abs/2605.17742) — `self-supervised`
- [Velox: Learning Representations of 4D Geometry and Appearance](https://arxiv.org/abs/2605.04527) — `compression`
- [Vista4D: Video Reshooting with 4D Point Clouds](https://arxiv.org/abs/2604.21915)
- [VLM-Loc: Localization in Point Cloud Maps via Vision-Language Models](https://arxiv.org/abs/2603.09826) — `localization` `vision-language`

</details>

<details><summary><b>ECCV</b> · 35</summary>

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
- [G2P: Gaussian-to-Point Attribute Alignment for Boundary-Aware 3D Segmentation](https://arxiv.org/abs/2601.03510) — `segmentation` `gaussian-splatting`
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
- [SA-ResGS: Self-Augmented Residual 3D Gaussian Splatting for Next Best View Selection](https://arxiv.org/abs/2601.03024) — `reconstruction` `gaussian-splatting`
- [Scale Matters: Adaptive Granularity Selection for Cross-Species 3D Plant Organ Segmentation](https://arxiv.org/abs/2608.17803) — `segmentation` — Workshop
- [Sen-Cap: Sensor-Flexible and Noise-Resilient Human Motion Capture via LiDAR-Camera Integration](https://arxiv.org/abs/2608.02285) — `multi-modal`
- [TopoField: Technical Report for ECCV 2026 SceneFun3D Challenge](https://arxiv.org/abs/2610.37218) — `segmentation` — Workshop
- [UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound](https://arxiv.org/abs/2609.11506) — `segmentation` `completion`
- [Unsupervised Point Cloud Registration via Training-Time Semantic Guidance](https://arxiv.org/abs/2609.15228) — `registration`
- [White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2509.13907) — `segmentation`

</details>

<details><summary><b>NeurIPS</b> · 13</summary>

- [ControlFlow3D: Distilling Multi-View Knowledge into Latent Flow Matching for Point Cloud Upsampling](https://arxiv.org/abs/2610.21190) — `generation` `upsampling`
- [Diffusion Masked Pretraining for Dynamic Point Cloud](https://arxiv.org/abs/2605.03639) — `reconstruction` `pre-training`
- [FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection](https://arxiv.org/abs/2611.09170) — `detection`
- [IGLOSS: Image Generation for Lidar Open-vocabulary Semantic Segmentation](https://arxiv.org/abs/2604.01361) — `segmentation` `generation` `open-vocabulary`
- [LiFi: LiDAR Generation from Multi-View Images via Geometric and Semantic Collaborative Guidance](https://arxiv.org/abs/2610.19786) — `generation`
- [MemReg: Streaming Outdoor LiDAR Point Cloud Registration with Hybrid Memory Buffers](https://arxiv.org/abs/2610.12624) — `registration`
- [Not All Tasks Quantize Equally: Fisher-Guided Quantization for Visual Geometry Transformer](https://arxiv.org/abs/2605.15828) — `reconstruction` `efficiency`
- [Point Cloud Sequence Encoding for Material-conditioned Graph Network Simulators](https://arxiv.org/abs/2605.20978)
- [Register Anything Model for Generalizable and Robust Point Cloud Registration](https://arxiv.org/abs/2610.28821) — `registration` `robustness` — [code](https://github.com/qinzheng93/RegisterAnything)
- [Rethinking Radar 3D Perception: Representation Learning from Raw Spectra](https://arxiv.org/abs/2611.12334) — `multi-modal`
- [RigidFormer: Learning Rigid Dynamics using Transformers](https://arxiv.org/abs/2605.09196)
- [SIEVE: Overcoming Topological Obstruction in Equivariant Self-Supervised Learning](https://arxiv.org/abs/2610.21087) — `self-supervised`
- [Towards Generalizable 3D Anomaly Detection via Relational Inconsistency Modeling](https://arxiv.org/abs/2609.35059) — `detection` `anomaly detection` — [code](https://github.com/VisualScienceLab-KHU/GRIM)

</details>

<details><summary><b>ICLR</b> · 6</summary>

- [Adaptive Augmentation-Aware Latent Learning for Robust LiDAR Semantic Segmentation](https://arxiv.org/abs/2603.01074) — `segmentation` `robustness`
- [Point-Focused Attention Meets Context-Scan State Space: Robust Biological Visual Perception for Point Cloud Representation](https://arxiv.org/abs/2610.11342) — `robustness`
- [Pointy - A Lightweight Transformer for Point Cloud Foundation Models](https://arxiv.org/abs/2603.10963) — `efficiency` — Workshop
- [Segment Any Events with Language](https://arxiv.org/abs/2601.23159) — `segmentation` `open-vocabulary`
- [Sparkle: A Robust and Versatile Representation for Point Cloud based Human Motion Capture](https://arxiv.org/abs/2604.00857) — `robustness`
- [SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors](https://arxiv.org/abs/2602.02000) — `reconstruction` `gaussian-splatting`

</details>

<details><summary><b>ICML</b> · 9</summary>

- [4DPC$^2$hat: Towards Dynamic Point Cloud Understanding with Failure-Aware Bootstrapping](https://arxiv.org/abs/2602.03890)
- [Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds](https://arxiv.org/abs/2602.00807) — `robustness`
- [AvAtar: Learning to Align via Active Optimal Transport](https://arxiv.org/abs/2605.24395) — `registration`
- [DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](https://arxiv.org/abs/2606.12189) — `reconstruction`
- [FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation](https://arxiv.org/abs/2605.27178) — `segmentation` `self-supervised` — [code](https://github.com/vLAR-group/FoundObj)
- [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://arxiv.org/abs/2606.12334)
- [SIMPC: Learning Self-Induced Mirror-Point Consistency for Unsupervised Point Cloud Denoising](https://arxiv.org/abs/2605.26894) — `denoising`
- [SplAttN: Bridging 2D and 3D with Gaussian Soft Splatting and Attention for Point Cloud Completion](https://arxiv.org/abs/2605.01466) — `completion`
- [Zero-Shot 3D Question Answering via Hierarchical View-to-Token Transportation](https://arxiv.org/abs/2606.03100) — `open-vocabulary`

</details>

<details><summary><b>AAAI</b> · 29</summary>

- [3D-ANC: Adaptive Neural Collapse for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2511.07040) — `robustness`
- [Adapt-As-You-Walk Through the Clouds: Training-Free Online Test-Time Adaptation of 3D Vision-Language Foundation Models](https://arxiv.org/abs/2511.15311) — `open-vocabulary` `vision-language`
- [Adaptive Agent Selection and Interaction Network for Image-to-point cloud Registration](https://arxiv.org/abs/2511.05965) — `registration` `detection`
- [BEVDilation: LiDAR-Centric Multi-Modal Fusion for 3D Object Detection](https://arxiv.org/abs/2512.02972) — `detection` `BEV` `multi-modal`
- [CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection](https://arxiv.org/abs/2511.12909) — `detection` `self-supervised` `anomaly detection`
- [Certified L2-Norm Robustness of 3D Point Cloud Recognition in the Frequency Domain](https://arxiv.org/abs/2511.07029) — `classification` `autonomous driving` `robustness`
- [Class-Partitioned VQ-VAE and Latent Flow Matching for Point Cloud Scene Generation](https://arxiv.org/abs/2601.12391) — `generation`
- [CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking](https://arxiv.org/abs/2511.15580) — `tracking` `compression` `autonomous driving`
- [DANCE: Density-agnostic and Class-aware Network for Point Cloud Completion](https://arxiv.org/abs/2511.07978) — `completion`
- [DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion](https://arxiv.org/abs/2511.20278) — `completion`
- [DeepRAHT: Learning Predictive RAHT for Point Cloud Attribute Compression](https://arxiv.org/abs/2601.12255) — `reconstruction` `compression`
- [DriveLiDAR4D: Sequential and Controllable LiDAR Scene Generation for Autonomous Driving](https://arxiv.org/abs/2511.13309) — `generation` `autonomous driving`
- [Enhancing Rotation-Invariant 3D Learning with Global Pose Awareness and Attention Mechanisms](https://arxiv.org/abs/2511.08833)
- [EPSegFZ: Efficient Point Cloud Semantic Segmentation for Few- and Zero-Shot Scenarios with Language Guidance](https://arxiv.org/abs/2511.11700) — `segmentation` `open-vocabulary` `efficiency`
- [Graph Smoothing for Enhanced Local Geometry Learning in Point Cloud Analysis](https://arxiv.org/abs/2601.11102)
- [HandMCM: Multi-modal Point Cloud-based Correspondence State Space Model for 3D Hand Pose Estimation](https://arxiv.org/abs/2602.01586) — `multi-modal`
- [Hierarchical Direction Perception via Atomic Dot-Product Operators for Rotation-Invariant Point Clouds Learning](https://arxiv.org/abs/2511.08240) — [code](https://github.com/wxszreal0/DiPVNet)
- [LiNeXt: Revisiting LiDAR Completion with Efficient Non-Diffusion Architectures](https://arxiv.org/abs/2511.10209) — `completion` `reconstruction` `efficiency`
- [MR-COSMO: Visual-Text Memory Recall and Direct CrOSs-MOdal Alignment Method for Query-Driven 3D Segmentation](https://arxiv.org/abs/2506.20991) — `segmentation`
- [P-SLCR: Unsupervised Point Cloud Semantic Segmentation via Prototypes Structure Learning and Consistent Reasoning](https://arxiv.org/abs/2603.06321) — `segmentation`
- [Point Cloud Quantization through Multimodal Prompting for 3D Understanding](https://arxiv.org/abs/2511.12079) — `multi-modal` `efficiency`
- [Point-SRA: Self-Representation Alignment for 3D Representation Learning](https://arxiv.org/abs/2601.01746) — `reconstruction`
- [RadarLLM: Empowering Large Language Models to Understand Human Motion from Millimeter-Wave Point Cloud Sequence](https://arxiv.org/abs/2504.09862)
- [Real-Time 3D Object Detection with Inference-Aligned Learning](https://arxiv.org/abs/2511.16140) — `detection` `efficiency`
- [Rethinking Multimodal Point Cloud Completion: A Completion-by-Correction Perspective](https://arxiv.org/abs/2511.12170) — `completion` `multi-modal`
- [Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation](https://arxiv.org/abs/2512.19088) — `segmentation` `open-vocabulary` — Workshop
- [TOSC: Task-Oriented Shape Completion for Open-World Dexterous Grasp Generation from Partial Point Clouds](https://arxiv.org/abs/2601.05499) — `completion` `generation`
- [Understanding Dynamic Scenes in Ego Centric 4D Point Clouds](https://arxiv.org/abs/2508.07251)
- [Walking Further: Semantic-aware Multimodal Gait Recognition Under Long-Range Conditions](https://arxiv.org/abs/2603.14189) — `multi-modal`

</details>

<details><summary><b>IJCAI</b> · 1</summary>

- [Rethinking Multimodal Few-Shot 3D Point Cloud Segmentation: From Fused Refinement to Decoupled Arbitration](https://arxiv.org/abs/2601.01456) — `segmentation` `multi-modal`

</details>

<details><summary><b>SIGGRAPH</b> · 1</summary>

- [A Bayesian Approach for Task-Specific Next-Best-View Selection with Uncertain Geometry](https://arxiv.org/abs/2605.05095) — `reconstruction` — [code](https://github.com/jingsenzhu/BayesianNBV)

</details>

<details><summary><b>SIGGRAPH Asia</b> · 1</summary>

- [CRAB: Cuboid-based Representation for As-built BIM from Point Clouds](https://arxiv.org/abs/2610.29257) — `reconstruction`

</details>

<details><summary><b>ACM MM</b> · 7</summary>

- [FocusTrack: One-Stage Focus-and-Suppress Framework for 3D Point Cloud Object Tracking](https://arxiv.org/abs/2602.24133) — `segmentation` `tracking`
- [Leveraging 2D Foundation Priors for Generalized Category Discovery under Test-Time Adaptation in 3D LiDAR Segmentation](https://arxiv.org/abs/2611.01682) — `segmentation` `autonomous driving`
- [MMCoT$^3$: Empowering 3D Scene Understanding with 3D-Text Interleaved Multi-Modal Chain-of-Thought Reasoning](https://arxiv.org/abs/2611.01676) — `multi-modal`
- [PointQ-Bench: Benchmarking Diagnostic and Interpretable Point Cloud Quality Assessment](https://arxiv.org/abs/2605.28241) — `reconstruction`
- [ProjFormer: Point Cloud Completion via Geometric-Projective Transformer and Cross-Modal Semantic Constraints](https://arxiv.org/abs/2608.15104) — `completion`
- [SeqAlign3DVG: A Sequence-Aligned Benchmark and Voxel Reasoning Framework for 3D Visual Grounding](https://arxiv.org/abs/2608.30451) — `dataset`
- [VGGT-Align: Bridging Local Reconstruction and Global Consistency for Long-Sequence 3D Reconstruction](https://arxiv.org/abs/2608.15260) — `reconstruction` — [code](https://github.com/WZ-CS/VGGT-Align)

</details>

<details><summary><b>3DV</b> · 4</summary>

- [Finding NeMO: A Geometry-Aware Representation of Template Views for Few-Shot Perception](https://arxiv.org/abs/2602.04343) — `segmentation`
- [Hierarchical Space Partition for Surface Reconstruction](https://arxiv.org/abs/2606.04891) — `reconstruction`
- [Layered Quantum Architecture Search for 3D Point Cloud Classification](https://arxiv.org/abs/2603.20024) — `classification`
- [Symmetry Informative and Agnostic Feature Disentanglement for 3D Shapes](https://arxiv.org/abs/2601.14804)

</details>

<details><summary><b>WACV</b> · 13</summary>

- [3D-BBDA: Backpropagation-Free Black-Box Domain Adaptation for Robust 3D Point Cloud Recognition](https://arxiv.org/abs/2611.03588) — `domain adaptation` `robustness`
- [Curve Skeletonization in Continuous domain for Meshes and Point Clouds](https://arxiv.org/abs/2605.25921)
- [Do We Still Need Rotation-Invariant Architectures? A Statistical Robustness Benchmark for Point Cloud Classification](https://arxiv.org/abs/2611.03952) — `classification` `robustness` `dataset`
- [Embedding Predictive Adaptation and Refinement for Multi-Modal Industrial Anomaly Detection](https://arxiv.org/abs/2611.09521) — `detection` `multi-modal` `anomaly detection`
- [GUSH3R: Everyone Everywhere All at Once as Gaussians](https://arxiv.org/abs/2607.05243) — `reconstruction` `monocular`
- [JOPP-3D: Joint Open Vocabulary Semantic Segmentation on Point Clouds and Panoramas](https://arxiv.org/abs/2603.06168) — `segmentation` `open-vocabulary`
- [RadPose: ISAC-based RF 3D Human Pose Estimation](https://arxiv.org/abs/2611.01400)
- [Recovering Black-Box Point Cloud Models from Pose Shifts via Derivative-Free Optimization](https://arxiv.org/abs/2610.34850)
- [Rohbau3D-Semantics: Dense Semantic and Instance Labels for Point Clouds of Indoor Shell Construction Scenes](https://arxiv.org/abs/2611.06180)
- [SAGE: Semantic-Augmented Geometric Experts for Point Cloud Registration](https://arxiv.org/abs/2610.36658) — `registration` `reconstruction`
- [SATOR: Backpropagation-Free 3D Test-Time Adaptation via Sample-Adaptive Token Routing](https://arxiv.org/abs/2610.21367)
- [VaViT: Vanilla ViT for Automotive Point Cloud Semantic Segmentation](https://arxiv.org/abs/2605.31177) — `segmentation`
- [You Only Flow Once: Calibrated and Real-Time Radar Pose Estimation with Multi-Hypothesis Normalizing Flows](https://arxiv.org/abs/2608.09579) — `denoising` `multi-modal` `efficiency`

</details>

<details><summary><b>BMVC</b> · 8</summary>

- [3D-MRL: Nested Multimodal 3D Representations via Matryoshka Representation Learning](https://arxiv.org/abs/2608.29285) — `open-vocabulary` `multi-modal`
- [Depth-Guided Privacy-Preserving Visual Localization Using 3D Sphere Clouds](https://arxiv.org/abs/2605.00562) — `localization`
- [End-to-End LiDAR optimization for 3D point cloud registration](https://arxiv.org/abs/2602.10492) — `registration`
- [FlexSplat: Flexible Feed-Forward 3D Gaussian Splatting without Point Cloud Correspondence](https://arxiv.org/abs/2608.07937) — `gaussian-splatting` — [code](https://github.com/amir-sbg/FlexSplat)
- [ForestMamba: Sparse Mamba with Geometry-guided Queries for 3D Forest Point Cloud Segmentation](https://arxiv.org/abs/2606.01549) — `segmentation`
- [GEKey: Learning Geodesic Eccentric 3D Keypoints via Self-Supervision](https://arxiv.org/abs/2611.07677) — `detection`
- [Hyper^2: Unleashing Hyperbolic Geometry's Full Potential via Dual-Space Consistency](https://arxiv.org/abs/2608.22238) — `completion`
- [ReFineR: Single image to dense point cloud registration at pixel level with point splatting](https://arxiv.org/abs/2611.16583) — `registration` `detection`

</details>

<details><summary><b>ICRA</b> · 9</summary>

- [Angle-I2P: Angle-Consistent-Aware Hierarchical Attention for Cross-Modality Outlier Rejection](https://arxiv.org/abs/2605.04541) — `registration` `localization`
- [D-Compress: Detail-Preserving LiDAR Range Image Compression for Real-Time Streaming on Resource-Constrained Robots](https://arxiv.org/abs/2603.13699) — `compression` `efficiency`
- [Dr-PoGO: Direct Radar Pose-Graph Optimization](https://arxiv.org/abs/2605.04806) — `slam` `localization` `multi-modal`
- [DRUM: Diffusion-based Raydrop-aware Unpaired Mapping for Sim2Real LiDAR Segmentation](https://arxiv.org/abs/2603.26263) — `segmentation`
- [Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model](https://arxiv.org/abs/2607.06896) — `detection` `tracking` `slam` — Workshop
- [P3T: Prototypical Point-level Prompt Tuning with Enhanced Generalization for 3D Vision-Language Models](https://arxiv.org/abs/2604.15703) — `vision-language`
- [PIRATR: Parametric Object Inference for Robotic Applications with Transformers in 3D Point Clouds](https://arxiv.org/abs/2602.05557) — `detection` `localization`
- [R3DPA: Leveraging 3D Representation Alignment and RGB Pretrained Priors for LiDAR Scene Generation](https://arxiv.org/abs/2601.07692) — `generation` `autonomous driving` `pre-training`
- [SLNet: A Super-Lightweight Geometry-Adaptive Network for 3D Point Cloud Recognition](https://arxiv.org/abs/2603.07454) — `efficiency`

</details>

<details><summary><b>IROS</b> · 11</summary>

- [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](https://arxiv.org/abs/2606.31329) — [code](https://github.com/DAVIAN-Robotics/3D_HAMSTER)
- [DeeperRadar: End-to-End MIMO Radar Design and Multi-Modal Fusion for Autonomous Vehicle Perception](https://arxiv.org/abs/2607.17351) — `detection` `multi-modal`
- [DiFF: Doppler-informed Flow Matching for Human Motion Flow](https://arxiv.org/abs/2609.39098) — `generation` `scene flow` — [code](https://github.com/keroseus/DiFF)
- [FIRE-LIVWO: Robust LiDAR-Inertial-Visual-Wheel Odometry via Failure-Immune mmWave Radar Enhancement](https://arxiv.org/abs/2609.05325) — `slam` `multi-modal` `robustness`
- [Hydra++: Real-Time Hierarchical 3D Scene Graph Construction With Object-Level Shape Estimation](https://arxiv.org/abs/2607.09455) — `efficiency`
- [Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping](https://arxiv.org/abs/2609.26325) — `detection` `autonomous driving` — Workshop
- [Multi-modal panoramic 3D outdoor datasets for place categorization](https://arxiv.org/abs/2604.13142) — `multi-modal`
- [Neural Surface and Reflectance Modelling from 3D Radar Data](https://arxiv.org/abs/2603.25623) — `reconstruction` `multi-modal`
- [NIDAR: NIR-Guided Intrinsic Decomposition for Scalable Scene-Agnostic LiDAR Intensity Reconstruction](https://arxiv.org/abs/2609.36878) — `reconstruction`
- [Two-Stage Extrinsic Calibration of a Static Line-Scanning Lidar with a Rotary Platform](https://arxiv.org/abs/2607.18578)
- [Vernata: Self-Supervised Learning of LiDAR Point Representations](https://arxiv.org/abs/2608.06919) — `self-supervised` — [code](https://github.com/rai-opensource/vernata)

</details>

<details><summary><b>RA-L</b> · 9</summary>

- [C-ARC: Continuous-Adaptive Range Clustering for Non-Repetitive LiDAR Sensors](https://arxiv.org/abs/2606.18948)
- [EquiGQNet: Fast Grasp Quality Evaluation via Shared Equivariant Point Cloud Encoding](https://arxiv.org/abs/2609.07145)
- [Geometry-Aware Fisheye-LiDAR Fusion for Robust 3D Object Detection in Low-Overlap Setups](https://arxiv.org/abs/2606.08844) — `detection` `robustness`
- [Layered Safety: Enhancing Autonomous Collision Avoidance via Multistage CBF Safety Filters](https://arxiv.org/abs/2603.00338)
- [Point Cloud Segmentation for Autonomous Clip Positioning in Laparoscopic Cholecystectomy on a Phantom](https://arxiv.org/abs/2606.12048) — `segmentation`
- [PointWalker: Mapless Quadruped Locomotion Directly From Raw LiDAR Point Clouds](https://arxiv.org/abs/2610.15548)
- [PROBE: Probabilistic Occupancy BEV Encoding with Analytical Translation Robustness for 3D Place Recognition](https://arxiv.org/abs/2603.05965) — `localization` `BEV` `robustness`
- [UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping](https://arxiv.org/abs/2606.26928)
- [Visual Sculpting: Visually-Aligned Planning Representations for Long-Horizon Robot Clay Sculpting](https://arxiv.org/abs/2605.17556)

</details>

<details><summary><b>TPAMI</b> · 3</summary>

- [Efficient Point Cloud Processing with High-Dimensional Positional Encoding and Non-Local MLPs](https://arxiv.org/abs/2603.04099) — `efficiency` — [code](https://github.com/zouyanmei/HPENet_v2.git)
- [GAPrompt++: Multi-Granular Geometry-Aware Point Cloud Prompt for 3D Vision Model](https://arxiv.org/abs/2609.19716) — [code](https://github.com/PKU-OV3-LAB/GAPromptPlus.git)
- [PPC-MT: Parallel Point Cloud Completion with Mamba-Transformer Hybrid Architecture](https://arxiv.org/abs/2603.00870) — `completion` `reconstruction`

</details>

<details><summary><b>TIP</b> · 1</summary>

- [SPARK: Scalable Real-Time Point Cloud Aggregation with Multi-View Self-Calibration](https://arxiv.org/abs/2601.08414) — `reconstruction` `efficiency`

</details>

<details><summary><b>TVCG</b> · 1</summary>

- [Viewpoint Recommendation for Point Cloud Labeling through Interaction Cost Modeling](https://arxiv.org/abs/2602.10871) — `segmentation` `autonomous driving`

</details>

<details><summary><b>ISPRS</b> · 10</summary>

- [3D Point Cloud from Close-Range Photogrammetry for Defect Characterisation of Rubberised Concrete](https://arxiv.org/abs/2608.21468) — `anomaly detection`
- [Accurate Point Measurement in 3DGS -- A New Alternative to Traditional Stereoscopic-View Based Measurements](https://arxiv.org/abs/2603.24716) — `gaussian-splatting`
- [BathyFacto: Refraction-Aware Two-Media Neural Radiance Fields for Bathymetry](https://arxiv.org/abs/2605.10174) — `nerf`
- [DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring](https://arxiv.org/abs/2610.09860)
- [Extrusion Segmentation Strategy to improve CAD Reconstruction from Point Cloud](https://arxiv.org/abs/2605.08971) — `segmentation` `reconstruction`
- [In-Field 3D Wheat Head Instance Segmentation From TLS Point Clouds Using Deep Learning Without Manual Labels](https://arxiv.org/abs/2603.14309) — `segmentation`
- [Incremental Semantics-Aided Meshing from LiDAR-Inertial Odometry and RGB Direct Label Transfer](https://arxiv.org/abs/2604.09478) — `reconstruction`
- [PC2Model: ISPRS benchmark on 3D point cloud to model registration](https://arxiv.org/abs/2604.19596) — `registration` `autonomous driving` `dataset`
- [Shape Representation using Gaussian Process mixture models](https://arxiv.org/abs/2604.00862)
- [Structured-Li-GS: Structured 3D Gaussians Splatting with LiDAR Incorporation and Spatial Constraints](https://arxiv.org/abs/2606.27509) — `slam` `gaussian-splatting`

</details>

<details><summary><b>PR</b> · 8</summary>

- [An Adapter-free Fine-tuning Approach for Tuning 3D Foundation Models](https://arxiv.org/abs/2603.23730)
- [LCF3D: A Robust and Real-Time Late-Cascade Fusion Framework for 3D Object Detection in Autonomous Driving](https://arxiv.org/abs/2601.09812) — `detection` `autonomous driving` `robustness` `efficiency`
- [Loss Landscape Topology Reveals Why Simple Baselines are Competitive at 3D Point Cloud Segmentation Under Class Imbalance](https://arxiv.org/abs/2607.21089) — `segmentation`
- [OPTNet: Ordering Point Transformer Network for Post-disaster 3D Semantic Segmentation](https://arxiv.org/abs/2605.17197) — `segmentation`
- [Physics-inspired Pseudo Anomaly Generation and Prototype Feature Guidance for 3D Anomaly Detection](https://arxiv.org/abs/2607.10544) — `detection` `generation` `anomaly detection`
- [Point Cloud as a Foreign Language for Multi-modal Large Language Model](https://arxiv.org/abs/2603.09173) — `multi-modal`
- [PointTransformerX: Portable and Efficient 3D Point Cloud Processing without Sparse Algorithms](https://arxiv.org/abs/2604.24169) — `efficiency` — Workshop
- [PRISM: Color-Stratified Point Cloud Sampling](https://arxiv.org/abs/2601.06839)

</details>

<details><summary><b>arXiv</b> · 409</summary>

- [2L-LSH: A Locality-Sensitive Hash Function-Based Method For Rapid Point Cloud Indexing](https://arxiv.org/abs/2604.21442) — `classification` `reconstruction`
- [3D LULC classification using multispectral LiDAR and deep learning: current and prospective schemes](https://arxiv.org/abs/2605.22328) — `segmentation` `classification`
- [3DTMDet: A Dual-Path Synergy Network of Transformer and SSM for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2605.15546) — `detection`
- [4DGS-WAM: Bridging Past and Future with an Object-Centric World Action Model based on 4D Gaussian Splatting](https://arxiv.org/abs/2608.25956) — `gaussian-splatting`
- [A B-Spline Function Based 3D Point Cloud Unwrapping Scheme for 3D Fingerprint Recognition and Identification](https://arxiv.org/abs/2604.16546)
- [A Clinical Point Cloud Paradigm for In-Hospital Mortality Prediction from Multi-Level Incomplete Multimodal EHRs](https://arxiv.org/abs/2604.04614) — `multi-modal`
- [A Closed-Form Persistence-Landmark Pipeline for Certified Point-Cloud and Graph Classification](https://arxiv.org/abs/2605.02836) — `classification`
- [A Complete Geometric Message-Passing Architecture for Point Clouds](https://arxiv.org/abs/2611.26384)
- [A Comprehensive Survey on Deep Learning-Based LiDAR Super-Resolution for Autonomous Driving](https://arxiv.org/abs/2602.15904) — `upsampling` `autonomous driving`
- [A Differentiable Optimization Framework for Registering Sequential Bounding Boxes with Point Cloud Stream](https://arxiv.org/abs/2609.34103) — `registration`
- [A meshfree exterior calculus for generalizable and data-efficient learning of physics from point clouds](https://arxiv.org/abs/2605.08436) — `efficiency`
- [A multi-platform LiDAR dataset for standardized forest inventory measurement at long term ecological monitoring sites](https://arxiv.org/abs/2604.14635) — `dataset`
- [A Numerically-Robust ROS 2 Port of iG-LIO: Diagnosing and Fixing Toolchain-Induced Failures in Incremental GICP LiDAR-Inertial Odometry](https://arxiv.org/abs/2607.09947) — `robustness`
- [A Persistent Homology Design Space for 3D Point Cloud Deep Learning](https://arxiv.org/abs/2604.04299)
- [A Point Cloud Transformer for Remote Monitoring and Automated Assessment of Physical Rehabilitation Exercises](https://arxiv.org/abs/2606.30309)
- [A Robust Point Cloud Analysis Framework Inspired By Primary Visual Cortex](https://arxiv.org/abs/2606.14292) — `robustness`
- [A Survey on Deep Learning Architectures for Point Cloud Classification and Segmentation](https://arxiv.org/abs/2605.17131) — `segmentation` `classification` — [code](https://github.com/MinhasKamal/DeepLearningForPointCloud)
- [A Systematic Point Cloud Edge Detection Framework for Automatic Aircraft Skin Milling](https://arxiv.org/abs/2611.04435) — `detection`
- [A Three-Dimensional Reverse-Projection Method for Sparse Point Cloud Completion and Its Application to High-Speed Train Nose Reconstruction](https://arxiv.org/abs/2610.05758) — `completion` `reconstruction`
- [A Unified Non-Parametric and Interpretable Point Cloud Analysis via t-FCW Graph Representation](https://arxiv.org/abs/2605.15475) — `classification`
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
- [An Open-Source LiDAR and Monocular Off-Road Autonomous Navigation Stack](https://arxiv.org/abs/2604.03096) — `detection` `monocular`
- [AnchorComplete: Recovering Complete Scene Meshes from Partial Point Clouds](https://arxiv.org/abs/2611.03228)
- [Annotation-Free Detection of Drivable Areas and Curbs Leveraging LiDAR Point Cloud Maps](https://arxiv.org/abs/2603.27553) — `detection` `autonomous driving`
- [Assessing the Operational Impact of Poisoning Attacks over Augmented 3D Point Cloud Public Datasets for Connected and Autonomous Vehicles](https://arxiv.org/abs/2607.06484)
- [Autoencoder Based Deep Clustering of Point Clouds](https://arxiv.org/abs/2611.01594) — `generation` `reconstruction`
- [Automated Digital Twin Construction for Highway Scenarios Using LiDAR Point Clouds and OpenStreetMap](https://arxiv.org/abs/2606.16570)
- [Automated Discontinuity Set Characterisation in Enclosed Rock Face Point Clouds Using Single-Shot Filtering and Cyclic Orientation Transformation](https://arxiv.org/abs/2602.01783)
- [Bayesian methods and Markov chain Monte Carlo algorithms for curve reconstruction and point cloud data analysis](https://arxiv.org/abs/2608.26490) — `localization` `reconstruction`
- [Benchmarking Deep Learning Models for Aerial LiDAR Point Cloud Semantic Segmentation under Real Acquisition Conditions: A Case Study in Navarre](https://arxiv.org/abs/2603.22229) — `segmentation`
- [Beyond Defenses: Manifold-Aligned Regularization for Intrinsic 3D Point Cloud Robustness](https://arxiv.org/abs/2605.07590) — `robustness`
- [Beyond Distance: Quantifying Point Cloud Dynamics with Persistent Homology and Dynamic Optimal Transport](https://arxiv.org/abs/2603.15683)
- [Beyond Gait: Person Identification from Millimeter-Wave Point Clouds Across Activities of Daily Living](https://arxiv.org/abs/2609.08818)
- [Beyond the Vehicle: Cooperative Localization by Fusing Point Clouds for GPS-Challenged Urban Scenarios](https://arxiv.org/abs/2602.03908) — `registration` `localization`
- [Beyond Visibility: Real-Time Surface Accessibility Fields from Sparse LiDAR](https://arxiv.org/abs/2608.06412) — `reconstruction` `efficiency`
- [BIEVR-LIO: Robust LiDAR-Inertial Odometry through Bump-Image-Enhanced Voxel Maps](https://arxiv.org/abs/2604.14421) — `registration` `robustness`
- [Blind Quality Enhancement for G-PCC Compressed Dynamic Point Clouds](https://arxiv.org/abs/2603.24026) — `reconstruction` `compression`
- [Boundary Detection for High-Dimensional Point Clouds](https://arxiv.org/abs/2610.23590) — `detection`
- [Boundary-Enhanced Segmentation of Pig Point Clouds in Commercial Housing Environments](https://arxiv.org/abs/2608.11697) — `segmentation` `completion`
- [BRICE: Brain-inspired Recurrent Illusory Contour Encoder for Point Cloud Completion](https://arxiv.org/abs/2610.23001) — `completion`
- [Bridging the Modality Gap in Roadside LiDAR: A Training-Free Vision-Language Model Framework for Vehicle Classification](https://arxiv.org/abs/2602.09425) — `classification` `vision-language`
- [Camera and LiDAR BEV Fusion for Cooperative 3D Object Detection on TUMTraf V2X](https://arxiv.org/abs/2606.12981) — `detection` `BEV`
- [Camera Radar LiDAR Fusion via Point-Cloud Projection for Multi-Task Learning](https://arxiv.org/abs/2611.03942) — `multi-modal` — Workshop
- [Can 3D point cloud data improve automated body condition score prediction in dairy cattle?](https://arxiv.org/abs/2601.22522)
- [Car Drag Coefficient Prediction from 3D Point Clouds Using a Slice-Based Surrogate Model](https://arxiv.org/abs/2601.02112)
- [CedarCypress3D: an annotated UAV-LiDAR dataset of individual trees in planted cedar and cypress forests](https://arxiv.org/abs/2608.30149) — `detection` `dataset`
- [Channel-Level Relation to Attentive Aggregation with Neighborhood-Homogeneity Constraint for Point Cloud Analysis](https://arxiv.org/abs/2605.02357) — `autonomous driving`
- [Characterizing the vertical continuity of fuel strata based on TLS point clouds Gaussian decomposition and overlap metrics](https://arxiv.org/abs/2611.05102)
- [CloudDiffusion: Diffusion-Based Scene Completion in the Point Cloud Domain](https://arxiv.org/abs/2606.16048) — `completion` `reconstruction` `autonomous driving`
- [CMHANet: A Cross-Modal Hybrid Attention Network for Point Cloud Registration](https://arxiv.org/abs/2603.12721) — `registration` `reconstruction`
- [Collaborative Learning for Semi-Supervised LiDAR Semantic Segmentation](https://arxiv.org/abs/2605.17135) — `segmentation`
- [Collision-Aware and Observation-Aligned Object-Centric Scene Reconstruction from Point Cloud](https://arxiv.org/abs/2609.37260) — `generation` `reconstruction`
- [Comparative evaluation of photogrammetric reconstruction methods and 3D Gaussian Splatting for road surface roughness analysis](https://arxiv.org/abs/2605.29452) — `reconstruction` `gaussian-splatting`
- [Complexity-Calibrated Reconstruction Discrepancy for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2610.13219) — `reconstruction`
- [Confidence-Driven Facade Refinement of 3D Building Models Using MLS Point Clouds](https://arxiv.org/abs/2604.03797)
- [Contextual Range-View Projection for 3D LiDAR Point Clouds](https://arxiv.org/abs/2601.18301)
- [Contrastive Metric Learning for Point Cloud Segmentation in Highly Granular Detectors](https://arxiv.org/abs/2603.23356) — `segmentation`
- [CORAL: Curriculum-Optimized Reward Adaptation for LiDAR-Based Goal-Directed Urban Driving](https://arxiv.org/abs/2608.14332) — `tracking`
- [CorrelationFlow: A Training-Free Geometric Approach for LiDAR Scene Flow Estimation](https://arxiv.org/abs/2607.29237) — `scene flow` `autonomous driving`
- [COSTA: A Cluster-Centric Paradigm for Annotation-Free Open-Set Semantic Segmentation of Aerial Point Clouds with Domain Shifts](https://arxiv.org/abs/2608.18479) — `segmentation`
- [Cross-Coordinate Correspondence Pruning for Image-to-Point Cloud Registration](https://arxiv.org/abs/2607.17200) — `registration` `detection` `efficiency`
- [Cross-view Domain Generalization via Geometric Consistency for LiDAR Semantic Segmentation](https://arxiv.org/abs/2602.14525) — `segmentation`
- [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](https://arxiv.org/abs/2607.00514) — `self-supervised`
- [CUFormer: Modality-Aware CT-Ultrasound Point Cloud Registration for Orthopedic Navigation](https://arxiv.org/abs/2611.01536) — `registration`
- [CVSD-Reg: Cross-Modal Visual Semantic Prior Distillation for Robust LiDAR Registration](https://arxiv.org/abs/2608.19536) — `registration` `robustness`
- [Cyclops: LiDAR as a Camera That Dreams in Color](https://arxiv.org/abs/2608.16264) — `detection` — [code](https://github.com/IMRL/Cyclops)
- [D-SLAMSpoof: An Environment-Agnostic LiDAR Spoofing Attack using Dynamic Point Cloud Injection](https://arxiv.org/abs/2603.11365) — `slam`
- [DAL-PCQA: Enabling Distortion-Level and Language-Driven Reasoning for Point Cloud Quality Assessment](https://arxiv.org/abs/2606.07938)
- [DALD-PCAC: Density-Adaptive Learning Descriptor for Point Cloud Lossless Attribute Compression](https://arxiv.org/abs/2601.12261) — `compression`
- [Damage Classification for 3D Point Cloud Data via 3D Data Analysis and Vision Foundation Model-based 2D Projections](https://arxiv.org/abs/2608.08955) — `classification` `pre-training`
- [DAPointRWKV: Domain Adaptive Vision RWKV for Point Cloud Completion](https://arxiv.org/abs/2611.10353) — `completion`
- [Data-Efficient Semantic Segmentation of 3D Point Clouds via Open-Vocabulary Image Segmentation-based Pseudo-Labeling](https://arxiv.org/abs/2604.11007) — `segmentation` `open-vocabulary` `efficiency`
- [DC-Reg: Globally Optimal Point Cloud Registration via Tight Bounding with Difference of Convex Programming](https://arxiv.org/abs/2603.25442) — `registration`
- [Deep learning based Non-Rigid Volume-to-Surface Registration for Brain Shift compensation Using Point Cloud](https://arxiv.org/abs/2604.17389) — `registration`
- [Degree Bounds for Separating Polynomial and Neural Invariants for Point Clouds](https://arxiv.org/abs/2610.26612)
- [Delaunay Canopy: Building Wireframe Reconstruction from Airborne LiDAR Point Clouds via Delaunay Graph](https://arxiv.org/abs/2604.02497) — `reconstruction`
- [Denoising-Aware Temporal Point Cloud Completion for 3D Crop Architecture Recovery and Phenotypic Trait Extraction](https://arxiv.org/abs/2608.28343) — `completion` `reconstruction` `denoising`
- [Denoising-GS: Gaussian Splatting with Spatial-aware Denoising](https://arxiv.org/abs/2605.14880) — `gaussian-splatting` `denoising`
- [Depth-Dependent Hidden-State Collapse in Dynamical System Autoencoders for LiDAR Point-Cloud Classification](https://arxiv.org/abs/2607.14463) — `classification`
- [Depth-Semantic Alignment and Affinity-Guided Fusion for Structured Radar Point Cloud Generation](https://arxiv.org/abs/2606.26743) — `detection` `tracking` `generation` `multi-modal`
- [Development and Validation of an Integrated LiDAR-Camera System for Real-Time Monitoring of Underground Longwall Operations](https://arxiv.org/abs/2605.02516) — `multi-modal` `efficiency`
- [DGS-Net: Learning Dexterous Grasps from Single-View Point Clouds via a Multi-Object Scene Dataset](https://arxiv.org/abs/2603.15410) — `dataset`
- [Diffusion-Driven Inter-Outer Surface Separation for Point Clouds with Open Boundaries](https://arxiv.org/abs/2602.00739) — `reconstruction`
- [DINE: Distance Is Not Enough -- Learning Global Deformation Priors for Robust Soft-Tissue Point Cloud Registration](https://arxiv.org/abs/2607.14946) — `registration` `robustness`
- [Direct Estimation of Tree Volume and Aboveground Biomass Using Deep Regression with Synthetic Lidar Data](https://arxiv.org/abs/2603.04683)
- [Discrete Fourier Transform-based Point Cloud Compression for Efficient SLAM in Featureless Terrain](https://arxiv.org/abs/2601.04551) — `slam` `localization` `compression` `efficiency`
- [Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations and Goals](https://arxiv.org/abs/2608.29434)
- [DPA-I2P: Depth-Guided Projective Alignment for Image-to-Point-Cloud Registration in Autonomous Driving](https://arxiv.org/abs/2608.26589) — `registration` `localization` `autonomous driving`
- [DRIFT: Dual-Representation Inter-Fusion Transformer for Automated Driving Perception with 4D Radar Point Clouds](https://arxiv.org/abs/2603.09695) — `multi-modal`
- [Drones as Annotators: Amodal 3D Auto-Labeling for Ground LiDAR with Aerial Priors](https://arxiv.org/abs/2609.06819) — `autonomous driving`
- [DUGAE: Unified Geometry and Attribute Enhancement via Spatiotemporal Correlations for G-PCC Compressed Dynamic Point Clouds](https://arxiv.org/abs/2603.26183) — `compression`
- [EdgeFormer: local patch-based edge detection transformer on point clouds](https://arxiv.org/abs/2604.21387) — `detection`
- [Efficient Dense Matching for Enhanced Gaussian Splatting Using AV1 Motion Vectors](https://arxiv.org/abs/2605.14629) — `reconstruction` `nerf` `gaussian-splatting` `efficiency`
- [Efficient RWKV-based Representation Learning for 3D Point Clouds](https://arxiv.org/abs/2606.10395) — `efficiency`
- [EgoNeMo: Transferable Map of Pedestrian Dynamics via Egocentric LiDAR Scan](https://arxiv.org/abs/2609.06195)
- [EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion](https://arxiv.org/abs/2609.26039) — `generation`
- [Enhancing 3D LiDAR Segmentation by Shaping Dense and Accurate 2D Semantic Predictions](https://arxiv.org/abs/2602.18869) — `segmentation`
- [EquiForm: Noise-Robust SE(3)-Equivariant Policy Learning from 3D Point Clouds](https://arxiv.org/abs/2601.17486) — `robustness`
- [EXACT-MPPI: Exact Signed-Distance Navigation for Arbitrary-Footprint Robots from Point Clouds via Path Integral Control](https://arxiv.org/abs/2605.29663)
- [Exploring Easy Boosts for Lidar Semantic Scene Completion](https://arxiv.org/abs/2606.03992) — `completion` `occupancy prediction`
- [Fast and Accurate Outlier-Aware LiDAR Super-Resolution for SLAM Applications](https://arxiv.org/abs/2606.28607) — `slam` `upsampling`
- [Fast Attention-Based Simplification of LiDAR Point Clouds for Object Detection and Classification](https://arxiv.org/abs/2603.07593) — `detection` `classification` `autonomous driving`
- [Fi-Gaussian: Frequency-Aware Implicit Gaussian Splatting for Single Image Dehazing](https://arxiv.org/abs/2606.16168) — `gaussian-splatting`
- [Finite-time Stable Pose Estimation on TSE(3) using Point Cloud and Velocity Sensors](https://arxiv.org/abs/2602.09414)
- [FlashFPS: Efficient Farthest Point Sampling for Large-Scale Point Clouds via Pruning and Caching](https://arxiv.org/abs/2604.17720) — `efficiency`
- [FlashReg: GPU-Accelerated 3-Clique Point Cloud Registration for Real-Time Correspondence-to-Pose Estimation](https://arxiv.org/abs/2608.21804) — `registration` `efficiency`
- [FLIP: Real-Time and Resilient Formation Planning for Large-Scale DIstributed Swarms via Point Cloud Registration](https://arxiv.org/abs/2605.29704) — `registration` `efficiency`
- [FLORA: A deep learning approach to predict forest attributes from heterogeneous LiDAR data](https://arxiv.org/abs/2606.32023)
- [FlowCalib: LiDAR-to-Vehicle Miscalibration Detection using Scene Flows](https://arxiv.org/abs/2601.23107) — `detection` `autonomous driving`
- [Fog-FWL: A Large-Scale Full-Waveform LiDAR Dataset for Recovering Fog-Hidden Objects](https://arxiv.org/abs/2611.16742) — `detection` `autonomous driving` `dataset`
- [ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation](https://arxiv.org/abs/2610.03403) — `segmentation`
- [FPSGen: Flexible Point Cloud Scene Generation with BEV-Supported Transport Flows](https://arxiv.org/abs/2607.26645) — `completion` `generation` `BEV`
- [FREE-LIVO: Physically Decoupled Yet Tightly Coupled LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2611.07463) — `slam`
- [From LiDAR Maps to Visual Localization: Unified Visual Association for Robust Point-Line-Plane Pose Estimation](https://arxiv.org/abs/2609.27363) — `localization` `robustness`
- [From Spherical to Gaussian: A Comparative Analysis of Point Cloud Cropping Strategies in Large-Scale 3D Environments](https://arxiv.org/abs/2605.02098)
- [FugSeg: Fast Uncertainty-aware Ground Segmentation for 3D Point Cloud](https://arxiv.org/abs/2605.08952) — `segmentation`
- [FUSE-Flow: Scalable Real-Time Multi-View Point Cloud Reconstruction Using Confidence](https://arxiv.org/abs/2602.01035) — `reconstruction` `efficiency`
- [G$^2$ARD-GS: Geometry-Guided Anchor-Regularized Gaussian Splatting Distillation](https://arxiv.org/abs/2608.05704) — `gaussian-splatting`
- [GATS: Gaussian Aware Temporal Scaling Transformer for Invariant 4D Spatio-Temporal Point Cloud Representation](https://arxiv.org/abs/2603.16154)
- [Gaussian Linear Functional Manifold Method for Massive Point Cloud Data](https://arxiv.org/abs/2609.05744) — `reconstruction`
- [GDPR-Compliant Person Recognition in Industrial Environments Using MEMS-LiDAR and Hybrid Data](https://arxiv.org/abs/2602.01764) — `detection`
- [GeGS-PCR: Effective and Robust 3D Point Cloud Registration with Two-Stage Color-Enhanced Geometric-3DGS Fusion](https://arxiv.org/abs/2604.17721) — `registration` `gaussian-splatting` `robustness`
- [GEM: Generating LiDAR World Model via Deformable Mamba](https://arxiv.org/abs/2605.07326) — `autonomous driving`
- [Generalized Wasserstein Flow Matching: Nested Couplings for Point Cloud Generation](https://arxiv.org/abs/2605.08424) — `generation`
- [Generalized-CVO: Fast and Correspondence-Free Local Point Cloud Registration with Second Order Riemannian Optimization](https://arxiv.org/abs/2606.10019) — `registration`
- [Generating Adversarial Events: A Motion-Aware Point Cloud Framework](https://arxiv.org/abs/2602.08230) — `autonomous driving` `robustness`
- [Generating Roadside LiDAR Datasets from Vehicle-Side Datasets via Novel View Synthesis](https://arxiv.org/abs/2605.05897)
- [GeoISF: Instance Semantic Forest Inspired Large-Scale Cross-View Geo-Localization via Ground LiDAR-to-Satellite Image](https://arxiv.org/abs/2606.28371) — `localization`
- [Geometry vs Structure: Graph-Based Diagnostics for LiDAR Point-Cloud Simulation Fidelity](https://arxiv.org/abs/2609.16378)
- [Geometry Without Coordinates: LiDAR Diffusion as a 3D Feature Bridge](https://arxiv.org/abs/2609.10322) — `generation`
- [Geometry-Based Compression of Plenoptic Point Clouds](https://arxiv.org/abs/2608.11273) — `compression`
- [Geometry-Constrained Bidirectional Point Cloud Registration for Thin, Sheet-Like Heritage Artifacts](https://arxiv.org/abs/2610.07793) — `registration` `reconstruction`
- [Geometry-Preserving Blind Watermarking for Raw 3D Point Clouds](https://arxiv.org/abs/2609.32222)
- [GRAR: Glass-induced Reflection Artifact Removal in LiDAR Point Clouds](https://arxiv.org/abs/2606.10541)
- [GreenSeg: Ground Segmentation Algorithm for Agricultural Robots in Mediterranean Greenhouses using RGB-D Point Clouds](https://arxiv.org/abs/2605.25279) — `segmentation`
- [GridFlow: Structured Latent Flow for Seamless City-Scale 3D Point Cloud Generation](https://arxiv.org/abs/2608.29793) — `generation`
- [GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.25966) — `registration`
- [GS-NFS: Bandwidth-adaptive Streaming of Dynamic Gaussian Splats and Point Clouds](https://arxiv.org/abs/2606.05650) — `gaussian-splatting`
- [GSeg3D: A High-Precision Grid-Based Algorithm for Safety-Critical Ground Segmentation in LiDAR Point Clouds](https://arxiv.org/abs/2603.04208) — `segmentation` `detection` `autonomous driving`
- [GSM-GS: Geometry-Constrained Single and Multi-view Gaussian Splatting for Surface Reconstruction](https://arxiv.org/abs/2602.12796) — `reconstruction` `gaussian-splatting`
- [GSPotential: Camera Potential Field for Sparse-View 3D Gaussian Splatting](https://arxiv.org/abs/2608.29346) — `gaussian-splatting`
- [GT-PCQA: Geometry-Texture Decoupled Point Cloud Quality Assessment with MLLM](https://arxiv.org/abs/2603.14951)
- [GTLR-GS: Geometry-Texture Aware LiDAR-Regularized 3D Gaussian Splatting for Realistic Scene Reconstruction](https://arxiv.org/abs/2603.23192) — `reconstruction` `gaussian-splatting`
- [GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly](https://arxiv.org/abs/2610.09068) — `segmentation` `reconstruction` `denoising`
- [H3DNAS: Hardware-Aware ONNX-Native 3D Point Cloud Model Compression](https://arxiv.org/abs/2609.02684) — `compression`
- [Hardware-triggered Time Synchronization of Roadside Multi-lidar, Multi-camera Measurement System for Accurate Data Alignment](https://arxiv.org/abs/2607.15889) — [code](https://github.com/shiva-THI/hardware-trigger-time-sync-lidar-cameras)
- [Heat Field Signatures: From Point Clouds to Smooth Geometry](https://arxiv.org/abs/2609.07975)
- [Height-Guided Projection Reparameterization for Camera-LiDAR Occupancy](https://arxiv.org/abs/2605.05072) — `multi-modal`
- [Hi-LOAM: Hierarchical Implicit Neural Fields for LiDAR Odometry and Mapping](https://arxiv.org/abs/2604.01720) — `reconstruction` `autonomous driving`
- [Hierarchical Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2608.05557) — `generation` `denoising`
- [Hierarchical Frequency-Domain Compression of Implicit Geometric Representations for Large-Scale Point Clouds](https://arxiv.org/abs/2609.32789) — `compression`
- [High-Precision Docking of Differential-Drive Mobile Robots Through LiDAR and Vision Collaboration](https://arxiv.org/abs/2611.24191)
- [How Sampling Strategy Affects Imbalance Mitigation in LiDAR Segmentation: A Study of Structured vs. Random Point-Based Architectures](https://arxiv.org/abs/2608.16673) — `segmentation`
- [HuLiGen: Human LiDAR Generation from Parametric Body Models](https://arxiv.org/abs/2610.10196) — `generation`
- [Hybrid-PCGC: Hybrid Point Cloud Geometry Compression Bridging Generalization-based Model and Implicit Neural Representation](https://arxiv.org/abs/2602.21662) — `compression` `autonomous driving`
- [HyperDet: 3D Object Detection with Hyper 4D Radar Point Clouds](https://arxiv.org/abs/2602.11554) — `detection` `multi-modal`
- [I See You: Initial Multi-Robot LiDAR Registration with Mutual-Observation Checks](https://arxiv.org/abs/2611.26276) — `registration`
- [IGASA: Integrated Geometry-Aware and Skip-Attention Modules for Enhanced Point Cloud Registration](https://arxiv.org/abs/2603.12719) — `registration` `autonomous driving`
- [Illumination-Invariant Anomaly Detection for Sub-Canopy UAV Multispectral Point Clouds](https://arxiv.org/abs/2606.09111) — `detection` `anomaly detection`
- [Image-to-Point Cloud Registration Made Easy with Rectified Flow-based LiDAR Upsampling](https://arxiv.org/abs/2607.14639) — `registration` `upsampling`
- [Implementation of Tightly-Coupled SLAM Fusion of GPS, IMU, and LiDAR for Autonomous Vehicles](https://arxiv.org/abs/2609.20321) — `slam` `localization`
- [IndoorBEV: A Lightweight Real-Time LiDAR BEV Perception System for Indoor Mobile Robots](https://arxiv.org/abs/2610.00355) — `BEV` `efficiency`
- [Industrial3D: A Water-Treatment TLS Point Cloud Dataset and Cross-Paradigm Benchmark for MEP Scene Understanding](https://arxiv.org/abs/2603.28660) — `dataset`
- [InstantHDR: Single-forward Gaussian Splatting Initialization for HDR 3D Reconstruction](https://arxiv.org/abs/2603.11298) — `reconstruction` `gaussian-splatting`
- [Integrating Object Detection, LiDAR-Enhanced Depth Estimation, and Segmentation Models for Railway Environments](https://arxiv.org/abs/2604.14781) — `segmentation` `detection`
- [Inter-LPCM: Learning-based Inter-Frame Predictive Coding for LiDAR Point Cloud Compression](https://arxiv.org/abs/2605.18006) — `compression`
- [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](https://arxiv.org/abs/2610.19201) — `generation` `reconstruction` `efficiency`
- [Invaria: Learning Scale and Density Invariance in Point Clouds via Next-Resolution Prediction](https://arxiv.org/abs/2605.15923)
- [InvariantCloud: A Globally Invariant, Uniquely Indexed Point Cloud Framework for Robust 6-DoF Tactile Pose Tracking](https://arxiv.org/abs/2605.25216) — `tracking` `robustness`
- [IRGNN: Efficient Invariant Radar Graph Neural Network for Radar Point Cloud Object Detection](https://arxiv.org/abs/2608.14394) — `detection` `autonomous driving` `multi-modal` `efficiency`
- [Iterative Differential Entropy Minimization (IDEM) method for fine rigid pairwise 3D Point Cloud Registration: A Focus on the Metric](https://arxiv.org/abs/2601.09601) — `registration`
- [Joint Optimization of Storage and Loading for High-Performance 3D Point Cloud Data Processing](https://arxiv.org/abs/2603.16945) — `autonomous driving`
- [Joint-Embedding Prediction of Masked Point Tubes for Self-Supervised Learning on 4D Point Cloud Videos](https://arxiv.org/abs/2608.24093) — `reconstruction` `self-supervised`
- [LEAR: Learning Edge-Aware Representations for Event-to-LiDAR Localization](https://arxiv.org/abs/2603.01839) — `localization`
- [Learned Elevation Models as a Lightweight Alternative to LiDAR for Radio Environment Map Estimation](https://arxiv.org/abs/2604.05520) — `generation` `efficiency`
- [Learned Radius Estimation for UDF-Based Point Cloud Reconstruction](https://arxiv.org/abs/2606.18787) — `reconstruction`
- [Learning Biomechanically Plausible Human Motion from Sparse Radar Point Clouds](https://arxiv.org/abs/2608.03637) — `multi-modal`
- [Learning Geometric and Photometric Features from Panoramic LiDAR Scans for Outdoor Place Categorization](https://arxiv.org/abs/2603.12663)
- [Learning Grasp Targeting from Point Clouds for Log Pile Clearing on a Hydraulic Crane](https://arxiv.org/abs/2610.07613)
- [Learning Hierarchical Orthogonal Prototypes for Generalized Few-Shot 3D Point Cloud Segmentation](https://arxiv.org/abs/2603.19788) — `segmentation`
- [Learning Human-Object Interaction for 3D Human Pose Estimation from LiDAR Point Clouds](https://arxiv.org/abs/2603.16343) — `autonomous driving`
- [Learning Laplacian Eigenspace with Mass-Aware Neural Operators on Point Clouds](https://arxiv.org/abs/2605.24390)
- [Learning Manifolds in High-D Point Embedding for Anisotropic Surface Approximation from Unstructured Point Clouds](https://arxiv.org/abs/2607.28855) — `reconstruction`
- [Learning Motion Feasibility from Point Clouds in Cluttered Environments](https://arxiv.org/abs/2606.26700)
- [Learning Point Cloud Geometry as a Statistical Manifold: Theory and Practice](https://arxiv.org/abs/2605.10456) — `localization`
- [Learning to Suppress SPAD-based LiDAR Flare](https://arxiv.org/abs/2607.03247) — `detection`
- [Learning-Based 3D Reconstruction of Power Networks from Aerial Point Clouds](https://arxiv.org/abs/2609.23915) — `segmentation` `reconstruction`
- [Learning-Based Reconstruction Attacks on Coordinate-Obfuscated Point Clouds](https://arxiv.org/abs/2609.02568) — `reconstruction` — Workshop
- [Leveraging Previous-Traversal Point Cloud Map Priors for Camera-Based 3D Object Detection and Tracking](https://arxiv.org/abs/2604.25405) — `detection` `tracking` `localization` `autonomous driving`
- [LexiCan: Lexicographic Canonicalization of Point Clouds for Machine Learning Applications](https://arxiv.org/abs/2610.15171)
- [LiDAR for Crowd Management: Applications, Benefits, and Future Directions](https://arxiv.org/abs/2603.27663) — `detection`
- [LiDAR-EVS: Enhance Extrapolated View Synthesis for 3D Gaussian Splatting with Pseudo-LiDAR Supervision](https://arxiv.org/abs/2603.14763) — `gaussian-splatting` `autonomous driving`
- [LIDARLearn: A Unified Deep Learning Library for 3D Point Cloud Classification, Segmentation, and Self-Supervised Representation Learning](https://arxiv.org/abs/2604.10780) — `segmentation` `classification` `self-supervised` `autonomous driving`
- [LiFlow: Flow Matching for 3D LiDAR Scene Completion](https://arxiv.org/abs/2602.02232) — `completion` `denoising` `autonomous driving`
- [Lightweight 3D LiDAR-Based UAV Tracking: An Adaptive Extended Kalman Filtering Approach](https://arxiv.org/abs/2603.09783) — `tracking` `efficiency`
- [Lightweight Super Resolution-enabled Coding Model for the JPEG Pleno Learning-based Point Cloud Coding Standard](https://arxiv.org/abs/2602.00863) — `efficiency`
- [LIORNet: Self-Supervised LiDAR Snow Removal Framework for Autonomous Driving under Adverse Weather Conditions](https://arxiv.org/abs/2603.19936) — `detection` `self-supervised` `autonomous driving`
- [LitS: A novel Neighborhood Descriptor for Point Clouds](https://arxiv.org/abs/2602.04838)
- [LiZIP: An Auto-Regressive Compression Framework for LiDAR Point Clouds](https://arxiv.org/abs/2603.23162) — `compression`
- [LmPT: Conditional Point Transformer for Anatomical Landmark Detection on 3D Point Clouds](https://arxiv.org/abs/2602.02808) — `detection`
- [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](https://arxiv.org/abs/2611.11912) — `BEV`
- [Local-Global Joint Modeling for Point Cloud Super-Resolution Guided by Multi-Scale Spatial Priors](https://arxiv.org/abs/2611.02786) — `upsampling`
- [LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351) — `gaussian-splatting` `efficiency`
- [LOGOS: LiDAR-Only Gaussian Elevation Splatting for Unified Tiny Obstacle Segmentation](https://arxiv.org/abs/2606.21527) — `segmentation`
- [Long-Tailed 3D Point Cloud Dataset Distillation](https://arxiv.org/abs/2607.26763) — `dataset`
- [Low-Density 3D Point Cloud Classification](https://arxiv.org/abs/2611.05291) — `classification` `autonomous driving`
- [LR-SGS: Robust LiDAR-Reflectance-Guided Salient Gaussian Splatting for Self-Driving Scene Reconstruction](https://arxiv.org/abs/2603.12647) — `reconstruction` `gaussian-splatting` `autonomous driving` `robustness`
- [M3GD: Multi-Modal Multi-View Geometric Diffusion for Camera--LiDAR Novel View Synthesis](https://arxiv.org/abs/2609.30056) — `generation` `multi-modal`
- [MAGE: View-guided Point Cloud Completion with Efficient Modality Alignment and Adaptive Geometry Enhancement](https://arxiv.org/abs/2607.02568) — `completion` `efficiency`
- [MAMVI: 3D Test-Time Adaptation via Masked Multi-View Point Clouds](https://arxiv.org/abs/2606.12939)
- [Manifold k-NN: Accelerated k-NN Queries for Manifold Point Clouds](https://arxiv.org/abs/2605.02224)
- [Manifold4D: Denoising on Point Cloud Rendered Manifolds for Video Re-shooting](https://arxiv.org/abs/2608.28174) — `denoising` `monocular`
- [Mantis: Mamba-native Tuning is Efficient for 3D Point Cloud Foundation Models](https://arxiv.org/abs/2605.03438) — `efficiency`
- [Mask 2D-3D: Adaptive Dual-Masked Autoencoder Network for Image-to-Point Cloud Registration](https://arxiv.org/abs/2609.18088) — `registration` `detection` `self-supervised`
- [MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes](https://arxiv.org/abs/2606.08744) — `localization` `BEV`
- [MedPCFM-TED: One-Step Point Cloud Flow Matching for Implant Generation via Teacher-Guided Endpoint Distillation](https://arxiv.org/abs/2609.16934) — `generation` `reconstruction`
- [MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching](https://arxiv.org/abs/2606.24433) — `completion` `generation` `reconstruction`
- [Meltdown: Circuits and Bifurcations in Point-Cloud-Conditioned 3D Diffusion Transformers](https://arxiv.org/abs/2602.11130) — `reconstruction`
- [Metric--Phase Fields: Decoupling Distance and Sign for Thin-Structure Reconstruction from Unoriented Point Clouds](https://arxiv.org/abs/2605.25503) — `reconstruction`
- [MGPC: Multimodal Network for Generalizable Point Cloud Completion With Modality Dropout and Progressive Decoding](https://arxiv.org/abs/2601.03660) — `completion` `generation` `multi-modal` — [code](https://github.com/L-J-Yuan/MGPC)
- [MirrorDrift: Actuated Mirror-Based Attacks on LiDAR SLAM](https://arxiv.org/abs/2603.11364) — `slam` `localization`
- [MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers](https://arxiv.org/abs/2607.24074)
- [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301) — `generation` `reconstruction` `autonomous driving` `multi-modal`
- [mmGAT: Pose Estimation by Graph Attention with Mutual Features from mmWave Radar Point Cloud](https://arxiv.org/abs/2603.08551) — `multi-modal`
- [MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM](https://arxiv.org/abs/2604.10593) — `slam` `gaussian-splatting` `monocular`
- [Motion-Saliency Complementary Masked Modeling for Point Cloud Video Understanding](https://arxiv.org/abs/2608.30279) — `self-supervised`
- [MS-Point: Multi-Modal Hierarchical Spectral Learning for Point Cloud Understanding](https://arxiv.org/abs/2611.25282) — `multi-modal`
- [MSSP: Multi-Scale Spatially-Constrained Partition for Unsupervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2609.06959) — `segmentation`
- [Multi-level latent-diffusion adaptation for cross-region point cloud segmentation of ancient terraces](https://arxiv.org/abs/2611.18033) — `segmentation` `detection`
- [Multi-Path Mamba Diffusion for 3D Point Cloud Semantic Scene Completion](https://arxiv.org/abs/2611.04583) — `completion` `generation` `occupancy prediction`
- [Multimodal Signal Processing For Thermo-Visible-Lidar Fusion In Real-time 3D Semantic Mapping](https://arxiv.org/abs/2601.09578) — `slam` `multi-modal` `efficiency`
- [Neural LiDAR Bundle Adjustment](https://arxiv.org/abs/2607.04169) — `reconstruction` `nerf`
- [Neural Reconstruction of LiDAR Point Clouds under Jamming Attacks via Full-Waveform Representation and Simultaneous Laser Sensing](https://arxiv.org/abs/2604.00371) — `reconstruction` `autonomous driving`
- [NeuroAPS-Net: Neuro-Anatomically Aware Point Cloud Representation for Efficient Alzheimer's Disease Classification](https://arxiv.org/abs/2604.22883) — `classification` `efficiency`
- [Neuromorphic LiDAR-based Bird's Eye View Object Detection using Energy-efficient Spiking Neural Networks](https://arxiv.org/abs/2605.25293) — `detection` `autonomous driving` `efficiency`
- [Objective Quality Assessment of Point Clouds Using Multi-scale Implicit Structural Similarity](https://arxiv.org/abs/2601.01200)
- [Octree-based Learned Point Cloud Geometry Compression: A Lossy Perspective](https://arxiv.org/abs/2603.28095) — `compression`
- [Offline-Online Hierarchical 3D Global Relocalization With Synthetic LiDAR Sensing and Descriptor-Space Retrieval](https://arxiv.org/abs/2605.07741)
- [On Exploring Input Resolution Scaling For Anytime LiDAR Object Detection](https://arxiv.org/abs/2607.08391) — `detection`
- [On Maximum Clique and Maximum Consensus Formulations in Point Cloud Registration](https://arxiv.org/abs/2610.27275) — `registration`
- [On the Efficacy of Self-Supervised Point Cloud Encoders for Efficient 3D Large Language Models](https://arxiv.org/abs/2607.29136) — `registration` `self-supervised` `efficiency`
- [One Shot Learning for Edge Detection on Point Clouds](https://arxiv.org/abs/2604.22354) — `detection`
- [Online Geometric Consistency Assessment of LiDAR Measurements via Recursive Bayesian Comparison](https://arxiv.org/abs/2611.10566) — `registration` `localization`
- [Optimizing 3D Gaussian Splatting via Point Cloud Upsampling](https://arxiv.org/abs/2606.00450) — `reconstruction` `gaussian-splatting` `upsampling`
- [OptimusMesh: Compact Autoregressive Mesh Generation from Point Clouds via Sparse Latent Pivots](https://arxiv.org/abs/2610.01148) — `generation` `reconstruction`
- [Overview and Comparison of AVS Point Cloud Compression Standard](https://arxiv.org/abs/2602.08613) — `compression` `autonomous driving`
- [PACE: Post-Causal Entropy Modeling for Learned LiDAR Point Cloud Compression](https://arxiv.org/abs/2605.01320) — `compression`
- [Parameter-Efficient Fine-Tuning for Spiking Point Cloud Models](https://arxiv.org/abs/2607.29048) — `efficiency`
- [PARTE: Plane-Assisted Robust Transformation Estimation for Point Cloud Registration](https://arxiv.org/abs/2609.25375) — `registration` `robustness`
- [PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds](https://arxiv.org/abs/2608.05586) — `generation`
- [Paving the Way for Point Cloud Video Representation Learning Using A PDE Model](https://arxiv.org/abs/2606.01604)
- [PC$^2$-AD: Point Cloud Upsampling to Safeguard 3D Anomaly Detection with Resolution-constrained Edge Devices](https://arxiv.org/abs/2609.14722) — `detection` `upsampling` `anomaly detection` — [code](https://github.com/gyutong406-commits/PC2-AD)
- [PCFEx: Point Cloud Feature Extraction for Graph Neural Networks](https://arxiv.org/abs/2603.08540)
- [PCFootprint: A Large-Scale Dataset and Benchmark for Vectorized Building Footprint Extraction from Aerial LiDAR Point Clouds](https://arxiv.org/abs/2606.20455) — `dataset`
- [PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning](https://arxiv.org/abs/2608.18627)
- [PCT-Prompt: A Prompt-Guided Transformer Framework for Dense Prediction Tasks in Point Clouds](https://arxiv.org/abs/2608.16225) — `classification`
- [PESTO: Formally Correct Registration of LiDAR Point Clouds with Limited Overlap](https://arxiv.org/abs/2609.18082) — `registration`
- [Physics-Aware Diffusion for LiDAR Point Cloud Densification](https://arxiv.org/abs/2603.26759) — `generation` `upsampling`
- [Pi-GS: Sparse-View Gaussian Splatting with Dense π^3 Initialization](https://arxiv.org/abs/2602.03327) — `nerf` `gaussian-splatting`
- [PinNet: Keypoint-Aware Learned Local Descriptors with Geometric Embedding for Loop Closure in LiDAR SLAM](https://arxiv.org/abs/2606.28637) — `slam`
- [PlantC2USeg: Cross-Scale Consistent Pre-Training for Few-Shot Unified Plant Point Cloud Segmentation](https://arxiv.org/abs/2609.02860) — `segmentation` `pre-training`
- [Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516) — `generation` `autonomous driving`
- [Point Cloud Diffusion with Global and Local Reconstruction for Instance-Level 3D Anomaly Detection](https://arxiv.org/abs/2606.25740) — `detection` `reconstruction` `anomaly detection`
- [Point Cloud Feature Coding for Object Detection over an Error-Prone Cloud-Edge Collaborative System](https://arxiv.org/abs/2603.03890) — `detection`
- [Point Cloud Registration for Fusion between SPECT MPI and CTA Images](https://arxiv.org/abs/2604.24524) — `registration` `localization`
- [Point Cloud Registration via Probabilistic Self-Update Local Correspondence and Line Vector Sets](https://arxiv.org/abs/2604.26318) — `registration`
- [Point Cloud Upsampling through Patch-based Frequency Superposition](https://arxiv.org/abs/2606.14355) — `upsampling`
- [Point-MF: Stabilizing One-Step Mean Flows for Single-Image Point Cloud Reconstruction](https://arxiv.org/abs/2604.24586) — `reconstruction`
- [Point-Selection Fine-Tuning Framework for Robust Point Cloud Classification](https://arxiv.org/abs/2607.19711) — `classification` `robustness`
- [Point-Wise Geometry-Aware Transformer for Partial-to-Full Point Cloud Registration in Computer-Assisted Surgery](https://arxiv.org/abs/2606.13488) — `registration`
- [Point2Radio: A Foundation Model for Cross-Scene Radio Fields from Material-Aware Point Clouds](https://arxiv.org/abs/2607.28994) — `pre-training`
- [PointCHR: Point Cloud Analysis via Curvature-Aware Hyperbolic Rectification](https://arxiv.org/abs/2607.24052)
- [PointCSP: Cross-Sample Semantic Propagation and Stability Preservation in Self-Supervised Point Cloud Learning](https://arxiv.org/abs/2605.01759) — `self-supervised`
- [PointLLM-R: Enhancing 3D Point Cloud Reasoning via Chain-of-Thought](https://arxiv.org/abs/2605.22013)
- [PointNDF: Cascaded Neural Displacement Fields for Point Cloud Denoising](https://arxiv.org/abs/2611.05411) — `denoising`
- [PointRFT: Explicit Reinforcement Fine-tuning for Point Cloud Few-shot Learning](https://arxiv.org/abs/2603.23957)
- [Points as Tori: Fast Pointwise Signed Distance for Point Clouds](https://arxiv.org/abs/2607.16946) — `reconstruction`
- [PointSLAM++: Robust Dense Neural Gaussian Point Cloud-based SLAM](https://arxiv.org/abs/2601.11617) — `slam` `localization` `reconstruction` `robustness`
- [PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors](https://arxiv.org/abs/2610.11612) — `registration` `open-vocabulary`
- [Position Anchor Tuning: Towards Efficient Adaptation of Pre-Trained Point Cloud Transformers](https://arxiv.org/abs/2609.18056) — `pre-training` `efficiency`
- [Proteus: A Truncation-Robust Entropy Model for Progressive LiDAR Compression](https://arxiv.org/abs/2608.00687) — `compression` `robustness`
- [ProtoPointNet: Prototype-Based Interpretable Classification of 3D Dental Point Clouds with Verifiable Spatial Activations](https://arxiv.org/abs/2607.12335) — `classification`
- [Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving](https://arxiv.org/abs/2610.27617) — `detection` `autonomous driving` `robustness` `efficiency`
- [PT$^3$: Prototype-Guided Self-Supervised Pretraining for Generalizable mmWave Human Point Cloud Representation](https://arxiv.org/abs/2610.38551) — `self-supervised` `pre-training`
- [PT-WNO: Point Transformer with Wavelet Neural Operator for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2606.11466) — `segmentation`
- [PWAVEP: Purifying Imperceptible Adversarial Perturbations in 3D Point Clouds via Spectral Graph Wavelets](https://arxiv.org/abs/2602.03333) — `robustness`
- [QFT-Based Hybrid PointNet-Quantum Neural Networks for LiDAR Point-Cloud Classification](https://arxiv.org/abs/2611.25578) — `classification`
- [Quartet of Diffusions: Structure-Aware Point Cloud Generation through Part and Symmetry Guidance](https://arxiv.org/abs/2601.20425) — `generation`
- [R1A-PC: Physics-Guided Electromagnetic Inversion of Three-Dimensional Human Point Clouds in Complex Static Environments](https://arxiv.org/abs/2610.05144)
- [R4Tun: LLM-guided adaptive segmental tunnel lining segmentation in point clouds](https://arxiv.org/abs/2609.11360) — `segmentation` `vision-language`
- [RAHF-Net: Range-Aware Heterogeneous Fusion for LiDAR-Assisted RGB Semantic Segmentation](https://arxiv.org/abs/2610.25400) — `segmentation`
- [Rail Track Extraction from Rasterized Classified Point Clouds Using a Full-Resolution, Fully Convolutional Recurrent Neural Network](https://arxiv.org/abs/2607.06829)
- [Random Walk on Point Clouds for Feature Detection](https://arxiv.org/abs/2604.20474) — `detection`
- [RangeNav: Task-Aligned LiDAR Range-Image Pretraining for Robot Navigation](https://arxiv.org/abs/2610.29845) — `pre-training`
- [RAPA: Ray-Aware Physics Augmentation for Robust Camera-LiDAR Calibration](https://arxiv.org/abs/2611.12129) — `multi-modal` `robustness`
- [RaSFNet: Ray-aligned and Scan-aware Fusion Network for LiDAR Semantic Segmentation](https://arxiv.org/abs/2610.31186) — `segmentation` `autonomous driving`
- [Real-Time LiDAR Point Cloud Densification for Low-Latency Spatial Data Transmission](https://arxiv.org/abs/2601.01210) — `upsampling` `efficiency`
- [ReaLiTy and LADS: A Unified Framework and Dataset Suite for LiDAR Adaptation Across Sensors and Adverse Weather Conditions](https://arxiv.org/abs/2604.10213) — `dataset`
- [Reconstructing Building Height from Spaceborne TomoSAR Point Clouds Using a Dual-Topology Network](https://arxiv.org/abs/2601.00658) — `reconstruction`
- [Recurrent Convolutional Neural Networks for LiDAR-Based Attitude Initialization of Rotating Spacecraft](https://arxiv.org/abs/2609.24685)
- [Refine Then Fusion: Training-Free 3D Point Cloud Adaptation with Priority Refinement and Multi-Modal Knowledge Fusion](https://arxiv.org/abs/2609.21522) — `multi-modal`
- [Refining Roadside 4D Radar Vehicle Classification Using Point-Cloud Dispersion](https://arxiv.org/abs/2611.02147) — `classification` `multi-modal`
- [RegFormer++: An Efficient Large-Scale 3D LiDAR Point Registration Network with Projection-Aware 2D Transformer](https://arxiv.org/abs/2603.14290) — `registration` `efficiency`
- [Resolving Long-Tail Ambiguity in Unsupervised 3D Point Cloud Segmentation with Language Priors](https://arxiv.org/abs/2605.20737) — `segmentation` — [code](https://github.com/Whisky0129/langtail_official)
- [Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction](https://arxiv.org/abs/2610.01206) — `reconstruction`
- [Resolving Primitive-Sharing Ambiguity in Long-Tailed TLS-Based Industrial MEP Point Cloud Segmentation via Spatial Context Constraints](https://arxiv.org/abs/2601.19128) — `segmentation` — [code](https://github.com/PointCloudYC/LongTail3D)
- [ResPCC: A Loss-Resilient Neural Point Cloud Codec over Lossy Networks](https://arxiv.org/abs/2608.11845) — `compression`
- [Rethinking 3D Segmentation from Individual LiDAR Scans: Incidence-Aware Sampling on the SIP Benchmark](https://arxiv.org/abs/2608.07757) — `segmentation` `dataset`
- [Rethinking Point Clouds as Sequences: A Causal Next-Token Predictive Learning Framework](https://arxiv.org/abs/2605.17566) — `generation` `reconstruction` `self-supervised`
- [Rethinking Transferable Adversarial Attacks on Point Clouds from a Compact Subspace Perspective](https://arxiv.org/abs/2601.23102) — `robustness`
- [Review and Evaluation of Point-Cloud based Leaf Surface Reconstruction Methods for Agricultural Applications](https://arxiv.org/abs/2604.03328) — `reconstruction`
- [REVNET: Rotation-Equivariant Point Cloud Completion via Vector Neuron Anchor Transformer](https://arxiv.org/abs/2601.08558) — `completion`
- [RFDT-Channel: RGB-LiDAR-Based RF Digital Twin Scene Construction for 28 GHz Indoor Ray-Tracing Channel Simulation](https://arxiv.org/abs/2606.01261)
- [RhinoNet: Unsupervised Learning for Phenoscaping and Generation of High Dimensional Point Clouds](https://arxiv.org/abs/2610.23898) — `generation`
- [RigPAPR: Rig-Based Animation of Static Neural Point Clouds from a Fixed-Viewpoint Video](https://arxiv.org/abs/2606.06685) — `generation` `reconstruction` `monocular`
- [Riverine Land Cover Mapping through Semantic Segmentation of Multispectral Point Clouds](https://arxiv.org/abs/2603.22230) — `segmentation`
- [RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware Robot Perception](https://arxiv.org/abs/2608.21380)
- [Robust LIDAR Sensor-to-Sensor Domain Generalization via Accumulated-Point Scene Completion](https://arxiv.org/abs/2610.39516) — `segmentation` `completion` `robustness`
- [Robust Reconstruction of Power Lines from Incomplete Mobile and Aerial LiDAR Data](https://arxiv.org/abs/2611.05197) — `detection` `reconstruction` `robustness`
- [Robust Single-Parameter Point Cloud Registration using Truncated Lp Functions](https://arxiv.org/abs/2610.34271) — `registration` `robustness`
- [Role-based Effectiveness of an Epistemic Uncertainty Estimate in Training Models for Semantic Segmentation of 3D LiDAR Point Clouds](https://arxiv.org/abs/2611.05569) — `segmentation` `classification`
- [Rotational Symmetry based Object Pose Estimation from Point Clouds in the Absence of Known 3D Models](https://arxiv.org/abs/2606.16593)
- [RoughSense: Lightweight Terrain-Induced Rover Vibration Prediction Using Point Clouds and IMU Feedback](https://arxiv.org/abs/2609.03720) — `detection` `efficiency`
- [RS2AD-LiDAR: End-to-End Autonomous Driving LiDAR Data Generation from Roadside Sensor Observations](https://arxiv.org/abs/2605.23406) — `generation` `autonomous driving`
- [Safety-Critical LiDAR-Inertial Odometry with On-Manifold Deterministic Protection Level](https://arxiv.org/abs/2605.09383)
- [SAFT: Sensitivity-Aware Filtering and Transmission for Adaptive 3D Point Cloud Communication over Wireless Channels](https://arxiv.org/abs/2603.26197)
- [SAVTrack: Selective Vote Aggregation for Reliability-Aware Point Cloud Tracking](https://arxiv.org/abs/2609.16662) — `tracking`
- [SC-MII: Infrastructure LiDAR-based 3D Object Detection on Edge Devices for Split Computing with Multiple Intermediate Outputs Integration](https://arxiv.org/abs/2601.07119) — `detection` `autonomous driving`
- [ScaleBlind: Point Cloud Completion under Unknown Scale](https://arxiv.org/abs/2609.23404) — `completion` `reconstruction`
- [SelectAnyTree: A Promptable Instance Segmentation Model for 3D Forest LiDAR Point Clouds](https://arxiv.org/abs/2606.27491) — `segmentation`
- [Self-supervised Geometry Reasoning for LiDAR Simultaneous Localization and Mapping](https://arxiv.org/abs/2606.30166) — `slam` `localization` `self-supervised`
- [Self-Supervised Pretraining Improves Cross-Site and Cross-Scale Robustness of Point Cloud Leaf-Wood Segmentation](https://arxiv.org/abs/2607.06948) — `segmentation` `self-supervised` `pre-training` `robustness`
- [Semantic Privacy Protection with Utility Preservation for 3D Point Clouds](https://arxiv.org/abs/2609.13823)
- [Semantic-weighted ICP for LiDAR Odometry: Class-Aware Residual Reweighting for Robust Scan Registration](https://arxiv.org/abs/2606.03905) — `registration` `robustness`
- [Send Less, Perceive More: Masked Quantized Point Cloud Communication for Loss-Tolerant Collaborative Perception](https://arxiv.org/abs/2602.21667) — `efficiency`
- [SF3D-RGB: Scene Flow Estimation from Monocular Camera and Sparse LiDAR](https://arxiv.org/abs/2602.21699) — `scene flow` `monocular`
- [Shape-Prior-Based Point Cloud Completion for Single-Stage Fully Sparse 3D Object Detection](https://arxiv.org/abs/2606.00688) — `detection` `completion` `autonomous driving`
- [SHReg: Strictly Rotation-Equivariant Point Cloud Registration via Spherical Harmonics](https://arxiv.org/abs/2607.23096) — `registration`
- [Sign Language Recognition Using Original and Synthetic Depth Image Based Point Cloud Data Models](https://arxiv.org/abs/2608.09400) — `monocular`
- [Simultaneous Monitoring of Shape and Surface Color via 4D Point Clouds: A Registration-free Approach](https://arxiv.org/abs/2605.08753) — `registration`
- [Sinkhorn-CPD: Robust point cloud registration via unbalanced entropic optimal transport](https://arxiv.org/abs/2606.16672) — `registration` `robustness`
- [SlingBAG Pro: Accelerating point cloud-based iterative reconstruction for 3D photoacoustic imaging with arbitrary array geometries](https://arxiv.org/abs/2601.00551) — `reconstruction`
- [Solution for UCF UrbanTwin LUMPI Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07590) — `detection`
- [Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection](https://arxiv.org/abs/2609.07608) — `detection`
- [Source-Free Domain Adaptation for Geospatial Point Cloud Semantic Segmentation](https://arxiv.org/abs/2601.08375) — `segmentation` `domain adaptation`
- [SpaceCache: Intermediate Feature Reuse for Efficient Semantic Segmentation on Point Cloud Streams](https://arxiv.org/abs/2610.21207) — `segmentation` `autonomous driving` `efficiency`
- [Spatially-Aware Evaluation Framework for Aerial LiDAR Point Cloud Semantic Segmentation: Distance-Based Metrics on Challenging Regions](https://arxiv.org/abs/2603.22420) — `segmentation`
- [Spectral Consistency-Guided Multiview Point Cloud Registration for Low-Overlap Scenes](https://arxiv.org/abs/2609.12417) — `registration`
- [SPEM: Scan-Prior Entropy Modeling for LiDAR Point Cloud Compression](https://arxiv.org/abs/2611.16212) — `compression`
- [SRENet: Spectral Re-Entry Network for Point Cloud Action Recognition](https://arxiv.org/abs/2606.03160) — `autonomous driving`
- [SSC-Priors: Exploring Semantic and Visibility Priors to Boost Lidar Semantic Scene Completion](https://arxiv.org/abs/2609.17413) — `segmentation` `completion` `occupancy prediction`
- [Structure-First Point Cloud Learning with Mapper Region Graphs](https://arxiv.org/abs/2602.05522) — `classification`
- [Sub-Footprint Effect Correction in FW-LiDAR Point Clouds via Intra-Footprint Target Unmixing](https://arxiv.org/abs/2605.09845) — `detection`
- [SUMI: Scalable Unified Model for 3D Point Cloud Inference](https://arxiv.org/abs/2608.08115) — `completion` `reconstruction` `upsampling`
- [Super-Resolution of Airborne Laser Scanning Point Clouds for Forest Inventory](https://arxiv.org/abs/2605.02201) — `localization` `upsampling`
- [SuperFlex: Deformable Superquadrics for Point Cloud Decomposition](https://arxiv.org/abs/2607.01015) — `reconstruction`
- [Superquadric Primitive Decomposition of 3D point clouds via Geometric-Aware Inlier Refinement](https://arxiv.org/abs/2609.35725)
- [SurfelSoup: Learned Point Cloud Geometry Compression With a Probablistic SurfelTree Representation](https://arxiv.org/abs/2602.00186) — `compression`
- [Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge](https://arxiv.org/abs/2608.07106) — `classification` `generation`
- [Systematic Evaluation of Depth Backbones and Semantic Cues for Monocular Pseudo-LiDAR 3D Detection](https://arxiv.org/abs/2601.03617) — `detection` `monocular`
- [TACTIC: Temporal and Context-Aware LLM Tactical Planning for Roadside LiDAR Attacks](https://arxiv.org/abs/2609.39969) — `vision-language`
- [TAFA-GSGC: Group-wise Scalable Point Cloud Geometry Compression with Progressive Residual Refinement](https://arxiv.org/abs/2604.28045) — `compression`
- [TAP3D: Thermal-Assisted 3D Human Point Clouds](https://arxiv.org/abs/2610.11241) — `reconstruction`
- [Task-Oriented Wireless Transmission of 3D Point Clouds: Geometric Versus Semantic Robustness](https://arxiv.org/abs/2603.13560) — `reconstruction` `compression` `robustness`
- [Test Time Adaptation Methods for Point Cloud Registration in Laparoscopic Surgery](https://arxiv.org/abs/2608.02883) — `registration`
- [Test-time Adaptation for Point Cloud Denoising under Unseen Noise](https://arxiv.org/abs/2610.27410) — `denoising`
- [TFTrack: A Template-Free Framework for Efficient 3D Point Cloud Tracking](https://arxiv.org/abs/2609.07738) — `tracking` `efficiency`
- [The Role of Initialization in 3D Gaussian Splatting](https://arxiv.org/abs/2603.20714) — `gaussian-splatting` — [code](https://github.com/deivse/ivd_splat)
- [The Role of Radiometric Features in Cross-Site Leaf-Wood Segmentation of LiDAR Point Clouds](https://arxiv.org/abs/2609.21903) — `segmentation`
- [TokenFlow: Latent Token Rectified Flow Matching for 3D Point Cloud Generation](https://arxiv.org/abs/2610.27418) — `generation`
- [Topo-ADV: Generating Topology-Driven Imperceptible Adversarial Point Clouds](https://arxiv.org/abs/2604.09879) — `classification` `robustness`
- [Toward a foundation model for forest point clouds](https://arxiv.org/abs/2609.24787) — `pre-training`
- [Towards Integrated Rock Support Visualisation in 3D Point Cloud of Underground Mines](https://arxiv.org/abs/2605.20973)
- [Towards Practical Lossless Neural Compression for LiDAR Point Clouds](https://arxiv.org/abs/2603.25260) — `compression`
- [Transcoding a 3D Gaussian Splatting Model from a Plenoptic Point Cloud or Mesh without the Original Multi-view Images](https://arxiv.org/abs/2605.21051) — `gaussian-splatting` — Workshop
- [TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects](https://arxiv.org/abs/2603.13869) — `reconstruction` `self-supervised` `pre-training`
- [Transform-Aligned Learned Features for Lossy Point Cloud Attribute Compression](https://arxiv.org/abs/2609.34834) — `compression`
- [TreeLoc++: Robust 6-DoF LiDAR Localization in Forests with a Compact Digital Forest Inventory](https://arxiv.org/abs/2603.03695) — `localization` `robustness`
- [TreeON: Reconstructing 3D Tree Point Clouds from Orthophotos and Heightmaps](https://arxiv.org/abs/2603.10996) — `reconstruction`
- [Tri-Efficient Transfer Learning for Point Cloud Videos](https://arxiv.org/abs/2606.24175) — `efficiency`
- [TriBand-BEV: Real-Time LiDAR-Only 3D Pedestrian Detection via Height-Aware BEV and High-Resolution Feature Fusion](https://arxiv.org/abs/2605.12220) — `detection` `BEV` `efficiency`
- [UGD: An Unsupervised Geometric Distance for Evaluating Real-world Noisy Point Cloud Denoising](https://arxiv.org/abs/2604.16976) — `denoising`
- [Uncertainty Evaluation to Support Safety of the Intended Functionality Analysis for Determining the Applicability of Performance Targets Across Triggering Conditions in ML-Based LiDAR Object Detection](https://arxiv.org/abs/2610.35092) — `detection`
- [Uncertainty-aware Prototype Learning with Variational Inference for Few-shot Point Cloud Segmentation](https://arxiv.org/abs/2603.19757) — `segmentation`
- [Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence](https://arxiv.org/abs/2609.02134)
- [Unsigned Distance Maps on 2D Point Cloud Registration](https://arxiv.org/abs/2609.25932) — `registration` `slam` `localization` — [code](https://github.com/INESCTEC/ricoslam)
- [UPDA: Unsupervised Progressive Domain Adaptation for No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2602.11969) — `domain adaptation`
- [UQ-Loc: Uncertainty-Aware LiDAR Scene Coordinate Regression](https://arxiv.org/abs/2608.06307) — `localization`
- [Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283) — `self-supervised`
- [ViCo3D: Empowering LiDAR-based Collaborative 3D Object Detection with Vision Foundation Models](https://arxiv.org/abs/2607.12959) — `detection` `BEV`
- [Viking Hill Dataset: A Lidar-Radar-Camera Dataset for Detection and Segmentation in Forest Scenes](https://arxiv.org/abs/2606.19154) — `segmentation` `detection` `multi-modal` `dataset`
- [VisTa3D: A Dataset and Benchmark for Thin Object Reconstruction from Vision, Tactile, and 3D Point Clouds](https://arxiv.org/abs/2608.20740) — `reconstruction` `dataset`
- [VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds](https://arxiv.org/abs/2607.16146) — `localization`
- [When Point Clouds Outperform Pixels: Rethinking Zero-Shot Multimodal Anomaly Detection](https://arxiv.org/abs/2609.25793) — `detection` `localization` `open-vocabulary` `multi-modal`
- [WHU-PCPR: A cross-platform heterogeneous point cloud dataset for place recognition in complex urban scenes](https://arxiv.org/abs/2601.06442) — `localization` `autonomous driving` `dataset`
- [WNOJ-LIO: A White-Noise-on-Jerk Motion-Prior EKF for High-Dynamic LiDAR-IMU Fusion](https://arxiv.org/abs/2607.13405)
- [xModel-KD: Cross-modal Knowledge Distillation for 3D Scene Perception using LiDAR](https://arxiv.org/abs/2605.30111) — `segmentation`
- [ZIL: Zero-shot Image-to-LiDAR Registration](https://arxiv.org/abs/2609.22716) — `registration` `autonomous driving` `open-vocabulary`
- [ZVeC: A Zero-Shot Framework for Instance-Level Vehicle Extraction and Generative Point Cloud Completion](https://arxiv.org/abs/2609.24825) — `completion` `generation` `reconstruction` `open-vocabulary`

</details>


### 2025 <sub>(831)</sub>

<details><summary><b>CVPR</b> · 52</summary>

- [3D-AVS: LiDAR-based 3D Auto-Vocabulary Segmentation](https://arxiv.org/abs/2406.09126) — `segmentation` `detection` `open-vocabulary` — Workshop
- [4Deform: Neural Surface Deformation for Robust Shape Interpolation](https://arxiv.org/abs/2502.20208) — `robustness`
- [ArcPro: Architectural Programs for Structured 3D Abstraction of Sparse Points](https://arxiv.org/abs/2503.02745)
- [AutoURDF: Unsupervised Robot Modeling from Point Cloud Frames Using Cluster Registration](https://arxiv.org/abs/2412.05507) — `registration`
- [CAP-Net: A Unified Network for 6D Pose and Size Estimation of Categorical Articulated Parts from a Single RGB-D Image](https://arxiv.org/abs/2504.11230) — `segmentation`
- [CMMLoc: Advancing Text-to-PointCloud Localization with Cauchy-Mixture-Model Based Framework](https://arxiv.org/abs/2503.02593) — `localization`
- [ColabSfM: Collaborative Structure-from-Motion by Point Cloud Registration](https://arxiv.org/abs/2503.17093) — `registration`
- [CoMapGS: Covisibility Map-based Gaussian Splatting for Sparse Novel View Synthesis](https://arxiv.org/abs/2503.20998) — `gaussian-splatting`
- [DSPNet: Dual-vision Scene Perception for Robust 3D Question Answering](https://arxiv.org/abs/2503.03190) — `robustness`
- [Ev-3DOD: Pushing the Temporal Boundaries of 3D Object Detection with Event Cameras](https://arxiv.org/abs/2502.19630) — `detection` `autonomous driving`
- [GBlobs: Explicit Local Structure via Gaussian Blobs for Improved Cross-Domain LiDAR-based 3D Object Detection](https://arxiv.org/abs/2503.08639) — `detection`
- [Generalized Few-shot 3D Point Cloud Segmentation with Vision-Language Model](https://arxiv.org/abs/2503.16282) — `segmentation` `vision-language`
- [GenPC: Zero-shot Point Cloud Completion via 3D Generative Priors](https://arxiv.org/abs/2502.19896) — `completion` `generation` `open-vocabulary`
- [HAECcity: Open-Vocabulary Scene Understanding of City-Scale Point Clouds with Superpoint Graph Clustering](https://arxiv.org/abs/2504.13590) — `open-vocabulary` — Workshop
- [HiLoTs: High-Low Temporal Sensitive Representation Learning for Semi-Supervised LiDAR Segmentation in Autonomous Driving](https://arxiv.org/abs/2503.17752) — `segmentation` `autonomous driving`
- [HOTFormerLoc: Hierarchical Octree Transformer for Versatile Lidar Place Recognition Across Ground and Aerial Views](https://arxiv.org/abs/2503.08140) — `localization`
- [Investigating Vision-Language Model for Point Cloud-based Vehicle Classification](https://arxiv.org/abs/2504.08154) — `classification` `autonomous driving` `vision-language` — Workshop
- [Learning Bijective Surface Parameterization for Inferring Signed Distance Functions from Sparse Point Clouds with Grid Deformation](https://arxiv.org/abs/2503.23670) — `reconstruction`
- [LiMoE: Mixture of LiDAR Representation Learners from Automotive Scenes](https://arxiv.org/abs/2501.04004)
- [LiSu: A Dataset and Method for LiDAR Surface Normal Estimation](https://arxiv.org/abs/2503.08601) — `normal estimation` `dataset`
- [LogoSP: Local-global Grouping of Superpoints for Unsupervised Semantic Segmentation of 3D Point Clouds](https://arxiv.org/abs/2506.07857) — `segmentation` — [code](https://github.com/vLAR-group/LogoSP)
- [MAMBA4D: Efficient Long-Sequence Point Cloud Video Understanding with Disentangled Spatial-Temporal State Space Models](https://arxiv.org/abs/2405.14338) — `efficiency`
- [MESC-3D:Mining Effective Semantic Cues for 3D Reconstruction from a Single Image](https://arxiv.org/abs/2502.20861) — `reconstruction`
- [Mitigating Ambiguities in 3D Classification with Gaussian Splatting](https://arxiv.org/abs/2503.08352) — `classification` `gaussian-splatting`
- [Occlusion-aware Text-Image-Point Cloud Pretraining for Open-World 3D Object Recognition](https://arxiv.org/abs/2502.10674) — `open-vocabulary` `pre-training`
- [OffsetOPT: Explicit Surface Reconstruction without Normals](https://arxiv.org/abs/2503.15763) — `reconstruction`
- [Parametric Point Cloud Completion for Polygonal Surface Reconstruction](https://arxiv.org/abs/2503.08363) — `completion` `reconstruction`
- [PerLA: Perceptive 3D Language Assistant](https://arxiv.org/abs/2411.19774)
- [PF3Det: A Prompted Foundation Feature Assisted Visual LiDAR 3D Detector](https://arxiv.org/abs/2504.03563) — `detection` `autonomous driving` — Workshop
- [PMA: Towards Parameter-Efficient Point Cloud Understanding via Point Mamba Adapter](https://arxiv.org/abs/2505.20941) — `efficiency`
- [Point-Cache: Test-time Dynamic and Hierarchical Cache for Robust and Generalizable Point Cloud Analysis](https://arxiv.org/abs/2503.12150) — `robustness`
- [PointLoRA: Low-Rank Adaptation with Token Selection for Point Cloud Learning](https://arxiv.org/abs/2504.16023) — `self-supervised`
- [ProtoDepth: Unsupervised Continual Depth Completion with Prototypes](https://arxiv.org/abs/2503.12745) — `completion` `reconstruction`
- [ProxyTransformation: Preshaping Point Cloud Manifold With Proxy Attention For 3D Visual Grounding](https://arxiv.org/abs/2502.19247)
- [Real-IAD MVN: A Multi-View Normal Vector Dataset and Benchmark for High-Fidelity Industrial Anomaly Detection](https://arxiv.org/abs/2605.07149) — `detection` `anomaly detection` `dataset`
- [Relation3D: Enhancing Relation Modeling for Point Cloud Instance Segmentation](https://arxiv.org/abs/2506.17891) — `segmentation` — [code](https://github.com/Howard-coder191/Relation3D)
- [SAB3R: Semantic-Augmented Backbone in 3D Reconstruction](https://arxiv.org/abs/2506.02112) — `segmentation` `detection` `reconstruction` `open-vocabulary`
- [SeaLion: Semantic Part-Aware Latent Point Diffusion Models for 3D Generation](https://arxiv.org/abs/2505.17721) — `segmentation` `generation` `denoising`
- [Self-Supervised Large Scale Point Cloud Completion for Archaeological Site Restoration](https://arxiv.org/abs/2503.04030) — `completion` `self-supervised`
- [Semantic-Free Procedural 3D Shapes Are Surprisingly Good Teachers](https://arxiv.org/abs/2411.17467) — `self-supervised`
- [Sonata: Self-Supervised Learning of Reliable Point Representations](https://arxiv.org/abs/2503.16429) — `self-supervised`
- [Sparse Point Cloud Patches Rendering via Splitting 2D Gaussians](https://arxiv.org/abs/2505.09413) — `nerf`
- [Speedy-Splat: Fast 3D Gaussian Splatting with Sparse Pixels and Sparse Primitives](https://arxiv.org/abs/2412.00578) — `reconstruction` `gaussian-splatting`
- [STAR-Edge: Structure-aware Local Spherical Curve Representation for Thin-walled Edge Extraction from Unstructured Point Clouds](https://arxiv.org/abs/2503.00801)
- [SUM Parts: Benchmarking Part-Level Semantic Segmentation of Urban Meshes](https://arxiv.org/abs/2503.15300) — `segmentation`
- [SuperPC: A Single Diffusion Model for Point Cloud Completion, Upsampling, Denoising, and Colorization](https://arxiv.org/abs/2503.14558) — `completion` `generation` `reconstruction` `upsampling`
- [TreeMeshGPT: Artistic Mesh Generation with Autoregressive Tree Sequencing](https://arxiv.org/abs/2503.11629) — `generation` — [code](https://github.com/sail-sg/TreeMeshGPT)
- [UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting](https://arxiv.org/abs/2506.09952) — `gaussian-splatting` `pre-training`
- [Unlocking Generalization Power in LiDAR Point Cloud Registration](https://arxiv.org/abs/2503.10149) — `registration` `autonomous driving`
- [V2X-R: Cooperative LiDAR-4D Radar Fusion with Denoising Diffusion for 3D Object Detection](https://arxiv.org/abs/2411.08402) — `detection` `denoising` `multi-modal`
- [Video-3D LLM: Learning Position-Aware Video Representation for 3D Scene Understanding](https://arxiv.org/abs/2412.00493) — `vision-language`
- [ZFusion: An Effective Fuser of Camera and 4D Radar for 3D Object Perception in Autonomous Driving](https://arxiv.org/abs/2504.03438) — `detection` `autonomous driving` `multi-modal`

</details>

<details><summary><b>ICCV</b> · 53</summary>

- [All in One: Visual-Description-Guided Unified Point Cloud Segmentation](https://arxiv.org/abs/2507.05211) — `segmentation`
- [Blended Point Cloud Diffusion for Localized Text-guided Shape Editing](https://arxiv.org/abs/2507.15399)
- [BUFFER-X: Towards Zero-Shot Point Cloud Registration in Diverse Scenes](https://arxiv.org/abs/2503.07940) — `registration` `open-vocabulary`
- [CA-I2P: Channel-Adaptive Registration Network with Global Optimal Selection](https://arxiv.org/abs/2506.21364) — `registration` `detection`
- [CanFields: Consolidating Diffeomorphic Flows for Non-Rigid 4D Interpolation from Arbitrary-Length Sequences](https://arxiv.org/abs/2406.18582)
- [Curve-Aware Gaussian Splatting for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2506.21401) — `reconstruction` `gaussian-splatting` — [code](https://github.com/zhirui-gao/Curve-Gaussian)
- [Describe, Adapt and Combine: Empowering CLIP Encoders for Open-set 3D Object Retrieval](https://arxiv.org/abs/2507.21489)
- [DeSPITE: Exploring Contrastive Deep Skeleton-Pointcloud-IMU-Text Embeddings for Advanced Point Cloud Human Activity Understanding](https://arxiv.org/abs/2506.13897) — `detection`
- [Diff$^2$I2P: Differentiable Image-to-Point Cloud Registration with Diffusion Prior](https://arxiv.org/abs/2507.06651) — `registration`
- [Domain-aware Category-level Geometry Learning Segmentation for 3D Point Clouds](https://arxiv.org/abs/2508.11265) — `segmentation`
- [DoppDrive: Doppler-Driven Temporal Aggregation for Improved Radar Object Detection](https://arxiv.org/abs/2508.12330) — `detection` `autonomous driving` `multi-modal`
- [Easi3R: Estimating Disentangled Motion from DUSt3R Without Training](https://arxiv.org/abs/2503.24391) — [code](https://github.com/Inception3D/Easi3R)
- [Efficient Spiking Point Mamba for Point Cloud Analysis](https://arxiv.org/abs/2504.14371) — `efficiency`
- [Egocentric Action-aware Inertial Localization in Point Clouds with Vision-Language Guidance](https://arxiv.org/abs/2505.14346) — `localization` `vision-language`
- [Enhancing Steering Estimation with Semantic-Aware GNNs](https://arxiv.org/abs/2503.17153) — `autonomous driving`
- [ERNet: Efficient Non-Rigid Registration Network for Point Sequences](https://arxiv.org/abs/2510.15800) — `registration` `efficiency`
- [Exploiting Vision Language Model for Training-Free 3D Point Cloud OOD Detection via Graph Score Propagation](https://arxiv.org/abs/2506.22375) — `detection`
- [FastPoint: Accelerating 3D Point Cloud Model Inference via Sample Point Distance Prediction](https://arxiv.org/abs/2507.23480)
- [From Binary to Semantic: Utilizing Large-Scale Binary Occupancy Data for 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2507.13387) — `autonomous driving` `occupancy prediction` — Workshop
- [GAP: Gaussianize Any Point Clouds with Text Guidance](https://arxiv.org/abs/2508.05631) — `gaussian-splatting`
- [Guiding Diffusion-Based Articulated Object Generation by Partial Point Cloud Alignment and Physical Plausibility Constraints](https://arxiv.org/abs/2508.00558) — `registration` `generation`
- [Harnessing Text-to-Image Diffusion Models for Point Cloud Self-Supervised Learning](https://arxiv.org/abs/2507.09102) — `generation` `self-supervised`
- [HORT: Monocular Hand-held Objects Reconstruction with Transformers](https://arxiv.org/abs/2503.21313) — `reconstruction` `denoising` `monocular`
- [HyperGCT: A Dynamic Hyper-GNN-Learned Geometric Constraint for 3D Registration](https://arxiv.org/abs/2503.02195) — `registration`
- [Learning Normals of Noisy Points by Local Gradient-Aware Surface Filtering](https://arxiv.org/abs/2507.03394) — `normal estimation`
- [Learning Point Cloud Representations with Pose Continuity for Depth-Based Category-Level 6D Object Pose Estimation](https://arxiv.org/abs/2508.14358) — Workshop
- [LINR-PCGC: Lossless Implicit Neural Representations for Point Cloud Geometry Compression](https://arxiv.org/abs/2507.15686) — `compression`
- [MinCD-PnP: Learning 2D-3D Correspondences with Approximate Blind PnP](https://arxiv.org/abs/2507.15257) — `registration`
- [Mixed Signals: A Diverse Point Cloud Dataset for Heterogeneous LiDAR V2X Collaboration](https://arxiv.org/abs/2502.14156) — `dataset`
- [MonoMVSNet: Monocular Priors Guided Multi-View Stereo Network](https://arxiv.org/abs/2507.11333) — `monocular`
- [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://arxiv.org/abs/2507.04047) — `reconstruction` `efficiency`
- [Open-Vocabulary Octree-Graph for 3D Scene Understanding](https://arxiv.org/abs/2411.16253) — `segmentation` `open-vocabulary`
- [OpenM3D: Open Vocabulary Multi-view Indoor 3D Object Detection without Human Annotations](https://arxiv.org/abs/2508.20063) — `detection` `open-vocabulary`
- [PlaceIt3D: Language-Guided Object Placement in Real 3D Scenes](https://arxiv.org/abs/2505.05288) — `localization`
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
- [TARS: Traffic-Aware Radar Scene Flow Estimation](https://arxiv.org/abs/2503.10210) — `scene flow` `autonomous driving` `multi-modal`
- [Toward Zero-Shot Point Cloud Registration Across Diverse Scales, Scenes, and Sensor Setups](https://arxiv.org/abs/2601.02759) — `registration` `open-vocabulary`
- [Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge](https://arxiv.org/abs/2507.04123) — `detection` `autonomous driving` `efficiency`
- [Towards More Diverse and Challenging Pre-training for Point Cloud Learning: Self-Supervised Cross Reconstruction with Decoupled Views](https://arxiv.org/abs/2509.01250) — `generation` `reconstruction` `self-supervised` `pre-training`
- [TurboReg: TurboClique for Robust and Efficient Point Cloud Registration](https://arxiv.org/abs/2507.01439) — `registration` `robustness` `efficiency`
- [UPP: Unified Point-Level Prompting for Robust Point Cloud Analysis](https://arxiv.org/abs/2507.18997) — `robustness`
- [UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling](https://arxiv.org/abs/2508.14604)
- [VolumetricSMPL: A Neural Volumetric Body Model for Efficient Interactions, Contacts, and Collisions](https://arxiv.org/abs/2506.23236) — `efficiency`

</details>

<details><summary><b>ECCV</b> · 2</summary>

- [PARE-Net: Position-Aware Rotation-Equivariant Networks for Robust Point Cloud Registration](https://arxiv.org/abs/2407.10142) — `registration` `robustness`
- [UniFlow: Zero-Shot LiDAR Scene Flow for Autonomous Vehicles](https://arxiv.org/abs/2511.18254) — `scene flow` `open-vocabulary`

</details>

<details><summary><b>NeurIPS</b> · 22</summary>

- [Avi: Action from Volumetric Inference](https://arxiv.org/abs/2510.21746) — `generation` — Workshop
- [Copresheaf Topological Neural Networks: A Generalized Deep Learning Framework](https://arxiv.org/abs/2505.21251)
- [CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning](https://arxiv.org/abs/2507.03707) — `dataset`
- [How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?](https://arxiv.org/abs/2511.05449) — `segmentation` `reconstruction`
- [L2RSI: Cross-view LiDAR-based Place Recognition for Large-scale Urban Scenes via Remote Sensing Imagery](https://arxiv.org/abs/2503.11245) — `localization`
- [Learning from Videos for 3D World: Enhancing MLLMs with 3D Vision Geometry Priors](https://arxiv.org/abs/2505.24625) — `BEV`
- [MIND: Material Interface Generation from UDFs for Non-Manifold Surface Reconstruction](https://arxiv.org/abs/2506.02938) — `generation` `reconstruction`
- [Novel Class Discovery for Point Cloud Segmentation via Joint Learning of Causal Representation and Reasoning](https://arxiv.org/abs/2510.13307) — `segmentation`
- [On Geometry-Enhanced Parameter-Efficient Fine-Tuning for 3D Scene Segmentation](https://arxiv.org/abs/2505.22444) — `segmentation` `efficiency` — [code](https://github.com/LiyaoTang/GEM)
- [On Transferring Transferability: Towards a Theory for Size Generalization](https://arxiv.org/abs/2505.23599)
- [Online Segment Any 3D Thing as Instance Tracking](https://arxiv.org/abs/2512.07599) — `segmentation` `tracking` — [code](https://github.com/AutoLab-SAI-SJTU/AutoSeg3D)
- [Pixel-Perfect Depth with Semantics-Prompted Diffusion Transformers](https://arxiv.org/abs/2510.07316) — `generation` `compression` `monocular`
- [PointMAC: Meta-Learned Adaptation for Robust Test-Time Point Cloud Completion](https://arxiv.org/abs/2510.10365) — `completion` `robustness`
- [Reconstructing the local density field with combined convolutional and point cloud architecture](https://arxiv.org/abs/2510.08573) — `reconstruction` — Workshop
- [Rectified Point Flow: Generic Point Cloud Pose Estimation](https://arxiv.org/abs/2506.05282) — `registration` `generation`
- [RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes](https://arxiv.org/abs/2509.15123)
- [SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions](https://arxiv.org/abs/2509.15693) — `self-supervised`
- [See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model](https://arxiv.org/abs/2509.16087) — `multi-modal`
- [SSR: Enhancing Depth Perception in Vision-Language Models via Rationale-Guided Spatial Reasoning](https://arxiv.org/abs/2505.12448) — `vision-language`
- [TriFusion-AE: Language-Guided Depth and LiDAR Fusion for Robust Point Cloud Processing](https://arxiv.org/abs/2509.18743) — `reconstruction` `denoising` `autonomous driving` `robustness` — Workshop
- [U-CAN: Unsupervised Point Cloud Denoising with Consistency-Aware Noise2Noise Matching](https://arxiv.org/abs/2510.25210) — `reconstruction` `denoising`
- [Unpaired Translation of Point Clouds for Modeling Detector Response](https://arxiv.org/abs/2501.18674) — `detection` — Workshop

</details>

<details><summary><b>ICLR</b> · 10</summary>

- [ConcreTizer: Model Inversion Attack via Occupancy Classification and Dispersion Control for 3D Point Cloud Restoration](https://arxiv.org/abs/2503.06986) — `classification`
- [GrabS: Generative Embodied Agent for 3D Object Segmentation without Scene Supervision](https://arxiv.org/abs/2504.11754) — `segmentation` `generation` — [code](https://github.com/vLAR-group/GrabS)
- [Implicit Neural Representations of Molecular Vector-Valued Functions](https://arxiv.org/abs/2502.10848) — Workshop
- [Implicit Neural Surface Deformation with Explicit Velocity Fields](https://arxiv.org/abs/2501.14038)
- [Learning Shape-Independent Transformation via Spherical Representations for Category-Level Object Pose Estimation](https://arxiv.org/abs/2503.13926)
- [Occlusion-aware Non-Rigid Point Cloud Registration via Unsupervised Neural Deformation Correntropy](https://arxiv.org/abs/2502.10704) — `registration` `reconstruction` — [code](https://github.com/zikai1/OAReg)
- [Point-based Instance Completion with Scene Constraints](https://arxiv.org/abs/2504.05698) — `completion`
- [PvNeXt: Rethinking Network Design and Temporal Motion for Point Cloud Video Recognition](https://arxiv.org/abs/2504.05075)
- [SecureGS: Boosting the Security and Fidelity of 3D Gaussian Splatting Steganography](https://arxiv.org/abs/2503.06118) — `nerf` `gaussian-splatting`
- [UniGS: Unified Language-Image-3D Pretraining with Gaussian Splatting](https://arxiv.org/abs/2502.17860) — `gaussian-splatting` `pre-training`

</details>

<details><summary><b>ICML</b> · 5</summary>

- [EPiC: Efficient Video Camera Control Learning with Precise Anchor-Video Guidance](https://arxiv.org/abs/2505.21876) — `generation` `efficiency`
- [GAPrompt: Geometry-Aware Point Cloud Prompt for 3D Vision Model](https://arxiv.org/abs/2505.04119)
- [Geometry-to-Image Synthesis-Driven Generative Point Cloud Registration](https://arxiv.org/abs/2512.09407) — `registration` `generation`
- [InfoCons: Identifying Interpretable Critical Concepts in Point Clouds via Information Theory](https://arxiv.org/abs/2505.19820)
- [WorldMirror: Universal 3D World Reconstruction with Any-Prior Prompting](https://arxiv.org/abs/2510.10726) — `reconstruction` — [code](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror)

</details>

<details><summary><b>AAAI</b> · 42</summary>

- [A New Adversarial Perspective for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2412.13017) — `detection` `robustness`
- [Bridge 2D-3D: Uncertainty-aware Hierarchical Registration Network with Domain Alignment](https://arxiv.org/abs/2504.01641) — `registration`
- [CAD-GPT: Synthesising CAD Construction Sequence with Spatial Reasoning-Enhanced Multimodal LLMs](https://arxiv.org/abs/2412.19663) — `multi-modal`
- [CloudMamba: Grouped Selective State Spaces for Point Cloud Analysis](https://arxiv.org/abs/2511.07823)
- [Cross-PCR: A Robust Cross-Source Point Cloud Registration Framework](https://arxiv.org/abs/2412.18873) — `registration` `robustness`
- [DAPoinTr: Domain Adaptive Point Transformer for Point Cloud Completion](https://arxiv.org/abs/2412.19062) — `completion`
- [DC-PCN: Point Cloud Completion Network with Dual-Codebook Guided Quantization](https://arxiv.org/abs/2501.10966) — `completion` `efficiency`
- [Digging into Intrinsic Contextual Information for High-fidelity 3D Point Cloud Completion](https://arxiv.org/abs/2412.08326) — `completion`
- [DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation](https://arxiv.org/abs/2512.11465) — `reconstruction` `self-supervised`
- [Efficient 3D Recognition with Event-driven Spike Sparse Convolution](https://arxiv.org/abs/2412.07360) — `efficiency`
- [FlowMamba: Learning Point Cloud Scene Flow with Global Motion Propagation](https://arxiv.org/abs/2412.17366) — `scene flow`
- [GaussianPainter: Painting Point Cloud into 3D Gaussians with Normal Guidance](https://arxiv.org/abs/2412.17715) — `gaussian-splatting`
- [Generalized Zero-Shot Learning for Point Cloud Segmentation with Evidence-Based Dynamic Calibration](https://arxiv.org/abs/2509.08280) — `segmentation` `open-vocabulary`
- [HGSFusion: Radar-Camera Fusion with Hybrid Generation and Synchronization for 3D Object Detection](https://arxiv.org/abs/2412.11489) — `detection` `generation` `autonomous driving` `multi-modal`
- [Hyperbolic-constraint Point Cloud Reconstruction from Single RGB-D Images](https://arxiv.org/abs/2412.09055) — `reconstruction`
- [IPDN: Image-enhanced Prompt Decoding Network for 3D Referring Expression Segmentation](https://arxiv.org/abs/2501.04995) — `segmentation`
- [L4DR: LiDAR-4DRadar Fusion for Weather-Robust 3D Object Detection](https://arxiv.org/abs/2408.03677) — `detection` `robustness`
- [LiON: Learning Point-wise Abstaining Penalty for LiDAR Outlier DetectioN Using Diverse Synthetic Data](https://arxiv.org/abs/2309.10230) — `detection` `classification` `autonomous driving` — [code](https://github.com/Daniellli/LiON)
- [Multi-Modal Assistance for Unsupervised Domain Adaptation on Point Cloud 3D Object Detection](https://arxiv.org/abs/2511.07966) — `detection` `multi-modal` `domain adaptation`
- [Noise-Injected Spiking Graph Convolution for Energy-Efficient 3D Point Cloud Denoising](https://arxiv.org/abs/2502.19660) — `classification` `denoising` `efficiency`
- [ObjVariantEnsemble: Advancing Point Cloud LLM Evaluation in Challenging Scenes with Subtly Distinguished Objects](https://arxiv.org/abs/2412.14837) — `vision-language`
- [OLiDM: Object-aware LiDAR Diffusion Models for Autonomous Driving](https://arxiv.org/abs/2412.17226) — `autonomous driving`
- [Pamba: Enhancing Global Interaction in Point Clouds via State Space Model](https://arxiv.org/abs/2406.17442) — `segmentation`
- [PointCFormer: a Relation-based Progressive Feature Extraction Network for Point Cloud Completion](https://arxiv.org/abs/2412.08421) — `segmentation` `detection` `completion`
- [PointTalk: Audio-Driven Dynamic Lip Point Cloud for 3D Gaussian-based Talking Head Synthesis](https://arxiv.org/abs/2412.08504)
- [Position-aware Guided Point Cloud Completion with CLIP Model](https://arxiv.org/abs/2412.08271) — `completion`
- [Pre-training a Density-Aware Pose Transformer for Robust LiDAR-based 3D Human Pose Estimation](https://arxiv.org/abs/2412.13454) — `autonomous driving` `pre-training` `robustness`
- [Preserving Topological and Geometric Embeddings for Point Cloud Recovery](https://arxiv.org/abs/2507.19121)
- [PSReg: Prior-guided Sparse Mixture of Experts for Point Cloud Registration](https://arxiv.org/abs/2501.07762) — `registration`
- [RaLiFlow: Scene Flow Estimation with 4D Radar and LiDAR Point Clouds](https://arxiv.org/abs/2512.10376) — `scene flow` `multi-modal`
- [RCTrans: Radar-Camera Transformer via Radar Densifier and Sequential Decoder for 3D Object Detection](https://arxiv.org/abs/2412.12799) — `detection` `multi-modal`
- [RI-MAE: Rotation-Invariant Masked AutoEncoders for Self-Supervised Point Cloud Representation Learning](https://arxiv.org/abs/2409.00353) — `self-supervised`
- [Riemann-based Multi-scale Attention Reasoning Network for Text-3D Retrieval](https://arxiv.org/abs/2408.13712)
- [SCKD: Semi-Supervised Cross-Modality Knowledge Distillation for 4D Radar Object Detection](https://arxiv.org/abs/2412.14571) — `detection` `multi-modal`
- [Sharpening Neural Implicit Functions with Frequency Consolidation Priors](https://arxiv.org/abs/2412.19720)
- [Simba: Towards High-Fidelity and Geometrically-Consistent Point Cloud Completion via Transformation Diffusion](https://arxiv.org/abs/2511.16161) — `completion`
- [Spiking Point Transformer for Point Cloud Classification](https://arxiv.org/abs/2502.15811) — `classification`
- [SSLFusion: Scale & Space Aligned Latent Fusion Model for Multimodal 3D Object Detection](https://arxiv.org/abs/2504.05170) — `detection` `multi-modal`
- [SymmCompletion: High-Fidelity and High-Consistency Point Cloud Completion with Symmetry Guidance](https://arxiv.org/abs/2503.18007) — `completion` — [code](https://github.com/HongyuYann/SymmCompletion)
- [Taylor Series-Inspired Local Structure Fitting Network for Few-shot Point Cloud Semantic Segmentation](https://arxiv.org/abs/2504.02454) — `segmentation`
- [UniPCGC: Towards Practical Point Cloud Geometry Compression via an Efficient Unified Approach](https://arxiv.org/abs/2503.18541) — `compression` `efficiency`
- [Weighted Poisson-disk Resampling on Large-Scale Point Clouds](https://arxiv.org/abs/2412.09177)

</details>

<details><summary><b>IJCAI</b> · 2</summary>

- [Exploring Semantic Masked Autoencoder for Self-supervised Point Cloud Understanding](https://arxiv.org/abs/2506.21957) — `self-supervised`
- [GPI-Net: Gestalt-Guided Parallel Interaction Network via Orthogonal Geometric Consistency for Robust Point Cloud Registration](https://arxiv.org/abs/2507.14452) — `registration` `robustness`

</details>

<details><summary><b>SIGGRAPH</b> · 3</summary>

- [A Divide-and-Conquer Approach for Global Orientation of Non-Watertight Scene-Level Point Clouds Using 0-1 Integer Optimization](https://arxiv.org/abs/2505.23469) — `segmentation` `reconstruction`
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

<details><summary><b>3DV</b> · 9</summary>

- [DINO in the Room: Leveraging 2D Foundation Models for 3D Segmentation](https://arxiv.org/abs/2503.18944) — `segmentation`
- [Fully-Geometric Cross-Attention for Point Cloud Registration](https://arxiv.org/abs/2502.08285) — `registration`
- [Is clustering enough for LiDAR instance segmentation? A state-of-the-art training-free baseline](https://arxiv.org/abs/2503.13203) — `segmentation` `autonomous driving`
- [LOSC: LiDAR Open-voc Segmentation Consolidator](https://arxiv.org/abs/2507.07605) — `segmentation` `open-vocabulary`
- [MorphoSkel3D: Morphological Skeletonization of 3D Point Clouds for Informed Sampling in Object Classification and Retrieval](https://arxiv.org/abs/2501.12974) — `classification`
- [Para-Lane: Multi-Lane Dataset Registering Parallel Scans for Benchmarking Novel View Synthesis](https://arxiv.org/abs/2502.15635) — `registration` `autonomous driving` `dataset`
- [Rethinking Metrics and Diffusion Architecture for 3D Point Cloud Generation](https://arxiv.org/abs/2511.05308) — `generation`
- [Self-Supervised Implicit Attention Priors for Point Cloud Reconstruction](https://arxiv.org/abs/2511.04864) — `reconstruction` `self-supervised`
- [SurfR: Surface Reconstruction with Multi-scale Attention](https://arxiv.org/abs/2506.08635) — `reconstruction`

</details>

<details><summary><b>WACV</b> · 10</summary>

- [CVP: Central-Peripheral Vision-Inspired Multimodal Model for Spatial Reasoning](https://arxiv.org/abs/2512.08135) — `multi-modal`
- [GFT: Graph Feature Tuning for Efficient Point Cloud Analysis](https://arxiv.org/abs/2511.10799) — `efficiency`
- [MambaTron: Efficient Cross-Modal Point Cloud Enhancement using Aggregate Selective State Space Modeling](https://arxiv.org/abs/2501.16384) — `completion` `reconstruction` `efficiency` — Workshop
- [MEGA-PCC: A Mamba-based Efficient Approach for Joint Geometry and Attribute Point Cloud Compression](https://arxiv.org/abs/2512.22463) — `compression` `efficiency`
- [MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection](https://arxiv.org/abs/2509.07507) — `detection`
- [PALMS+: Modular Image-Based Floor Plan Localization Leveraging Depth Foundation Model](https://arxiv.org/abs/2511.09724) — `localization` `pre-training`
- [Point2Pose: A Generative Framework for 3D Human Pose Estimation with Multi-View Point Cloud Dataset](https://arxiv.org/abs/2512.10321) — `generation` `dataset`
- [SDT-6D: Fully Sparse Depth-Transformer for Staged End-to-End 6D Pose Estimation in Industrial Multi-View Bin Picking](https://arxiv.org/abs/2512.08430)
- [Towards Streaming LiDAR Object Detection with Point Clouds as Egocentric Sequences](https://arxiv.org/abs/2506.06944) — `detection` `autonomous driving`
- [ViGG: Robust RGB-D Point Cloud Registration using Visual-Geometric Mutual Guidance](https://arxiv.org/abs/2511.22908) — `registration` `robustness`

</details>

<details><summary><b>BMVC</b> · 3</summary>

- [Generative Data Augmentation for Object Point Cloud Segmentation](https://arxiv.org/abs/2505.17783) — `segmentation` `generation` `denoising`
- [Hierarchical Image-Guided 3D Point Cloud Segmentation in Industrial Scenes via Multi-View Bayesian Fusion](https://arxiv.org/abs/2512.06882) — `segmentation`
- [Improving Multimodal Distillation for 3D Semantic Segmentation under Domain Shift](https://arxiv.org/abs/2511.17455) — `segmentation` `multi-modal`

</details>

<details><summary><b>ICRA</b> · 23</summary>

- [3DWG: 3D Weakly Supervised Visual Grounding via Category and Instance-Level Alignment](https://arxiv.org/abs/2505.01809)
- [Beyond Frame-wise Tracking: A Trajectory-based Paradigm for Efficient Point Cloud Tracking](https://arxiv.org/abs/2509.11453) — `tracking` `efficiency`
- [Diffusion Based Robust LiDAR Place Recognition](https://arxiv.org/abs/2504.12412) — `localization` `robustness`
- [Domain Adaptation-Based Crossmodal Knowledge Distillation for 3D Semantic Segmentation](https://arxiv.org/abs/2509.00379) — `segmentation` `autonomous driving` `domain adaptation`
- [Improving Monocular Visual-Inertial Initialization with Structureless Visual-Inertial Bundle Adjustment](https://arxiv.org/abs/2502.16598) — `tracking` `reconstruction` `monocular`
- [Introspective Loop Closure for SLAM with 4D Imaging Radar](https://arxiv.org/abs/2503.02383) — `slam` `localization` `multi-modal`
- [Joint 3D Point Cloud Segmentation using Real-Sim Loop: From Panels to Trees and Branches](https://arxiv.org/abs/2503.05630) — `segmentation`
- [LiDAR-enhanced 3D Gaussian Splatting Mapping](https://arxiv.org/abs/2503.05425) — `gaussian-splatting`
- [LiLa-Net: Lightweight Latent LiDAR Autoencoder for 3D Point Cloud Reconstruction](https://arxiv.org/abs/2510.02028) — `reconstruction` `efficiency`
- [M3CAD: Towards Generic Cooperative Autonomous Driving Benchmark](https://arxiv.org/abs/2505.06746) — `detection` `tracking` `autonomous driving` `dataset`
- [Mapping Semantic Segmentation to Point Clouds Using Structure from Motion for Forest Analysis](https://arxiv.org/abs/2505.10751) — `segmentation` — Workshop
- [MFSeg: Efficient Multi-frame 3D Semantic Segmentation](https://arxiv.org/abs/2505.04408) — `segmentation` `upsampling` `efficiency`
- [PlaneHEC: Efficient Hand-Eye Calibration for Multi-view Robotic Arm via Any Point Cloud Plane Detection](https://arxiv.org/abs/2507.19851) — `detection` `efficiency`
- [Radar Tracker: Moving Instance Tracking in Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2507.03441) — `segmentation` `tracking` `multi-modal`
- [Radar Velocity Transformer: Single-scan Moving Object Segmentation in Noisy Radar Point Clouds](https://arxiv.org/abs/2507.03463) — `segmentation` `autonomous driving` `multi-modal`
- [RadarSFD: Single-Frame Diffusion with Pretrained Priors for Radar Point Clouds](https://arxiv.org/abs/2509.18068) — `pre-training` `multi-modal`
- [Real-Time LiDAR Point Cloud Compression and Transmission for Resource-constrained Robots](https://arxiv.org/abs/2502.06123) — `compression` `efficiency`
- [SANDRO: a Robust Solver with a Splitting Strategy for Point Cloud Registration](https://arxiv.org/abs/2503.07743) — `registration` `robustness`
- [SSF: Sparse Long-Range Scene Flow for Autonomous Driving](https://arxiv.org/abs/2501.17821) — `scene flow` `autonomous driving`
- [TDFANet: Encoding Sequential 4D Radar Point Clouds Using Trajectory-Guided Deformable Feature Aggregation for Place Recognition](https://arxiv.org/abs/2504.05103) — `localization` `multi-modal`
- [Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems](https://arxiv.org/abs/2506.06995) — `segmentation` — Workshop
- [Towards Terrain-Aware Task-Driven 3D Scene Graph Generation in Outdoor Environments](https://arxiv.org/abs/2506.06562) — `generation` — Workshop
- [You Only Estimate Once: Unified, One-stage, Real-Time Category-level Articulated Object 6D Pose Estimation for Robotic Grasping](https://arxiv.org/abs/2506.05719) — `efficiency`

</details>

<details><summary><b>IROS</b> · 29</summary>

- [A Direct Semi-Exhaustive Search Method for Robust, Partial-to-Full Point Cloud Registration](https://arxiv.org/abs/2502.00115) — `registration` `robustness`
- [AKF-LIO: LiDAR-Inertial Odometry with Gaussian Map by Adaptive Kalman Filter](https://arxiv.org/abs/2503.06891) — [code](https://github.com/xpxie/AKF-LIO.git)
- [CLAIM: Camera-LiDAR Alignment with Intensity and Monodepth](https://arxiv.org/abs/2512.14001) — `multi-modal`
- [Class-Aware PillarMix: Can Mixed Sample Data Augmentation Enhance 3D Object Detection with Radar Point Clouds?](https://arxiv.org/abs/2503.02687) — `detection` `multi-modal` — [code](https://github.com/boschresearch/CAPMIX)
- [CORENet: Cross-Modal 4D Radar Denoising Network with LiDAR Supervision for Autonomous Driving](https://arxiv.org/abs/2508.13485) — `detection` `denoising` `autonomous driving` `multi-modal`
- [Correspondence-Free Multiview Point Cloud Registration via Depth-Guided Joint Optimisation](https://arxiv.org/abs/2506.18922) — `registration`
- [DAMM-LOAM: Degeneracy Aware Multi-Metric LiDAR Odometry and Mapping](https://arxiv.org/abs/2510.13287) — `slam` `localization` `reconstruction` — Workshop
- [Distilling 3D distinctive local descriptors for 6D pose estimation](https://arxiv.org/abs/2503.15106) — `open-vocabulary`
- [DPGLA: Bridging the Gap between Synthetic and Real Data for Unsupervised Domain Adaptation in 3D LiDAR Semantic Segmentation](https://arxiv.org/abs/2510.23525) — `segmentation` `domain adaptation`
- [EAROL: Environmental Augmented Perception-Aware Planning and Robust Odometry via Downward-Mounted Tilted LiDAR](https://arxiv.org/abs/2508.14554) — `localization` `robustness`
- [Estimating Continuum Robot Shape under External Loading using Spatiotemporal Neural Networks](https://arxiv.org/abs/2510.22339)
- [GBlobs: Local LiDAR Geometry for Improved Sensor Placement Generalization](https://arxiv.org/abs/2510.18539) — `detection`
- [GS-SDF: LiDAR-Augmented Gaussian Splatting and Neural SDF for Geometrically Consistent Rendering and Reconstruction](https://arxiv.org/abs/2503.10170) — `reconstruction` `gaussian-splatting` `autonomous driving`
- [Label-Efficient Grasp Joint Prediction with Point-JEPA](https://arxiv.org/abs/2509.13349) — `self-supervised` `efficiency` — Workshop
- [Label-Efficient LiDAR Panoptic Segmentation](https://arxiv.org/abs/2503.02372) — `segmentation` `efficiency`
- [Leveraging Semantic Graphs for Efficient and Robust LiDAR SLAM](https://arxiv.org/abs/2503.11145) — `slam` `localization` `robustness` `efficiency`
- [LiHRA: A LiDAR-Based HRI Dataset for Automated Risk Monitoring Methods](https://arxiv.org/abs/2509.06597) — `dataset`
- [mmWave Radar-Based Non-Line-of-Sight Pedestrian Localization at T-Junctions Utilizing Road Layout Extraction via Camera](https://arxiv.org/abs/2508.02348) — `detection` `localization` `autonomous driving` `multi-modal`
- [OREN: Octree Residual Network for Real-Time Euclidean Signed Distance Mapping](https://arxiv.org/abs/2510.18999) — `localization` `reconstruction` `efficiency`
- [Overlap-Aware Feature Learning for Robust Unsupervised Domain Adaptation for 3D Semantic Segmentation](https://arxiv.org/abs/2504.01668) — `segmentation` `classification` `autonomous driving` `domain adaptation`
- [R2LDM: An Efficient 4D Radar Super-Resolution Framework Leveraging Diffusion Model](https://arxiv.org/abs/2503.17097) — `generation` `upsampling` `BEV` `multi-modal`
- [Radar-Based NLoS Pedestrian Localization for Darting-Out Scenarios Near Parked Vehicles with Camera-Assisted Point Cloud Interpretation](https://arxiv.org/abs/2508.04033) — `detection` `localization` `multi-modal`
- [RaGNNarok: A Light-Weight Graph Neural Network for Enhancing Radar Point Clouds on Unmanned Ground Vehicles](https://arxiv.org/abs/2507.00937) — `multi-modal` `efficiency`
- [Simulating Automotive Radar with Lidar and Camera Inputs](https://arxiv.org/abs/2503.08068) — `autonomous driving` `multi-modal`
- [TartanGround: A Large-Scale Dataset for Ground Robot Perception and Navigation](https://arxiv.org/abs/2505.10696) — `dataset`
- [TopoLiDM: Topology-Aware LiDAR Diffusion Models for Interpretable and Realistic LiDAR Point Cloud Generation](https://arxiv.org/abs/2507.22454) — `generation` `autonomous driving` — [code](https://github.com/IRMVLab/TopoLiDM)
- [Transformer-Based Spatio-Temporal Association of Apple Fruitlets](https://arxiv.org/abs/2503.03200)
- [TWC-SLAM: Multi-Agent Cooperative SLAM with Text Semantics and WiFi Features Integration for Similar Indoor Environments](https://arxiv.org/abs/2510.22754) — `slam`
- [UAV See, UGV Do: Aerial Imagery and Virtual Teach Enabling Zero-Shot Ground Vehicle Repeat](https://arxiv.org/abs/2505.16912) — `nerf` `open-vocabulary`

</details>

<details><summary><b>RA-L</b> · 11</summary>

- [Breaking the Static Assumption: A Dynamic-Aware LIO Framework Via Spatio-Temporal Normal Analysis](https://arxiv.org/abs/2510.22313) — `localization`
- [CaRaFFusion: Improving 2D Semantic Segmentation with Camera-Radar Point Cloud Fusion and Zero-Shot Image Inpainting](https://arxiv.org/abs/2505.03679) — `segmentation` `autonomous driving` `open-vocabulary` `multi-modal`
- [GOTPR: General Outdoor Text-based Place Recognition Using Scene Graph Retrieval with OpenStreetMap](https://arxiv.org/abs/2501.08575) — `localization`
- [Have We Scene It All? Scene Graph-Aware Deep Point Cloud Compression](https://arxiv.org/abs/2510.08512) — `compression`
- [HOTFLoc++: End-to-End Hierarchical LiDAR Place Recognition, Re-Ranking, and 6-DoF Metric Localisation in Forests](https://arxiv.org/abs/2511.09170) — `localization`
- [PPL: Point Cloud Supervised Proprioceptive Locomotion Reinforcement Learning for Legged Robots in Crawl Spaces](https://arxiv.org/abs/2508.09950)
- [PRISM: Pointcloud Reintegrated Inference via Segmentation and Cross-attention for Manipulation](https://arxiv.org/abs/2507.04633) — `segmentation`
- [Rad-GS: Radar-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments](https://arxiv.org/abs/2511.16091) — `slam` `gaussian-splatting` `multi-modal`
- [Real-Time Adaptive Motion Planning via Point Cloud-Guided, Energy-Based Diffusion and Potential Fields](https://arxiv.org/abs/2507.09383) — `generation` `efficiency`
- [Robust LiDAR-Camera Calibration with 2D Gaussian Splatting](https://arxiv.org/abs/2504.00525) — `gaussian-splatting` `multi-modal` `robustness` — [code](https://github.com/ShuyiZhou495/RobustCalibration)
- [SemRaFiner: Panoptic Segmentation in Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2507.06906) — `segmentation` `classification` `multi-modal`

</details>

<details><summary><b>TPAMI</b> · 4</summary>

- [Flexible-weighted Chamfer Distance: Enhanced Objective Function for Point Cloud Completion](https://arxiv.org/abs/2505.14218) — `completion` — [code](https://github.com/Carroll-Li/FCD)
- [High-quality Pseudo-labeling for Point Cloud Segmentation with Scene-level Annotation](https://arxiv.org/abs/2506.23227) — `segmentation` — [code](https://github.com/LHDuan/WSegPC)
- [Rotation-Adaptive Point Cloud Domain Generalization via Intricate Orientation Learning](https://arxiv.org/abs/2502.02247)
- [Text2Loc++: Generalizing 3D Point Cloud Localization from Natural Language](https://arxiv.org/abs/2511.15308) — `localization`

</details>

<details><summary><b>TVCG</b> · 2</summary>

- [PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation](https://arxiv.org/abs/2511.21365) — `normal estimation`
- [PKSS-Align: Robust Point Cloud Registration on Pre-Kendall Shape Space](https://arxiv.org/abs/2508.04286) — `registration` `robustness`

</details>

<details><summary><b>ISPRS</b> · 7</summary>

- [AIM2PC: Aerial Image to 3D Building Point Cloud Reconstruction](https://arxiv.org/abs/2503.18527) — `reconstruction`
- [APCoTTA: Continual Test-Time Adaptation for Semantic Segmentation of Airborne LiDAR Point Clouds](https://arxiv.org/abs/2505.09971) — `segmentation`
- [Cross-modal feature fusion for robust point cloud registration with ambiguous geometry](https://arxiv.org/abs/2505.13088) — `registration` `robustness`
- [L2M-Reg: Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models](https://arxiv.org/abs/2509.16832) — `registration` `detection`
- [RoofSeg: An edge-aware transformer-based network for end-to-end roof plane segmentation](https://arxiv.org/abs/2508.19003) — `segmentation` `detection` `reconstruction`
- [Uncertainty Quantification Framework for Aerial and UAV Photogrammetry through Error Propagation](https://arxiv.org/abs/2507.13486)
- [Unsupervised deep learning for semantic segmentation of multispectral LiDAR forest point clouds](https://arxiv.org/abs/2502.06227) — `segmentation`

</details>

<details><summary><b>PR</b> · 6</summary>

- [A Lightweight 3D Anomaly Detection Method with Rotationally Invariant Features](https://arxiv.org/abs/2511.13115) — `detection` `anomaly detection` `efficiency`
- [CE-NPBG: Connectivity Enhanced Neural Point-Based Graphics for Novel View Synthesis in Autonomous Driving Scenes](https://arxiv.org/abs/2504.19557) — `autonomous driving` — Workshop
- [Enhancing 3D Point Cloud Classification with ModelNet-R and Point-SkipNet](https://arxiv.org/abs/2509.05198) — `classification` `autonomous driving`
- [PointSlice: Accurate and Efficient Slice-Based Representation for 3D Object Detection from Point Clouds](https://arxiv.org/abs/2509.01487) — `segmentation` `detection` `autonomous driving` `efficiency`
- [SFGFusion: Surface Fitting Guided 3D Object Detection with 4D Radar and Camera Fusion](https://arxiv.org/abs/2510.19215) — `detection` `autonomous driving` `multi-modal`
- [Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge](https://arxiv.org/abs/2510.08316) — `segmentation`

</details>

<details><summary><b>arXiv</b> · 528</summary>

- [3D Can Be Explored In 2D: Pseudo-Label Generation for LiDAR Point Clouds Using Sensor-Intensity-Based 2D Semantic Segmentation](https://arxiv.org/abs/2505.03300) — `segmentation` `generation` `autonomous driving`
- [3D forest semantic segmentation using multispectral LiDAR and 3D deep learning](https://arxiv.org/abs/2507.08025) — `segmentation` `detection`
- [3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction](https://arxiv.org/abs/2503.12001) — `reconstruction` `nerf` `gaussian-splatting` `autonomous driving`
- [3D Human Pose and Shape Estimation from LiDAR Point Clouds: A Review](https://arxiv.org/abs/2509.12197)
- [3D Modeling and Automated Measurement of Concrete Cracks via Segment Anything Refinement and Visual Inertial LiDAR Fusion](https://arxiv.org/abs/2501.09203) — `segmentation` `detection` `reconstruction`
- [3D Point Cloud Object Detection on Edge Devices for Split Computing](https://arxiv.org/abs/2511.02293) — `detection` `autonomous driving`
- [3D-PointZshotS: Geometry-Aware 3D Point Cloud Zero-Shot Semantic Segmentation Narrowing the Visual-Semantic Gap](https://arxiv.org/abs/2504.12442) — `segmentation` `generation` `open-vocabulary`
- [3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh](https://arxiv.org/abs/2501.07478) — `gaussian-splatting`
- [3DKeyAD: High-Resolution 3D Point Cloud Anomaly Detection via Keypoint-Guided Point Clustering](https://arxiv.org/abs/2507.13110) — `registration` `detection` `anomaly detection`
- [3DSES: an indoor Lidar point cloud segmentation dataset with real and pseudo-labels from a 3D model](https://arxiv.org/abs/2501.17534) — `segmentation` `dataset`
- [4D-ROLLS: 4D Radar Occupancy Learning via LiDAR Supervision](https://arxiv.org/abs/2505.13905) — `multi-modal`
- [4DR P2T: 4D Radar Tensor Synthesis with Point Clouds](https://arxiv.org/abs/2502.05550) — `generation` `multi-modal`
- [6D Pose Estimation on Point Cloud Data through Prior Knowledge Integration: A Case Study in Autonomous Disassembly](https://arxiv.org/abs/2505.24669)
- [A Bag of Tricks for Efficient Implicit Neural Point Clouds](https://arxiv.org/abs/2508.19140) — `efficiency`
- [A Coarse to Fine 3D LiDAR Localization with Deep Local Features for Long Term Robot Navigation in Large Environments](https://arxiv.org/abs/2505.18340) — `localization`
- [A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds](https://arxiv.org/abs/2504.09129) — `reconstruction` `gaussian-splatting`
- [A Continuous-Time Consistency Model for 3D Point Cloud Generation](https://arxiv.org/abs/2509.01492) — `generation`
- [A Cross Branch Fusion-Based Contrastive Learning Framework for Point Cloud Self-supervised Learning](https://arxiv.org/abs/2505.24641) — `self-supervised`
- [A Deep Learning Approach to Identify Rock Bolts in Complex 3D Point Clouds of Underground Mines Captured Using Mobile Laser Scanners](https://arxiv.org/abs/2506.20464)
- [A Graph Attention Network-Based Framework for Reconstructing Missing LiDAR Beams](https://arxiv.org/abs/2512.12410) — `reconstruction`
- [A Multi-View High-Resolution Foot-Ankle Complex Point Cloud Dataset During Gait for Occlusion-Robust 3D Completion](https://arxiv.org/abs/2507.11037) — `completion` `robustness` `dataset`
- [A Novel Benchmark and Dataset for Efficient 3D Gaussian Splatting with Gaussian Point Cloud Compression](https://arxiv.org/abs/2505.18197) — `gaussian-splatting` `compression` `autonomous driving` `efficiency`
- [A Novel Grouping-Based Hybrid Color Correction Algorithm for Color Point Clouds](https://arxiv.org/abs/2511.02397) — `compression`
- [A PCA Based Model for Surface Reconstruction from Incomplete Point Clouds](https://arxiv.org/abs/2509.15675) — `reconstruction`
- [A Point Cloud Completion Approach for the Grasping of Partially Occluded Objects and Its Applications in Robotic Strawberry Harvesting](https://arxiv.org/abs/2506.14066) — `segmentation` `detection` `completion`
- [A Real-Time Multi-Model Parametric Representation of Point Clouds](https://arxiv.org/abs/2509.14773) — `detection` `efficiency`
- [A Sensor-Aware Phenomenological Framework for Lidar Degradation Simulation and SLAM Robustness Evaluation](https://arxiv.org/abs/2512.08653) — `slam` `robustness`
- [A Strong View-Free Baseline Approach for Single-View Image Guided Point Cloud Completion](https://arxiv.org/abs/2506.15747) — `completion`
- [A Survey of Deep Learning-based Point Cloud Denoising](https://arxiv.org/abs/2508.17011) — `denoising` `autonomous driving`
- [A Survey of Medical Point Cloud Shape Learning: Registration, Reconstruction and Variation](https://arxiv.org/abs/2508.03057) — `registration` `reconstruction`
- [A workflow for generating synthetic LiDAR datasets in simulation environments](https://arxiv.org/abs/2506.17378)
- [Accurate 3D Grapevine Structure Extraction from High-Resolution Point Clouds](https://arxiv.org/abs/2502.20417)
- [Accurate and Efficient Surface Reconstruction from Point Clouds via Geometry-Aware Local Adaptation](https://arxiv.org/abs/2511.08233) — `reconstruction` `efficiency`
- [Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model](https://arxiv.org/abs/2509.14560) — `generation` `denoising`
- [Adaptive Dual-Weighted Gravitational Point Cloud Denoising Method](https://arxiv.org/abs/2512.10386) — `detection` `reconstruction` `denoising` `autonomous driving`
- [Adaptive Point-Prompt Tuning: Fine-Tuning Heterogeneous Foundation Models for 3D Point Cloud Analysis](https://arxiv.org/abs/2509.00374)
- [Adaptive Voxelization for Transform coding of 3D Gaussian splatting data](https://arxiv.org/abs/2506.00271) — `gaussian-splatting` `compression`
- [Adaptive-LIO: Enhancing Robustness and Precision through Environmental Adaptation in LiDAR Inertial Odometry](https://arxiv.org/abs/2503.05077) — `slam` `autonomous driving` `robustness`
- [Advancing Precision in Multi-Point Cloud Fusion Environments](https://arxiv.org/abs/2508.03179) — `registration`
- [AEOS: Active Environment-aware Optimal Scanning Control for UAV LiDAR-Inertial Odometry in Complex Scenes](https://arxiv.org/abs/2509.09141) — `localization`
- [AF-RLIO: Adaptive Fusion of Radar-LiDAR-Inertial Information for Robust Odometry in Challenging Environments](https://arxiv.org/abs/2507.18317) — `multi-modal` `robustness`
- [AHA! Animating Human Avatars in Diverse Scenes with Gaussian Splatting](https://arxiv.org/abs/2511.09827) — `gaussian-splatting`
- [ALICE-LRI: A General Method for Lossless Range Image Generation for Spinning LiDAR Sensors without Calibration Metadata](https://arxiv.org/abs/2510.20708) — `generation`
- [Aligned Manifold Property and Topology Point Clouds for Learning Molecular Properties](https://arxiv.org/abs/2507.16223)
- [ALISE: Annotation-Free LiDAR Instance Segmentation for Autonomous Driving](https://arxiv.org/abs/2510.05752) — `segmentation` `autonomous driving`
- [Ambiguity-aware Point Cloud Segmentation by Adaptive Margin Contrastive Learning](https://arxiv.org/abs/2507.06592) — `segmentation` `self-supervised`
- [An Adaptive ICP LiDAR Odometry Based on Reliable Initial Pose](https://arxiv.org/abs/2509.22058) — `registration` `detection` `autonomous driving`
- [An Experimental Study of SOTA LiDAR Segmentation Models](https://arxiv.org/abs/2502.12860) — `segmentation`
- [An Indoor Radio Mapping Dataset Combining 3D Point Clouds and RSSI](https://arxiv.org/abs/2511.00494) — `dataset`
- [An Iterative Task-Driven Framework for Resilient LiDAR Place Recognition in Adverse Weather](https://arxiv.org/abs/2504.14806) — `localization`
- [APML: Adaptive Probabilistic Matching Loss for Robust 3D Point Cloud Reconstruction](https://arxiv.org/abs/2509.08104) — `completion` `generation` `reconstruction` `robustness`
- [ArrowPose: Segmentation, Detection, and 5 DoF Pose Estimation Network for Colorless Point Clouds](https://arxiv.org/abs/2506.08699) — `segmentation` `detection`
- [Atlas Gaussian processes on restricted domains and point clouds](https://arxiv.org/abs/2511.15822)
- [Attention-Guided Multi-Scale Local Reconstruction for Point Clouds via Masked Autoencoder Self-Supervised Learning](https://arxiv.org/abs/2507.04084) — `reconstruction` `self-supervised`
- [AttentionGS: Towards Initialization-Free 3D Gaussian Splatting via Structural Attention](https://arxiv.org/abs/2506.23611) — `reconstruction` `nerf` `gaussian-splatting`
- [Audio-3DVG: Unified Audio -- Point Cloud Fusion for 3D Visual Grounding](https://arxiv.org/abs/2507.00669)
- [Autoencoder Models for Point Cloud Environmental Synthesis from WiFi Channel State Information: A Preliminary Study](https://arxiv.org/abs/2504.20541) — `generation`
- [Automated Detection and Analysis of Minor Deformations in Flat Walls Due to Railway Vibrations Using LiDAR and Machine Learning](https://arxiv.org/abs/2501.06457) — `detection`
- [Automated Road Extraction and Centreline Fitting in LiDAR Point Clouds](https://arxiv.org/abs/2502.07486)
- [Automating Infrastructure Surveying: A Framework for Geometric Measurements and Compliance Assessment Using Point Cloud Data](https://arxiv.org/abs/2505.05752) — `segmentation` `detection`
- [BAGNet: A Boundary-Aware Graph Attention Network for 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2506.00475) — `segmentation`
- [BasketLiDAR: The First LiDAR-Camera Multimodal Dataset for Professional Basketball MOT](https://arxiv.org/abs/2508.15299) — `tracking` `reconstruction` `multi-modal` `dataset`
- [BATISNet: Instance Segmentation of Tooth Point Clouds with Boundary Awareness](https://arxiv.org/abs/2512.24201) — `segmentation`
- [Been There, Scanned That: Nostalgia-Driven LiDAR Compression for Self-Driving Cars](https://arxiv.org/abs/2511.00652) — `compression` `autonomous driving`
- [Bench-RNR: Dataset for Benchmarking Repetitive and Non-repetitive Scanning LiDAR for Infrastructure-based Vehicle Localization](https://arxiv.org/abs/2509.15583) — `localization` `dataset`
- [Benefit from Reference: Retrieval-Augmented Cross-modal Point Cloud Completion](https://arxiv.org/abs/2507.14485) — `completion` `generation`
- [BEV-LIO(LC): BEV Image Assisted LiDAR-Inertial Odometry with Loop Closure](https://arxiv.org/abs/2502.19242) — `registration` `BEV`
- [Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders](https://arxiv.org/abs/2509.14975)
- [Bidirectional Feature-aligned Motion Transformation for Efficient Dynamic Point Cloud Compression](https://arxiv.org/abs/2509.14591) — `compression` `efficiency`
- [Boosting Global-Local Feature Matching via Anomaly Synthesis for Multi-Class Point Cloud Anomaly Detection](https://arxiv.org/abs/2505.07375) — `detection` `anomaly detection`
- [Boosting the Class-Incremental Learning in 3D Point Clouds via Zero-Collection-Cost Basic Shape Pre-Training](https://arxiv.org/abs/2504.08412) — `pre-training`
- [Cage-Based Deformation for Transferable and Undefendable Point Cloud Attack](https://arxiv.org/abs/2507.00690)
- [Calibrated Keyframe-Segment Selection for Descriptor-Agnostic LiDAR Loop Closure in Repetitive Environments](https://arxiv.org/abs/2512.09447) — `registration` `segmentation`
- [CaLiV: LiDAR-to-Vehicle Calibration of Arbitrary Sensor Setups](https://arxiv.org/abs/2504.01987) — `detection`
- [CALM-Net: Curvature-Aware LiDAR Point Cloud-based Multi-Branch Neural Network for Vehicle Re-Identification](https://arxiv.org/abs/2510.14576)
- [CanonNet: Canonical Ordering and Curvature Learning for Point Cloud Analysis](https://arxiv.org/abs/2504.02763)
- [CAR-LOAM: Color-Assisted Robust LiDAR Odometry and Mapping](https://arxiv.org/abs/2502.17249) — `robustness`
- [CasPoinTr: Point Cloud Completion with Cascaded Networks and Knowledge Distillation](https://arxiv.org/abs/2509.23375) — `completion` `reconstruction`
- [Channel-adaptive Cross-modal Generative Semantic Communication for Point Cloud Transmission](https://arxiv.org/abs/2506.03211) — `generation` `autonomous driving`
- [Characterizing Lidar Point-Cloud Adversities Using a Vector Field Visualization](https://arxiv.org/abs/2510.13619)
- [CL3DOR: Contrastive Learning for 3D Large Multimodal Models via Odds Ratio on High-Resolution Point Clouds](https://arxiv.org/abs/2501.03879) — `self-supervised` `multi-modal`
- [CLIP-PCQA: Exploring Subjective-Aligned Vision-Language Modeling for Point Cloud Quality Assessment](https://arxiv.org/abs/2501.10071) — `vision-language`
- [Co-Win: Joint Object Detection and Instance Segmentation in LiDAR Point Clouds via Collaborative Window Processing](https://arxiv.org/abs/2507.19691) — `segmentation` `detection` `BEV`
- [Computation-Efficient and Recognition-Friendly 3D Point Cloud Privacy Protection](https://arxiv.org/abs/2503.15818) — `autonomous driving` `efficiency`
- [Convexity-Driven Projection for Point Cloud Dimensionality Reduction](https://arxiv.org/abs/2509.22043)
- [CRISTAL: Real-time Camera Registration in Static LiDAR Scans using Neural Rendering](https://arxiv.org/abs/2511.16349) — `registration` `localization` `efficiency`
- [Cross-Dataset Semantic Segmentation Performance Analysis: Unifying NIST Point Cloud City Datasets for 3D Deep Learning](https://arxiv.org/abs/2508.00822) — `segmentation` `dataset`
- [Cross3DReg: Towards a Large-scale Real-world Cross-source Point Cloud Registration Benchmark](https://arxiv.org/abs/2509.06456) — `registration` `dataset`
- [CS-Net:Contribution-based Sampling Network for Point Cloud Simplification](https://arxiv.org/abs/2501.10789)
- [CURL-SLAM: Continuous and Compact LiDAR Mapping](https://arxiv.org/abs/2506.21077) — `slam` `localization`
- [D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction](https://arxiv.org/abs/2510.25173) — `reconstruction` `gaussian-splatting` `autonomous driving`
- [DAGLFNet: Deep Feature Attention Guided Global and Local Feature Fusion for Pseudo-Image Point Cloud Segmentation](https://arxiv.org/abs/2510.10471) — `segmentation`
- [DAP-MAE: Domain-Adaptive Point Cloud Masked Autoencoder for Effective Cross-Domain Learning](https://arxiv.org/abs/2510.21635) — `self-supervised`
- [Data-Efficient Point Cloud Semantic Segmentation Pipeline for Unimproved Roads](https://arxiv.org/abs/2508.20135) — `segmentation` `efficiency`
- [Dataset Distillation of 3D Point Clouds via Distribution Matching](https://arxiv.org/abs/2503.22154) — `dataset`
- [DCReg: Decoupled Characterization for Efficient Degenerate LiDAR Registration](https://arxiv.org/abs/2509.06285) — `registration` `efficiency`
- [DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring](https://arxiv.org/abs/2509.18898) — `gaussian-splatting` `robustness`
- [Decision PCR: Decision version of the Point Cloud Registration task](https://arxiv.org/abs/2507.14965) — `registration`
- [Deep Imbalanced Multi-Target Regression: 3D Point Cloud Voxel Content Estimation in Simulated Forests](https://arxiv.org/abs/2511.12740) — `detection`
- [Deep Learning based Joint Geometry and Attribute Up-sampling for Large-Scale Colored Point Clouds](https://arxiv.org/abs/2506.22749)
- [Deep learning for 3D point cloud processing - from approaches, tasks to its implications on urban and environmental applications](https://arxiv.org/abs/2509.12452)
- [Deep Learning For Point Cloud Denoising: A Survey](https://arxiv.org/abs/2508.11932) — `denoising`
- [Deep Neural Watermarking for Robust Copyright Protection in 3D Point Clouds](https://arxiv.org/abs/2510.27533) — `robustness`
- [Deep Subspace Learning for Surface Anomaly Classification Based on 3D Point Cloud Data](https://arxiv.org/abs/2502.11669) — `classification`
- [Deep Unrolling of Sparsity-Induced RDO for 3D Point Cloud Attribute Coding](https://arxiv.org/abs/2509.08685) — `compression`
- [Deep Unsupervised Segmentation of Log Point Clouds](https://arxiv.org/abs/2503.14244) — `segmentation`
- [Deep-JGAC: End-to-End Deep Joint Geometry and Attribute Compression for Dense Colored Point Clouds](https://arxiv.org/abs/2502.17939) — `compression`
- [DefTransNet: A Transformer-based Method for Non-Rigid Point Cloud Registration in the Simulation of Soft Tissue Deformation](https://arxiv.org/abs/2502.06336) — `registration`
- [Denoising Diffusion Probabilistic Model for Point Cloud Compression at Low Bit-Rates](https://arxiv.org/abs/2505.13316) — `reconstruction` `compression` `denoising`
- [Denoising-While-Completing Network (DWCNet): Robust Point Cloud Completion Under Corruption](https://arxiv.org/abs/2507.16743) — `completion` `denoising` `autonomous driving` `robustness`
- [Dense 3D Displacement Estimation for Landslide Monitoring via Fusion of TLS Point Clouds and Embedded RGB Images](https://arxiv.org/abs/2506.16265)
- [Dense-depth map guided deep Lidar-Visual Odometry with Sparse Point Clouds and Images](https://arxiv.org/abs/2507.15496) — `completion` `slam` `localization`
- [DensifyBeforehand: LiDAR-assisted Content-aware Densification for Efficient and Quality 3D Gaussian Splatting](https://arxiv.org/abs/2511.19294) — `gaussian-splatting` `monocular` `efficiency`
- [Depth-Aware Range Image-Based Model for Point Cloud Segmentation](https://arxiv.org/abs/2503.14955) — `segmentation`
- [DepthFusion: Depth-Aware Hybrid Feature Fusion for LiDAR-Camera 3D Object Detection](https://arxiv.org/abs/2505.07398) — `detection` `multi-modal`
- [DepthVision: Enabling Robust Vision-Language Models with GAN-Based LiDAR-to-RGB Synthesis for Autonomous Driving](https://arxiv.org/abs/2509.07463) — `autonomous driving` `vision-language` `robustness`
- [Desensitizing for Improving Corruption Robustness in Point Cloud Classification through Adversarial Training](https://arxiv.org/abs/2509.23010) — `classification` `robustness`
- [DetVPCC: RoI-based Point Cloud Sequence Compression for 3D Object Detection](https://arxiv.org/abs/2502.04804) — `detection` `compression`
- [DFG-PCN: Point Cloud Completion with Degree-Flexible Point Graph](https://arxiv.org/abs/2509.23703) — `completion` `reconstruction`
- [DG-MVP: 3D Domain Generalization via Multiple Views of Point Clouds for Classification](https://arxiv.org/abs/2504.12456) — `classification`
- [Differentiable High-Performance Ray Tracing-Based Simulation of Radio Propagation with Point Clouds](https://arxiv.org/abs/2507.04021)
- [DiffPCN: Latent Diffusion Model Based on Multi-view Depth Images for Point Cloud Completion](https://arxiv.org/abs/2509.23723) — `completion` `generation`
- [DiffS-NOCS: 3D Point Cloud Reconstruction through Coloring Sketches to NOCS Maps Using Diffusion Models](https://arxiv.org/abs/2506.12835) — `reconstruction`
- [Diffusion-Based mmWave Radar Point Cloud Enhancement Driven by Range Images](https://arxiv.org/abs/2503.02300) — `autonomous driving` `multi-modal`
- [DINOReg: Strong Point Cloud Registration with Vision Foundation Model](https://arxiv.org/abs/2509.24370) — `registration` `pre-training`
- [DINOSTAR: Deep Iterative Neural Object Detector Self-Supervised Training for Roadside LiDAR Applications](https://arxiv.org/abs/2501.17076) — `detection` `self-supervised`
- [DisorientLiDAR: Physical Attacks on LiDAR-based Localization](https://arxiv.org/abs/2509.12595) — `localization` `autonomous driving`
- [DLBAcalib: Robust Extrinsic Calibration for Non-Overlapping LiDARs Based on Dual LBA](https://arxiv.org/abs/2507.09176) — `reconstruction` `robustness`
- [DM3D: Dynamic Mamba via Offset-Guided Feature Resampling for Point Cloud Understanding](https://arxiv.org/abs/2512.03424)
- [DPCD: A Quality Assessment Database for Dynamic Point Clouds](https://arxiv.org/abs/2505.12431)
- [Dual-Branch Center-Surrounding Contrast: Rethinking Contrastive Learning for 3D Point Clouds](https://arxiv.org/abs/2512.08673) — `generation` `self-supervised`
- [EdgeRegNet: Edge Feature-based Multimodal Registration Network between Images and LiDAR Point Clouds](https://arxiv.org/abs/2503.15284) — `registration` `autonomous driving` `multi-modal`
- [EEPNet-V2: Patch-to-Pixel Solution for Efficient Cross-Modal Registration between LiDAR Point Cloud and Camera Image](https://arxiv.org/abs/2503.15285) — `registration` `efficiency`
- [Efficient and Distributed Large-Scale Point Cloud Bundle Adjustment via Majorization-Minimization](https://arxiv.org/abs/2502.18801) — `efficiency`
- [Efficient Continuous Group Convolutions for Local SE(3) Equivariance in 3D Point Clouds](https://arxiv.org/abs/2502.07505) — `efficiency`
- [Efficient Implicit Neural Compression of Point Clouds via Learnable Activation in Latent Space](https://arxiv.org/abs/2504.14471) — `compression` `efficiency`
- [Efficient LiDAR Reflectance Compression via Scanning Serialization](https://arxiv.org/abs/2505.09433) — `compression` `efficiency`
- [Efficient Model-Based Purification Against Adversarial Attacks for LiDAR Segmentation](https://arxiv.org/abs/2508.19290) — `segmentation` `generation` `robustness` `efficiency`
- [Efficient Point Clouds Upsampling via Flow Matching](https://arxiv.org/abs/2501.15286) — `upsampling` `efficiency`
- [Efficiently Closing Loops in LiDAR-Based SLAM Using Point Cloud Density Maps](https://arxiv.org/abs/2501.07399) — `detection` `slam` `localization`
- [Enhanced Sparse Point Cloud Data Processing for Privacy-aware Human Action Recognition](https://arxiv.org/abs/2508.10469) — `tracking`
- [Enhancing Human-Robot Collaboration: A Sim2Real Domain Adaptation Algorithm for Point Cloud Segmentation in Industrial Environments](https://arxiv.org/abs/2506.09552) — `segmentation` `domain adaptation`
- [Enhancing Lidar Point Cloud Sampling via Colorization and Super-Resolution of Lidar Imagery](https://arxiv.org/abs/2505.02049) — `generation` `upsampling`
- [Enhancing point cloud analysis via neighbor aggregation correction based on cross-stage structure correlation](https://arxiv.org/abs/2506.15160)
- [Enhancing Tree Species Classification: Insights from YOLOv8 and Explainable AI Applied to TLS Point Cloud Projections](https://arxiv.org/abs/2512.16950) — `classification`
- [Environment-Driven Online LiDAR-Camera Extrinsic Calibration](https://arxiv.org/abs/2502.00801) — `multi-modal`
- [Equivariant Flow Matching for Point Cloud Assembly](https://arxiv.org/abs/2505.21539)
- [Evaluation of Intra-operative Patient-specific Methods for Point Cloud Completion for Minimally Invasive Liver Interventions](https://arxiv.org/abs/2503.11969) — `registration` `completion`
- [Explainable LiDAR 3D Point Cloud Segmentation and Clustering for Detecting Airplane-Generated Wind Turbulence](https://arxiv.org/abs/2503.00518) — `segmentation` `detection`
- [Exploring Single Domain Generalization of LiDAR-based Semantic Segmentation under Imperfect Labels](https://arxiv.org/abs/2510.09035) — `segmentation` `autonomous driving`
- [Face recognition on point cloud with cgan-top for denoising](https://arxiv.org/abs/2506.06864) — `generation` `denoising`
- [FACT: Multinomial Misalignment Classification for Point Cloud Registration](https://arxiv.org/abs/2504.06627) — `registration` `classification`
- [Fast 3D point clouds retrieval for Large-scale 3D Place Recognition](https://arxiv.org/abs/2502.21067) — `localization`
- [Fast globally optimal Truncated Least Squares point cloud registration with fixed rotation axis](https://arxiv.org/abs/2508.15613) — `registration`
- [Few to Big: Prototype Expansion Network via Diffusion Learner for Point Cloud Few-shot Semantic Segmentation](https://arxiv.org/abs/2509.12878) — `segmentation`
- [FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking](https://arxiv.org/abs/2504.01732) — `reconstruction` `dataset`
- [FLARES: Fast and Accurate LiDAR Multi-Range Semantic Segmentation](https://arxiv.org/abs/2502.09274) — `segmentation` `autonomous driving`
- [FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds](https://arxiv.org/abs/2511.20065) — `reconstruction` `compression` `efficiency`
- [FlexCloud: Direct, Modular Georeferencing and Drift-Correction of Point Cloud Maps](https://arxiv.org/abs/2502.00395) — `slam` `localization` `generation` `autonomous driving`
- [Flying on Point Clouds with Reinforcement Learning](https://arxiv.org/abs/2503.00496)
- [ForestFormer3D: A Unified Framework for End-to-End Segmentation of Forest LiDAR 3D Point Clouds](https://arxiv.org/abs/2506.16991) — `segmentation`
- [Foundational Models for 3D Point Clouds: A Survey and Outlook](https://arxiv.org/abs/2501.18594)
- [Fourier Decomposition for Explicit Representation of 3D Point Cloud Attributes](https://arxiv.org/abs/2503.10055)
- [FractalCloud: A Fractal-Inspired Architecture for Efficient Large-Scale Point Cloud Processing](https://arxiv.org/abs/2511.07665) — `autonomous driving` `efficiency` — [code](https://github.com/Yuzhe-Fu/FractalCloud)
- [From Canopy to Ground via ForestGen3D: Learning Cross-Domain Generation of 3D Forest Structure from Aerial-to-Terrestrial LiDAR](https://arxiv.org/abs/2509.16346) — `generation`
- [From Images to Point Clouds: An Efficient Solution for Cross-media Blind Quality Assessment without Annotated Training](https://arxiv.org/abs/2501.13387) — `efficiency`
- [From Propagation to Prediction: Point-level Uncertainty Evaluation of MLS Point Clouds under Limited Ground Truth](https://arxiv.org/abs/2511.03053)
- [GaRLIO: Gravity enhanced Radar-LiDAR-Inertial Odometry](https://arxiv.org/abs/2502.07703) — `multi-modal`
- [Gaussian2Scene: 3D Scene Representation Learning via Self-supervised Learning with 3D Gaussian Splatting](https://arxiv.org/abs/2506.08777) — `reconstruction` `gaussian-splatting` `self-supervised`
- [GeMS: Efficient Gaussian Splatting for Extreme Motion Blur](https://arxiv.org/abs/2508.14682) — `generation` `gaussian-splatting` `efficiency`
- [Generalized Gaussian Entropy Model for Point Cloud Attribute Compression with Dynamic Likelihood Intervals](https://arxiv.org/abs/2506.09510) — `compression`
- [Generating Adversarial Point Clouds Using Diffusion Model](https://arxiv.org/abs/2507.21163) — `classification` `generation` `robustness`
- [Geo-Registration of Terrestrial LiDAR Point Clouds with Satellite Images without GNSS](https://arxiv.org/abs/2507.05999) — `registration`
- [Geographical hotspot prediction based on point cloud-voxel-community partition clustering](https://arxiv.org/abs/2503.21084) — `detection`
- [Geometry-Aware Cross Modal Alignment for Light Field-LiDAR Semantic Segmentation](https://arxiv.org/abs/2510.06687) — `segmentation` `autonomous driving`
- [GeoT: Geometry-guided Instance-dependent Transition Matrix for Semi-supervised Tooth Point Cloud Segmentation](https://arxiv.org/abs/2503.16976) — `segmentation`
- [GMOR: A Lightweight Robust Point Cloud Registration Framework via Geometric Maximum Overlapping](https://arxiv.org/abs/2508.17427) — `registration` `robustness` `efficiency`
- [GP-GS: Gaussian Processes Densification for 3D Gaussian Splatting](https://arxiv.org/abs/2502.02283) — `gaussian-splatting` `upsampling`
- [Graph Attention-Driven Bayesian Deep Unrolling for Dual-Peak Single-Photon Lidar Imaging](https://arxiv.org/abs/2504.02480)
- [Graph-based Point Cloud Surface Reconstruction using B-Splines](https://arxiv.org/abs/2509.16050) — `reconstruction`
- [Grasping Partially Occluded Objects Using Autoencoder-Based Point Cloud Inpainting](https://arxiv.org/abs/2503.12549)
- [Ground Awareness in Deep Learning for Large Outdoor Point Cloud Segmentation](https://arxiv.org/abs/2501.18246) — `segmentation`
- [GroundFlow: A Plug-in Module for Temporal Reasoning on 3D Point Cloud Sequential Grounding](https://arxiv.org/abs/2506.21188)
- [GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting](https://arxiv.org/abs/2501.13971) — `nerf` `gaussian-splatting` `autonomous driving`
- [Guided and Unguided Conditional Diffusion Mechanisms for Structured and Semantically-Aware 3D Point Cloud Generation](https://arxiv.org/abs/2509.17206) — `segmentation` `generation`
- [Guided Model-based LiDAR Super-Resolution for Resource-Efficient Automotive scene Segmentation](https://arxiv.org/abs/2509.01317) — `segmentation` `upsampling` `autonomous driving` `efficiency`
- [HeartFormer: Semantic-Aware Dual-Structure Transformers for 3D Four-Chamber Cardiac Point Cloud Reconstruction](https://arxiv.org/abs/2512.00264) — `reconstruction`
- [HFBRI-MAE: Handcrafted Feature Based Rotation-Invariant Masked Autoencoder for 3D Point Cloud Analysis](https://arxiv.org/abs/2504.14132) — `self-supervised`
- [HGACNet: Hierarchical Graph Attention Network for Cross-Modal Point Cloud Completion](https://arxiv.org/abs/2509.13692) — `completion` `reconstruction`
- [Hierarchical Attention Networks for Lossless Point Cloud Attribute Compression](https://arxiv.org/abs/2504.00481) — `compression`
- [Hierarchical Feature Learning for Medical Point Clouds via State Space Model](https://arxiv.org/abs/2504.13015)
- [High Efficiency Wiener Filter-based Point Cloud Quality Enhancement for MPEG G-PCC](https://arxiv.org/abs/2503.17467) — `compression` `efficiency`
- [HiMo: High-Speed Objects Motion Compensation in Point Clouds](https://arxiv.org/abs/2503.00803)
- [Hint: hierarchical inter-frame correlation for one-shot point cloud sequence compression](https://arxiv.org/abs/2509.14859) — `compression`
- [HiPoNet: A Multi-View Simplicial Complex Network for High Dimensional Point-Cloud and Single-Cell Data](https://arxiv.org/abs/2502.07746) — `classification`
- [HLS4PC: A Parametrizable Framework For Accelerating Point-Based 3D Point Cloud Models on FPGA](https://arxiv.org/abs/2512.22139) — `segmentation` `classification`
- [Human Action Recognition from Point Clouds over Time](https://arxiv.org/abs/2510.05506)
- [Human-Interpretable Uncertainty Explanations for Point Cloud Registration](https://arxiv.org/abs/2509.18786) — `registration`
- [Hybrid Long and Short Range Flows for Point Cloud Filtering](https://arxiv.org/abs/2508.08542) — `denoising`
- [HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder](https://arxiv.org/abs/2505.01938) — `generation` `gaussian-splatting` `compression` `efficiency`
- [HybridReg: Robust 3D Point Cloud Registration with Hybrid Motions](https://arxiv.org/abs/2503.07019) — `registration` `robustness`
- [HydraMamba: Multi-Head State Space Model for Global Point Cloud Learning](https://arxiv.org/abs/2507.19778)
- [HyPCV-Former: Hyperbolic Spatio-Temporal Transformer for 3D Point Cloud Video Anomaly Detection](https://arxiv.org/abs/2508.00473) — `detection` `anomaly detection`
- [Hyperbolic Contrastive Learning for Hierarchical 3D Point Cloud Embedding](https://arxiv.org/abs/2501.02285) — `self-supervised`
- [IAENet: An Importance-Aware Ensemble Model for 3D Point Cloud-Based Anomaly Detection](https://arxiv.org/abs/2508.20492) — `detection` `anomaly detection`
- [IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection](https://arxiv.org/abs/2511.03267) — `detection` `anomaly detection` `dataset`
- [iMatcher: Improve matching in point cloud registration via local-to-global geometric consistency learning](https://arxiv.org/abs/2509.08982) — `registration`
- [ImLPR: Image-based LiDAR Place Recognition using Vision Foundation Models](https://arxiv.org/abs/2505.18364) — `localization`
- [Improving Open-Set Semantic Segmentation in 3D Point Clouds by Conditional Channel Capacity Maximization: Preliminary Results](https://arxiv.org/abs/2505.11521) — `segmentation`
- [INDOOR-LiDAR: Bridging Simulation and Reality for Robot-Centric 360 degree Indoor LiDAR Perception -- A Robot-Centric Hybrid Dataset](https://arxiv.org/abs/2512.12377) — `dataset`
- [InfraDiffusion: zero-shot depth map restoration with diffusion models and prompted segmentation from sparse infrastructure point clouds](https://arxiv.org/abs/2509.03324) — `segmentation` `detection` `open-vocabulary`
- [Initialize to Generalize: A Stronger Initialization Pipeline for Sparse-View 3DGS](https://arxiv.org/abs/2510.17479) — `gaussian-splatting`
- [InJecteD: Analyzing Trajectories and Drift Dynamics in Denoising Diffusion Probabilistic Models for 2D Point Cloud Generation](https://arxiv.org/abs/2509.12239) — `generation` `denoising`
- [Inland-LOAM: Voxel-Based Structural Semantic LiDAR Odometry and Mapping for Inland Waterway Navigation](https://arxiv.org/abs/2508.03672) — `slam`
- [Integrating Product Coefficients for Improved 3D LiDAR Data Classification](https://arxiv.org/abs/2503.11943) — `classification`
- [Integrating Product Coefficients for Improved 3D LiDAR Data Classification (Part II)](https://arxiv.org/abs/2510.15219) — `classification`
- [Integrating SAM Supervision for 3D Weakly Supervised Point Cloud Segmentation](https://arxiv.org/abs/2508.19909) — `segmentation`
- [Intelligent driving vehicle front multi-target tracking and detection based on YOLOv5 and point cloud 3D projection](https://arxiv.org/abs/2504.11310) — `detection` `tracking`
- [Interpretable Affordance Detection on 3D Point Clouds with Probabilistic Prototypes](https://arxiv.org/abs/2504.18355) — `detection`
- [Introducing the Short-Time Fourier Kolmogorov Arnold Network: A Dynamic Graph CNN Approach for Tree Species Classification in 3D Point Clouds](https://arxiv.org/abs/2503.23647) — `classification`
- [IPCD: Intrinsic Point-Cloud Decomposition](https://arxiv.org/abs/2511.09866)
- [J-SGFT: Joint Spatial and Graph Fourier Domain Learning for Point Cloud Attribute Deblocking](https://arxiv.org/abs/2511.05047) — `compression` `autonomous driving` — Workshop
- [Joint graph entropy knowledge distillation for point cloud classification and robustness against corruptions](https://arxiv.org/abs/2509.22150) — `classification` `robustness`
- [KAN or MLP? Point Cloud Shows the Way Forward](https://arxiv.org/abs/2504.13593)
- [KNN-Defense: Defense against 3D Adversarial Point Clouds using Nearest-Neighbor Search](https://arxiv.org/abs/2506.06906) — `robustness`
- [Label-Efficient LiDAR Semantic Segmentation with 2D-3D Vision Transformer Adapters](https://arxiv.org/abs/2503.03299) — `segmentation` `efficiency`
- [Label-Efficient Point Cloud Segmentation with Active Learning](https://arxiv.org/abs/2512.05759) — `segmentation` `efficiency`
- [LAHNet: Local Attentive Hashing Network for Point Cloud Registration](https://arxiv.org/abs/2512.00927) — `registration`
- [Laplace-Beltrami Operator for Gaussian Splatting](https://arxiv.org/abs/2502.17531) — `reconstruction` `gaussian-splatting`
- [LDRFusion: A LiDAR-Dominant multimodal refinement framework for 3D object detection](https://arxiv.org/abs/2507.16224) — `detection` `completion` `multi-modal`
- [Learning better representations for crowded pedestrians in offboard LiDAR-camera 3D tracking-by-detection](https://arxiv.org/abs/2505.16029) — `detection` `tracking` `generation` `multi-modal`
- [Learning Point Correspondences In Radar 3D Point Clouds For Radar-Inertial Odometry](https://arxiv.org/abs/2506.18580) — `multi-modal`
- [Learning Smooth State-Dependent Traversability from Dense Point Clouds](https://arxiv.org/abs/2506.04362)
- [LEMON-Mapping: Loop-Enhanced Large-Scale Multi-Session Point Cloud Merging and Optimization for Globally Consistent Mapping](https://arxiv.org/abs/2505.10018)
- [Less is More: Efficient Point Cloud Reconstruction via Multi-Head Decoders](https://arxiv.org/abs/2505.19057) — `reconstruction` `efficiency`
- [Leveraging CVAE for Joint Configuration Estimation of Multifingered Grippers from Point Cloud Data](https://arxiv.org/abs/2511.17276) — `generation`
- [LiDAR Based Semantic Perception for Forklifts in Outdoor Environments](https://arxiv.org/abs/2505.22258) — `segmentation`
- [LiDAR MOT-DETR: A LiDAR-based Two-Stage Transformer for 3D Multiple Object Tracking](https://arxiv.org/abs/2505.12753) — `tracking`
- [LiDAR Point Cloud Colourisation Using Multi-Camera Fusion and Low-Light Image Enhancement](https://arxiv.org/abs/2509.25859)
- [LiDAR Point Cloud Image-based Generation Using Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2509.18917) — `detection` `generation` `denoising`
- [LiDAR Registration with Visual Foundation Models](https://arxiv.org/abs/2502.19374) — `registration` `localization`
- [Lidar Variability: A Novel Dataset and Comparative Study of Solid-State and Spinning Lidars](https://arxiv.org/abs/2507.04321) — `localization` `reconstruction` `dataset`
- [LiDAR-based 3D Change Detection at City Scale](https://arxiv.org/abs/2510.21112) — `detection`
- [LiDAR-based Human Activity Recognition through Laplacian Spectral Analysis](https://arxiv.org/abs/2509.23255) — [code](https://github.com/Arritmic/oulu-pointcloud-har)
- [LiDAR-based Object Detection with Real-time Voice Specifications](https://arxiv.org/abs/2504.02920) — `detection` `efficiency`
- [LiDAR-Based Vehicle Detection and Tracking for Autonomous Racing](https://arxiv.org/abs/2501.14502) — `detection` `tracking`
- [LiDAR-VGGT: Cross-Modal Coarse-to-Fine Fusion for Globally Consistent and Metric-Scale Dense Mapping](https://arxiv.org/abs/2511.01186) — `slam` `reconstruction`
- [LiDARDraft: Generating LiDAR Point Cloud from Versatile Inputs](https://arxiv.org/abs/2512.20105) — `generation` `autonomous driving`
- [LiDARDustX: A LiDAR Dataset for Dusty Unstructured Road Environments](https://arxiv.org/abs/2505.21914) — `localization` `autonomous driving` `dataset`
- [LidarScout: Direct Out-of-Core Rendering of Massive Point Clouds](https://arxiv.org/abs/2509.20198)
- [LifelongPR: Lifelong point cloud place recognition based on sample replay and prompt learning](https://arxiv.org/abs/2507.10034) — `localization` `autonomous driving`
- [LiM-Loc: Visual Localization with Dense and Accurate 3D Reference Maps Directly Corresponding 2D Keypoints to 3D LiDAR Point Clouds](https://arxiv.org/abs/2503.23664) — `localization` `reconstruction`
- [Linearized Optimal Transport for Analysis of High-Dimensional Point-Cloud and Single-Cell Data](https://arxiv.org/abs/2510.22033)
- [Linearized Optimal Transport pyLOT Library: A Toolkit for Machine Learning on Point Clouds](https://arxiv.org/abs/2502.03439)
- [LIR-LIVO: A Lightweight,Robust LiDAR/Vision/Inertial Odometry with Illumination-Resilient Deep Features](https://arxiv.org/abs/2502.08676) — `slam` `robustness` `efficiency`
- [LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving](https://arxiv.org/abs/2511.16049) — `generation` `autonomous driving`
- [LLM-Guided Material Inference for 3D Point Clouds](https://arxiv.org/abs/2512.03237) — `vision-language`
- [LLM-Guided Taxonomy and Hierarchical Uncertainty for 3D Point Cloud Active Learning](https://arxiv.org/abs/2505.18924) — `segmentation` `vision-language`
- [Locating and Mitigating Gradient Conflicts in Point Cloud Domain Adaptation via Saliency Map Skewness](https://arxiv.org/abs/2504.15796) — `classification` `domain adaptation`
- [Low-Complexity Patch-based No-Reference Point Cloud Quality Metric exploiting Weighted Structure and Texture Features](https://arxiv.org/abs/2503.15001) — `compression` — [code](https://github.com/michaelneri/PST-PCQA)
- [LP-ICP: General Localizability-Aware Point Cloud Registration for Robust Localization in Extreme Unstructured Environments](https://arxiv.org/abs/2501.02580) — `registration` `slam` `localization` `robustness`
- [LPCM: Learning-based Predictive Coding for LiDAR Point Cloud Compression](https://arxiv.org/abs/2505.20059) — `compression`
- [LPRnet: A self-supervised registration network for LiDAR and photogrammetric point clouds](https://arxiv.org/abs/2501.05669) — `registration` `self-supervised`
- [MaizeField3D: A Curated 3D Point Cloud and Procedural Model Dataset of Field-Grown Maize from a Diversity Panel](https://arxiv.org/abs/2503.07813) — `dataset`
- [MambaH-Fit: Rethinking Hyper-surface Fitting-based Point Cloud Normal Estimation via State Space Modelling](https://arxiv.org/abs/2510.09088) — `normal estimation`
- [MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation](https://arxiv.org/abs/2511.15077) — `tracking`
- [Manifold-Aware Point Cloud Completion via Geodesic-Attentive Hierarchical Feature Learning](https://arxiv.org/abs/2512.05710) — `completion` `reconstruction`
- [Mapping and Localization Using LiDAR Fiducial Markers](https://arxiv.org/abs/2502.03510) — `localization`
- [Masked Clustering Prediction for Unsupervised Point Cloud Pre-training](https://arxiv.org/abs/2508.08910) — `pre-training`
- [MaskPlanner: Learning-Based Object-Centric Motion Generation from 3D Point Clouds](https://arxiv.org/abs/2502.18745) — `generation`
- [Matching Distance and Geometric Distribution Aided Learning Multiview Point Cloud Registration](https://arxiv.org/abs/2505.03692) — `registration`
- [Matching the Optimal Denoiser in Point Cloud Diffusion with (Improved) Rotational Alignment](https://arxiv.org/abs/2510.03335) — `generation` `denoising`
- [Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin](https://arxiv.org/abs/2511.20348) — `reconstruction` `gaussian-splatting`
- [MCI-Net: A Robust Multi-Domain Context Integration Network for Point Cloud Registration](https://arxiv.org/abs/2512.23472) — `registration` `robustness`
- [Med-PU: Point Cloud Upsampling for High-Fidelity 3D Medical Shape Reconstruction](https://arxiv.org/abs/2501.16716) — `segmentation` `reconstruction` `upsampling`
- [Memory-Guided Point Cloud Completion for Dental Reconstruction](https://arxiv.org/abs/2512.03598) — `completion` `reconstruction`
- [MeshCoder: LLM-Powered Structured Mesh Code Generation from Point Clouds](https://arxiv.org/abs/2508.14879) — `generation` `reconstruction` `vision-language`
- [Methods for the Segmentation of Reticular Structures Using 3D LiDAR Data: A Comparative Evaluation](https://arxiv.org/abs/2507.20589) — `segmentation` `detection`
- [MFM-point: Multi-scale Flow Matching for Point Cloud Generation](https://arxiv.org/abs/2511.20041) — `generation`
- [Mind the Domain Gap: Measuring the Domain Gap Between Real-World and Synthetic Point Clouds for Automated Driving Development](https://arxiv.org/abs/2505.17959) — `domain adaptation`
- [Minkowski-MambaNet: A Point Cloud Framework with Selective State Space Models for Forest Biomass Quantification](https://arxiv.org/abs/2510.09367)
- [MinkUNeXt-SI: Improving point cloud-based place recognition including spherical coordinates and LiDAR intensity](https://arxiv.org/abs/2505.17591) — `localization`
- [MLATC: Fast Hierarchical Topological Mapping from 3D LiDAR Point Clouds Based on Adaptive Resonance Theory](https://arxiv.org/abs/2511.22238)
- [mmDEAR: mmWave Point Cloud Density Enhancement for Accurate Human Body Reconstruction](https://arxiv.org/abs/2503.02375) — `reconstruction`
- [Modeling high dimensional point clouds with the spherical cluster model](https://arxiv.org/abs/2512.21960)
- [ModelNet40-E: An Uncertainty-Aware Benchmark for Point Cloud Classification](https://arxiv.org/abs/2508.01269) — `classification` `dataset`
- [MOGS: Monocular Object-guided Gaussian Splatting in Large Scenes](https://arxiv.org/abs/2509.06685) — `gaussian-splatting` `autonomous driving` `monocular`
- [MoRAL: Motion-aware Multi-Frame 4D Radar and LiDAR Fusion for Robust 3D Object Detection](https://arxiv.org/abs/2505.09422) — `detection` `autonomous driving` `multi-modal` `robustness`
- [MRG: A Multi-Robot Manufacturing Digital Scene Generation Method Using Multi-Instance Point Cloud Registration](https://arxiv.org/abs/2501.02041) — `registration` `segmentation` `generation`
- [MS-DGCNN++: Multi-Scale Dynamic Graph Convolution with Scale-Dependent Normalization for Robust LiDAR Tree Species Classification](https://arxiv.org/abs/2507.12602) — `classification` `robustness`
- [MT-PCR: Hybrid Mamba-Transformer Network with Spatial Serialization for Point Cloud Registration](https://arxiv.org/abs/2506.13183) — `registration`
- [MT-PCR: Leveraging Modality Transformation for Large-Scale Point Cloud Registration with Limited Overlap](https://arxiv.org/abs/2503.12833) — `registration` `BEV`
- [Multi-dataset synergistic in supervised learning to pre-label structural components in point clouds from shell construction scenes](https://arxiv.org/abs/2502.14721) — `segmentation` `dataset`
- [Multi-Head Adaptive Graph Convolution Network for Sparse Point Cloud-Based Human Activity Recognition](https://arxiv.org/abs/2504.02778)
- [Multi-Mapcher: Loop Closure Detection-Free Heterogeneous LiDAR Multi-Session SLAM Leveraging Outlier-Robust Registration for Autonomous Vehicles](https://arxiv.org/abs/2511.00635) — `registration` `detection` `slam` `localization`
- [Multi-modal Multi-task Pre-training for Improved Point Cloud Understanding](https://arxiv.org/abs/2507.17533) — `pre-training` `multi-modal`
- [Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds](https://arxiv.org/abs/2502.20316) — `self-supervised`
- [Multi-view Structural Convolution Network for Domain-Invariant Point Cloud Recognition of Autonomous Vehicles](https://arxiv.org/abs/2501.16289)
- [MultiEditor: Controllable Multimodal Object Editing for Driving Scenarios Using 3D Gaussian Splatting Priors](https://arxiv.org/abs/2507.21872) — `gaussian-splatting` `autonomous driving` `multi-modal`
- [Multimodal classification of forest biodiversity potential from 2D orthophotos and 3D airborne laser scanning point clouds](https://arxiv.org/abs/2501.01728) — `classification` `multi-modal`
- [Multimodal Point Cloud Semantic Segmentation With Virtual Point Enhancement](https://arxiv.org/abs/2504.01449) — `segmentation` `multi-modal`
- [Multimodal Robust Prompt Distillation for 3D Point Cloud Models](https://arxiv.org/abs/2511.21574) — `multi-modal` `robustness`
- [Multiview Point Cloud Registration Based on Minimum Potential Energy for Free-Form Blade Measurement](https://arxiv.org/abs/2502.07680) — `registration` `reconstruction`
- [Multiview Point Cloud Registration via Optimization in an Autoencoder Latent Space](https://arxiv.org/abs/2504.21467) — `registration` `generation`
- [MutualForce: Mutual-Aware Enhancement for 4D Radar-LiDAR 3D Object Detection](https://arxiv.org/abs/2501.10266) — `detection` `autonomous driving` `multi-modal`
- [Natively Trainable Sparse Attention for Hierarchical Point Cloud Datasets](https://arxiv.org/abs/2508.10758)
- [NeuRadar: Neural Radiance Fields for Automotive Radar Point Clouds](https://arxiv.org/abs/2504.00859) — `nerf` `autonomous driving` `multi-modal`
- [Neural Shortest Path for Surface Reconstruction from Point Clouds](https://arxiv.org/abs/2502.06047) — `reconstruction`
- [NeuralBoneReg: An Instance-Specific Label-Free Point Cloud-Based Method for Multi-Modal Bone Surface Registration](https://arxiv.org/abs/2511.14286) — `registration` `multi-modal`
- [No-reference geometry quality assessment for colorless point clouds via list-wise rank learning](https://arxiv.org/abs/2502.11726) — `reconstruction` `compression`
- [Noise2Score3D: Tweedie's Approach for Unsupervised Point Cloud Denoising](https://arxiv.org/abs/2503.09283) — `denoising`
- [Noise2Score3D:Unsupervised Tweedie's Approach for Point Cloud Denoising](https://arxiv.org/abs/2502.16826) — `denoising`
- [NoKSR: Kernel-Free Neural Surface Reconstruction via Point Cloud Serialization](https://arxiv.org/abs/2502.12534) — `reconstruction`
- [Non-uniform Point Cloud Upsampling via Local Manifold Distribution](https://arxiv.org/abs/2504.11701) — `upsampling`
- [NoPain: No-box Point Cloud Attack via Optimal Transport Singular Boundary](https://arxiv.org/abs/2503.00063)
- [NormalView: tree species classification from backpack and aerial lidar data using geometric projections](https://arxiv.org/abs/2512.05610) — `classification`
- [Not-So-Optimal Transport Flows for 3D Point Cloud Generation](https://arxiv.org/abs/2502.12456) — `generation`
- [NUC-Net: Non-uniform Cylindrical Partition Network for Efficient LiDAR Semantic Segmentation](https://arxiv.org/abs/2505.24634) — `segmentation` `autonomous driving` `efficiency` — [code](https://github.com/alanWXZ/NUC-Net)
- [Object Pose Distribution Estimation for Determining Revolution and Reflection Uncertainty in Point Clouds](https://arxiv.org/abs/2512.07211)
- [OCCDiff: Occupancy Diffusion Model for High-Fidelity 3D Building Reconstruction from Noisy Point Clouds](https://arxiv.org/abs/2512.08506) — `generation` `reconstruction`
- [OG-PCL: Efficient Sparse Point Cloud Processing for Human Activity Recognition](https://arxiv.org/abs/2511.08910) — `efficiency`
- [OmniJet-$α_C$: Learning point cloud calorimeter simulations using generative transformers](https://arxiv.org/abs/2501.05534) — `detection` `generation`
- [OmniPlantSeg: Species Agnostic 3D Point Cloud Organ Segmentation for High-Resolution Plant Phenotyping Across Modalities](https://arxiv.org/abs/2509.21038) — `segmentation`
- [On the Impact of LiDAR Point Cloud Compression on Remote Semantic Segmentation](https://arxiv.org/abs/2509.23341) — `segmentation` `detection` `compression`
- [On-the-Fly Object-aware Representative Point Selection in Point Cloud](https://arxiv.org/abs/2508.01980)
- [Open-Set Gait Recognition from Sparse mmWave Radar Point Clouds](https://arxiv.org/abs/2503.07435) — `multi-modal`
- [Open-source automatic pipeline for efficient conversion of large-scale point clouds to IFC format](https://arxiv.org/abs/2503.11498) — `reconstruction` `efficiency`
- [Open-world Point Cloud Semantic Segmentation: A Human-in-the-loop Framework](https://arxiv.org/abs/2508.04962) — `segmentation`
- [OpenLiDARMap: Zero-Drift Point Cloud Mapping using Map Priors](https://arxiv.org/abs/2501.11111) — `slam` `localization`
- [OpenUrban3D: Annotation-Free Open-Vocabulary Semantic Segmentation of Large-Scale Urban Point Clouds](https://arxiv.org/abs/2509.10842) — `segmentation` `open-vocabulary`
- [OT-MeanFlow3D: Bridging Optimal Transport and Meanflow for Efficient 3D Point Cloud Generation](https://arxiv.org/abs/2509.22592) — `generation` `efficiency`
- [Out-of-Distribution Detection in LiDAR Semantic Segmentation Using Epistemic Uncertainty from Hierarchical GMMs](https://arxiv.org/abs/2510.08631) — `segmentation` `detection`
- [Panoptic-CUDAL: Rural Australia Point Cloud Dataset in Rainy Conditions](https://arxiv.org/abs/2503.16378) — `segmentation` `autonomous driving` `dataset`
- [ParticleFormer: A 3D Point Cloud World Model for Multi-Object, Multi-Material Robotic Manipulation](https://arxiv.org/abs/2506.23126)
- [Path Planning on Multi-level Point Cloud with a Weighted Traversability Graph](https://arxiv.org/abs/2504.21622)
- [PCE-GAN: A Generative Adversarial Network for Point Cloud Attribute Quality Enhancement based on Optimal Transport](https://arxiv.org/abs/2503.00047) — `generation` `reconstruction` `compression` `robustness`
- [PCR-ORB: Enhanced ORB-SLAM3 with Point Cloud Refinement Using Deep Learning-Based Dynamic Object Filtering](https://arxiv.org/abs/2512.23318) — `tracking` `localization`
- [Physically-Based Mesh Generation for Confined 3D Point Clouds Using Flexible Foil Models](https://arxiv.org/abs/2502.06541) — `generation`
- [Physics-Driven Local-Whole Elastic Deformation Modeling for Point Cloud Representation Learning](https://arxiv.org/abs/2505.13812)
- [PI3DETR: Parametric Instance Detection of 3D Point Cloud Edges With a Geometry-Aware 3DETR](https://arxiv.org/abs/2509.03262) — `detection`
- [Pillar-Voxel Fusion Network for 3D Object Detection in Airborne Hyperspectral Point Clouds](https://arxiv.org/abs/2504.09506) — `detection`
- [PillarMamba: Learning Local-Global Context for Roadside Point Cloud via Hybrid State Space Model](https://arxiv.org/abs/2505.05397) — `detection`
- [Pipe Reconstruction from Point Cloud Data](https://arxiv.org/abs/2506.22118) — `reconstruction`
- [PIT-QMM: A Large Multimodal Model For No-Reference Point Cloud Quality Assessment](https://arxiv.org/abs/2510.07636) — `multi-modal`
- [Planning from Point Clouds over Continuous Actions for Multi-object Rearrangement](https://arxiv.org/abs/2509.04645)
- [PlantSegNeRF: A few-shot, cross-species method for plant 3D instance point cloud reconstruction via joint-channel NeRF with multi-view image instance matching](https://arxiv.org/abs/2507.00371) — `segmentation` `reconstruction` `nerf`
- [POD: Predictive Object Detection with Single-Frame FMCW LiDAR Point Cloud](https://arxiv.org/abs/2504.05649) — `detection` `autonomous driving`
- [Point Cloud Based Scene Segmentation: A Survey](https://arxiv.org/abs/2503.12595) — `segmentation` `detection` `autonomous driving`
- [Point Cloud Compression and Objective Quality Assessment: A Survey](https://arxiv.org/abs/2506.22902) — `compression` `autonomous driving`
- [Point Cloud Geometry Scalable Coding Using a Resolution and Quality-conditioned Latents Probability Estimator](https://arxiv.org/abs/2502.14099)
- [Point Cloud Objective Quality: Benchmarking Features and Quality Evaluation](https://arxiv.org/abs/2504.03381)
- [Point Cloud Quality Assessment Using the Perceptual Clustering Weighted Graph (PCW-Graph) and Attention Fusion Network](https://arxiv.org/abs/2506.04081)
- [Point Cloud Recombination: Systematic Real Data Augmentation Using Robotic Targets for LiDAR Perception Validation](https://arxiv.org/abs/2505.02476) — `generation`
- [Point cloud segmentation for 3D Clothed Human Layering](https://arxiv.org/abs/2508.05531) — `segmentation` `generation`
- [Point Cloud Segmentation of Agricultural Vehicles using 3D Gaussian Splatting](https://arxiv.org/abs/2506.05009) — `segmentation` `gaussian-splatting`
- [Point Cloud Segmentation of Integrated Circuits Package Substrates Surface Defects Using Causal Inference: Dataset Construction and Methodology](https://arxiv.org/abs/2511.05853) — `segmentation` `detection` `dataset`
- [Point Cloud-Based Control Barrier Functions for Model Predictive Control in Safety-Critical Navigation of Autonomous Mobile Robots](https://arxiv.org/abs/2510.02885) — `tracking`
- [Point Cloud-based Grasping for Soft Hand Exoskeleton](https://arxiv.org/abs/2504.03369)
- [Point-level Uncertainty Evaluation of Mobile Laser Scanning Point Clouds](https://arxiv.org/abs/2510.24773)
- [Point-LN: A Lightweight Framework for Efficient Point Cloud Classification Using Non-Parametric Positional Encoding](https://arxiv.org/abs/2501.14238) — `classification` `efficiency`
- [Point-Plane Projections for Accurate LiDAR Semantic Segmentation in Small Data Scenarios](https://arxiv.org/abs/2509.10841) — `segmentation` `autonomous driving`
- [Point-RTD: Replaced Token Denoising for Pretraining Transformer Models on Point Clouds](https://arxiv.org/abs/2509.17207) — `reconstruction` `denoising` `pre-training`
- [Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction](https://arxiv.org/abs/2505.02043) — `reconstruction`
- [Point2Quad: Generating Quad Meshes from Point Clouds via Face Prediction](https://arxiv.org/abs/2504.19545) — `generation`
- [PointCubeNet: 3D Part-level Reasoning with 3x3x3 Point Cloud Blocks](https://arxiv.org/abs/2511.06744)
- [PointDGRWKV: Generalizing RWKV-like Architecture to Unseen Domains for Point Cloud Classification](https://arxiv.org/abs/2508.20835) — `classification`
- [PointDiffuse: A Dual-Conditional Diffusion Model for Enhanced Point Cloud Semantic Segmentation](https://arxiv.org/abs/2503.06094) — `segmentation` `generation` `denoising`
- [PointGauss: Point Cloud-Guided Multi-Object Segmentation for Gaussian Splatting](https://arxiv.org/abs/2508.00259) — `segmentation` `gaussian-splatting`
- [PointLAMA: Latent Attention meets Mamba for Efficient Point Cloud Pretraining](https://arxiv.org/abs/2507.17296) — `pre-training` `efficiency`
- [PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning](https://arxiv.org/abs/2510.20406) — `multi-modal`
- [PointNet4D: A Lightweight 4D Point Cloud Video Backbone for Online and Offline Perception in Robotic Applications](https://arxiv.org/abs/2512.01383) — `efficiency`
- [PointNSP: Autoregressive 3D Point Cloud Generation with Next-Scale Level-of-Detail Prediction](https://arxiv.org/abs/2510.05613) — `generation`
- [PointODE: Lightweight Point Cloud Learning with Neural Ordinary Differential Equations on Edge](https://arxiv.org/abs/2506.00438) — `efficiency`
- [PointRAFT: 3D deep learning for high-throughput prediction of potato tuber weight from partial point clouds](https://arxiv.org/abs/2512.24193)
- [PointSFDA: Source-free Domain Adaptation for Point Cloud Completion](https://arxiv.org/abs/2503.15144) — `completion` `domain adaptation`
- [PointVDP: Learning View-Dependent Projection by Fireworks Rays for 3D Point Cloud Segmentation](https://arxiv.org/abs/2507.06618) — `segmentation`
- [Pole-Image: A Self-Supervised Pole-Anchored Descriptor for Long-Term LiDAR Localization and Map Maintenance](https://arxiv.org/abs/2510.17237) — `detection` `localization` `self-supervised`
- [Position: Untrained Machine Learning for Anomaly Detection by using 3D Point Cloud Data](https://arxiv.org/abs/2502.03876) — `detection` `anomaly detection`
- [Pre-training with 3D Synthetic Data: Learning 3D Point Cloud Instance Segmentation from 3D Synthetic Scenes](https://arxiv.org/abs/2503.24229) — `segmentation` `pre-training`
- [Procedural Generation of 3D Maize Plant Architecture from LIDAR Data](https://arxiv.org/abs/2501.13963) — `generation`
- [ProDAT: Progressive Density-Aware Tail-Drop for Point Cloud Coding](https://arxiv.org/abs/2510.17068) — `autonomous driving`
- [ProtoGuard-guided PROPEL: Class-Aware Prototype Enhancement and Progressive Labeling for Incremental 3D Point Cloud Segmentation](https://arxiv.org/abs/2504.01648) — `segmentation`
- [PSA-SSL: Pose and Size-aware Self-Supervised Learning on LiDAR Point Clouds](https://arxiv.org/abs/2503.13914) — `localization` `self-supervised`
- [PUFM++: Point Cloud Upsampling via Enhanced Flow Matching](https://arxiv.org/abs/2512.20988) — `generation` `reconstruction` `upsampling`
- [Purge-Gate: Backpropagation-Free Test-Time Adaptation for Point Clouds Classification via Token Purging](https://arxiv.org/abs/2509.09785) — `classification`
- [PVINet: Point-Voxel Interlaced Network for Point Cloud Compression](https://arxiv.org/abs/2509.01097) — `compression`
- [PVNet: Point-Voxel Interaction LiDAR Scene Upsampling Via Diffusion Models](https://arxiv.org/abs/2508.17050) — `upsampling`
- [QLIO: Quantized LiDAR-Inertial Odometry](https://arxiv.org/abs/2503.07949) — `efficiency`
- [Quality-controlled registration of urban MLS point clouds reducing drift effects by adaptive fragmentation](https://arxiv.org/abs/2510.23416) — `registration`
- [Query-aware Hub Prototype Learning for Few-Shot 3D Point Cloud Semantic Segmentation](https://arxiv.org/abs/2512.08253) — `segmentation`
- [Querying Autonomous Vehicle Point Clouds: Enhanced by 3D Object Counting with CounterNet](https://arxiv.org/abs/2507.19209) — `detection`
- [QuickGrasp: Lightweight Antipodal Grasp Planning with Point Clouds](https://arxiv.org/abs/2504.19716) — `efficiency`
- [RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion](https://arxiv.org/abs/2511.07067) — `multi-modal`
- [Range Image-Based Implicit Neural Compression for LiDAR Point Clouds](https://arxiv.org/abs/2504.17229) — `detection` `compression`
- [Range-Edit: Semantic Mask Guided Outdoor LiDAR Scene Editing](https://arxiv.org/abs/2511.17269) — `autonomous driving`
- [RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation](https://arxiv.org/abs/2509.15886) — `segmentation` `autonomous driving`
- [RARE: Refine Any Registration of Pairwise Point Clouds via Zero-Shot Learning](https://arxiv.org/abs/2507.19950) — `registration` `open-vocabulary`
- [rareboost3d: a synthetic lidar dataset with enhanced rare classes](https://arxiv.org/abs/2510.10876) — `segmentation` `autonomous driving` `dataset`
- [Rate-distortion Optimized Point Cloud Preprocessing for Geometry-based Point Cloud Compression](https://arxiv.org/abs/2508.01633) — `compression`
- [RBFIM: Perceptual Quality Assessment for Compressed Point Clouds Using Radial Basis Function Interpolation](https://arxiv.org/abs/2503.14154) — `compression`
- [Re-Densification Meets Cross-Scale Propagation: Real-Time Neural Compression of LiDAR Point Clouds](https://arxiv.org/abs/2508.20466) — `compression` `efficiency`
- [Real-time Neural Rendering of LiDAR Point Clouds](https://arxiv.org/abs/2502.11618) — `efficiency`
- [Real-time Point Cloud Data Transmission via L4S for 5G-Edge-Assisted Robotics](https://arxiv.org/abs/2511.15677) — `detection` `efficiency`
- [Redefining Radar Segmentation: Simultaneous Static-Moving Segmentation and Ego-Motion Estimation using Radar Point Clouds](https://arxiv.org/abs/2511.20003) — `segmentation` `multi-modal`
- [RefComp: A Reference-guided Unified Framework for Unpaired Point Cloud Completion](https://arxiv.org/abs/2504.13788) — `completion`
- [Reflectance Prediction-based Knowledge Distillation for Robust 3D Object Detection in Compressed Point Clouds](https://arxiv.org/abs/2505.17442) — `detection` `compression` `robustness`
- [Register Any Point: Scaling 3D Point Cloud Registration by Flow Matching](https://arxiv.org/abs/2512.01850) — `registration` `localization` `generation` `reconstruction`
- [Registering the 4D Millimeter Wave Radar Point Clouds Via Generalized Method of Moments](https://arxiv.org/abs/2508.02187) — `registration` `multi-modal`
- [Registration-Free Monitoring of Unstructured Point Cloud Data via Intrinsic Geometrical Properties](https://arxiv.org/abs/2511.05623) — `registration` — [code](https://github.com/franci2312/RFM)
- [REHEARSE-3D: A Multi-modal Emulated Rain Dataset for 3D Point Cloud De-raining](https://arxiv.org/abs/2504.21699) — `autonomous driving` `multi-modal` `dataset`
- [Relative Energy Learning for LiDAR Out-of-Distribution Detection](https://arxiv.org/abs/2511.06720) — `detection` `autonomous driving` — [code](https://github.com/343gltysprk/rel)
- [RENO: Real-Time Neural Compression for 3D LiDAR Point Clouds](https://arxiv.org/abs/2503.12382) — `compression` `efficiency`
- [Representation Learning for Point Cloud Understanding](https://arxiv.org/abs/2512.06058)
- [Representation Learning of Point Cloud Upsampling in Global and Local Inputs](https://arxiv.org/abs/2501.07076) — `reconstruction` `upsampling`
- [Rethinking Gradient-based Adversarial Attacks on Point Cloud Classification](https://arxiv.org/abs/2505.21854) — `classification` `robustness`
- [Rethinking the Detail-Preserved Completion of Complex Tubular Structures based on Point Cloud: a Dataset and a Benchmark](https://arxiv.org/abs/2508.17658) — `segmentation` `detection` `completion` `dataset`
- [Rethinking the Encoding and Annotating of 3D Bounding Box: Corner-Aware 3D Object Detection from Point Clouds](https://arxiv.org/abs/2511.17619) — `detection` `BEV`
- [Revisiting Depth Representations for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2506.05327) — `gaussian-splatting`
- [Revisiting Physically Realizable Adversarial Object Attack against LiDAR-based Detection: Clarifying Problem Formulation and Experimental Protocols](https://arxiv.org/abs/2507.18457) — `detection` `robustness`
- [RL-AD-Net: Reinforcement Learning Guided Adaptive Displacement in Latent Space for Refined Point Cloud Completion](https://arxiv.org/abs/2511.17054) — `completion` `denoising`
- [Robust Human Registration with Body Part Segmentation on Noisy Point Clouds](https://arxiv.org/abs/2504.03602) — `registration` `segmentation` `robustness`
- [Robust Partial 3D Point Cloud Registration via Confidence Estimation under Global Context](https://arxiv.org/abs/2509.24275) — `registration` `robustness`
- [Robust Point Cloud Reinforcement Learning via PCA-Based Canonicalization](https://arxiv.org/abs/2510.20974) — `robustness`
- [Robust Single Object Tracking in LiDAR Point Clouds under Adverse Weather Conditions](https://arxiv.org/abs/2501.07133) — `tracking` `robustness`
- [Robust Unsupervised Domain Adaptation for 3D Point Cloud Segmentation Under Source Adversarial Attacks](https://arxiv.org/abs/2504.01659) — `segmentation` `generation` `domain adaptation` `robustness`
- [ROI-Guided Point Cloud Geometry Compression Towards Human and Machine Vision](https://arxiv.org/abs/2504.14240) — `compression` `autonomous driving`
- [RW-Net: Enhancing Few-Shot Point Cloud Classification with a Wavelet Transform Projection-based Network](https://arxiv.org/abs/2501.03221) — `classification`
- [SALT: A Flexible Semi-Automatic Labeling Tool for General LiDAR Point Clouds with Cross-Scene Adaptability and 4D Consistency](https://arxiv.org/abs/2503.23980) — `segmentation` `open-vocabulary`
- [SAMBLE: Shape-Specific Point Cloud Sampling for an Optimal Trade-Off Between Local Detail and Global Uniformity](https://arxiv.org/abs/2504.19581)
- [SASep: Saliency-Aware Structured Separation of Geometry and Feature for Open Set Learning on Point Clouds](https://arxiv.org/abs/2506.13224)
- [SC-NeRF: NeRF-based Point Cloud Reconstruction using a Stationary Camera for Agricultural Applications](https://arxiv.org/abs/2503.21958) — `reconstruction` `nerf`
- [SDFs from Unoriented Point Clouds using Neural Variational Heat Distances](https://arxiv.org/abs/2504.11212)
- [SEDD-PCC: A Single Encoder-Dual Decoder Framework For End-To-End Learned Point Cloud Compression](https://arxiv.org/abs/2505.16709) — `compression`
- [SELECT: A Submodular Approach for Active LiDAR Semantic Segmentation](https://arxiv.org/abs/2505.11516) — `segmentation` `autonomous driving`
- [Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration](https://arxiv.org/abs/2509.15882) — `registration` `self-supervised`
- [Self-Supervised Moving Object Segmentation of Sparse and Noisy Radar Point Clouds](https://arxiv.org/abs/2511.02395) — `segmentation` `slam` `self-supervised` `autonomous driving`
- [Self-Supervised Point Cloud Completion based on Multi-View Augmentations of Single Partial Point Cloud](https://arxiv.org/abs/2509.22132) — `completion` `self-supervised`
- [SemICP: Semantic Non-Rigid Point Cloud Registration with Elastic Energy Regularization](https://arxiv.org/abs/2503.00972) — `registration`
- [Separability Membrane: 3D Active Contour for Point Cloud Surface Reconstruction](https://arxiv.org/abs/2503.05217) — `reconstruction`
- [SG-LDM: Semantic-Guided LiDAR Generation via Latent-Aligned Diffusion](https://arxiv.org/abs/2506.23606) — `generation`
- [SHIELD: Spherical-Projection Hybrid-Frontier Integration for Efficient LiDAR-based Drone Exploration](https://arxiv.org/abs/2512.23972) — `efficiency`
- [Shortest-Path Decomposition for Foliage-Robust 3D Tree Modeling and Above-Ground Biomass Estimation from Point Clouds](https://arxiv.org/abs/2506.15577) — `robustness`
- [SIM-Net: A Multimodal Fusion Network Using Inferred 3D Object Shape Point Clouds from RGB Images for 2D Classification](https://arxiv.org/abs/2506.18683) — `classification` `multi-modal`
- [Simulation-Based Performance Evaluation of 3D Object Detection Methods with Deep Learning for a LiDAR Point Cloud Dataset in a SOTIF-related Use Case](https://arxiv.org/abs/2503.03548) — `detection` `dataset`
- [Skeleton-based Robust Registration Framework for Corrupted 3D Point Clouds](https://arxiv.org/abs/2509.24273) — `registration` `reconstruction` `autonomous driving` `robustness`
- [Skeletonization Quality Evaluation: Geometric Metrics for Point Cloud Analysis in Robotics](https://arxiv.org/abs/2504.00032)
- [SkinningGS: Editable Dynamic Human Scene Reconstruction Using Gaussian Splatting Based on a Skinning Model](https://arxiv.org/abs/2506.21632) — `reconstruction` `gaussian-splatting` `monocular`
- [SM3D: Mitigating Spectral Bias and Semantic Dilution in Point Cloud State Space Models](https://arxiv.org/abs/2505.11099)
- [SMART-PC: Skeletal Model Adaptation for Robust Test-Time Training in Point Clouds](https://arxiv.org/abs/2505.19546) — `classification` `robustness`
- [SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis](https://arxiv.org/abs/2504.08361) — `segmentation` `autonomous driving`
- [SNAP: Towards Segmenting Anything in Any Point Cloud](https://arxiv.org/abs/2510.11565) — `segmentation`
- [SODA: Out-of-Distribution Detection in Domain-Shifted Point Clouds via Neighborhood Propagation](https://arxiv.org/abs/2506.21892) — `detection`
- [Sparse2DGS: Sparse-View Surface Reconstruction using 2D Gaussian Splatting with Dense Point Cloud](https://arxiv.org/abs/2505.19854) — `reconstruction` `gaussian-splatting`
- [Spectral Informed Mamba for Robust Point Cloud Processing](https://arxiv.org/abs/2503.04953) — `self-supervised` `robustness`
- [Spira: Exploiting Voxel Data Structural Properties for Efficient Sparse Convolution in Point Cloud Networks](https://arxiv.org/abs/2511.20834) — `autonomous driving` `efficiency`
- [Splatblox: Traversability-Aware Gaussian Splatting for Outdoor Robot Navigation](https://arxiv.org/abs/2511.18525) — `gaussian-splatting`
- [SPPSFormer: High-quality Superpoint-based Transformer for Roof Plane Instance Segmentation from Point Clouds](https://arxiv.org/abs/2505.24475) — `segmentation`
- [SPU-IMR: Self-supervised Arbitrary-scale Point Cloud Upsampling via Iterative Mask-recovery Network](https://arxiv.org/abs/2502.19452) — `self-supervised` `upsampling`
- [SRKD: Towards Efficient 3D Point Cloud Segmentation via Structure- and Relation-aware Knowledge Distillation](https://arxiv.org/abs/2506.17290) — `segmentation` `efficiency`
- [SRMamba: Mamba for Super-Resolution of LiDAR Point Clouds](https://arxiv.org/abs/2505.10601) — `upsampling`
- [SRMambaV2: Biomimetic Attention for Sparse Point Cloud Upsampling in Autonomous Driving](https://arxiv.org/abs/2507.17479) — `upsampling` `autonomous driving`
- [SSCATeR: Sparse Scatter-Based Convolution Algorithm with Temporal Data Recycling for Real-Time 3D Object Detection in LiDAR Point Clouds](https://arxiv.org/abs/2512.08557) — `detection` `efficiency`
- [Stealthy Patch-Wise Backdoor Attack in 3D Point Cloud via Curvature Awareness](https://arxiv.org/abs/2503.09336)
- [STONE: Pioneering the One-to-N Universal Backdoor Threat in 3D Point Cloud](https://arxiv.org/abs/2511.11210) — `autonomous driving`
- [STQE: Spatial-Temporal Attribute Quality Enhancement for G-PCC Compressed Dynamic Point Clouds](https://arxiv.org/abs/2507.17522) — `compression`
- [StripDet: Strip Attention-Based Lightweight 3D Object Detection from Point Cloud](https://arxiv.org/abs/2509.05954) — `detection` `efficiency`
- [StrucADT: Generating Structure-controlled 3D Point Clouds with Adjacency Diffusion Transformer](https://arxiv.org/abs/2509.23709) — `generation`
- [SuperiorGAT: Graph Attention Networks for Sparse LiDAR Point Cloud Reconstruction in Autonomous Systems](https://arxiv.org/abs/2512.22439) — `reconstruction`
- [SurfFill: Completion of LiDAR Point Clouds via Gaussian Surfel Splatting](https://arxiv.org/abs/2512.03010) — `completion` `reconstruction`
- [Symmetria: A Synthetic Dataset for Learning in Point Clouds](https://arxiv.org/abs/2510.23414) — `dataset`
- [Talk2PC: Enhancing 3D Visual Grounding through LiDAR and Radar Point Clouds Fusion for Autonomous Driving](https://arxiv.org/abs/2503.08336) — `autonomous driving` `multi-modal`
- [Targetless 6DoF Calibration of LiDAR and 2D Scanning Radar Based on Cylindrical Occupancy](https://arxiv.org/abs/2503.17002) — `multi-modal`
- [Teleoperated Driving: a New Challenge for 3D Object Detection in Compressed Point Clouds](https://arxiv.org/abs/2506.11804) — `detection` `compression`
- [Terrain-Aided Navigation Without Raycasting: A Sliding Grid Approach for Point Cloud Processing](https://arxiv.org/abs/2510.06470)
- [TeSO: Representing and Compressing 3D Point Cloud Scenes with Textured Surfel Octree](https://arxiv.org/abs/2508.07083) — `compression`
- [TexLiDAR: Automated Text Understanding for Panoramic LiDAR Data](https://arxiv.org/abs/2502.04385)
- [TFDM: Time-Variant Frequency-Based Point Cloud Diffusion with Mamba](https://arxiv.org/abs/2503.13004) — `generation`
- [The Impact of 2D Segmentation Backbones on Point Cloud Predictions Using 4D Radar](https://arxiv.org/abs/2509.19644) — `segmentation` `autonomous driving` `multi-modal`
- [The Point, the Vision and the Text: Does Point Cloud Boost Spatial Reasoning of Large Language Models? A Bias-Controlled Study](https://arxiv.org/abs/2504.04540)
- [The Worse The Better: Content-Aware Viewpoint Generation Network for Projection-related Point Cloud Quality Assessment](https://arxiv.org/abs/2502.11710) — `generation`
- [Three-dimentional reconstruction of complex, dynamic population canopy architecture for crops with a novel point cloud completion model: A case study in Brassica napus rapeseed](https://arxiv.org/abs/2506.18292) — `completion` `reconstruction`
- [Through the Perspective of LiDAR: A Feature-Enriched and Uncertainty-Aware Annotation Pipeline for Terrestrial Point Cloud Segmentation](https://arxiv.org/abs/2510.06582) — `segmentation`
- [Tightly Coupled Range Inertial Odometry and Mapping with Exact Point Cloud Downsampling](https://arxiv.org/abs/2505.01017) — `registration`
- [Tiny LiDARs for Manipulator Self-Awareness: Sensor Characterization and Initial Localization Experiments](https://arxiv.org/abs/2503.03449) — `localization`
- [Token Adaptation via Side Graph Convolution for Efficient Fine-tuning of 3D Point Cloud Transformers](https://arxiv.org/abs/2502.14142) — `efficiency`
- [TopoDiT-3D: Topology-Aware Diffusion Transformer with Bottleneck Structure for 3D Point Cloud Generation](https://arxiv.org/abs/2505.09140) — `generation`
- [Topology-Aware Modeling for Unsupervised Simulation-to-Reality Point Cloud Recognition](https://arxiv.org/abs/2506.21165)
- [Topology-Guided Knowledge Distillation for Efficient Point Cloud Processing](https://arxiv.org/abs/2505.08101) — `autonomous driving` `efficiency`
- [TopoRec: Point Cloud Recognition Using Topological Data Analysis](https://arxiv.org/abs/2506.18725) — `localization` `reconstruction` `autonomous driving`
- [Toward Patient-specific Partial Point Cloud to Surface Completion for Pre- to Intra-operative Registration in Image-guided Liver Interventions](https://arxiv.org/abs/2505.19518) — `registration` `completion`
- [Toward Scalable, Flexible Scene Flow for Point Clouds](https://arxiv.org/abs/2503.15666) — `scene flow`
- [Toward Using Machine Learning as a Shape Quality Metric for Liver Point Cloud Generation](https://arxiv.org/abs/2508.02482) — `generation`
- [Towards Explicit Geometry-Reflectance Collaboration for Generalized LiDAR Segmentation in Adverse Weather](https://arxiv.org/abs/2506.02396) — `segmentation`
- [Towards Fusing Point Cloud and Visual Representations for Imitation Learning](https://arxiv.org/abs/2502.12320)
- [Towards Training-Free Underwater 3D Object Detection from Sonar Point Clouds: A Comparison of Traditional and Deep Learning Approaches](https://arxiv.org/abs/2508.18293) — `detection`
- [TrackAny3D: Transferring Pretrained 3D Models for Category-unified 3D Point Cloud Tracking](https://arxiv.org/abs/2507.19908) — `tracking` `pre-training`
- [Training-Free Global Geometric Association for 4D LiDAR Panoptic Segmentation](https://arxiv.org/abs/2512.18991) — `segmentation`
- [Transferable and Undefendable Point Cloud Attacks via Medial Axis Transform](https://arxiv.org/abs/2507.18870)
- [Transferable Foundation Models for Geometric Tasks on Point Cloud Representations: Geometric Neural Operators](https://arxiv.org/abs/2503.04649)
- [Transmit Weights, Not Features: Orthogonal-Basis Aided Wireless Point-Cloud Transmission](https://arxiv.org/abs/2512.03819)
- [treeX: Unsupervised Tree Instance Segmentation in Dense Forest Point Clouds](https://arxiv.org/abs/2509.03633) — `segmentation`
- [Turin3D: Evaluating Adaptation Strategies under Label Scarcity in Urban LiDAR Segmentation with Semi-Supervised Techniques](https://arxiv.org/abs/2504.05882) — `segmentation`
- [UAV Position Estimation using a LiDAR-based 3D Object Detection Method](https://arxiv.org/abs/2504.07028) — `detection`
- [UGAE: Unified Geometry and Attribute Enhancement for G-PCC Compressed Point Clouds](https://arxiv.org/abs/2510.23009) — `compression`
- [UMIGen: A Unified Framework for Egocentric Point Cloud Generation and Cross-Embodiment Robotic Imitation Learning](https://arxiv.org/abs/2511.09302) — `generation`
- [Uni-Mapper: Unified Mapping Framework for Multi-modal LiDARs in Complex and Dynamic Environments](https://arxiv.org/abs/2507.20538) — `multi-modal`
- [Uni4D: A Unified Self-Supervised Learning Framework for Point Cloud Videos](https://arxiv.org/abs/2504.04837) — `self-supervised`
- [Unified Geometry and Color Compression Framework for Point Clouds via Generative Diffusion Priors](https://arxiv.org/abs/2503.18083) — `generation` `compression`
- [UniLGL: Learning Uniform Place Recognition for FOV-limited/Panoramic LiDAR Global Localization](https://arxiv.org/abs/2507.12194) — `localization`
- [Unlocking Hidden Potential in Point Cloud Networks with Attention-Guided Grouping-Feature Coordination](https://arxiv.org/abs/2509.16639)
- [Unposed 3DGS Reconstruction with Probabilistic Procrustes Mapping](https://arxiv.org/abs/2507.18541) — `reconstruction` `gaussian-splatting`
- [Unsupervised Learning for Feature Extraction and Temporal Alignment of 3D+t Point Clouds of Zebrafish Embryos](https://arxiv.org/abs/2502.06543)
- [Unsupervised Radar Point Cloud Enhancement via Arbitrary LiDAR Guided Diffusion Prior](https://arxiv.org/abs/2505.09887) — `multi-modal`
- [UVG-VPC: Voxelized Point Cloud Dataset for Visual Volumetric Video-based Coding](https://arxiv.org/abs/2504.05888) — `compression` `dataset`
- [VAD-GS: Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic Urban Scenes](https://arxiv.org/abs/2510.09364) — `gaussian-splatting`
- [Vehicle-Scene Interaction: A Text-Driven 3D Lidar Place Recognition Method for Autonomous Driving](https://arxiv.org/abs/2503.18035) — `localization` `autonomous driving`
- [ViewPCL: a point cloud based active learning method for multi-view segmentation](https://arxiv.org/abs/2506.13043) — `segmentation`
- [Visualization of a multidimensional point cloud as a 3D swarm of avatars](https://arxiv.org/abs/2504.06751)
- [Visualizing Spatial Point Clouds: A Task-Oriented Taxonomy](https://arxiv.org/abs/2510.02651)
- [Voxel-based Point Cloud Geometry Compression with Space-to-Channel Context](https://arxiv.org/abs/2503.18283) — `compression`
- [Warm-Starting Optimization-Based Motion Planning for Robotic Manipulators via Point Cloud-Conditioned Flow Matching](https://arxiv.org/abs/2510.03460) — `generation`
- [Wavelet-based Global Orientation and Surface Reconstruction for Point Clouds](https://arxiv.org/abs/2506.16299) — `reconstruction`
- [Weakly-Supervised Learning for Tree Instances Segmentation in Airborne Lidar Point Clouds](https://arxiv.org/abs/2508.15646) — `segmentation`
- [WeatherGen: A Unified Diverse Weather Generator for LiDAR Point Clouds via Spider Mamba Diffusion](https://arxiv.org/abs/2504.13561) — `generation`
- [Which LiDAR scanning pattern is better for roadside perception: Repetitive or Non-repetitive?](https://arxiv.org/abs/2511.00060)
- [WLTCL: Wide Field-of-View 3-D LiDAR Truck Compartment Automatic Localization System](https://arxiv.org/abs/2504.18870) — `localization`
- [XAI for Point Cloud Data using Perturbations based on Meaningful Segmentation](https://arxiv.org/abs/2507.22020) — `segmentation` `classification`
- [ZigzagPointMamba: Spatial-Semantic Mamba for Point Cloud Understanding](https://arxiv.org/abs/2505.21381) — `self-supervised`

</details>


### 2024 <sub>(838)</sub>

→ [查看 2024 年完整列表](docs/year/2024.md)

### 2023 <sub>(799)</sub>

→ [查看 2023 年完整列表](docs/year/2023.md)

### 2022 <sub>(689)</sub>

→ [查看 2022 年完整列表](docs/year/2022.md)

### 2021 <sub>(536)</sub>

→ [查看 2021 年完整列表](docs/year/2021.md)

---

### 更早年份 / Earlier years

[2024](docs/year/2024.md) | [2023](docs/year/2023.md) | [2022](docs/year/2022.md) | [2021](docs/year/2021.md)

## 说明 / Notes

- 共 **4338** 篇（2021 年至今），其中 **242** 篇附带代码链接；年份为会议年份，纯 arXiv 为首次提交年份。
- 收录范围：点云相关（检测、分割、配准、补全、分类、跟踪、SLAM、生成、压缩、预训练等），不限于单一子方向。
- 2021 年前的经典工作未收录；数据集见 [DATASETS.md](DATASETS.md)（不受年份限制）。
- 每日自动同步：[`.github/workflows/arxiv-sync.yml`](.github/workflows/arxiv-sync.yml)。
- 灵感与对照：[zhulf0804/3D-PointCloud](https://github.com/zhulf0804/3D-PointCloud)（2024-08 起停更）。

## License

内容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 发布，脚本以 MIT 发布。
