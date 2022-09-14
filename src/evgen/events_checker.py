import sys
from difflib import unified_diff
from hashlib import md5
from pathlib import Path
from shutil import copyfile, rmtree

from evgen import evgen_config
from evgen.scripts import run_evgen


class EventsChecker:
    def __init__(
        self,
        events_path: str,
        evgen_config_path: str,
    ):
        self.source_dir_path = Path(evgen_config_path).parent
        self.events_path = Path(events_path)
        self.working_dir_path = Path("/tmp") / "Evgen"
        if self.working_dir_path.exists():
            rmtree(self.working_dir_path.as_posix())
        self.working_dir_path.mkdir()
        self.working_evgen_config_path = self.working_dir_path / "evgen.yaml"
        copyfile(evgen_config_path, self.working_evgen_config_path.as_posix())

    def check_generation(self):
        run_evgen.generate(
            events_path=self.events_path.as_posix(),
            evgen_config_path=self.working_evgen_config_path.as_posix(),
        )

    def check_consistency(self):
        config = evgen_config.EvgenConfig.load(self.working_evgen_config_path)

        if config.code:
            for platform, code_config in config.code.items():
                self.assert_all_generated_files(
                    output_dir_name=code_config.output_dir,
                    extension=evgen_config.EXTENSIONS[code_config.language],
                )

        if config.doc:
            for doc, doc_config in config.doc.items():
                self.assert_all_generated_files(
                    output_dir_name=doc_config.output_dir,
                    extension=doc_config.extension,
                )

    def assert_all_generated_files(self, output_dir_name: str, extension: str):
        source_dir = self.source_dir_path / output_dir_name
        working_dir = self.working_dir_path / output_dir_name
        if len(list(working_dir.rglob(f"*.{extension}"))) == 0:
            raise RuntimeError(f"Could not find any files generated for checking")
        for working_file_path in working_dir.rglob(f"*.{extension}"):
            relative_path = working_file_path.relative_to(working_dir)
            source_file_path = source_dir / relative_path
            print(working_file_path)
            print(source_file_path)
            self.assert_files_identity(source_file_path, working_file_path)

    @staticmethod
    def get_file_without_spaces(in_path: Path, out_path: Path):
        with open(in_path.as_posix(), "r", 1, "UTF-8") as read_fp:
            file_lines = read_fp.read()
            file_lines = file_lines.replace(" ", "").replace("-", "")
            with open(out_path.as_posix(), "w+", 1, "UTF-8") as write_fp:
                write_fp.write(file_lines)

    def assert_files_identity(self, first_file_path: Path, second_file_path: Path):
        tmp_first_file_path = self.working_dir_path / "tmp_file_1"
        tmp_second_file_path = self.working_dir_path / "tmp_file_2"
        self.get_file_without_spaces(first_file_path, tmp_first_file_path)
        self.get_file_without_spaces(second_file_path, tmp_second_file_path)
        if self.get_checksum(tmp_first_file_path) != self.get_checksum(
            tmp_second_file_path
        ):
            raise RuntimeError(
                f"{first_file_path.as_posix()} is not consistent with"
                f" {second_file_path.as_posix()}."
                f" Regenerate files"
            )

    @staticmethod
    def get_checksum(file_path: Path):
        hash_function = md5()
        with open(file_path.as_posix(), "r", 1, "UTF-8") as fp:
            for line in fp.readlines():
                hash_function.update(line.encode())
        return hash_function.digest()
