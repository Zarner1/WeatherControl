from cx_Freeze import setup, Executable

setup(
    name = "my_program",
    version = "0.1",
    description = "My GUI program",
    executables = [Executable("weather.py",base="Win32GUI")]
)
