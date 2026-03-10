#ifndef LAYER_CONTROL
#define LAYER_CONTROL

#include "../../config/ai_settings.mqh"

datetime lastEntryTime=0;

bool CanOpenLayer()
{

   if(PositionsTotal() >= MaxLayers)
      return(false);

   if(RequireNewCandleForLayer)
   {

      datetime candle = iTime(_Symbol,PERIOD_CURRENT,0);

      if(candle == lastEntryTime)
         return(false);

   }

   lastEntryTime = iTime(_Symbol,PERIOD_CURRENT,0);

   return(true);

}

#endif
