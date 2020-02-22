Google HashCode 2020 Contest 20th February 2020

It's the repository that we used in the contest,
We ended 3055th world, 258th France and 5th from the Epitech Paris Hub's with a total of 22,924,312 pts.

We used python for the challenge.

You can see our code in the src directory and our answers in the sample directory.
The subject is the pdf file.

We made a little script in bash to run the program for all each input files.

Algorithm:

Our algorithm calculates the "score" of each library from the score of each books that it had.
With all the scores we sort all the libraries from the highest score to the lowest.
With the classement score we take the first library and we sign it up.
Once the sign up is completed, we scan all the books, unfortunately we have not the time to sort the books scanned by score.
Each book we have already sent get down his score to '0' point.
As the book's score changes, the classement needs to be updated, so we re-sort the libraries with its new score and we restart the process as long as needed.
So we recalculate the classement for each books send.

Malus of the algorithm:

- The books arent scanned from the highest score to the lowest
- At the end, some library view it's score fall to '0' and we already sign them, we should not register if all of her books are already scanned.
- We recalculate each library score, even if her score equals 0 (easy to change with an if)
