# import genism package and summarizer
import gensim
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import wikipedia

# wikipedia content
wikisearch = wikipedia.page("Eclogite")
wikicontent = wikisearch.content
print(wikicontent)

# summary by 0.1% of the original content
summary_ratio = summarize(wikicontent, ratio = 0.01)
print("summary by ratio")
print(summary_ratio)

# summary by count of words
summary_wordcount = summarize(wikicontent, word_count = 200)
print("summary by word count")
print(summary_wordcount)
