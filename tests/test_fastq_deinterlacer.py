import os
import unittest

from galaxy_utils.sequence.fastq import fastqReader, fastqFormatError
from galaxy_utils.sequence.scripts.fastq_paired_end_deinterlacer import Deinterlacer

TEST_DIR = os.path.dirname(__file__)
TEST_DATA_DIR = os.path.join(TEST_DIR, 'test_data')


class FastqDeinterlacerTestCase(unittest.TestCase):

    def test_something(self):
        di = Deinterlacer()
#        di.run() # what happens here? where do the args come from?
        #input filename - no prob. OUtput filenames - ouch.




def _data_path(filename):
    path = os.path.join(TEST_DATA_DIR, filename)
    assert os.path.exists(path)
    return os.path.abspath(path)
