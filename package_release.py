"""Package source only. Never include secrets, local databases or dependencies."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
out=root.parent/'outputs/v7'
out.mkdir(parents=True,exist_ok=True)
archive=out/'VBNA_Chapter11_V7_Dang_hoan_thien.zip'
root_docs={'README.md','V7_230_dieu_chinh.md','V7_Ra_soat_va_dieu_kien_golive.md'}
blocked={'.venv','node_modules','__pycache__','private-files','staticfiles','.git'}
allowed_dirs={'src','assets','vendor','tests','server','docs'}
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(root.rglob('*')):
  rel=p.relative_to(root)
  if not p.is_file() or p.is_symlink() or blocked.intersection(rel.parts):continue
  if any(part.startswith('.') for part in rel.parts) and p.name not in {'.env.example','.gitignore'}:continue
  if p.suffix in {'.sqlite3','.db','.pyc','.log','.pem','.key'}:continue
  if p.name.startswith('.env') and p.name!='.env.example':continue
  if len(rel.parts)==1 and not (p.name in root_docs or p.suffix in {'.html','.css','.js'} or p.name in {'build.py','package_release.py','database_schema.sql','.gitignore'}):continue
  if len(rel.parts)>1 and rel.parts[0] not in allowed_dirs:continue
  z.write(p,Path('Website_V7')/rel)
print(archive)
