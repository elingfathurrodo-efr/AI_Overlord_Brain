#ifndef EQUITY_GUARD
#define EQUITY_GUARD

#include "../../config/ai_settings.mqh"

bool EquitySafe()
{

   if(!EnableEquityGuard)
      return(true);

   double balance = AccountInfoDouble(ACCOUNT_BALANCE);
   double equity  = AccountInfoDouble(ACCOUNT_EQUITY);

   double drawdown = (balance-equity)/balance*100;

   if(drawdown > MaxDrawdownPercent)
   {
      Print("Equity Guard Triggered");
      return(false);
   }

   return(true);

}

#endif
