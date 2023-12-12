from utils.utils import *

TRAIN_DIR = 'dataset/train'
TEST_DIR = 'dataset/test'
TRAIN_FILE = 'etc/db_train.transcription'
TEST_FILE = 'etc/db_test.transcription'
TRAIN_FILEIDS = 'etc/db_train.fileids'
TEST_FILEIDS = 'etc/db_test.fileids'
PHONETIC_DICT = 'etc/db.dict'
FILLER_FILE = 'etc/db.filler'


create_transcription(TRAIN_DIR, TRAIN_FILE)
create_transcription(TEST_DIR, TEST_FILE)
create_fileids(TRAIN_DIR, TRAIN_FILEIDS)
create_fileids(TEST_DIR, TEST_FILEIDS)
create_phonetic_dictionary(TRAIN_DIR, PHONETIC_DICT, FILLER_FILE)
