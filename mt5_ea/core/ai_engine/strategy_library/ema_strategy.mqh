#ifndef EMA_STRATEGY
#define EMA_STRATEGY

int emaFastHandle;
int emaSlowHandle;

void InitEMA()
{
   emaFastHandle = iMA(_Symbol,PERIOD_CURRENT,20,0,MODE_EMA,PRICE_CLOSE);
   emaSlowHandle = iMA(_Symbol,PERIOD_CURRENT,50,0,MODE_EMA,PRICE_CLOSE);
}

double FastEMA()
{
   double buf[];

   if(CopyBuffer(emaFastHandle,0,0,1,buf)<=0)
      return 0;

   return buf[0];
}

double SlowEMA()
{
   double buf[];

   if(CopyBuffer(emaSlowHandle,0,0,1,buf)<=0)
      return 0;

   return buf[0];
}

bool EMA_BuySignal()
{
   if(FastEMA() > SlowEMA())
      return true;

   return false;
}

bool EMA_SellSignal()
{
   if(FastEMA() < SlowEMA())
      return true;

   return false;
}

#endif
