#ifndef RSI_STRATEGY
#define RSI_STRATEGY

double GetRSI(int period=14)
{
   return(iRSI(_Symbol,PERIOD_CURRENT,period,PRICE_CLOSE,0));
}

bool RSI_BuySignal()
{

   double rsi = GetRSI();

   if(rsi < 30)
      return(true);

   return(false);

}

bool RSI_SellSignal()
{

   double rsi = GetRSI();

   if(rsi > 70)
      return(true);

   return(false);

}

#endif
