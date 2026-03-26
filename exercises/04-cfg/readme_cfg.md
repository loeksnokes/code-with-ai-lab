# CFG 

The game CFG was a creation of John Conway.  We whiled away many hours in the Fine Hall lounge, with Conway shredding me and all other comers with tremendous ease.  Good times.

When I applied for graduate school, I have been told that Conway's letter for me said, I might become a good mathematician, if only they could convince me to stop playing games.  Well good sir, it is worth noting, but, I rather have no comment to add.

# The Board

The game is played on a classical Go Board (a 19x19 grid) with Slate and Shell stones as in the game of Go.  The players sit opposite each other, and initially, on the central vertex a white stone sits: the football.

# The Play

For a player's turn, they may take one of two types of action: placing a stone, or chaining some jumps.

## Placing a stone

One option of a player on-turn is to place a black stone on the board (on any free vertex).  This single placement then is their whole turn.

## Chaining jumps 

The other option for a turn is much busier.  One may create a chain of jumps of the football.

### The endzone, out-of-bounds, and a single jump
On turn, the play territory is on the board, and also, within the opponent's endzone (the "nominal" territory which is comprised of the 21 imaginary vertices that are off the board, and which reside across the line traced by the vertices on the row nearest to the opponent, including two imaginary vertices which are on the "outside diagonal" locations).  All other locations which are off the board are out-of-bounds. 

To make a single jump, one picks up the football, and moves it over any unbroken straight line of black stones (extending in one of the eight directions corresponding to the eight neighbouring positions of the football's original position) until one places the football on the first free vertex in the jump's initial direction of motion.  This free vertex must be on the board, or in happy circumstances, in the opponent's endzone.

A jump itself (as opposed to the motion of the jump) is not finished until the stones which were jumped over are removed from the board.

### A jump-chain

After any jump, the turn is not yet done: the acting player may choose to chain another jump onto their current chain of previously made jumps (their jump-chain).  In this case, they launch a new jump over stones existing in a neighbouring direction from the football's current location (note this cannot be back over the line they have just travelled, since those stones have been removed from the board already).

Instead of adding a new jump to an existing jump-chain, the player may choose to end their turn.

### Compassion
If one is playing a jump and realises after placing the football that they do not like the results of this jump, they are allowed to return to the position before the jump an reconsider that jump, choosing to stop their turn instead, or perhaps, going forward with that jump, or, another legal jump from that position.  One cannot "undo" the previous two jumps: one can only reconsider the very last jump taken in a chain/.  This power is preserved for later in the jump chain if one carries on for further jumps (it may be used multiple times in the determination of a chain, but never to undo the previous two jumps).

Once one has declared their turn is over, they forfeit this ability for the turn. and they are now at the mercy of their opponent's play.

## Winning

If a player makes a jump that lands in their opponent's endzone, then, they win the round.  In this case, the two players should reset the board to the initial setup, and start a new round with the initial player being the one who did not win the previous round.  Players may choose to keep score of rounds won.

# Courtesy and Defense
It is a courtesy to declare "Shot!" at the end of one's turn if one could win on one's following turn by executing some jump-chain.  (This can happen, for instance, if one places a stone on the board in some location so that there now exists a jump chain from the football's current location and ending in the endzone.)

If, for instance, one's opponent has called "Shot!" at the end of their turn, then it behooves the player to analyze the current jump chains from the football's current location, to understand the opponent's winning jump-chains.  In many cases it may be possible to disrupt the opponent's winning lines with a well-placed defensive stone.  Alternatively, one might be forced to jump the football away from the dangerous location, removing stones along the way and severing contact with the danger zone.  If none of these things are possible, then the opponent shall win on the following turn.
