import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "SPACE MARKER",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["space.png",
                            "Space_Machine.mp3",
                            "bg.jpg"]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi

