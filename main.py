import os
import shutil
import argparse
import logging
from pathlib import Path
from datetime import datetime

DOWNLOAD_FOLDER = str(Path.home() / "Downloads")
FILE_TYPES = {
    "images": [".jpg", ".png", ".gif", ".jpeg", ".webp"],
    "documents": [".pdf", ".docx", ".txt", ".pptx", ".odt"],
    "spreadsheets": [".xlsx", ".csv", ".ods"],
    "compressed_files": [".zip", ".rar", ".7z", ".tar.gz"],
    "videos": [".mp4", ".mov", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".flac"],
    "apps": [".exe", ".msi", ".dmg"],
    "programming": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "torrents": [".torrent"]
}

class UTF8FileHandler(logging.FileHandler):
    """Handler para arquivos de log com encoding UTF-8"""
    def __init__(self, filename, mode='a', encoding='utf-8', delay=False):
        super().__init__(filename, mode, encoding, delay)

def setup_logging():
    """Configura o sistema de logging"""
    log_file = Path(__file__).parent / "file_organizer.log"
    
    logging.getLogger().handlers.clear()
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            UTF8FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def organize_files(target_folder: str, dry_run: bool = False):
    """
    Organiza arquivos por extensão nas pastas correspondentes
    
    Args:
        target_folder: Pasta a ser organizada (deve ser um caminho absoluto)
        dry_run: Se True, apenas simula sem mover arquivos
    """
    target_folder = os.path.abspath(os.path.expanduser(target_folder))
    
    if not os.path.exists(target_folder):
        logging.error(f"Pasta não encontrada: {target_folder}")
        return 0, 0

    moved_files = 0
    created_folders = set()
    
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if not os.path.isfile(file_path) or filename.startswith('.'):
            continue

        extension = os.path.splitext(filename)[1].lower()
        file_category = "others"

        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                file_category = category
                break

        destination_folder = os.path.join(target_folder, file_category)
        
        if not os.path.exists(destination_folder):
            if dry_run:
                logging.info(f"[DRY RUN] Criaria pasta: {destination_folder}")
            else:
                os.makedirs(destination_folder, exist_ok=True)
                logging.info(f"Pasta criada: {destination_folder}")
            created_folders.add(destination_folder)

        new_path = os.path.join(destination_folder, filename)
        if dry_run:
            logging.info(f"[DRY RUN] Movendo: {filename} -> {new_path}")
        else:
            try:
                shutil.move(file_path, new_path)
                logging.info(f"Arquivo movido: {filename} -> {file_category}/")
                moved_files += 1
            except Exception as e:
                logging.error(f"Erro ao mover {filename}: {str(e)}")

    return moved_files, len(created_folders)

def main():
    """Função principal com tratamento de argumentos CLI"""
    setup_logging()
    
    parser = argparse.ArgumentParser(
        description="Organizador de Arquivos - Organiza arquivos por tipo em subpastas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--folder",
        type=str,
        default=DOWNLOAD_FOLDER,
        help="Pasta a ser organizada (padrão: Downloads do usuário)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula a organização sem mover arquivos"
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Nível de detalhe do log"
    )
    
    args = parser.parse_args()
    logging.getLogger().setLevel(args.log_level)
    
    logging.info(f"Iniciando organização da pasta: {args.folder}")
    if args.dry_run:
        logging.warning("Modo de simulação ativado (nenhum arquivo será movido)")
    
    start_time = datetime.now()
    moved_files, created_folders = organize_files(args.folder, args.dry_run)
    duration = datetime.now() - start_time
    
    logging.info("\nResumo:")
    logging.info(f"• Arquivos movidos: {moved_files}")
    logging.info(f"• Pastas criadas: {created_folders}")
    logging.info(f"• Tempo de execução: {duration.total_seconds():.2f} segundos")
    
    if not args.dry_run:
        logging.info("• Organização concluída com sucesso!")
    else:
        logging.info("• Simulação concluída (use sem --dry-run para executar)")

if __name__ == "__main__":
    main()