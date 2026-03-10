#ifndef VOLATILITY_DETECTOR
#define VOLATILITY_DETECTOR

#include "../../config/ai_settings.mqh"

bool VolatilityOK()
{

   if(!UseATRFilter)
      return(true);

   double atr = iATR(_Symbol,PERIOD_CURRENT,ATR_Period,0);

   if(atr < ATR_Minimum)
   {
      Print("Volatility too low");
      return(false);
   }

   return(true);
}

#endif
