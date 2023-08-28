import sublime
import sublime_plugin
import os


class CreateTestFilePythonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = self.view.file_name()
        file_directory = os.path.dirname(file_name)
        parent_folder_name = os.path.basename(os.path.dirname(file_name))
        tests_directory = os.path.join(file_directory, "tests_" + parent_folder_name)
        if not os.path.exists(tests_directory):
            os.makedirs(tests_directory)
        result_file_name = os.path.join(tests_directory, "test_" + os.path.basename(file_name))
        with open(result_file_name, "w") as file:
            file.write("# Your place to write tests for the code")

    
