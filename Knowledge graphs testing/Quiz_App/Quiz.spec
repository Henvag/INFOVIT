import sys

block_cipher = None

# Platform specific settings
if sys.platform.startswith('win'):
    console = True
    exe_extension = '.exe'
    bundle_required = False
else:  # macOS
    console = False
    exe_extension = ''
    bundle_required = True

a = Analysis(
    ['quiz_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('info216_2023exam_questions.json', '.'),
        ('fonts/ProductSans-Black.ttf', 'fonts'),
        ('quiz.png', '.'),
        ('henvagdevborder.jpg', '.')
    ],
    hiddenimports=['PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets', 'PyQt6.QtWebEngineCore', 'PyQt6.QtWebEngineWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Quiz' + exe_extension,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=console,
)

if bundle_required:
    # macOS bundle
    BUNDLE(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        name='Quiz.app',
        icon=None,
        bundle_identifier=None,
        version='1.0.0'
    )
else:
    # Windows collection
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='Quiz'
    )