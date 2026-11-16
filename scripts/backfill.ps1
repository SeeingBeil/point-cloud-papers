$ErrorActionPreference = 'Stop'
$years = @(2021, 2022, 2023, 2024, 2025, 2026)
foreach ($y in $years) {
    $out = "data\raw_$y.json"
    if (Test-Path $out) { "skip $y (exists)"; continue }
    "=== $y ==="
    python scripts\crawl_arxiv.py --out $out --max 1000 --query-set core `
        --date-from "$y-01-01" --date-to "$y-12-31" --sleep 3
}
"done"
