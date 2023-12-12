import os
from .phon_czech import ipa_czech


def create_transcription(directory, write_to):
    with open(write_to, 'w', encoding='utf-8') as transcript:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.trn') and 'proto-non-speech-events' not in file:
                    file_path = os.path.join(root, file)

                    with open(file_path, 'r', encoding='utf-8') as target:
                        lines = target.readlines()

                        file_id = file_path.split('\\')[-1][:-8]
                        for line in lines:
                            parsed_line = f'<s> {line.strip().replace("_", "+")} <s> ({file_id})\n'
                            transcript.write(parsed_line)


def create_fileids(directory, write_to):
    with open(write_to, 'w', encoding='utf-8') as fields:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if not file.endswith('.trn') and 'proto-non-speech-events' not in file:
                    file_path = os.path.join(root, file)

                    formatted_path = file_path.replace("\\", '/')
                    fields.write(f'{formatted_path[:-4]}\n')


def create_phonetic_dictionary(directory, phonetic_file, filler_file):
    words_set = set()
    filler_set = set()
    with open(phonetic_file, 'w', encoding='utf-8') as phones_f:
        with open(filler_file, 'w', encoding='utf-8') as filler_f:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.trn') and 'proto-non-speech-events' not in file:
                        file_path = os.path.join(root, file)

                        with open(file_path, 'r', encoding='utf-8') as target:
                            lines = target.readlines()

                            for line in lines:
                                words = line.strip().split(' ')
                                for word in words:
                                    if word.startswith('_'):
                                        filler_set.add(word.replace("_", "+"))

                                    else:
                                        words_set.add(word)

            for word in words_set:
                phone_trans = ipa_czech(word)
                phones_f.write(f'{word} {phone_trans}\n')

            for sound in filler_set:
                filler_f.write(f'{sound} +{sound}+\n')


def create_lm_transcription(directory, write_to):
    with open(write_to, 'w', encoding='utf-8') as transcript:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.trn') and 'proto-non-speech-events' not in file:
                    file_path = os.path.join(root, file)

                    with open(file_path, 'r', encoding='utf-8') as target:
                        lines = target.readlines()

                        for line in lines:
                            words = line.split()
                            new_words = [w for w in words if not w.startswith('_')]
                            if not new_words:
                                continue

                            new_line = ' '.join(new_words).lower()
                            parsed_line = f'<s> {new_line} <s>\n'
                            transcript.write(parsed_line)

