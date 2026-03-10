#ifndef TRADE_FREQUENCY_AI
#define TRADE_FREQUENCY_AI

#include "../../config/ai_settings.mqh"

datetime lastTradeTime=0;

bool CanTradeNow()
{

   datetime now = TimeCurrent();

   int delay = ScalpingFrequency * 60;

   if(now - lastTradeTime < delay)
      return(false);

   lastTradeTime = now;

   return(true);

}

#endif
