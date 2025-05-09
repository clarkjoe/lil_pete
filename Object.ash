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

import Point* Destination(this Object*, int x = -1, int y = -1);