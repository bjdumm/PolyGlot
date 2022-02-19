# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['pickle', 'wx', 'plyglt.py'],
             pathex=['C:\\Users\\bjdum\\Documents\\Python\\PlyGlt'],
             binaries=[],
             datas=[('words.txt,Nouns.txt,nounSections.txt,Adjectives.txt,adjSections.txt,adverbSections.txt,numLangs.txt,Other.txt,Adverbs.txt,Verbs.txt,Prepositions.txt,Household.txt,Basic.txt,Animals.txt', '.')],
             hiddenimports=['os'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='pickle',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pickle')
