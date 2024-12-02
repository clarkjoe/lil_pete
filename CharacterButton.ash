enum CharacterButtonVariant
{
  eSilhouette,
  eGrey, 
  eColored
};

managed struct CharacterButton
{
  int SilhouetteGraphic;
  int SilhouetteMousedOverGraphic;
  int SilhouettePushedGraphic;
  int GreyGraphic;
  int GreyMousedOverGraphic;
  int GreyPushedGraphic;
  CharacterButtonVariant Variant;
  
  import function Init(
    int SilhouetteGraphic = 0,
    int SilhouetteMousedOverGraphic = 0, 
    int SilhouettePushedGraphic = 0, 
    int GreyGraphic = 0, 
    int GreyMousedOverGraphic = 0, 
    int GreyPushedGraphic = 0,
    CharacterButtonVariant = eColored
  );
};