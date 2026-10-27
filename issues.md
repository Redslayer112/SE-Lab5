# Issue table

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (B608) | Security, Medium | 10 | `addSong` builds the INSERT with `%` formatting, so a title such as `x'); DROP TABLE songs;--` alters the query | Use `?` placeholders and pass a parameter tuple |
| Unsafe pickle load (B301) | Security, Medium | 33 | `pickle.loads` runs arbitrary code from untrusted bytes | Store playlists as JSON with `json.dumps` and `json.loads` |
| Pickle import (B403) | Security, Low | 1 | Import of `pickle` flagged | Remove the import and use `json` |
| Weak random (B311) | Security, Low | 17 | `random.choice` is not a secure generator | Use `secrets.choice` |
| Mutable default arg (W0102) | Bug | 9 | `playlist=[]` is shared across calls, so unrelated playlists mix | Default to `None` and create a new list in the function |
| Bare except (W0702, E722) | Bug | 39 | `except:` hides every error, including `KeyboardInterrupt` | Catch `sqlite3.Error` |
| Naming (C0103) | Style | 9, 15, 28, 32, 36 | camelCase function names break PEP 8 | Rename to `add_song`, `shuffle_pick`, `save_playlist`, `load_playlist`, `total_plays` |
| Missing docstrings (C0114, C0116) | Style | 1, 9, 15, 20, 28, 32, 36, 43 | Module and functions have no docstring | Add one-line docstrings |
| Unnecessary else (R1705) | Style | 22 | `else` follows a `return` | Remove the `else` and de-indent |
| Ambiguous name (E741) | Style | 47 | Variable `l` looks like `1` | Rename to `loaded` |
| Multiple statements (E701, C0321) | Style | 48 | `if` and `print` share one line | Put `print` on its own line |
| Line too long (E501, C0301) | Style | 6, 10, 21, 49 | Lines exceed 79 characters | Wrap the lines |
| F-string suggestion (C0209) | Style | 10 | `%` formatting on a regular string | Resolved by the parameterised query |
| Import-time run | Design | 52 | `main()` runs on import | Guard with `if __name__ == "__main__":` |
