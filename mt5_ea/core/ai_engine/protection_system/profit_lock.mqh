#ifndef PROFIT_LOCK
#define PROFIT_LOCK

#include "../../config/ai_settings.mqh"

double LockedBalance = 0;

void CheckProfitLock()
{

   if(!EnableProfitLock)
      return;

   double balance = AccountInfoDouble(ACCOUNT_BALANCE);

   if(LockedBalance == 0)
      LockedBalance = balance;

   if(balance >= LockedBalance * ProfitLockStart)
   {

      LockedBalance = balance * (1 - ProfitLockRatio);

      Print("Profit Locked at: ",LockedBalance);

   }

}

bool ProfitProtected()
{

   double equity = AccountInfoDouble(ACCOUNT_EQUITY);

   if(equity < LockedBalance)
   {
      Print("Profit protection triggered");
      return(false);
   }

   return(true);

}

#endif
