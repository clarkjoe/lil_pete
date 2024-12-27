import function TalkerSay(this Character*, const string text);
import function TurnOnDetails(this Character*);
import function TurnOffDetails(this Character*);
import bool ShowDetails(this Character*);
import Point* GetDestination(this Character*);
import function SetDestination(this Character*, int x, int y);
import bool HasReachedDestination(this Character*);
import function MyWalk(this Character*, int x, int y, BlockingStyle blockingStyle = eBlock, WalkWhere walkWhere = eWalkableAreas);
import bool ResumableWalk(this Character*, int x, int y, WalkWhere walkWhere = eWalkableAreas);
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

import function handle_overlays();

import bool CancelableWalk(this Character*, int x, int y, CharacterDirection dir);