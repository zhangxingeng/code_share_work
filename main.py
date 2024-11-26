https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken
Rename it to 9b5ad71b2ce5302211f9c61530b329a4922fc6a4
Transfer to your remote machine in a folder called "tiktoken_cache"
Run the following code every time you need to use tiktoken
import os

tiktoken_cache_dir = "path_to_tiktoken_cache_folder"
os.environ["TIKTOKEN_CACHE_DIR"] = tiktoken_cache_dir

# validate
assert os.path.exists(os.path.join(tiktoken_cache_dir,"9b5ad71b2ce5302211f9c61530b329a4922fc6a4"))
Just ran into this issue today as well. Not the exact same error, but solution for running this offline should be the same. We'll download the necessary file, then "trick" tiktoken into caching it.

This method works if, say you have a remote machine with no internet access and a local machine with internet.

I'm outlining a generalized version below, but you can skip to the tl;dr if you have an updated version of tiktoken and are using the cl100k_base tokenizer.
