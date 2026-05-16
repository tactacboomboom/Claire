#!/usr/bin/env python3
"""
claude-mem → graphify bridge
Exporte les conversations SQLite de claude-mem en fichiers texte
exploitables par /graphify pour construire un graphe de connaissance.

Usage:
  python claude-mem-to-graphify.py                    # export + graphify
  python claude-mem-to-graphify.py --export-only      # export sans lancer graphify
  python claude-mem-to-graphify.py --db <path>        # chemin DB custom
"""

import sqlite3
import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# Chemins par défaut
DEFAULT_DB = Path.home() / ".claude-mem" / "claude-mem.db"
DEFAULT_OUT = Path.home() / ".claude-mem" / "graphify-export"


def export_sessions(conn, out_dir: Path) -> int:
    """Exporte chaque session comme un fichier .txt pour graphify."""
    c = conn.cursor()

    # Charger sessions
    c.execute("""
        SELECT s.id, s.content_session_id, s.project, s.started_at, s.status,
               s.custom_title
        FROM sdk_sessions s
        ORDER BY s.started_at DESC
    """)
    sessions = c.fetchall()
    count = 0

    for sess in sessions:
        sess_id, content_id, project, started_at, status, title = sess
        if not content_id:
            continue

        lines = []
        label = title or f"Session {content_id[:8]}"
        lines.append(f"# {label}")
        lines.append(f"Project: {project or 'unknown'}")
        lines.append(f"Date: {started_at or 'unknown'}")
        lines.append(f"Status: {status or 'unknown'}")
        lines.append("")

        # Prompts utilisateur
        c.execute("""
            SELECT prompt_number, prompt_text FROM user_prompts
            WHERE content_session_id = ? ORDER BY prompt_number
        """, (content_id,))
        prompts = c.fetchall()
        if prompts:
            lines.append("## Prompts")
            for num, text in prompts:
                if text and text.strip():
                    lines.append(f"[{num}] {text.strip()[:500]}")
            lines.append("")

        # Observations
        c.execute("""
            SELECT type, content, created_at FROM observations
            WHERE content_session_id = ?
            ORDER BY created_at
        """, (content_id,))
        obs = c.fetchall()
        if obs:
            lines.append("## Observations")
            for otype, content, ts in obs:
                if content and content.strip():
                    lines.append(f"[{otype}] {content.strip()[:300]}")
            lines.append("")

        # Résumé de session
        c.execute("""
            SELECT summary_text FROM session_summaries
            WHERE content_session_id = ?
            ORDER BY created_at DESC LIMIT 1
        """, (content_id,))
        summary = c.fetchone()
        if summary and summary[0]:
            lines.append("## Résumé")
            lines.append(summary[0].strip())
            lines.append("")

        if len(lines) > 6:  # session non vide
            safe_id = content_id[:12].replace("/", "_")
            date_prefix = (started_at or "0000")[:10]
            filename = out_dir / f"{date_prefix}_{safe_id}.txt"
            filename.write_text("\n".join(lines), encoding="utf-8")
            count += 1

    return count


def main():
    parser = argparse.ArgumentParser(description="claude-mem → graphify bridge")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Chemin vers claude-mem.db")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Dossier d'export")
    parser.add_argument("--export-only", action="store_true", help="Export sans lancer graphify")
    args = parser.parse_args()

    db_path = Path(args.db)
    out_dir = Path(args.out)

    if not db_path.exists():
        print(f"❌ Base de données introuvable : {db_path}")
        print(f"   Lance d'abord une session Claude Code avec claude-mem actif.")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"📂 Export vers : {out_dir}")

    conn = sqlite3.connect(db_path)
    try:
        count = export_sessions(conn, out_dir)
    finally:
        conn.close()

    print(f"✅ {count} sessions exportées")

    if count == 0:
        print("   Aucune session avec contenu — relance après quelques sessions Claude Code.")
        return

    if args.export_only:
        print(f"\n→ Pour graphifier : /graphify {out_dir}")
        return

    # Lancer graphify
    print(f"\n🔬 Lancement de graphify sur {out_dir}...")
    graphify_out = out_dir / "graphify-out"
    graphify_out.mkdir(exist_ok=True)

    try:
        import subprocess
        result = subprocess.run(
            ["python3", "-m", "graphify", str(out_dir)],
            capture_output=True, text=True, timeout=300
        )
        if result.returncode == 0:
            print("✅ Graphify terminé")
            graph_file = graphify_out / "graph.json"
            if graph_file.exists():
                print(f"   → graph.json : {graph_file}")
        else:
            print(f"⚠️  Graphify non disponible en mode direct — utilise /graphify dans Claude Code :")
            print(f"   /graphify {out_dir}")
    except Exception as e:
        print(f"→ Lance depuis Claude Code : /graphify {out_dir}")


if __name__ == "__main__":
    main()
