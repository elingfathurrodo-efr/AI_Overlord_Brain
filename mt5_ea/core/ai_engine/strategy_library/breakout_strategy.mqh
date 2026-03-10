#ifndef BREAKOUT_STRATEGY
#define BREAKOUT_STRATEGY

bool BreakoutBuy()
{

   double prevHigh = iHigh(_Symbol,PERIOD_CURRENT,1);
   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price > prevHigh)
      return true;

   return false;
}

bool BreakoutSell()
{

   double prevLow = iLow(_Symbol,PERIOD_CURRENT,1);
   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price < prevLow)
      return true;

   return false;
}

#endif
