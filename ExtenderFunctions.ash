// Mouse
import bool IsOverWalkableArea(static Mouse);
import bool IsOverHotspot(static Mouse);
import bool IsOverCharacter(static Mouse);
import bool IsOverObject(static Mouse);
import bool IsOverNothing(static Mouse);

// Object
import bool IsUnderMouse(this Object*);

// Character
import bool IsSitting(this Character*);
import bool SetIsSitting(this Character*, bool isSitting);