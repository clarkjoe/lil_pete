import function TalkerSay(this Character*, const string text);
import function TurnOnDetails(this Character*);
import function TurnOffDetails(this Character*);
import bool ShowDetails(this Character*);
import Point* Destination(this Character*, int x = -1, int y = -1);
import LocationType DestinationType(this Character*, LocationType destinationType = -1);
import int DestinationID(this Character*, int destinationID = -1);
import bool IsDestination(this Character*, Character* targetCharacter);
import bool HasReachedDestination(this Character*);
import bool ResumableWalk(this Character*, int x, int y, BlockingStyle blockingStyle = eNoBlock, WalkWhere walkWhere = eWalkableAreas);

import int Graphic(this Character*);
import bool Sitting(this Character*, bool sitting = -1);
import CharacterDirection Direction(this Character*, CharacterDirection direction = eDirectionNone, BlockingStyle blockingStyle = eBlock);
import CharacterDirection DestinationDirection(this Character*, CharacterDirection direction = eDirectionNone);

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

import function handle_overlays();

import int GetFurthestRightX(this Character*);
import bool CancelableWalk(this Character*, int x, int y, CharacterDirection dir = eDirectionNone);
//import function SendToCharacterRight(this Character*, Character* player, int offset);
//import function SendToCharacterLeft(this Character*, Character* player, int offset);
//import function SendToCharacterTop(this Character*, Character* targetCharacter, int offset);
//import function SendToCharacterBottom(this Character*, Character* targetCharacter, int offset);
//import function SendToCharacter(this Character*, Character* targetCharacter, int offset = 5);
import bool SendToCharacterSide(this Character*, Character* targetCharacter, int offset, bool toRight);
import bool SendToCharacterVertical(this Character*, Character* targetCharacter, int offset, bool toBottom);
import bool SendToCharacter(this Character*, Character* targetCharacter, int offset = 5);

import bool TalkHandler_Before(this Character*);