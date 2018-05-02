from cx_Freeze import setup, Executable

setup(name='EvilKeyLogger', version='0.1', description='doesn\'t spy on you',
      executables = [Executable('EvilKeyLogger')])
