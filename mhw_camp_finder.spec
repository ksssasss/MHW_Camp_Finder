# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['mhw_camp_finder_qt.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='魔物獵人荒野 最近營地查詢小工具',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    info_plist={
        'NSHighResolutionCapable': 'True',
        'NSRequiresAquaSystemAppearance': 'False',
        'CFBundleDisplayName': '魔物獵人荒野 最近營地查詢小工具',
        'CFBundleName': '魔物獵人荒野 最近營地查詢小工具',
        'CFBundleIdentifier': 'com.mhw.campfinder',
        'CFBundleVersion': '1.0.0',
        'CFBundlePackageType': 'APPL',
        'LSMinimumSystemVersion': '10.13.0',
        'NSPrincipalClass': 'NSApplication',
        'LSApplicationCategoryType': 'public.app-category.utilities',
    }
) 