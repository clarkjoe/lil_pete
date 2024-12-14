// Mouse
import bool IsOverWalkableArea(static Mouse);
import bool IsOverHotspot(static Mouse);
import bool IsOverCharacter(static Mouse);
import bool IsOverObject(static Mouse);
import bool IsOverNothing(static Mouse);
import Hotspot* GetOverHotspot(static Mouse);
import Character* GetOverCharacter(static Mouse);
import Object* GetOverObject(static Mouse);
import int GetWalkableArea(static Mouse);

// Object
import bool IsUnderMouse(this Object*);
import bool IsInteractable(this Object*);

// Character
import function TalkerSay(this Character*, const string text);
import function TurnOnDetails(this Character*);
import function TurnOffDetails(this Character*);
import bool ShowDetails(this Character*);
import Point* GetDestination(this Character*);
import function SetDestination(this Character*, int x, int y);
import bool HasReachedDestination(this Character*);
import function MyWalk(this Character*, int x, int y, BlockingStyle blockingStyle = eBlock, WalkWhere walkWhere = eWalkableAreas);

import function SendToCharacterNear(this Character*, Character* target, int maxDistance = 15);

import function handle_overlays();

// Hotspot
import bool IsInteractable(this Hotspot*);
import int Baseline(this Hotspot*);