import cx_Freeze

executables = [cx_Freeze.Executable("Main.py")]

cx_Freeze.setup(
    name="Mayo_Game",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["Assets"]}},
    executables=executables

    )