# Python Projects

This folder now contains several standalone Python projects:

- `main.py`: 2D sandbox builder
- `sheep_game.py`: match-style puzzle game
- `fps_3d_game.py`: 3D shooter prototype
- `lifeafter_event_app.py`: LifeAfter event and reward viewer
- `lifeafter_event_viewer.html`: cross-platform responsive LifeAfter viewer

## LifeAfter event viewer

`lifeafter_event_app.py` is a touch-friendly UI app for browsing current LifeAfter activities, prize pools, battle content, and strategy notes.

## Cross-platform web version

If you want one version that works on Windows, macOS, Android, and iPhone/iPad, use:

`lifeafter_event_viewer.html`

You can open it directly in a browser on desktop. For phones, upload it to a static host or file-sharing link and open it in the mobile browser.

### Highlights

- Phone-like vertical layout
- Home hero section for the current most important events
- Category navigation for main events, PVP, prize pools, appearance, review, and archived content
- Tap-to-open detail popups with rewards, highlights, and recommended play order
- Quick audience guide for free-to-play players, returnees, builders, and combat players

### Run

```powershell
python lifeafter_event_app.py
```

This version uses only the Python standard library (`tkinter`), so it does not require installing `kivy`.

If your machine has multiple Python versions, run it with the same interpreter path you already used in the terminal.

### Build a standalone exe

If you want to send this app to people who do not have Python installed, build a Windows `.exe`.

```powershell
build_lifeafter_exe.bat
```

After the build finishes, the app will be generated at:

```text
dist\lifeafter_event_viewer.exe
```

Users can open that exe directly without installing Python.

## 3D shooter

```powershell
python fps_3d_game.py
```
