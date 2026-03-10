#ifndef EMA_STRATEGY
#define EMA_STRATEGY

double FastEMA()
{
   return(iMA(_Symbol,PERIOD_CURRENT,20,0,MODE_EMA,PRICE_CLOSE,0));
}

double SlowEMA()
{
   return(iMA(_Symbol,PERIOD_CURRENT,50,0,MODE_EMA,PRICE_CLOSE,0));
}

bool EMA_BuySignal()
{

   if(FastEMA() > SlowEMA())
      return(true);

   return(false);

}

bool EMA_SellSignal()
{

   if(FastEMA() < SlowEMA())
      return(true);

   return(false);

}

#endif
