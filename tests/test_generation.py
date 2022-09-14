from pathlib import Path
from subprocess import DEVNULL, call, check_call, run
from unittest import TestCase

from evgen.scripts import run_evgen

PROJECT_DIR = Path(__file__).parent.parent
C_SHARP_PROJECT_NAME = "CSharpProject"


def _java_compilation(cwd: Path):
    print("JAVA compilation")
    call(["rm", "Main_Java.jar"], cwd=cwd, stderr=DEVNULL)
    check_call(
        ["cp", "EvgenAnalytics.java", "src/ru/yandex/kinopoisk/EvgenAnalytics.java"],
        cwd=cwd,
    )
    check_call(
        [
            "javac",
            "-d",
            "out",
            "src/ru/yandex/kinopoisk/EvgenAnalytics.java",
            "src/ru/yandex/kinopoisk/Main.java",
        ],
        cwd=cwd,
    )
    check_call(
        ["jar", "-cfm", "Main_Java.jar", "manifest.txt", "-C", "out", "ru"], cwd=cwd
    )
    check_call(["java", "-jar", "Main_Java.jar"], cwd=cwd)
    call(["rm", "Main_Java.jar"], cwd=cwd)


def _kotlin_compilation(cwd: Path):
    print("")
    print("KOTLIN compilation")
    call(["rm", "Main_Kotlin.jar"], cwd=cwd, stderr=DEVNULL)
    check_call(
        [
            "kotlinc",
            "Main.kt",
            "EvgenAnalytics.kt",
            "-include-runtime",
            "-d",
            "Main_Kotlin.jar",
        ],
        cwd=cwd,
    )
    check_call(["java", "-jar", "Main_Kotlin.jar"], cwd=cwd)
    call(["rm", "Main_Kotlin.jar"], cwd=cwd)


def _swift_compilation(cwd: Path):
    print("")
    print("SWIFT compilation")
    call(["rm", "run"], cwd=cwd, stderr=DEVNULL)
    check_call(["swiftc", "-o", "run", "main.swift", "EvgenAnalytics.swift"], cwd=cwd)
    check_call(["chmod", "u+x", "run"], cwd=cwd)
    check_call(["./run"], cwd=cwd)
    call(["rm", "run"], cwd=cwd)


def _type_script_compilation(cwd: Path):
    print("")
    print("TypeScript")
    call(["rm", "main.js"], cwd=cwd, stderr=DEVNULL)
    check_call(["tsc", "main.ts"], cwd=cwd)
    check_call(["node", "main.js"], cwd=cwd)
    call(["rm", "main.js"], cwd=cwd)


def _c_sharp_compilation(cwd: Path):
    print("")
    print("C#")
    call(["rm", "-rf", C_SHARP_PROJECT_NAME], cwd=cwd, stderr=DEVNULL)
    check_call(
        [f"/usr/local/share/dotnet/dotnet new console -o {C_SHARP_PROJECT_NAME}"],
        cwd=cwd,
        shell=True,
    )
    call(
        ["rm", "Program.cs"],
        cwd=cwd.joinpath(C_SHARP_PROJECT_NAME).as_posix(),
        stderr=DEVNULL,
    )
    check_call([f"cp *.cs {C_SHARP_PROJECT_NAME}"], cwd=cwd.as_posix(), shell=True)
    check_call(
        [f"/usr/local/share/dotnet/dotnet run"],
        cwd=cwd.joinpath(C_SHARP_PROJECT_NAME).as_posix(),
        shell=True,
    )
    call(["rm", "-rf", C_SHARP_PROJECT_NAME], cwd=cwd, stderr=DEVNULL)


def _test_project(project_path: Path):
    kotlin_path = project_path / "android_kotlin"
    _kotlin_compilation(cwd=kotlin_path)

    java_path = project_path / "android_java"
    _java_compilation(cwd=java_path)

    swift_path = project_path / "ios_swift"
    _swift_compilation(cwd=swift_path)

    c_sharp_path = project_path / "ios_c_sharp"
    _c_sharp_compilation(cwd=c_sharp_path)

    web_smart_tv_path = project_path / "web_smart_tv"
    _type_script_compilation(cwd=web_smart_tv_path)


class TestGeneration(TestCase):
    def test_example(self):
        test_example_dir = PROJECT_DIR / "test_example"
        run_evgen.generate(
            events_path=test_example_dir / "events.yaml",
            evgen_config_path=test_example_dir / "evgen.yaml",
        )
        _test_project(test_example_dir)

    def test_tutorial_1(self):
        dir_path = PROJECT_DIR / "tutorial" / "1.event_parameters"
        run_evgen.generate(
            events_path=dir_path / "events.yaml",
            evgen_config_path=dir_path / "evgen.yaml",
        )
        _test_project(dir_path)

    def test_tutorial_2(self):
        dir_path = PROJECT_DIR / "tutorial" / "2.interfaces"
        run_evgen.generate(
            events_path=dir_path / "events.yaml",
            evgen_config_path=dir_path / "evgen.yaml",
        )
        _test_project(dir_path)

    def test_tutorial_4(self):
        dir_path = PROJECT_DIR / "tutorial" / "4.single_param_tracker"
        run_evgen.generate(
            events_path=dir_path / "events.yaml",
            evgen_config_path=dir_path / "evgen.yaml",
        )
        _test_project(dir_path)

    def test_tutorial_5(self):
        dir_path = PROJECT_DIR / "tutorial" / "5.modules"
        run_evgen.generate(
            events_path=dir_path / "events", evgen_config_path=dir_path / "evgen.yaml"
        )
        _test_project(dir_path)

    def test_tutorial_6(self):
        dir_path = PROJECT_DIR / "tutorial" / "6.ytt"
        run_evgen.generate(
            events_path=dir_path / "events",
            evgen_config_path=dir_path / "evgen.yaml",
            ytt=True,
        )
        _test_project(dir_path)
