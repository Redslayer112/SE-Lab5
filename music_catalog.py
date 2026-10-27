"""Music catalog: songs, play counts, popularity and playlists."""
import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE songs (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, plays INTEGER)")


def add_song(title, artist, plays=0, playlist=None):
    """Insert a song and append its title to the playlist."""
    if playlist is None:
        playlist = []
    conn.execute("INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)", (title, artist, plays))
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return the id of a random song."""
    ids = [r[0] for r in conn.execute("SELECT id FROM songs")]
    return secrets.choice(ids)


def popularity(title):
    """Return unknown, popular or niche for a song title."""
    row = conn.execute("SELECT plays FROM songs WHERE title = ?", (title,)).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialise a playlist to JSON."""
    return json.dumps(playlist)


def load_playlist(blob):
    """Load a playlist from JSON."""
    return json.loads(blob)


def total_plays():
    """Return the sum of all play counts."""
    try:
        return conn.execute("SELECT SUM(plays) FROM songs").fetchone()[0]
    except sqlite3.Error:
        return 0


def main():
    """Run a short demonstration."""
    pl = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, pl)
    blob = save_playlist(pl)
    loaded = load_playlist(blob)
    if len(loaded) > 1:
        print("multi-song playlist")
    print(popularity("Aurora"), popularity("Monsoon"), shuffle_pick(), total_plays())


if __name__ == "__main__":
    main()
