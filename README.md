# Semantle-Helper
Helps the user find answers to the online game, Semantle.

# Before Running Helper.py
Install the required packages by entering the Semantle-Helper directory and running:
```
pip install -r requirements.txt
```
Note: You may also need to install Microsoft C++ Build Tools from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

Next, you'll have to download and unzip the GoogleNews-vectors-negative300.bin.gz file accessible [here](https://code.google.com/archive/p/word2vec/) and move the resulting .bin file into the Semantle-Helper directory.

Run makeKVModel.py. This will take a while, so give it a few minutes -- it'll create two files: wordVectors.kvmodel and wordVectors.kvmodel.vectors.npy; keep those there.

# Disclaimer
Making this was only possible because the source code of Semantle was viewable in its early days. I wouldn't have been able to figure any of this out if not for that (or, it would've been much more difficult for me otherwise).

Also, I just made this to see if it was possible; actually cheating in a single-player word game seems a bit pointless, but to each their own.
