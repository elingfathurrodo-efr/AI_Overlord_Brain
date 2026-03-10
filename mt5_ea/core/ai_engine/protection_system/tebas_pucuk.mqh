#ifndef TEBAS_PUCUK
#define TEBAS_PUCUK

void TebasPucuk()
{

   for(int i=PositionsTotal()-1;i>=0;i--)
   {

      ulong ticket = PositionGetTicket(i);

      if(PositionSelectByTicket(ticket))
      {

         double profit = PositionGetDouble(POSITION_PROFIT);

         if(profit > 1.0)
         {

            Print("Tebas pucuk close");

            ClosePosition(ticket);

         }

      }

   }

}

#endif
