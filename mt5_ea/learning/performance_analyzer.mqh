#ifndef PERFORMANCE_ANALYZER
#define PERFORMANCE_ANALYZER

#include <Files\File.mqh>

double CalculateWinRate()
{

   int file=FileOpen("trade_memory.csv",FILE_READ|FILE_CSV|FILE_ANSI);

   if(file==INVALID_HANDLE)
      return(0);

   int total=0;
   int wins=0;

   while(!FileIsEnding(file))
   {

      datetime time=FileReadDatetime(file);
      double profit=FileReadNumber(file);

      total++;

      if(profit>0)
         wins++;

   }

   FileClose(file);

   if(total==0)
      return(0);

   return((double)wins/total);

}

#endif
