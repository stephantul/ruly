# ruly
A short script to generate stuff based on binary cellular automata.

Binary cellular automata consist of a binary start vector, i.e. a vector in
which some bits are 1 and others are 0, and a set of rules by which the
vector evolves over time.

# rules

Rules are created by converting a simple integer number to an 8-bit vector.
For example, the binary representation of the number 30 in 8 bits is
'01111000'.

# evolution

The binary automaton evolves by converting the current vector into trigrams,
and converting each of these trigrams into a 3-bit integer representation.

For example, given the rule '01111000' above, the trigram '000' would produce
a '0' in the position below the middle position of the trigram, while
'010' would produce a '1' below the middle position.

# Example

```
from ruly import rule

# Create wolfram's classic rule 30 automaton.
result = rule(150, 75, [75], 30)

from matplotlib import pyplot as plt
plt.imshow(p)
plt.show()
```
