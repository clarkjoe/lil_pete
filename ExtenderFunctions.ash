// Mouse
import bool IsOverWalkableArea(static Mouse);
import bool IsOverHotspot(static Mouse);
import bool IsOverCharacter(static Mouse);
import bool IsOverObject(static Mouse);
import bool IsOverNothing(static Mouse);

// Object
import bool IsUnderMouse(this Object*);

// Character
import function TalkerSay(this Character*, const string text);
import function TurnOnDetails(this Character*);
import function TurnOffDetails(this Character*);
import bool ShowDetails(this Character*);

import function handle_overlays();