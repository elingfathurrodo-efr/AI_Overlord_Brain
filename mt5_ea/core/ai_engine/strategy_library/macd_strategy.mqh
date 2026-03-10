#ifndef MACD_STRATEGY
#define MACD_STRATEGY

int macdHandle;

void InitMACD()
{
   macdHandle = iMACD(_Symbol,PERIOD_CURRENT,12,26,9,PRICE_CLOSE);
}

double MACD_Main()
{
   double buf[];

   if(CopyBuffer(macdHandle,0,0,1,buf)<=0)
      return 0;

   return buf[0];
}

double MACD_Signal()
{
   double buf[];

   if(CopyBuffer(macdHandle,1,0,1,buf)<=0)
      return 0;

   return buf[0];
}

bool MACD_BuySignal()
{
   if(MACD_Main() > MACD_Signal())
      return true;

   return false;
}

bool MACD_SellSignal()
{
   if(MACD_Main() < MACD_Signal())
      return true;

   return false;
}

#endif
