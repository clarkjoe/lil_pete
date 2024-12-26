managed struct ReflectedCharacter
{
  int characterIDToReflect;
  //protected DynamicSprite* reflectedSprite;
  int mirrorY;
  
  import function Update(Object* reflectedCharacter);
  import function Remove();
};

import ReflectedCharacter* Create(static ReflectedCharacter, Character* characterToReflect, int mirrorY);