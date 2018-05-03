from cx_Freeze import setup, Executable

setup(name ='Not a Key Logger',
      version = '0.1',
      options = { 'build_exe': {
        'include_msvcr': True,
      }},
      description = 'KeyLogger',
      executables = [Executable('main.py')]
      )
