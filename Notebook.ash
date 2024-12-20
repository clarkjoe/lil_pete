import function initialize_notebook();
import NotebookButtonVariant get_notebook_character_button_variant(Character *contextCharacter, Character *actionCharacter);
import NotebookButtonVariant get_notebook_subject_button_variant(Character *contextCharacter, int subjectID);
import NotebookButtonVariant get_notebook_evidence_button_variant(Character *contextCharacter, int evidenceID);
import function change_context_notebook_character_button_variant(Character *contextCharacter, Character *actionCharacter, NotebookButtonVariant variant);
import function change_context_notebook_subject_button_variant(Character *contextCharacter, int subjectID, NotebookButtonVariant variant);
import function change_context_notebook_evidence_button_variant(Character *contextCharacter, int evidenceID, NotebookButtonVariant variant);
import function populate_notebook();

// Characters
import function gNotebookCharacters_OnClickHandler(GUI *theGui, MouseButton button);
import function claraNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function stoneNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function veraNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function joannaNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function salvatoreNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function queenieNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function maxNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function teresaNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function lucindaNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function samirNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function drkhanNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function carlosNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function btnCharactersToSubjects_OnClickHandler(GUIControl *control, MouseButton button);
import function btnCharactersToEvidence_OnClickHandler(GUIControl *control, MouseButton button);

// Subjects
import function gNotebookSubjects_OnClickHandler(GUI *theGui, MouseButton button);
import function btnSubjectsToCharacters_OnClickHandler(GUIControl *control, MouseButton button);
import function btnSubjectsToEvidence_OnClickHandler(GUIControl *control, MouseButton button);
import function stonecliffManorNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function madamWhiteSnakeNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function theBanterNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function mauledScientistNotebook_OnClickHandler(GUIControl *control, MouseButton button);
import function tigersBloodNotebook_OnClickHandler(GUIControl *control, MouseButton button);

// Evidence
import function gNotebookEvidence_OnClickHandler(GUI *theGui, MouseButton button);
import function btnEvidenceToCharacters_OnClickHandler(GUIControl *control, MouseButton button);
import function btnEvidenceToSubjects_OnClickHandler(GUIControl *control, MouseButton button);

// Summary
import function gNotebookSummary_OnClickHandler(GUI *theGui, MouseButton button);
