
#Introduction
This project will handle three different algorithms for text processing, specifically patten recognition.
A problem arises when processing a large text file, performance can be significantly enhanced by using algorithms other then the naive approach.
We will explore the Brute Force algorithm, Boyer Moore algorithm and KMP algorithms.


#Description
Brute Force algorithm:


Boyer Moore algorithm:


KMP algorithm:
This algorithm is the most efficient of the 3, it avoids the waste of the work done in the previous steps when a mismatch is encountered, thus has a shorter running time O(n+m), m here signifies the length of the pattern and n the length of the text. The KMP algorithms precomputes self-overlaps between portions of the pattern so that when a mismatch occurs at one location, we immediately know the maximum amout to shift the pattern (using the fail algorithm) before continuing the search. It also takes into consideration if the number of the immediately preceding characters (before encountering a mismatch) can be used to restart the pattern.


#Description of text documents
The text documents used are:
* Vibrio_cholerae.txt, It contains the genome of Vibrio cholerae, a bactirium resposible for the cholera disease
* ori.txt, It contains the location of the origin of replication

All three algorithms will process the text files to find the pattern (origin of replication) inside the genome of the bacteria


