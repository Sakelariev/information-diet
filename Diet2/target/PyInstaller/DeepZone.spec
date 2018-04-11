# -*- mode: python -*-

block_cipher = None


a = Analysis(['../../src/main/python/deepzone/main.py'],
             pathex=['/Users/user/Dropbox/Python/NoDistraction/Diet2/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='DeepZone',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/user/Dropbox/Python/NoDistraction/Diet2/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='DeepZone')
app = BUNDLE(coll,
             name='DeepZone.app',
             icon='/Users/user/Dropbox/Python/NoDistraction/Diet2/target/Icon.icns',
             bundle_identifier='com.example.tutorial')
