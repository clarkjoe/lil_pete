import function choose_cursor();
//import function handle_overlays();
import function handle_time();

import function StartTimerByLoops(int timerID, int durationInLoops);
import function StartTimerBySeconds(int timerID, float durationInSeconds);

import int GetTimeRemainingInLoops(int timerID);
import float GetTimeRemainingInSeconds(int timerID);

import function PauseTimer(int timerID);
import function ResumeTimer(int timerID);

import int GetCurrentLoop();

import int GetMax(int a, int b);
import int GetMin(int a, int b);

import function GetFingerprint(InventoryItem* inventoryItem);