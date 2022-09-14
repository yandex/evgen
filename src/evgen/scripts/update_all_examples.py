from pathlib import Path

from evgen.scripts import run_evgen


def main():
    project_path = Path(__file__).parent.parent.parent
    for events_yaml_path in project_path.rglob("events.yaml"):
        evgen_yaml_path = events_yaml_path.parent / "evgen.yaml"
        run_evgen.generate(events_yaml_path.as_posix(), evgen_yaml_path.as_posix())


if __name__ == "__main__":
    main()
