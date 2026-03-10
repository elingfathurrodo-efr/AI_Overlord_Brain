#ifndef MACD_STRATEGY
#define MACD_STRATEGY

double MACD_Main()
{
   return(iMACD(_Symbol,PERIOD_CURRENT,12,26,9,PRICE_CLOSE,MODE_MAIN,0));
}

double MACD_Signal()
{
   return(iMACD(_Symbol,PERIOD_CURRENT,12,26,9,PRICE_CLOSE,MODE_SIGNAL,0));
}

bool MACD_BuySignal()
{

   if(MACD_Main() > MACD_Signal())
      return(true);

   return(false);

}

bool MACD_SellSignal()
{

   if(MACD_Main() < MACD_Signal())
      return(true);

   return(false);

}

#endif
