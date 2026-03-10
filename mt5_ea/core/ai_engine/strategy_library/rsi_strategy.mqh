#ifndef RSI_STRATEGY
#define RSI_STRATEGY

int rsiHandle;

void InitRSI()
{
   rsiHandle = iRSI(_Symbol,PERIOD_CURRENT,14,PRICE_CLOSE);
}

double GetRSI()
{
   double buf[];

   if(CopyBuffer(rsiHandle,0,0,1,buf) <=0)
      return 50;

   return buf[0];
}

bool RSI_BuySignal()
{
   if(GetRSI() < 30)
      return true;

   return false;
}

bool RSI_SellSignal()
{
   if(GetRSI() > 70)
      return true;

   return false;
}

#endif
