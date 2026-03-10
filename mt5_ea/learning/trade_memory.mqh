#ifndef TRADE_MEMORY
#define TRADE_MEMORY

#include <Files\File.mqh>

string memoryFile="trade_memory.csv";

void SaveTradeMemory(double profit)
{

   int file=FileOpen(memoryFile,FILE_WRITE|FILE_READ|FILE_CSV|FILE_ANSI|FILE_SHARE_WRITE);

   if(file==INVALID_HANDLE)
   {
      Print("Cannot open memory file");
      return;
   }

   FileSeek(file,0,SEEK_END);

   FileWrite(file,TimeCurrent(),profit);

   FileClose(file);

}

#endif
