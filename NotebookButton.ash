enum NotebookButtonVariant
{
  eSilhouette,
  eGrey, 
  eColored
};

managed struct NotebookButton
{
  int coloredGraphic;
  int coloredMousedOverGraphic;
  int coloredPushedGraphic;
  int greyGraphic;
  int greyMousedOverGraphic;
  int greyPushedGraphic;
  int silhouetteGraphic;
  int silhouetteMousedOverGraphic;
  int silhouettePushedGraphic;
  NotebookButtonVariant variant;
};
