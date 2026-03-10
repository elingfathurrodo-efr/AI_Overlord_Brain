#ifndef GHOST_TRAILING
#define GHOST_TRAILING

void GhostTrailing()
{

   for(int i=PositionsTotal()-1;i>=0;i--)
   {

      ulong ticket = PositionGetTicket(i);

      if(PositionSelectByTicket(ticket))
      {

         double open = PositionGetDouble(POSITION_PRICE_OPEN);
         double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

         double profit = price-open;

         if(profit > 50*_Point)
         {

            if(profit < 20*_Point)
            {
               Print("Ghost trailing close");
               ClosePosition(ticket);
            }

         }

      }

   }

}

#endif
