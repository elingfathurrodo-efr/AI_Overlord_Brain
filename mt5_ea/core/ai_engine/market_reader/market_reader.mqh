#ifndef MARKET_READER
#define MARKET_READER

#include "spread_monitor.mqh"
#include "volatility_detector.mqh"
#include "regime_detector.mqh"

//--------------------------------------------------
// BASIC MARKET DATA
//--------------------------------------------------

double GetSpread()
{
   return(SymbolInfoInteger(_Symbol,SYMBOL_SPREAD));
}

double GetBid()
{
   return(SymbolInfoDouble(_Symbol,SYMBOL_BID));
}

double GetAsk()
{
   return(SymbolInfoDouble(_Symbol,SYMBOL_ASK));
}

double GetATR(int period=14)
{
   return(iATR(_Symbol,PERIOD_CURRENT,period,0));
}

//--------------------------------------------------
// MARKET STATUS
//--------------------------------------------------

bool MarketHealthy()
{

   if(!SpreadOK())
      return(false);

   if(!VolatilityOK())
      return(false);

   return(true);
}

#endif
