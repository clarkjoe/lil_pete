struct NotebookDialog
{
  import static void Update(Character* characterSpeakingTo, Dialog* charactersDialog, Dialog* subjectsDialog);
  import static void UpdateOptionId(int optionId);
  import static void Clear();
  import static bool IsSet();
  // necessary -2 because -1 means not set
  import static int ActiveDialogOptionId(int activeDialogOptionId_param = -2);
  import static void StartDialog();
  import static void Log();
};