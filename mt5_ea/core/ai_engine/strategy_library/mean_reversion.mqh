#ifndef MEAN_REVERSION
#define MEAN_REVERSION

int meanHandle;

void InitMean()
{
   meanHandle = iMA(_Symbol,PERIOD_CURRENT,50,0,MODE_SMA,PRICE_CLOSE);
}

double GetMean()
{
   double buf[];

   if(CopyBuffer(meanHandle,0,0,1,buf)<=0)
      return 0;

   return buf[0];
}

bool MeanBuy()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price < GetMean())
      return true;

   return false;
}

bool MeanSell()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price > GetMean())
      return true;

   return false;
}

#endif
