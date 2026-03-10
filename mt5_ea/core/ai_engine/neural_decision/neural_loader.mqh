#ifndef NEURAL_LOADER
#define NEURAL_LOADER

#include <Files\File.mqh>

void LoadNeuralWeights()
{

   int file = FileOpen("neural_weights.json",FILE_READ|FILE_TXT);

   if(file == INVALID_HANDLE)
   {
      Print("Neural weight file not found");
      return;
   }

   while(!FileIsEnding(file))
   {
      string line = FileReadString(file);
      Print("Weight data: ",line);
   }

   FileClose(file);

}

#endif
