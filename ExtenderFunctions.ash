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
import bool HasUsedCompact(this Object*);
import bool HasUsedClearTape(this Object*);
import function SetUsedCompact(this Object*,  bool usedCompact);
import function SetUsedClearTape(this Object*,  bool usedClearTape);
import bool IsFingerprintable(this Object*);
import bool HasFingerprint(this Object*);
import function SetFingerprintable(this Object*,  bool fingerprintable);
import function SetFingerprint(this Object*,  bool hasFingerprint);

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

import function ColorInCharacter(this Character*, Character *actionCharacter);
import function GreyInCharacter(this Character*, Character *actionCharacter);
import function SilhouetteInCharacter(this Character*, Character *actionCharacter);
import bool CharacterIsColor(this Character*, Character *actionCharacter);
import bool CharacterIsGrey(this Character*, Character *actionCharacter);
import bool CharacterIsSilhouette(this Character*, Character *actionCharacter);
import function ColorInCharacterEverywhere(static Character, Character *actionCharacter);
import function GreyInCharacterEverywhere(static Character, Character *actionCharacter);
import function SilhouetteInCharacterEverywhere(static Character, Character *actionCharacter);

import function ColorInSubject(this Character*, Button *subject);
import function GreyInSubject(this Character*, Button *subject);
import function SilhouetteInSubject(this Character*, Button *subject);
import bool SubjectIsColor(this Character*, Button *subject);
import bool SubjectIsGrey(this Character*, Button *subject);
import bool SubjectIsSilhouette(this Character*, Button *subject);
import function ColorInSubjectEverywhere(static Character, Button *subject);
import function GreyInSubjectEverywhere(static Character, Button *subject);
import function SilhouetteInSubjectEverywhere(static Character, Button *subject);

import function ColorInEvidence(this Character*, Button *evidence);
import function GreyInEvidence(this Character*, Button *evidence);
import function SilhouetteInEvidence(this Character*, Button *evidence);
import bool EvidenceIsColor(this Character*, Button *evidence);
import bool EvidenceIsGrey(this Character*, Button *evidence);
import bool EvidenceIsSilhouette(this Character*, Button *evidence);
import function ColorInEvidenceEverywhere(static Character, Button *evidence);
import function GreyInEvidenceEverywhere(static Character, Button *evidence);
import function SilhouetteInEvidenceEverywhere(static Character, Button *evidence);

// Hotspot
import bool IsInteractable(this Hotspot*);
import int Baseline(this Hotspot*);

// Inventory Item
import bool HasUsedCompact(this InventoryItem*);
import bool HasUsedClearTape(this InventoryItem*);
import function SetUsedCompact(this InventoryItem*,  bool usedCompact);
import function SetUsedClearTape(this InventoryItem*,  bool usedClearTape);
import bool IsFingerprintable(this InventoryItem*);
import bool HasFingerprint(this InventoryItem*);
import function SetFingerprintable(this InventoryItem*,  bool fingerprintable);
import function SetFingerprint(this InventoryItem*,  bool hasFingerprint);
import function HandleLeftClick(this InventoryItem*);
import function HandleRightClick(this InventoryItem*);

// String
import bool MyContains(this String*, String search);

// Other
import function handle_overlays();
