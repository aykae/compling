# compling
A compilation of computational linguistics projects by A.K. Rai.

## SentGen
SentGen is a computational linguistics program that is meant to stochastically generate gramatically correct English sentences. The generator works by taking in a specified Engilsh grammar in the form of phrase structure rules, and building a tree structure whose root is a 'Sentence' node and whose leaves are English words (terminal symbols). Optional rules are followed randomly to produce some variations in sentence structure.<br><br>The English word data was generated by unifying the Google 10k most common English word <a class="desc-link" href="https://github.com/first20hours/google-10000-english" target="_blank">dataset</a> with a 370k Part of Speech tagged English <a class="desc-link" href="https://www.kaggle.com/datasets/ruchi798/part-of-speech-tagging" target="_blank">dataset</a>. This program is a computational implementation of the Phrase Structure theory presented in UCLA Prof. Bruce Hayes' <a class="desc-link" href="https://linguistics.ucla.edu/people/hayes/20/Text/HayesIntroductoryLinguistics2021.pdf" target="_blank">Introductory Linguistics</a>. The grammar used in the program is also directly from this text. Work still needs to be done to add proper articles, prepositions, and inflection. Semantics are completely ignored, so the sentences will likely not make sense.

Try it out yourself [here.](https://aykae.com/compling)

<br>

<p align="center">
  <img src="sentgen.gif"/>

</p>
<br>

