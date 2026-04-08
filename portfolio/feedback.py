import json
import os
from pathlib import Path

import gspread
import pandas as pd
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

DOTENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(DOTENV_PATH)

SHEET_NAME = "avaliacoes-portfolio"
WORKSHEET_NAME = "avaliacao"
DEFAULT_COLUMNS = ["Timestamp", "Projeto", "Nota", "Comentario"]


def _normalize_text(value: str) -> str:
    return (
        str(value)
        .strip()
        .lower()
        .replace("á", "a")
        .replace("à", "a")
        .replace("â", "a")
        .replace("ã", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )


def _normalize_feedback_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {}
    for col in df.columns:
        norm_col = _normalize_text(col)
        if norm_col in {"timestamp", "data", "created_at"}:
            rename_map[col] = "Timestamp"
        elif norm_col in {"projeto", "project"}:
            rename_map[col] = "Projeto"
        elif norm_col in {"nota", "rating"}:
            rename_map[col] = "Nota"
        elif norm_col in {"comentario", "comentarios", "comment", "comments"}:
            rename_map[col] = "Comentario"

    df = df.rename(columns=rename_map)

    for col in DEFAULT_COLUMNS:
        if col not in df.columns:
            df[col] = "" if col != "Nota" else 0

    df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce").fillna(0).clip(0, 5)
    return df[DEFAULT_COLUMNS]


def _get_worksheet():
    service_account_raw = os.getenv("GCP_SERVICE_ACCOUNT", "")
    if not service_account_raw:
        return None

    service_account_info = json.loads(service_account_raw)
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(service_account_info, scopes=scopes)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)


def load_feedback() -> tuple[pd.DataFrame, str]:
    try:
        worksheet = _get_worksheet()
        if worksheet is None:
            return pd.DataFrame(columns=DEFAULT_COLUMNS), "offline"

        df = pd.DataFrame(worksheet.get_all_records())
        return _normalize_feedback_columns(df), "online"
    except Exception:
        return pd.DataFrame(columns=DEFAULT_COLUMNS), "offline"


def save_feedback(project_id: str, note: int, comment: str) -> tuple[bool, str]:
    try:
        worksheet = _get_worksheet()
        if worksheet is None:
            return False, "Nao foi possivel conectar ao Google Sheets."

        row = [str(pd.Timestamp.now()), project_id, int(note), comment.strip()]
        worksheet.append_row(row)
        return True, "Avaliacao registrada com sucesso."
    except Exception:
        return False, "Erro ao enviar avaliacao. Tente novamente em instantes."
