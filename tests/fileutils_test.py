from utils.fileutils import read_json_file_as_string


def test_read_valid_json_file_as_string():
    sample_file_path = "resources/schema.json"
    file_content = read_json_file_as_string(sample_file_path)
    assert type(file_content) == str
