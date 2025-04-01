# 📂 Organizador de Arquivos em Python

Script para organizar automaticamente arquivos por tipo (imagens, documentos, etc) em subpastas.

## 🚀 Como Usar

### Instalação
```bash
git clone https://github.com/Pedr88/organizador_arquivos
cd organizador_arquivos
```
### Execução

# Organizar pasta Downloads (padrão)
python main.py

# Organizar outra pasta
python main.py --folder "C:\Users\user\Desktop"

# Modo simulação (sem alterar arquivos)
python main.py --dry-run

## ⚙️ Opções
- `--folder` *`caminho`*  
  Pasta a organizar (padrão: `~/Downloads`)
- `--dry-run`  
  Simula sem mover arquivos
- `--log-level` *`nível`*  
  Detalhe do log: `DEBUG`|`INFO`|`WARNING`|`ERROR`

## 📦 Pastas Criadas
- **Imagens**: .jpg, .png, .gif  
- **Documentos**: .pdf, .docx, .txt  
- **Planilhas**: .xlsx, .csv  
- **Compactados**: .zip, .rar  
- *(Lista completa no código)*
