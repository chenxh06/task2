import yaml

from config import Config


class CaseLoader:
    def __init__(self, filepath: str = Config.TESTCASE_DATA_DIR):
        self.filepath = filepath
        self.data = None

    def load(self, filepath: str = None):
        filepath = filepath or self.filepath
        if not filepath.split('.')[-1] == 'yml':
            raise Exception('File type not supported')
        with open(filepath, 'rt') as f:
            data = yaml.safe_load(f)
        return data
