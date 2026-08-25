# dehessen-download
Mapterhorn download scripts for Hessen


```bash
uv run python get_nav.py
mkdir -p source-store/dehessen
# download to source-store/dehessen
uv run python nested_unzip.py
uv run python source_to_cog.py dehessen
uv run python source_set_crs.py dehessen EPSG:25832
uv run python source_bounds.py dehessen
uv run python source_polygonize.py dehessen 32
```