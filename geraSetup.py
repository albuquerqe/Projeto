import cx_Freeze
executables =[
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "Proje",
    options={
        "build_exe":{
            "include_files":["space.png",
                            "Space_Machine_Power.mp3",
                            "space.png"]
        }
    }, executables = executables
)

#py geraSetup.py build
#py geraSetup.py bdist_msi
