### 📂 File Organizer in Python

Script to automatically organize files by type (images, documents, etc.) into subfolders.

#### 🚀 How to Use

##### Installation

```sh
git clone https://github.com/Pedr88/organizador_arquivos
cd organizador_arquivos
```

##### Execution

To organize the Downloads folder (default):

```sh
python main.py
```

To organize another folder:

```sh
python main.py --folder "C:\Users\user\Desktop"
```

To run in simulation mode (without modifying files):

```sh
python main.py --dry-run
```

#### ⚙️ Options

- `--folder` *`path`*  
  Folder to organize (default: `~/Downloads`)
- `--dry-run`  
  Simulate without moving files
- `--log-level` *`level`*  
  Log detail level: `DEBUG`|`INFO`|`WARNING`|`ERROR`

#### 📦 Created Folders

- **Images**: .jpg, .png, .gif  
- **Documents**: .pdf, .docx, .txt  
- **Spreadsheets**: .xlsx, .csv  
- **Compressed**: .zip, .rar  
- *(Complete list in the code)*
