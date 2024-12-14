enum CharacterButtonVariant
{
  eSilhouette,
  eGrey, 
  eColored
};

managed struct CharacterButton
{
  int ColoredGraphic;
  int ColoredMousedOverGraphic;
  int ColoredPushedGraphic;
  int GreyGraphic;
  int GreyMousedOverGraphic;
  int GreyPushedGraphic;
  int SilhouetteGraphic;
  int SilhouetteMousedOverGraphic;
  int SilhouettePushedGraphic;
  CharacterButtonVariant Variant;
  
  import function Init(
    int ColoredGraphic = 0, 
    int ColoredMousedOverGraphic = 0, 
    int ColoredPushedGraphic = 0,
    int GreyGraphic = 0, 
    int GreyMousedOverGraphic = 0, 
    int GreyPushedGraphic = 0,
    int SilhouetteGraphic = 0,
    int SilhouetteMousedOverGraphic = 0, 
    int SilhouettePushedGraphic = 0, 
    CharacterButtonVariant = eColored
  );
};