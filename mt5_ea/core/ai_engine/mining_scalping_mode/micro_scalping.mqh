#ifndef MICRO_SCALPING
#define MICRO_SCALPING

#include "../../config/ai_settings.mqh"

double CalculateMicroLot()
{

   double balance = AccountInfoDouble(ACCOUNT_BALANCE);

   double lot = balance / 10000;

   if(lot < BaseLot)
      lot = BaseLot;

   if(lot > MaxLot)
      lot = MaxLot;

   return(lot);

}

bool ScalpingAllowed()
{

   if(!EnableMiningMode)
      return(false);

   double spread = SymbolInfoInteger(_Symbol,SYMBOL_SPREAD);

   if(spread > MaxSpread)
      return(false);

   return(true);

}

#endif
