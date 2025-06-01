import json
import os
from threading import Lock

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.lock = Lock()
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.filename) or not self._is_valid_json():
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def _is_valid_json(self):
        try:
            with open(self.filename, 'r') as f:
                json.load(f)
            return True
        except (json.JSONDecodeError, FileNotFoundError):
            return False

    def _read_notes(self):
        with self.lock:
            with open(self.filename, 'r') as f:
                return json.load(f)

    def _write_notes(self, notes):
        with self.lock:
            with open(self.filename, 'w') as f:
                json.dump(notes, f, indent=2)

    def add_note(self, note):
        notes = self._read_notes()
        notes.append(note)
        self._write_notes(notes)

    def list_notes(self):
        return self._read_notes()

    def search_notes(self, keyword):
        return [note for note in self._read_notes() if keyword.lower() in note.lower()]
