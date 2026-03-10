#ifndef NEURAL_SIGNALS
#define NEURAL_SIGNALS

#include "../strategy_library/rsi_strategy.mqh"
#include "../strategy_library/ema_strategy.mqh"
#include "../strategy_library/macd_strategy.mqh"
#include "../strategy_library/breakout_strategy.mqh"
#include "../strategy_library/mean_reversion.mqh"

double Signal_RSI()
{
   if(RSI_BuySignal()) return(1);
   if(RSI_SellSignal()) return(-1);
   return(0);
}

double Signal_EMA()
{
   if(EMA_BuySignal()) return(1);
   if(EMA_SellSignal()) return(-1);
   return(0);
}

double Signal_MACD()
{
   if(MACD_BuySignal()) return(1);
   if(MACD_SellSignal()) return(-1);
   return(0);
}

double Signal_Breakout()
{
   if(BreakoutBuy()) return(1);
   if(BreakoutSell()) return(-1);
   return(0);
}

double Signal_Mean()
{
   if(MeanBuy()) return(1);
   if(MeanSell()) return(-1);
   return(0);
}

#endif
