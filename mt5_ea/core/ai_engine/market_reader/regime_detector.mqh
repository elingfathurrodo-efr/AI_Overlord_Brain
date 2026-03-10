#ifndef REGIME_DETECTOR
#define REGIME_DETECTOR

//--------------------------------------------------
// MARKET REGIME
//--------------------------------------------------

enum MARKET_REGIME
{
   TRENDING,
   RANGING
};

MARKET_REGIME DetectMarketRegime()
{

   double emaFast = iMA(_Symbol,PERIOD_CURRENT,20,0,MODE_EMA,PRICE_CLOSE,0);
   double emaSlow = iMA(_Symbol,PERIOD_CURRENT,50,0,MODE_EMA,PRICE_CLOSE,0);

   if(MathAbs(emaFast-emaSlow) > 20*_Point)
      return(TRENDING);

   return(RANGING);

}

#endif
