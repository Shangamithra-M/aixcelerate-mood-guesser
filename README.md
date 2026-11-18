# Mood Guesser

## Level 3: Testing

Accuracy on the 5 practice sentences: **100%**

1. **Which sentence went wrong (or was closest to going wrong), and why?**

   No sentence went wrong. "Today was a great day" was the closest to going wrong because the word "great" was not included in my happy_words list. Both counts were zero, so my program selected Happy as the default mood.

2. **One change that would make my program better:**

   I can add more useful clue words to improve the prediction accuracy for new sentences.

## Learning questions

1. **Total score of "good party today" and its mood:**

   good = +2, party = +1, today = 0.

   Total score = +3. Mood = Happy.

2. **Total score of "bad exam day" and its mood:**

   bad = -2, exam = 0, day = -1.

   Total score = -3. Mood = Sad.

3. **Why did "exam" get a score of 0, and is that good or bad?**

   The word "exam" appeared once in Happy sentences and once in Sad sentences. So, both counts are equal and its score becomes 0. It is useful because the word does not influence the prediction.

4. **Why is "not good" labelled Happy by this method, and how could it be fixed?**

   The program sees the word "good" and gives it a positive score. It does not understand the meaning of "not". We can fix this by teaching the program to identify negative words like "not" and consider their effect on the following word.

## AI declaration

I used an AI tool: **Yes**

If yes, what I asked it:

I used ChatGPT to understand the project instructions, learn Python and understand the mood guessing program, and check my program output.

## Reflection

What was hardest, and what I learned that I did not know before:

The hardest part was choosing useful clue words for predicting Happy and Sad moods. I learned how Python uses functions, lists, loops and conditions to process sentences. I also learned how a program can predict moods using words from examples.
