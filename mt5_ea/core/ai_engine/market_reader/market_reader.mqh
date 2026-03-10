#ifndef MARKET_READER
#define MARKET_READER

double GetSpread()
{
   return(SymbolInfoInteger(_Symbol,SYMBOL_SPREAD));
}

double GetATR(int period=14)
{
   return(iATR(_Symbol,PERIOD_CURRENT,period,0));
}

bool IsHighVolatility()
{
   if(GetATR()>50)
      return(true);

   return(false);
}

#endif
