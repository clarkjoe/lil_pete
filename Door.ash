struct Door {
  Object* doorObject;
  bool isOpen;
  bool approachX;
  bool approachY;
  bool exitX;
  bool exitY;

  import void Init(Object* doorObject, int approachXOffset = 0, int approachYOffset = 0, int exitXOffset = 0, int exitYOffset = 0);
  import void Open();
  import void Close();
};