# 贡献指南 / Contributing

感谢你愿意补充这个列表！整个流程被设计成**改一个 JSON 文件**就够了。

## 最快的贡献方式：只加一条

```bash
# 只需 arXiv id（或整条 URL），元数据、会议、标签会自动抓取
python scripts/add.py 2312.10035

# 顺便把代码链接和标签也带上
python scripts/add.py 2312.10035 \
  --code https://github.com/pointcept/pointtransformerv3 \
  --tags segmentation detection
```

脚本会：抓 arXiv 元数据 → 从 arXiv comment 里识别会议 → 自动打标签 → 去重 → 重新生成 `README.md`。

## 手动编辑的方式

打开 [`data/entries.json`](data/entries.json)，加一行（**一条论文一行**，这样 git diff 才干净）：

```json
{"title": "Point Transformer V3: Simpler, Faster, Stronger", "year": 2024, "venue": "CVPR", "arxiv": "2312.10035", "tags": ["segmentation", "detection"], "code": "https://github.com/pointcept/pointtransformerv3", "note": ""}
```

字段说明：

| 字段 | 必填 | 说明 |
|:--|:--:|:--|
| `title` | ✅ | 论文标题，保持 arXiv 原样（不要自行翻译） |
| `year` | ✅ | **会议年份**；纯 arXiv 用首次提交年份 |
| `venue` | ✅ | 会议/期刊简称；没有正式发表就写 `"arXiv"` |
| `arxiv` | | arXiv id，如 `"2312.10035"`（不含 `arXiv:` 前缀和版本号） |
| `url` | | 无 arXiv 时用官方链接（如 `openaccess.thecvf.com`） |
| `code` | | 代码仓库 |
| `project` | | 项目主页 |
| `tags` | | 从 [`data/tags.json`](data/tags.json) 里选，**最多 4 个** |
| `note` | | 可选备注，如 `Oral`、`Best Paper` |

改完本地跑一次：

```bash
python scripts/build.py
```

`README.md` 和 `docs/topics/*.md` 会自动重新生成，**不要手动改这两个地方**。

## 需要新标签？

先在 [`data/tags.json`](data/tags.json) 里加：

```json
{"id": "radar", "name": "4D Radar", "zh": "4D 毫米波雷达"}
```

然后再在条目里使用 `radar`。CI 会检查条目里有没有用到未注册的标签。

## 收录标准

- ✅ 与 3D 点云相关：检测、分割、配准、补全、分类、跟踪、SLAM、定位、生成、重建、压缩、上采样、去噪、法向、场景流、占据预测、预训练等
- ✅ 正式发表（CVPR/ICCV/ECCV/NeurIPS/ICLR/ICML/AAAI/IJCAI/SIGGRAPH/3DV/WACV/BMVC/ICRA/IROS/RA-L/TPAMI/IJCV/T-ITS…）或高质量 arXiv 预印本
- ✅ 2021 年及以后
- ❌ 与点云无关的纯图像/纯网格工作（除非方法直接面向点云）
- ❌ 重复条目（同一工作的 arXiv 版和会议版只保留一条，`year`/`venue` 取正式发表信息）

## 提交前自检

```bash
python scripts/build.py --check     # README 是否与数据同步
python scripts/check_links.py       # 链接是否有效（可选，较慢）
```

## CI 会替你检查什么

| 检查 | 触发条件 | 说明 |
|:--|:--|:--|
| 数据格式 | 每个 PR | 必填字段、年份格式、arXiv id 格式、标签是否已注册 |
| README 同步 | 每个 PR | 忘记跑 `build.py` 会失败，并提示你运行 |
| 死链 | 每周一 | 自动开 issue 提醒 |
| arXiv 增量 | 每天 | 自动开 PR，人工审核后合并 |

## 关于“直接抄别家列表”

请不要整份拷贝其它 awesome 列表。收录范围可以重合，但条目请自己核对——尤其是会议名和年份，二手来源错误率很高。
