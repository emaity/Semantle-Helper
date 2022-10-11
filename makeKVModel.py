# takes bin file, makes kvmodel out of it

from pathlib import Path
import gensim.models.keyedvectors as word2vec
import tqdm

vectors = str(Path(__file__).parent / "GoogleNews-vectors-negative300.bin")   # vectors = binary(in this case) file holding vector information
model = word2vec.KeyedVectors.load_word2vec_format(vectors, binary=True)      # loads KeyedVectors from the file, I think?


# removes words containing: #, _, @, =,
# ASSUMES THAT THEY WILL NOT BE USED FOR ANY SEMANTLE ANSWERS
# toDelete = ["#", "_", "@", "="]
for key in tqdm.tqdm(reversed(model.index_to_key)):
    #if any(character in key for character in toDelete): # this seems to be a bit slower than a bunch of 'in' statements, so I'll keep it that way
    if "#" in key or "_" in key or "@" in key or "=" in key:
        del model.index_to_key[model.key_to_index[key]]


model.save('wordVectors.kvmodel') # creates wordVectors.kvmodel as well as its .npy vectors, keep those

# NOTE:
# words are deleted, but the vectors for all the deleted data seems to remain
# I'm not going to try to fix that, but that's a decent amount of space being wasted; perhaps in the future I will