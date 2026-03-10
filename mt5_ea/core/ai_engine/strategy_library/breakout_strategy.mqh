#ifndef BREAKOUT_STRATEGY
#define BREAKOUT_STRATEGY

bool BreakoutBuy()
{

   double high = iHigh(_Symbol,PERIOD_CURRENT,1);
   double current = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(current > high)
      return(true);

   return(false);

}

bool BreakoutSell()
{

   double low = iLow(_Symbol,PERIOD_CURRENT,1);
   double current = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(current < low)
      return(true);

   return(false);

}

#endif
