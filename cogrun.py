# Prediction interface for Cog ⚙️
# Reference: https://github.com/replicate/cog/blob/main/docs/python.md

import cog
import pathlib
from explorer import do_setup, perform_analysis

# https://stackoverflow.com/a/6587648/1010653
import tempfile, shutil
def create_temporary_copy(src_path):
    _, tf_suffix = os.path.splitext(src_path)
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, f"tempfile{tf_suffix}")
    shutil.copy2(src_path, temp_path)
    return temp_path

class Explorer(cog.Predictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        do_setup()
        self.photos_path = 'twem/'
        self.features_path, self.analysis_path = prepare_folder(self.photos_path)

    @cog.input("query", type=str, help="text to input")
    def predict(self, query):
        """Run a single prediction on the model"""
        numberResults = 5
        newAnalysisPath = perform_analysis(query, numberResults, self.photos_path, self.features_path, self.analysis_path, show_result=0)
        temp_copy = create_temporary_copy(f"{newAnalysisPath}/analysisResults.jpg")
        return pathlib.Path(os.path.realpath(temp_copy))
