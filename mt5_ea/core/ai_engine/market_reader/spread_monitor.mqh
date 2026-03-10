#ifndef SPREAD_MONITOR
#define SPREAD_MONITOR

#include "../../config/ai_settings.mqh"

bool SpreadOK()
{

   double spread = SymbolInfoInteger(_Symbol,SYMBOL_SPREAD);

   if(spread > MaxSpread)
   {
      Print("Spread too high: ",spread);
      return(false);
   }

   return(true);

}

#endif
