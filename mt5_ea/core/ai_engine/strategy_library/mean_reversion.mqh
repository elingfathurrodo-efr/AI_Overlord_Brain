#ifndef MEAN_REVERSION
#define MEAN_REVERSION

double GetMean()
{
   return(iMA(_Symbol,PERIOD_CURRENT,50,0,MODE_SMA,PRICE_CLOSE,0));
}

bool MeanBuy()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price < GetMean())
      return(true);

   return(false);

}

bool MeanSell()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   if(price > GetMean())
      return(true);

   return(false);

}

#endif
