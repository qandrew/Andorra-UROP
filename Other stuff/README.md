Autocomplete
============

*Submission to website:* Monday, November 2, 10pm

*Checkoff by LA/TA*: Tuesday, November 3, 10pm

This lab assumes you have Python 2.7 installed on your machine.  Please use the Chrome web browser.

Introduction
------------

Type "aren't you" into Google search and you'll get a handful of search suggestions, ranging from "aren't you clever?" to "aren't you a little short for a stormtrooper?". If you've ever done a Google search, you've probably seen autocomplete. It's that handy list of words that pops up under your search, guessing at what you were about to type.

Search engines aren't the only place you'll find this list. Powerful code editors, like Eclipse and Visual Studio, use autocomplete to make coding go faster by saving you the work of remembering and typing out particularly long function or variable names.

In Lab 7, we are going to implement our own version of autocomplete, using a tree structure called a "trie." The staff have already found a nice corpus of words for you to use-- the full text of Jules Verne's "In the Year 2889." The lab will ask you first to generate the trie using the list of words we give you. Then, you will use the trie to write your own autocomplete, which selects the top few words that someone is likely to be typing.

Tries
-----

A trie, also known as a prefix tree, is a type of tree that stores words with their different characters distributed across successive levels, starting with the root.

Say for example we wanted to store the words `'bat'`, `'bar'`, and `'bark'`. Our generated trie would look like the image on the next page.

![Simple Trie](images/trie1.png)

If we want to see what words start with the string `'ba'`, we follow the tree down through the `'b'` and `'a'` edges until we get to the node representing `'ba'`. Then we search through all the children of the `'ba'` node and return all valid words (`'bat'`, `'bar'`, and `'bark'`). Note that we also search through the `'ba'` node itself, but we don't return `'ba'` since it's not marked as a valid word.

If we wanted to see what words start with the string `'bar'`, we would perform a similar operation: follow the `'b'`, `'a'`, and `'r'` edges to the `'bar'` node, then check all of its children (and itself) to find the valid words `'bar'` and `'bark'`.

This trie structure on its own, however, is not enough for our autocomplete. If we type only a few characters, like `'b'`, we don't want all the words that start with a `'b'`-- only the most likely ones. To this end, we will augment the nodes of our trie with a frequency metric. Frequency will denote how often each word appears in our corpus. We will assume that words with higher frequency are more likely to be what the user meant to type. When we get words out of our trie, we only want to display to the user the ones with the highest frequencies.

Imagine our corpus was just this nonsensical sentence: `"bat bark bat bar"`. Then our trie would look like this:

![Frequency Trie](images/trie2.png)

Say we want to display only the top result for our autocomplete, and we type in the string `'ba'`. Now instead of giving us all of `'bat'`, `'bark'`, and `'bar'`, we should just get the highest-frequency word-- `'bat'`.

Note that in the tree above, the `'b'` and `'ba'` nodes have frequencies of `0`, meaning they're not valid words.

Lab7.py
-------
`Lab7.py` contains two functions, `generate_trie`, and `autocomplete`. 

`generate_trie` will take as input `words`, a list of words representing a corpus, (e.g. `["bat", "bark", "bat", "bar"]`) and should return a trie representing that list of words. `words` is guaranteed to contain words consisting only of lowercase letters.

The format of each trie should be a nested dictionary containing:

 - `frequency`: the frequency of the word ending at that node
 - `children`: a dictionary that maps suffix characters to other tries

A small trie for just the corpus `["a", "i"]` would look like this:

```
{"frequency": 0,
  "children":{
              'a': {"frequency": 1,
                    "children": {}
                   },
              'i': {"frequency": 1,
                    "children": {}
                   }
             }
}
```

A slightly larger trie for the corpus `["bat", "bark", "bat", "bar"]` would look like the following:

```
{"frequency": 0,
  "children":{
              'b': {"frequency": 0,
                    "children":{
                                'a': {"frequency": 0,
                                      "children":{
                                                  'r': {"frequency": 1,
                                                        "children:{
                                                                   'k': {"frequency": 1,
                                                                         "children": {}
                                                                        }
                                                                  }
                                                       },
                                                  't': {"frequency": 2,
                                                        "children": {}
                                                       }

                                                 }
                                     }
                               }

                   }   
             }
}
```

`generate_trie` should return the root trie, which should, via `"children"` links, cover all words in the corpus. Note that the root trie represents the empty string `""`, so it should always have a frequency of 0.

`autocomplete` takes as input:

 - `trie`, the trie that you generated in `generate_trie`
 - `prefix`, the prefix string you are trying to autocomplete
 - `N`, how many words of autocomplete you want.

That is, given `trie`, `prefix`, and `N`, you should return a list of the top `N` words in `trie` that start with `prefix`. In the case of a tie, you may output any of the top words. If there are less than `N` valid words available starting with `prefix`, return only as many as there are.

Hints
-----

We include a file `HINTS.pdf` that you may find useful if you find yourself stuck on this lab.

In-Browser UI (`./server.py`)
-----------------------------

We've included a 6.S04-autocomplete-powered search bar so you can see your code in action. Run `server.py` and open your browser to [localhost:8000](http://localhost:8000) and type into the search bar to see the top 5 results from your `autocomplete` function, using the corpus of words from Jules Verne's "In the Year 2889."

Unit Tester (`./test.py`)
-------------------------

As in the previous labs, we provide you with a `test.py` script to help you verify the correctness of your code. The script has tests for both `generate_trie` and `autocomplete`, but the `autocomplete` tests are dependent on a successful `generate_trie` implementation. Consider implementing `generate_trie` first and making sure its tests pass before moving on to `autocomplete`.

Note that in our tester, the `autocomplete` results are actually a list of possible answers (there may be multiple in case of a tie). Your code, however, should only output one of the valid answers.

Does your lab work? Do all tests in `test.py` pass? You're done! Submit your `Lab7.py` on funprog, and get your lab checked off by a friendly staff member. Consider tackling the bonus section below.

Bonus: Autocorrect
------------------

You may have noticed that for some words, our autocomplete implementation generates very few or no suggestions. In cases such as these, we may want to guess that the user mistyped something in the original word. For the bonus, we ask you to implement a more sophisticated code editing tool: autocorrect. 

The `autocorrect` method in `Lab7.py` takes in `trie`,`prefix`, and `N`, just like `autocomplete`. However, its behavior is slightly more interesting.

`autocorrect` should first run your existing `autocomplete` method. If running just `autocomplete` alone generates less than `N` results, you will add valid edits of your original word until you get up to `N` words (or run out of valid edits).

An *edit* for a word can be any one of the following:

 - A single-character insertion (add any one character in the range `a-z` at any place in the word)
 - A single-character deletion (remove any one character from the word)
 - A single-character replacement (replace any one character in the word with a character in the range `a-z`)
 - A two-character transpose (switch the positions of any two characters in the word)

A *valid edit* will be any edit that actually exists in the corpus (has a `frequency` not equal to `0` in the trie).

As before, we want to prioritize displaying edits with higher `frequency`, so after filling in your `N` suggestions with `autocomplete` results, fill them in with the highest-frequency valid edits. Be careful not to repeat words!

To test your bonus, you may run `test_bonus.py`.
